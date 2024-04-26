import requests
import flask
'''
def test_first():
    res = requests.get('http://127.0.0.1')
    assert res.status_code == 200
'''  

def test_main(client):
    res =  client.get('/main')
    assert res.status_code == 302

def test_login(client):
    res = client.post('/login')
    print(res)
    assert res.status_code == 200
    assert b"Birthday" in res.data
    assert b"ID number" in res.data
    assert b"Account Not Registered" in res.data

def test_invaliid_login(client):
    res = client.post('/login',data=dict(IDnumber='B223376305',
                                         birthday='91/08/04'),
                      follow_redirects=True)
    print('aaaa')
    print(res.data)
    assert res.status_code == 200
    assert b"Birthday" in res.data
    assert b"ID number" in res.data

def test_search(client):
    res = client.post('/searchHospital')
    print('aaaa')
    print(res.data)
    assert res.status_code == 302
   

def test_deleteContact(client):
    res = client.post('/deleteContact')
    print('aaaa')
    print(res.data)
    assert res.status_code == 302
  
   
    
def test_login2(client):
    res = client.get('/login')
    print(res)
    assert res.status_code == 200

    
    
def test_register(client):
    res = client.get('/register')
    print(res)
    assert res.status_code == 200
    assert b"Birthday" in res.data
    assert b"ID number" in res.data
    

def test_validateUser(client):
    res =  client.post('/validateUser')
    print(res.data)
    assert res.status_code == 200
    assert b"nameResult" in res.data
    

