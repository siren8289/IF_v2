from data.etl.transform import parse_data, normalize_rows


def test_parse_xml():
    xml = b"""
    <response>
      <body>
        <items>
          <item>
            <jobId>100</jobId>
            <title>Test Job</title>
          </item>
        </items>
      </body>
    </response>
    """

    source = {
        "format": "xml",
        "item_path": "response.body.items.item",
    }

    rows = parse_data(xml, source)

    assert len(rows) == 1
    assert rows[0]["jobId"] == "100"


def test_duplicate_removed():
    source = {
        "key_fields": ["jobId"],
        "required_fields": ["jobId"],
    }

    rows = [
        {"jobId": "100", "title": "A"},
        {"jobId": "100", "title": "A"},
    ]

    result = normalize_rows(rows, source)

    assert len(result) == 1


def test_json_parsing():
    payload = b'{"items":[{"id":"1"}]}'

    source = {
        "format": "json",
        "item_path": "items",
    }

    result = parse_data(payload, source)

    assert result == [{"id": "1"}]