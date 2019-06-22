def test_manifest(app):
    resp = app.get('/')
    assert resp.status_code == 200
    data = resp.json()
    assert 'asmuo' in data['contents']
    assert resp.json() == {
        'contents': data['contents'],
        'datasets': [],
    }
