from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user_delete_complete(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("회원 삭제 완료")
        Dialog.resize(420, 117)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(160, 70, 101, 41))
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(Dialog.close)
        self.Complete_str = QtWidgets.QLabel(Dialog)
        self.Complete_str.setGeometry(QtCore.QRect(65, 30, 290, 30))
        self.Complete_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Complete_str.setObjectName("Complete_str")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("Dialog", "회원 삭제 완료"))
        self.OK.setText(_translate("Dialog", "돌아가기"))
        self.Complete_str.setText(_translate("Dialog", "회원정보를 삭제했습니다."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_user_delete_complete()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())