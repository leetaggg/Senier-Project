from pyrsistent import b
import requests
from requests import get
import os

def find_len(name):
    user_name = {"uname" : name}
    r = requests.post('http://39.124.26.132/Py_php/dirlen.php', user_name)
    a = r.text
    return int(a)

def srv_img(user_name, path):
    length = find_len(user_name)
    for i in range(1, length + 1):
        file_num = format(i, '03')
        url = "http://39.124.26.132/user_img/" + user_name + "/"+ user_name + "_" + file_num + ".jpg"
        with open(path + "/" + user_name + "_" + file_num +".jpg", "wb") as file:
            response = get(url)
            file.write(response.content)
            
def img_download(user_name, path):
    user_path = path + "/" + user_name + "/"
    if not os.path.exists(user_path):
        os.makedirs(user_path)
        srv_img(user_name, path)
    else:
        srv_img(user_name, path)
            

