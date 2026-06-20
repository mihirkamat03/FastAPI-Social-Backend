from app import schemas
    
def test_create_user(client):
    # Registration uses /users/, requires "email", and uses json
    res = client.post("/users/", json={"email": "mihir2@gmail.com", "password": "12345678"})
    assert res.status_code == 201

def test_login_user(client):
    # Login uses /login, requires "username", and uses data= (Form Data)
    res = client.post("/login", data={"username": "mihir2@gmail.com", "password": "12345678"})
    assert res.status_code == 200