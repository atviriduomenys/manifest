def test_manifest(app):
    resp = app.get('/')
    assert resp.status_code == 404
    assert resp.json() == {'error': 'Not Found'}
