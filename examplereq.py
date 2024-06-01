import requests 
r = requests.post('http://127.0.0.1:5001/api/writeplace', json={"key": "6258a5e0eb772911d4f92be5b5db0e14511edbe01d1d0ddd1d5a2cb9db9a56ba", "name": "salve", "loc": (1.0, 2.0), "rating": 0, "imgurl": "nope"})
print(r.status_code)