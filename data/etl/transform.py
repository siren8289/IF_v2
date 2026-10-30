# 받아 온 원본을 "한 행 = 딕셔너리" 목록으로 바꾸고, 저장해도 되는 행만 남긴다.
# 형식은 source["format"] 에 적힌 json / xml / csv 중 하나다.
import csv
import hashlib
import io
import json
import xml.etree.ElementTree as ET


def _select_path(value, path):
    """점(.)으로 된 경로를 따라 들어간다. 예: "response.body.items".

    중간에 리스트를 만나면, 그 리스트의 각 원소에서 같은 키를 꺼낸다.
    경로가 끊기면 None.
    """
    for part in filter(None, path.split(".")):
        if isinstance(value, dict):
            value = value.get(part)
        elif isinstance(value, list):
            value = [item.get(part) for item in value if isinstance(item, dict)]
        else:
            return None
        if value is None:
            return None
    return value


def _xml_value(element):
    """XML 원소 하나를 딕셔너리(또는 글자)로 바꾼다.

    자식이 없으면 그 태그의 글자.
    같은 이름 태그가 여러 번이면 리스트로 모은다.
    태그 이름 앞의 네임스페이스({...})는 잘라 낸다.
    """
    children = list(element)
    if not children:
        return element.text or ""

    result = {}
    for child in children:
        name = child.tag.rsplit("}", 1)[-1]
        value = _xml_value(child)
        if name in result:
            if not isinstance(result[name], list):
                result[name] = [result[name]]
            result[name].append(value)
        else:
            result[name] = value
    return result


def parse_data(payload, source):
    """원본 문자열을 행(dict) 리스트로 바꾼다. 아직 검증은 하지 않는다."""
    data_format = source.get("format", "").lower()
    if isinstance(payload, bytes):
        # utf-8-sig: 엑셀이 붙이는 BOM(파일 맨 앞의 보이지 않는 문자)을 떼고 읽는다.
        text = payload.decode("utf-8-sig")
    else:
        text = payload

    if data_format == "json":
        data = json.loads(text)
        # item_path가 가리키는 곳이 실제 행 목록이다. 공공 API는 겉에 응답 코드가 감싸져 있다.
        selected = _select_path(data, source.get("item_path", ""))
        if selected is None:
            return []
        return selected if isinstance(selected, list) else [selected]

    if data_format == "xml":
        root = ET.fromstring(text)
        path = source.get("item_path", "")
        parts = list(filter(None, path.split(".")))
        # 경로의 첫 칸이 루트 태그 자신이면 이미 그 자리에 있으므로 건너뛴다.
        if parts and parts[0] == root.tag.rsplit("}", 1)[-1]:
            parts.pop(0)
        elements = [root]
        for part in parts:
            elements = [
                child
                for element in elements
                for child in element
                if child.tag.rsplit("}", 1)[-1] == part
            ]
        return [_xml_value(element) for element in elements]

    if data_format == "csv":
        # 첫 줄을 열 이름으로 보고, 나머지 줄을 dict로 만든다.
        return list(csv.DictReader(io.StringIO(text)))

    raise ValueError(f"Unsupported data format: {data_format}")


def normalize_rows(rows, source):
    """필수 칸이 빈 행을 버리고, 같은 키의 중복 행은 첫 번째만 남긴다.

    돌려주는 각 행은 {record_key, payload} 다.
    record_key는 키 칸들을 SHA-256으로 해시한 64자리 문자열이라,
    같은 데이터는 다시 넣어도 DB에서 한 행으로 겹친다.
    """
    required_fields = source.get("required_fields", [])
    key_fields = source.get("key_fields", [])
    normalized = []
    seen = set()

    for row in rows:
        # 필수 칸이 하나라도 없거나 공백이면 그 행은 버린다.
        if any(row.get(field) is None or str(row[field]).strip() == "" for field in required_fields):
            continue

        # 키 칸이 지정돼 있으면 그 칸만으로 중복을 판단한다. 없으면 행 전체를 비교한다.
        key_values = [row.get(field) for field in key_fields] if key_fields else row
        encoded_key = json.dumps(key_values, sort_keys=True, ensure_ascii=False, default=str)
        if encoded_key in seen:
            continue
        seen.add(encoded_key)

        record_key = hashlib.sha256(encoded_key.encode("utf-8")).hexdigest()
        normalized.append({"record_key": record_key, "payload": row})

    return normalized
