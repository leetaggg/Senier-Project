from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Save_Error(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 117)
        self.Back = QtWidgets.QPushButton(Dialog)
        self.Back.setGeometry(QtCore.QRect(170, 70, 80, 41))
        self.Back.setObjectName("Back")
        self.Error_str = QtWidgets.QLabel(Dialog)
        self.Error_str.setGeometry(QtCore.QRect(65, 30, 290, 30))
        self.Error_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Error_str.setObjectName("Error_str")
        self.Back.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "파일 저장 실패"))
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.Back.setText(_translate("Dialog", "돌아가기"))
        self.Error_str.setText(_translate("Dialog", "파일을 저장하지 못했습니다."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Save_Error()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
