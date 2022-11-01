from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Temp_error(object):
    def __init__(self, Temp):
        self.Temp = Temp
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 150)
        self.Back = QtWidgets.QPushButton(Dialog)
        self.Back.setGeometry(QtCore.QRect(170, 95, 80, 41))
        self.Back.setObjectName("Back")
        Complete_font = QtGui.QFont()
        Complete_font.setPointSize(15)
        Complete_font.setWeight(75)
        self.Complete_str = QtWidgets.QLabel(Dialog)
        self.Complete_str.setGeometry(QtCore.QRect(55, 20, 310, 30))
        self.Complete_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Complete_str.setObjectName("Complete_str")
        self.Complete_str.setFont(Complete_font)
        self.Complete_str.setStyleSheet("Color : red")
        Temp_font = QtGui.QFont()
        Temp_font.setPointSize(13)
        Temp_font.setWeight(75)
        self.Temp_str = QtWidgets.QLabel(Dialog)
        self.Temp_str.setGeometry(QtCore.QRect(125, 60, 165, 20))
        self.Temp_str.setFont(Temp_font)
        self.Temp_str.setObjectName("Temp_str")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "제한"))
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.Back.setText(_translate("Dialog", "돌아가기"))
        self.Back.clicked.connect(Dialog.close)
        self.Complete_str.setText(_translate("Dialog", "※현재 체온이 너무 높습니다!!※"))
        self.Temp_str.setText(_translate("Dialog", "현재 체온 :"+ " " +str(self.Temp) +"°C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Temp_error()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
