#돌아가기 눌렀을때 피클파일 삭제 및 사진 삭제
from PyQt5 import QtCore, QtGui, QtWidgets
from user_create_complete import Ui_user_complete
from user_create_error import Ui_user_error
from user_create_photo import Ui_user_photo
from mysql.connector import Error
from DB.register import register
from DB.user_list import user_list
from sqlalchemy import false
from Face_detection import *
from __default__ import *
from completion.face_detection.detector import RetinaFace
import os
import shutil

class Ui_user_create(object):
    def Back_btn(self, ID, Dialog):
        if ID:
            if os.path.isdir(default.NoMask_DB_Path +"/"+ID) and os.path.isdir(default.Mask_DB_Path +"/"+ID) :
                shutil.rmtree(default.NoMask_DB_Path +"/"+ID)
                shutil.rmtree(default.Mask_DB_Path +"/"+ID)
                with open("C:/AHard/Project/user_img/User_Register.txt", "w") as f:
                    f.write("")  
                Dialog.close()
        else:
            Dialog.close()
    def information_check(self, Dialog):
        embedding_list = []
        ID = self.ID.text()
        NAME = self.NAME.text()
        PW = self.PW.text()
        GRADE = self.Grade.currentText()
        if ID and NAME and PW and GRADE: # 생성
            register(ID,PW,NAME,GRADE)
            First_pickle()
            with open('C:/AHard/Project/user_img/User_Register.txt', 'r') as file:
                line = None
                while line != '':
                    line = file.readline()
                    line = line.strip('\n')
                    embedding_list.append(line)
            print(embedding_list)
            del embedding_list[len(embedding_list)-1]
            for i in embedding_list:
        # 파일 피클 파일 생성
                embedding = DE.represent(img_path = i, enforce_detection = False )
                user_embedding = [i, embedding]
                with open(default.PKL_NoMask_Path ,"ab") as train:
                    pickle.dump(user_embedding, train)
                mask_embed_save(i,ID)
            embedding_list = []
            with open("C:/AHard/Project/user_img/User_Register.txt", "w") as f:
                f.write("")   
            user_list()
            self.window = QtWidgets.QDialog()
            self.ui = Ui_user_complete()
            self.ui.setupUi(self.window)
            self.window.show()
            Dialog.close()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_user_error()
            self.ui.setupUi(self.window)
            self.window.show()
    def take_photo(self):
        file = self.ID.text()
        if file:
            os.mkdir('C:/AHard/Project/user_img/NoMask/' + file)
            os.mkdir('C:/AHard/Project/user_img/Mask/' + file)
            self.window = QtWidgets.QDialog()
            self.ui = Ui_user_photo(file)
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_user_error()
            self.ui.setupUi(self.window)
            self.window.show()
    def setupUi(self, user_create):
        user_create.setObjectName("회원가입")
        user_create.resize(390, 411)
        user_create.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ID_explain = QtWidgets.QLabel(user_create)
        self.ID_explain.setGeometry(QtCore.QRect(10, 10, 24, 16))
        self.ID_explain.setObjectName("ID_explain")
        self.Name_explain = QtWidgets.QLabel(user_create)
        self.Name_explain.setGeometry(QtCore.QRect(10, 80, 24, 16))
        self.Name_explain.setObjectName("Name_explain")
        self.PW_explain = QtWidgets.QLabel(user_create)
        self.PW_explain.setGeometry(QtCore.QRect(10, 150, 48, 16))
        self.PW_explain.setObjectName("PW_explain")
        self.Photo_explain = QtWidgets.QLabel(user_create)
        self.Photo_explain.setGeometry(QtCore.QRect(10, 290, 24, 16))
        self.Photo_explain.setObjectName("Photo_explain")
        self.Back = QtWidgets.QPushButton(user_create)
        self.Back.setGeometry(QtCore.QRect(180, 360, 91, 41))
        self.Back.clicked.connect(lambda : self.Back_btn(self.ID.text(),user_create))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.Complete = QtWidgets.QPushButton(user_create)
        self.Complete.setGeometry(QtCore.QRect(290, 360, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Complete.setFont(font)
        self.Complete.setObjectName("Complete")
        self.Complete.clicked.connect(lambda: self.information_check(user_create))
        self.PW = QtWidgets.QLineEdit(user_create)
        self.PW.setGeometry(QtCore.QRect(10, 170, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PW.setFont(font)
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW.setObjectName("PW")
        self.NAME = QtWidgets.QLineEdit(user_create)
        self.NAME.setGeometry(QtCore.QRect(10, 100, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NAME.setFont(font)
        self.NAME.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NAME.setObjectName("NAME")
        self.ID = QtWidgets.QLineEdit(user_create)
        self.ID.setGeometry(QtCore.QRect(10, 30, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID.setFont(font)
        self.ID.setText("")
        self.ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ID.setObjectName("ID")
        self.Photo = QtWidgets.QPushButton(user_create)
        self.Photo.setGeometry(QtCore.QRect(10, 310, 370, 40))
        self.Photo.setObjectName("Photo")
        self.Photo.clicked.connect(lambda: self.take_photo())
        self.label = QtWidgets.QLabel(user_create)
        self.label.setGeometry(QtCore.QRect(10, 220, 22, 16))
        self.label.setObjectName("label")
        self.Grade = QtWidgets.QComboBox(user_create)
        self.Grade.setGeometry(QtCore.QRect(10, 240, 370, 40))
        self.Grade.setObjectName("Grade")
        self.Grade.addItem("")
        self.Grade.addItem("")
        self.Grade.addItem("")
        self.Grade.addItem("")

        self.retranslateUi(user_create)
        QtCore.QMetaObject.connectSlotsByName(user_create)

    def retranslateUi(self, user_create):
        _translate = QtCore.QCoreApplication.translate
        user_create.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        user_create.setWindowTitle(_translate("user_create", "회원가입"))
        self.ID_explain.setText(_translate("user_create", "학번"))
        self.Name_explain.setText(_translate("user_create", "이름"))
        self.PW_explain.setText(_translate("user_create", "비밀번호"))
        self.Photo_explain.setText(_translate("user_create", "사진"))
        self.Back.setText(_translate("user_create", "돌아가기"))
        self.Complete.setText(_translate("user_create", "생성하기"))
        self.PW.setPlaceholderText(_translate("user_create", "비밀번호를 입력해주세요."))
        self.NAME.setPlaceholderText(_translate("user_create", "이름을 입력해주세요."))
        self.ID.setPlaceholderText(_translate("user_create", "학번을 입력해주세요."))
        self.Photo.setText(_translate("user_create", "사진 촬영"))
        self.label.setText(_translate("user_create", "학년l"))
        self.Grade.setItemText(0, _translate("user_create", "1학년"))
        self.Grade.setItemText(1, _translate("user_create", "2학년"))
        self.Grade.setItemText(2, _translate("user_create", "3학년"))
        self.Grade.setItemText(3, _translate("user_create", "4학년"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_user_create()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())