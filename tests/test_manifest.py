def test_manifest(app):
    resp = app.get('/')
    assert resp.status_code == 200
    data = resp.json()
    data = {d['_id'] for d in data['_data']}
    assert 'asmuo/:ns' in data
