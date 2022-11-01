import numpy as np
from completion.face_detection.detector import RetinaFace
from completion.deep.deepface import DeepFace as DE
import time
import os
import pickle
import re
from pathlib import Path
import __default__ as default
import cv2

#------------------------

DB_Path = default.Mask_DB_Path
default_PKL = default.PKL_Mask_Path
Modal_Name = 'ArcFace'
Distance_Metric = 'cosine'
Detector_Backend = 'retinaface'

mask_file_patha = ""
embedding_list_No = []
file_list = []
count = 0
embedding_list = []


#------------------------
count = 0
down = 0.35
up = 0.05
embedding_list_No = []
embedding_list_Ma = []
fail_count = 0                           
                            
#피클파일 저장                            
def save_pickle():
    print("파일 추가중입니다.")
    with open("C:/AHard/Project/NoMask.txt") as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    for i in lines:
        embedding = DE.represent(img_path = i)
        path_embedding = [i, embedding]
        with open(default.PKL_NoMask_Path,"ab") as train:
            pickle.dump(path_embedding, train)
    
    with open("C:/AHard/Project/Mask.txt") as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    for i in lines:
        embedding = DE.represent(img_path = i)
        path_embedding = [i, embedding]
        with open(default.PKL_Mask_Path,"ab") as train:
            pickle.dump(path_embedding, train)    
    print("파일 추가 완료")
    with open('C:/AHard/Project/NoMask.txt','w',encoding='UTF-8') as f:
            pass
    with open('C:/AHard/Project/Mask.txt','w',encoding='UTF-8') as f:
            pass
    #os.remove('NoMask.txt')
    #os.remove('Mask.txt')
    
def save_list(path):
    print(path)
    
    if "NoMask" in path:
        with open('C:/AHard/Project/NoMask.txt','a',encoding='UTF-8') as f:
                f.write(path +'\n')
    else: 
        with open('C:/AHard/Project/Mask.txt','a',encoding='UTF-8') as ff:
                ff.write(path +'\n') 
    
    #불러오기        
    '''
    file_path = "Nomask.txt"
    with open(file_path) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    #print(lines)
    '''

def mask_embed_save(img_path, Myname):
    Mask_folder_name =default.Mask_DB_Path+  "/" + Myname
    img1 = cv2.imread(img_path)
    detector = RetinaFace(0)
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    faces = detector(img)
    if not faces == []:
        box, landmarks, score = faces[0]
    else:
        box, landmarks, score = [], [], 0        
    box = box.astype(np.int)
        
    b = box[3] + box[1]
    b = b / 100 * 50
    mask_file_path = ""    
    save_file = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.rectangle(save_file, (box[0], int(b)), (box[2], box[3]), color=(255, 255, 255), thickness=-1)
    for (root, directories, files) in os.walk(Mask_folder_name):
        for file in files:
            if '.jpg' in file:
                mask_file_path = os.path.join(root, file)
                
    if mask_file_path == "":
        mask_file_path = Mask_folder_name+ "/" + Myname + "_000.jpg" 
   
    numbers = re.sub(r'[^0-9]', '', mask_file_path)
    numbers = int(numbers) % 1000;
    numbers = format(numbers, '03')
    a1 = mask_file_path.replace("_"+str(numbers), "")
    a2 = a1.replace(".jpg", "")
    #print(numbers)
    numbers = int(numbers) + 1
    numbers = format(numbers, '03')
    cameraimg_path = str(a2) + "_" +numbers +".jpg"
    cameraimg_path = cameraimg_path.replace("\\", "/")
                                    
    cv2.imwrite(cameraimg_path, save_file)
    embedding = DE.represent(img_path = cameraimg_path)
    user_embedding = [cameraimg_path, embedding]
    
    with open(default.PKL_Mask_Path ,"ab") as train:
        pickle.dump(user_embedding, train)   
        
'''
def embedding_save(path):
    embedding_path = path
    embedding = DE.represent(img_path = embedding_path)
    user_embedding = [embedding_path, embedding]
    
    with open(default.PKL_NoMask_Path ,"ab") as train:
        pickle.dump(user_embedding, train)
'''
        
'''
def embedding_save(path):
    embedding_path = path
    embedding = DE.represent(img_path = embedding_path)
    user_embedding = [embedding_path, embedding]
    
    with open(default.PKL_NoMask_Path ,"ab") as train:
        pickle.dump(user_embedding, train)
'''
'''
def save_pickle_File():
    First_Path =[default.Mask_DB_Path, default.NoMask_DB_Path]
    file_list = []

    for i in First_Path: 
        for (root, directories, files) in os.walk(i):
            for file in files:
                if '.pkl' in file:
                   file_path = os.path.join(root, file)
                   file_list.append(file_path)
                   
    if len(file_list) > 1:
        print("파일 다 있음")
    else:
        try:
            print("파일 생성 중")
            #try 안해주면 피클 생성하고 에러 뜨면서 멈춤
            a = DE.find(img_path=default.ex_img, db_path=default.Mask_DB_Path, 
                        enforce_detection=False)
        except:
            try:
            #피클파일 완성되고 코드 실행
                a = DE.find(img_path=default.ex_img, db_path=default.NoMask_DB_Path,
                    enforce_detection=False)
            except:
                print("생성됨")
'''    
                
def First_pickle():
    DB_Patha =[default.Mask_DB_Path, default.NoMask_DB_Path]
    file_list = []
    for i in DB_Patha: 
        for (root, directories, files) in os.walk(i):
            for file in files:
                if '.pkl' in file:
                   file_path = os.path.join(root, file)
                   file_path = file_path.replace("\\", "/")
                   file_list.append(file_path)
                   
    if default.PKL_Mask_Path not in file_list:
        with open(default.PKL_Mask_Path,"wb") as traina:
            pickle.dump(default.empty_pkl, traina)
            
    if default.PKL_NoMask_Path not in file_list:
        with open(default.PKL_NoMask_Path,"wb") as trainb:
            pickle.dump(default.empty_pkl, trainb)
            
def img_save(path):
    numbers = re.sub(r'[^0-9]', '', path)
    numbers = int(numbers) % 1000
    numbers = format(numbers, '03')
    a1 = path.replace("_"+str(numbers), "")
    a2 = a1.replace(".jpg", "")
    numbers = int(numbers) + 1
    numbers = format(numbers, '03')
    cameraimg_path = str(a2)+ "_" + numbers +".jpg"
    cameraimg_path = cameraimg_path.replace("\\", "/")
    return cameraimg_path                              

First_pickle()