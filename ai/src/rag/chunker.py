"""텍스트 청킹(Chunking) 모듈.

긴 지침 문서를 검색에 적합한 작은 덩어리(청크)로 나눕니다.
문맥이 끊기지 않도록 일정한 글자 수만큼 겹치게(overlap) 처리합니다.
"""


def split_text_into_chunks(
    text: str,
    chunk_size: int = 250,
    chunk_overlap: int = 50,
) -> list[str]:
    """긴 글을 일정한 크기의 청크 목록으로 나눕니다.
    
    매개변수:
        text: 나눌 원본 텍스트
        chunk_size: 하나의 청크에 들어갈 최대 글자 수 (기본 250자)
        chunk_overlap: 앞뒤 청크 사이에 겹칠 글자 수 (기본 50자)
        
    반환값:
        분할된 문자열 조각 리스트
    """
    clean_text = text.strip()
    if not clean_text:
        return []

    # 글이 청크 크기보다 작으면 그대로 하나만 반환합니다.
    if len(clean_text) <= chunk_size:
        return [clean_text]

    chunks = []
    start = 0
    step = chunk_size - chunk_overlap

    while start < len(clean_text):
        end = start + chunk_size
        chunk = clean_text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += step

    return chunks


def chunk_documents(
    documents: list[dict],
    chunk_size: int = 250,
    chunk_overlap: int = 50,
) -> list[dict]:
    """페이지별 문서 목록을 받아서 메타데이터를 유지하며 청크 단위로 분할합니다.
    
    매개변수:
        documents: [{"doc_name": ..., "page": ..., "content": ..., "source": ...}, ...]
        chunk_size: 청크 크기
        chunk_overlap: 겹치는 길이
        
    반환값:
        청크 딕셔너리 목록:
        [{"chunk_id": "...", "doc_name": "...", "page": 1, "source": "...", "content": "..."}, ...]
    """
    all_chunks = []
    chunk_counter = 1

    for doc in documents:
        raw_text = doc.get("content", "")
        text_pieces = split_text_into_chunks(raw_text, chunk_size, chunk_overlap)

        for piece in text_pieces:
            all_chunks.append({
                "chunk_id": f"chunk_{chunk_counter}",
                "doc_name": doc.get("doc_name", "미상 문서"),
                "page": doc.get("page", 1),
                "source": doc.get("source", "출처 미상"),
                "content": piece,
            })
            chunk_counter += 1

    return all_chunks
