from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user_error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("회원가입 실패")
        Dialog.resize(420, 120)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(170, 70, 80, 41))
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(lambda: self.sign_error(Dialog))
        self.Error_str = QtWidgets.QLabel(Dialog)
        self.Error_str.setGeometry(QtCore.QRect(60, 30, 290, 30))
        self.Error_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Error_str.setObjectName("Complete_str")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("Dialog", "회원가입 실패"))
        self.OK.setText(_translate("Dialog", "돌아가기"))
        self.Error_str.setText(_translate("Dialog", "모든정보를 입력해주세요."))
    def sign_error(self, Dialog):
        Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_user_error()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
