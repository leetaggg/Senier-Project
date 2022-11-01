from pyrsistent import b
import requests
from requests import get
import requests
from mysql.connector import Error
import pickle
import __default__ as default
import shutil
import os
import urllib.request


def find_len(name):
    user_name = {"uname" : name}
    r = requests.post('http://39.124.26.132/Py_php/dirlen.php', user_name)
    a = r.text
    return int(a)

def srv_img(user_name, path):
    length = find_len(user_name)
    print(length)
    for i in range(1, length + 1):
        file_num = format(i, '03')
        url = "http://39.124.26.132/user_img/" + user_name + "/"+ user_name + "_" + file_num + ".jpg"
        urllib.request.urlretrieve(url, path + "/" + user_name + "/" + user_name + "_" + file_num + ".jpg")
        print("사진 저장하는 중")
            

def filelist():
    try:
        url = 'http://39.124.26.132/Py_php/filelist.php'
        r = requests.post(url)
        x = r.text
        x = x.split()
        del x[0:2]
        print(x)
    except:
        print("요청 오류")
    for i in range(0, len(x)):
        if(not os.path.isdir("C:/AHard/Project/user_img/Temp/"+x[i])):
            os.mkdir("C:/AHard/Project/user_img/Temp/"+x[i])
        
    if(len(x) != 0):
        for i in range(0, len(x)):
            srv_img(x[i], "C:/AHard/Project/user_img/Temp")
        
        try:
            url = 'http://39.124.26.132/Py_php/delete.php'
            
            for i in range(0, len(x)):
                name = {'uname':x[i]}
                r = requests.post(url, data=name)               
        except:
            print("요청 오류")
    else:
        print("서버에 파일이 없습니다.")
        
def delete_userlist():
    try:
        url = 'http://39.124.26.132/Py_php/stdid.php'
        r = requests.post(url)
        x = r.text
        x = x.split()
        del x[0:2]
    except:
        print("요청 오류")
    if(len(x) != 0):
        try:
            url = 'http://39.124.26.132/Py_php/stdiddelte.php'
            
            for i in range(0, len(x)):
                name = {'uname':x[i]}
                r = requests.post(url, data=name)
            
                
        except:
            print("요청 오류")
    return(x)

def delete_pickle(name):
        dir_path = [default.Mask_DB_Path,default.NoMask_DB_Path]
        for Dir in dir_path:
            a = []
            c = []
            pkl_file = Dir + "/Folder_PKL.pkl"
            with open(pkl_file ,"rb") as rd:
                data = pickle.load(rd)
                while 1:
                    try:
                        data.append(pickle.load(rd))
                    except EOFError:
                        break
            
            for i in range(0, len(data)):
                a.append(data[i][0])
            for i in range(0, len(a)):
                if str(name) in a[i]:
                    c.append(i)          
            for i in c:
                number = i - c.index(i)
                del data[number]
                del a [number]
                
            with open(pkl_file,"wb") as pkl:
                pickle.dump(data, pkl)
            dir_pathf = Dir+ "/" + str(name)
            if os.path.exists(dir_pathf):
                print(dir_pathf)
                shutil.rmtree(dir_pathf)