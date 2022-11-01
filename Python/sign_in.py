from PyQt5 import QtCore, QtGui, QtWidgets
from DB.login import *
from sign_in_complete import Ui_sign_in_complete
from sign_in_error import Ui_sign_in_error

class Ui_user_sign_in(object):
    def Login_check(self, Dialog):
        ID = self.ID.text()
        PW = self.PW.text()
        if(login(ID,PW)):
            self.window = QtWidgets.QDialog()
            self.ui = Ui_sign_in_complete()
            
            self.ui.setupUi(self.window)
            self.window.show()
            Dialog.close()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_sign_in_error()
            self.ui.setupUi(self.window)
            self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("로그인")
        Dialog.resize(390, 194)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ID_explain = QtWidgets.QLabel(Dialog)
        self.ID_explain.setGeometry(QtCore.QRect(10, 10, 24, 16))
        self.ID_explain.setObjectName("ID_explain")
        self.PW_explain = QtWidgets.QLabel(Dialog)
        self.PW_explain.setGeometry(QtCore.QRect(10, 75, 48, 16))
        self.PW_explain.setObjectName("PW_explain")
        self.Back = QtWidgets.QPushButton(Dialog)
        self.Back.setGeometry(QtCore.QRect(180, 145, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Back.setFont(font)
        self.Back.setObjectName("Back")
        self.Complete = QtWidgets.QPushButton(Dialog)
        self.Complete.setGeometry(QtCore.QRect(290, 145, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Complete.setFont(font)
        self.Complete.setObjectName("Complete")
        self.PW = QtWidgets.QLineEdit(Dialog)
        self.PW.setGeometry(QtCore.QRect(10, 95, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PW.setFont(font)
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW.setObjectName("PW")
        self.ID = QtWidgets.QLineEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(10, 30, 370, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID.setFont(font)
        self.ID.setText("")
        self.ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ID.setObjectName("ID")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("user_create", "관리자 모드 로그인"))
        self.ID_explain.setText(_translate("user_create", "학번"))
        self.PW_explain.setText(_translate("user_create", "비밀번호"))
        self.Back.setText(_translate("user_create", "돌아가기"))
        self.Complete.setText(_translate("user_create", "로그인"))
        self.PW.setPlaceholderText(_translate("user_create", "비밀번호를 입력해주세요."))
        self.ID.setPlaceholderText(_translate("user_create", "학번을 입력해주세요."))
        self.Back.clicked.connect(Dialog.close)
        self.Complete.clicked.connect(lambda :self.Login_check(Dialog))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_create = QtWidgets.QDialog()
    ui = Ui_user_sign_in()
    ui.setupUi(user_create)
    user_create.show()
    sys.exit(app.exec_())
