import requests
from PIL import Image

img=Image.open(r"test.jpg")
URL = "http://127.0.0.1:8000/cu/ica"
data={
    "id": "10",
    "name": "python ",
    "text": "python for every budy",
    "Reference": "https://www.coursera.com",
    "time": 2,
    "img": img,
    "time": 3
}
r = requests.post(url =URL , data = data)
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)