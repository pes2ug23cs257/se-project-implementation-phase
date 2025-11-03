def test_index_has_input():
    with open('frontend/index.html','r') as f:
        content = f.read()
    assert 'id="imageInput"' in content
