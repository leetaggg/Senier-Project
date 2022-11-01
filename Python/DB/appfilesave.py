# app 에서 사진 찍은 경우
# 피클 리스트 만들기
# 마스크 벗은 얼굴
import os
import sys
import mysql.connector
from mysql.connector import Error

from completion.deep.deepface import DeepFace as DE
import os
import cv2
import re
import pickle
import numpy as np
import time
from completion.face_detection.detector import RetinaFace
import __default__ as default
import shutil
import gc
import torch




# app 파일 매칭
def app_verify(Name):                               # 수정 5/23
    print("매칭 중 : " + str(Name))
    app_file_list = []
    for (root, directories, files) in os.walk(default.Photo_Path):
                                for file in files:
                                    if str(Name) in file:
                                        file_path = os.path.join(root, file)
                                        file_path = file_path.replace("\\", "/")
                                        app_file_list.append(file_path)
    one, two = 0,-1
    for_exit = False     
    for i in range(0,len(app_file_list)):
        one = i
        for j in range(1,len(app_file_list)):
            two = j
            if i < j:                
                try:
                    result = DE.verify(img1_path = app_file_list[i], img2_path = app_file_list[j])
                    print(result)
                    if result['distance'] > 0.55:               # 거리값 
                        for_exit = True
                        print("사진 안맞음")
                        break 
                except:
                    for_exit = True
                    print("얼굴인식 안됨")
                    break
        if for_exit:
            break
        

    if for_exit == False and one == two:                                  #사진이 맞을때
        print("다 맞음")
        pickle_upload(app_file_list, Name)        # 사진 저장
        try:
            os.rmdir(default.Photo_Path +"/"+ Name)
        except OSError:
            print("디렉터리가 비어 있지 않습니다")    
        try:
            connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

            cursor = connection.cursor(prepared = True)
            sql = 'UPDATE user SET renewal = 3 WHERE userID = %s;'

            data = (str(Name), )
            cursor.execute(sql, data)
            connection.commit()
            print("업로드 완료")

        except mysql.connector.Error as error:
            print("업로드 실패 {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("접속 종료")      
    elif for_exit:                                   # 사진이 매칭 안될 때(삭제)
        print("매칭안된 파일\n" + app_file_list[one] +"\n" +app_file_list[two])
        for k in app_file_list:
            if os.path.isfile(k):
                os.remove(k)
        try:
            os.rmdir(default.Photo_Path +"/"+ Name)
        except OSError:
            print("디렉터리가 비어 있지 않습니다")        
        print("delete :" + str(app_file_list))
        
        try:
            connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

            cursor = connection.cursor(prepared = True)
            sql = 'UPDATE user SET renewal = 2 WHERE userID = %s;'

            data = (str(Name), )
            cursor.execute(sql, data)
            connection.commit()
            print("업로드 완료")

        except mysql.connector.Error as error:
            print("업로드 실패 {}".format(error))

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("접속 종료")
    


def pickle_upload(list, Name):
    path = ""
    b = []
    
    Save_Folder_Path = default.NoMask_DB_Path + "/" + str(Name)         # 폴더 없으면 생성
    Save_MaFolder_Path = default.Mask_DB_Path +"/"+ str(Name)
    try:
        if not os.path.exists(Save_Folder_Path):
            os.makedirs(Save_Folder_Path)
        if not os.path.exists(Save_MaFolder_Path):
            os.makedirs(Save_MaFolder_Path)    
    except OSError:
        print("Error: Failed to create the directory.")
    
    for (root, directories, files) in os.walk(Save_Folder_Path):
                                for file in files:
                                    if str(Name) in file:
                                        path = os.path.join(root, file)
                                        path = path.replace("\\", "/")
    if path == "":
       path = Save_Folder_Path + "/" + str(Name) +"_000.jpg"
       
    number = re.sub(r'[^0-9]', '', path)
    number = int(number) % 1000;
    number = format(number, '03')
    a1 = path.replace("_"+str(number), "")
    a2 = a1.replace(".jpg", "")
    number = int(number) + 1
    number = format(number, '03')
    Save_File_Path = str(a2) + "_" +number +".jpg"
    Save_File_Path = Save_File_Path.replace("\\", "/") 
    
    
        
    for k in list:
            
        shutil.move(k, Save_File_Path)
        b.append(Save_File_Path)
            
        number = re.sub(r'[^0-9]', '', Save_File_Path)
        number = int(number) % 1000;
        number = format(number, '03')
        a1 = Save_File_Path.replace("_"+str(number), "")
        a2 = a1.replace(".jpg", "")
        number = int(number) + 1
        number = format(number, '03')
        Save_File_Path = str(a2) + "_" +number +".jpg"
        Save_File_Path = Save_File_Path.replace("\\", "/")
            
    
    for i in b:
        embedding = DE.represent(img_path = i)
        user_embedding = [i, embedding]
        with open(default.PKL_NoMask_Path,"ab") as train:
            pickle.dump(user_embedding, train)
        mask_embed_save(i,str(Name))                      # mask 임베딩

    print("업로드 및 nomask 사진 이동 완료")
                
    
def mask_embed_save(img_path, Name):        # 마스크
    folder = default.Mask_DB_Path +"/"+ str(Name)   
    img1 = cv2.imread(img_path)
    detector = RetinaFace(0)
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    faces = detector(img)
    if not faces == []:
        box, landmarks, score = faces[0]
            
    box = box.astype(np.int)
        
    b = box[3] + box[1]
    b = b / 100 * 50
    mask_file_path = ""    
    save_file = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.rectangle(save_file, (box[0], int(b)), (box[2], box[3]), color=(255, 255, 255), thickness=-1)
    for (root, directories, files) in os.walk(folder):
        for file in files:
            if '.jpg' in file:
                mask_file_path = os.path.join(root, file)
                
    if mask_file_path == "":
        mask_file_path = folder + "/" + str(Name) + "_000.jpg" 
        
    numbers = re.sub(r'[^0-9]', '', mask_file_path)
    numbers = int(numbers) % 1000;
    numbers = format(numbers, '03')
    a1 = mask_file_path.replace("_" + str(numbers), "")
    a2 = a1.replace(".jpg", "")
    #print(numbers)
    numbers = int(numbers) + 1
    numbers = format(numbers, '03')
    mask_cameraimg_path = str(a2) + "_" + numbers +".jpg"
    mask_cameraimg_path = mask_cameraimg_path.replace("\\", "/")
                                    
    cv2.imwrite(mask_cameraimg_path, save_file)        
    #print(mask_cameraimg_path)  
    embedding = DE.represent(img_path = mask_cameraimg_path)
    user_embedding = [mask_cameraimg_path, embedding]
    with open(default.PKL_Mask_Path ,"ab") as train:
        pickle.dump(user_embedding, train) 
        print("업로드 끝")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gc.collect()
    torch.cuda.empty_cache()
