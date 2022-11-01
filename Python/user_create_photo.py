from tkinter import Frame
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import re
import numpy as np
import os
from sqlalchemy import false
from Face_detection import *
from __default__ import NoMask_DB_Path
from completion.face_detection.detector import RetinaFace
embedding_list = []
class FrameGrabber(QtCore.QThread):
    def __init__(self, parent=None):
        super(FrameGrabber, self).__init__(parent)
        self.cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)
        self.frame = None
        self.save_file = None
        self.score = 0.1
    signal = QtCore.pyqtSignal(QtGui.QImage)
    def run(self):
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        while True:
            self.success, self.frame = self.cap.read()
            if self.success:
                detector = RetinaFace(0)
                self.save_file = self.frame
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                
                faces = detector(self.frame)
                if not faces == []:
                    box, landmarks, self.score = faces[0]
            #print(score)
                if self.score >= 0.93:
                    box = box.astype(np.int)
                    cv2.rectangle(self.frame, (box[0], box[1]), (box[2], box[3]), color=(255, 0, 0), thickness=2)
            try:
                image = QtGui.QImage(self.frame, self.frame.shape[1], self.frame.shape[0], QtGui.QImage.Format_RGB888)
                self.signal.emit(image)
            except:
                continue
                
    def stop(self):
        self.cap.release()
class Ui_user_photo(object):
    def __init__(self,message):
        self.name = message
    def setupUi(self, Dialog):
        Dialog.setObjectName("사진 촬영")
        Dialog.resize(660, 550)
        self.count = 0
        self.grabber = FrameGrabber()
        self.grabber.signal.connect(self.updateFrame)
        self.grabber.start()
        self.Photo = QtWidgets.QPushButton(Dialog)
        self.Photo.setGeometry(QtCore.QRect(10, 500, 640, 40))
        self.Photo.setObjectName("Photo")
        self.Photo.clicked.connect(lambda : self.Take_photo(self.name,self.grabber.save_file,self.grabber.score, Dialog))
        #self.Back = QtWidgets.QPushButton(Dialog)
        #self.Back.setGeometry(QtCore.QRect(335, 500, 315, 40))
        #self.Back.setObjectName("Back")
        #self.Back.clicked.connect(lambda : self.close_video(Dialog, self.name))
        self.Video = QtWidgets.QLabel(Dialog)
        self.Video.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.Video.setText("")
        self.Video.setObjectName("Video")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("Dialog", "사진 촬영"))
        self.Photo.setText(_translate("Dialog", "사진 촬영" + "("+ str(self.count) + "장" + ")"))
        #self.Back.setText(_translate("Dialog", "돌아가기"))

    def Take_photo(self, StudentID, frame, score, Dialog):
        global embedding_list
        file_path = ""
        numbers = ""
            
        NoMask_folder_name = NoMask_DB_Path +"/"+ str(StudentID)
        if score > 0.9:
             
            for (root, directories, files) in os.walk(NoMask_folder_name):
                for file in files:
                    if '.jpg' in file:
                        file_path = os.path.join(root, file)
                        
                        
            if file_path == "":
                file_path = NoMask_folder_name+ "/" + str(StudentID) + "_000.jpg" 
                            
            numbers = re.sub(r'[^0-9]', '', file_path)
            numbers = int(numbers) % 1000;
            numbers = format(numbers, '03')
            a1 = file_path.replace("_"+str(numbers), "")
            a2 = a1.replace(".jpg", "")
            numbers = int(numbers) + 1
            numbers = format(numbers, '03')
            cameraimg_path = str(a2)+ "_" + numbers +".jpg"
            cameraimg_path = cameraimg_path.replace("\\", "/")
            print(cameraimg_path)
            cv2.imwrite(cameraimg_path, frame)
            with open("C:/AHard/Project/user_img/User_Register.txt", "a") as f:
                f.write(cameraimg_path+'\n')
            if self.count == 4:
                Dialog.close()
            self.count = self.count + 1
            self.Photo.setText("사진 촬영" + "("+ str(self.count) + "장" + ")")    
    

    def updateFrame(self, image):
        self.Video.setPixmap(QtGui.QPixmap.fromImage(image))
    def close_video(self,Dialog,StudentID):
        if self.count == 4:
            First_pickle()
            for i in embedding_list:
            # 파일 피클 파일 생성
                embedding = DE.represent(img_path = i, enforce_detection = False )
                user_embedding = [i, embedding]

                with open(default.PKL_NoMask_Path ,"ab") as train:
                    pickle.dump(user_embedding, train)
                mask_embed_save(i,StudentID)
            self.grabber.stop()
            embedding_list = []
            Dialog.close()
        self.count = self.count + 1
        self.Photo.setText("사진 촬영" + "("+ str(self.count) + "장" + ")")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_user_photo()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
