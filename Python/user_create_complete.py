from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_user_complete(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("회원가입 성공")
        Dialog.resize(420, 120)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(170, 70, 80, 41))
        self.OK.setObjectName("OK")
        self.Complete_str = QtWidgets.QLabel(Dialog)
        self.Complete_str.setGeometry(QtCore.QRect(60, 30, 290, 30))
        self.Complete_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Complete_str.setObjectName("Complete_str")
        self.OK.clicked.connect(lambda : self.sign_end(Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("Dialog", "회원가입 성공"))
        self.OK.setText(_translate("Dialog", "돌아가기"))
        self.Complete_str.setText(_translate("Dialog", "회원가입을 완료했습니다."))
    def sign_end(self, Dialog):
        Dialog.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_user_complete()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
