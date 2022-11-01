from PyQt5 import QtCore, QtGui, QtWidgets
import time
from user_create_photo import Ui_user_photo
Window = None #이 창을 컨트롤 할수있는 포인터? 같은 개념
class Ui_Progress_bar(object):
    def setupUi(self, Dialog):
        global Window
        Dialog.setObjectName("Form")
        Dialog.resize(400, 105)
        Window = Dialog
        self.Complete_str = QtWidgets.QLabel(Dialog)
        self.Complete_str.setGeometry(QtCore.QRect(50, 40, 290, 30))
        self.Complete_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Complete_str.setObjectName("Complete_str")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Form", "Form"))
        self.Complete_str.setText(_translate("Form", "창 내용."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Progress_bar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
