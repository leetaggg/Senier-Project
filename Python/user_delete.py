from PyQt5 import QtCore, QtGui, QtWidgets
from DB.user_list import user_list
from user_delete_error import Ui_user_delete_error
from user_delete_complete import Ui_user_delete_complete
from DB.delete import user_remove
import __default__ as default
import shutil 
import os
import pickle

class Ui_user_delete(object):
    def information_remove(self, name, Dialog):
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
            dir_pathf = Dir +"/"+ str(name)
            if os.path.exists(dir_pathf):
                shutil.rmtree(dir_pathf)
        Dialog.close
        
    def information_check(self, Dialog):
        ID = self.ID.text()
        PW = self.PW.text()
        if ID and PW:
            user_remove(ID)
            user_list()
            self.window = QtWidgets.QDialog()
            self.ui = Ui_user_delete_complete()
            self.ui.setupUi(self.window)
            self.window.show()
            Dialog.close()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_user_delete_error()
            self.ui.setupUi(self.window)
            self.window.show()
    def setupUi(self, user_delete):
        user_delete.setObjectName("회원삭제")
        user_delete.resize(390, 194)
        user_delete.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ID_explain = QtWidgets.QLabel(user_delete)
        self.ID_explain.setGeometry(QtCore.QRect(10, 10, 24, 16))
        self.ID_explain.setObjectName("ID_explain")
        self.PW_explain = QtWidgets.QLabel(user_delete)
        self.PW_explain.setGeometry(QtCore.QRect(10, 75, 48, 16))
        self.PW_explain.setObjectName("PW_explain")
        self.Back = QtWidgets.QPushButton(user_delete)
        self.Back.setGeometry(QtCore.QRect(180, 145, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.Back.clicked.connect(user_delete.close)
        self.Complete = QtWidgets.QPushButton(user_delete)
        self.Complete.setGeometry(QtCore.QRect(290, 145, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Complete.setFont(font)
        self.Complete.setObjectName("Complete")
        self.Complete.clicked.connect(lambda : self.information_check(user_delete))
        self.PW = QtWidgets.QLineEdit(user_delete)
        self.PW.setGeometry(QtCore.QRect(10, 95, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PW.setFont(font)
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW.setObjectName("PW")
        self.ID = QtWidgets.QLineEdit(user_delete)
        self.ID.setGeometry(QtCore.QRect(10, 30, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID.setFont(font)
        self.ID.setText("")
        self.ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ID.setObjectName("ID")

        self.retranslateUi(user_delete)
        QtCore.QMetaObject.connectSlotsByName(user_delete)

    def retranslateUi(self, user_delete):
        _translate = QtCore.QCoreApplication.translate
        user_delete.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        user_delete.setWindowTitle(_translate("user_create", "회원 삭제"))
        self.ID_explain.setText(_translate("user_create", "학번"))
        self.PW_explain.setText(_translate("user_create", "비밀번호"))
        self.Back.setText(_translate("user_create", "돌아가기"))
        self.Complete.setText(_translate("user_create", "삭제하기"))
        self.PW.setPlaceholderText(_translate("user_create", "비밀번호를 입력해주세요."))
        self.ID.setPlaceholderText(_translate("user_create", "학번을 입력해주세요."))
        self.Complete.clicked.connect(lambda : self.information_remove(self.ID.text(),user_delete))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_delete = QtWidgets.QDialog()
    ui = Ui_user_delete()
    ui.setupUi(user_delete)
    user_delete.show()
    sys.exit(app.exec_())