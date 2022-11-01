from PyQt5 import QtCore, QtGui, QtWidgets
from Attend_List import Ui_User_Attend_List
import cv2
from Face_detection import *


class Ui_choose_student_name(object):
    def __init__(self,message, path, img):
        self.name = message
        self.File_path = path
        self.Student_img = img
    def setupUi(self, Dialog):
        Dialog.setObjectName("학번 정보")
        Dialog.resize(420, 117)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(80, 70, 100, 37))
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(lambda : self.show_list(Dialog))
        self.Complete_str = QtWidgets.QLabel(Dialog)
        self.Complete_str.setGeometry(QtCore.QRect(65, 30, 290, 30))
        self.Complete_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Complete_str.setObjectName("Complete_str")
        self.Back = QtWidgets.QPushButton(Dialog)
        self.Back.setGeometry(QtCore.QRect(240, 70, 100, 37))
        self.Back.setObjectName("Back")        
        self.Back.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "학번 정보"))
        self.OK.setText(_translate("Dialog", "출석하기"))
        self.Complete_str.setText(_translate("Dialog", str(self.name) + "님이 맞습니까?"))
        self.Back.setText(_translate("Dialog", "돌아가기"))
        
    def show_list(self, Dialog):
        cv2.imwrite(self.File_path,self.Student_img)
        save_list(self.File_path)
        self.window = QtWidgets.QDialog()
        self.ui = Ui_User_Attend_List(self.name)
        self.ui.setupUi(self.window)
        self.window.show()#창전환
        Dialog.close()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_choose_student_name()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
