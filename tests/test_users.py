from app import schemas
import pytest
from jose import jwt
from app.config import settings


@pytest.fixture()
def test_users(client):
    user_data={
        "email":"mihir2@gmail.com",
        "password": "12345678"
    }
    res= client.post("/users/", json=user_data)
    new_user=res.json()
    new_user['password']=user_data['password']
    return new_user
    
def test_create_user(client):
    # Registration uses /users/, requires "email", and uses json
    res = client.post("/users/", json={"email": "mihir2@gmail.com", "password": "12345678"})
    assert res.status_code == 201

def test_login_user(test_users, client):
    # Login uses /login, requires "username", and uses data= (Form Data)
    res = client.post("/login", data={"username": test_users['email'], "password": test_users['password']})
    login_res=schemas.token(**res.json())
    payload=jwt.decode(login_res.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    id: str=payload.get("user_id")
    assert id==test_users['id']
    assert login_res.token_type== "bearer"
    assert res.status_code == 200
    

@pytest.mark.parametrize("email, password, status_code", [
    ('ccdrv@gmail.com', "12345678", 403),
    ('mihir2@gmail.com', "3562789", 403),
    (None, "12345678", 422),
    ("mihir2@gmail.com", None, 422)
])

def test_incorrect_login(test_users, client, email, password, status_code):
    res=client.post("/login", data={"username": email, "password": password})
    
    assert res.status_code==status_code
