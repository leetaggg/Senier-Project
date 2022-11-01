from PyQt5 import QtCore, QtGui, QtWidgets
from DB.read import user_down,user_upload
from save_complete import Ui_Save_Complete
from save_error import Ui_Save_Error
class Ui_sign_in_complete(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("로그인 성공")
        Dialog.resize(420, 120)
        self.File_path = None
        self.Dir = None
        self.OK = QtWidgets.QPushButton(Dialog)
        self.OK.setGeometry(QtCore.QRect(280, 70, 100, 37))
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(Dialog.close)
        self.Complete_str = QtWidgets.QLabel(Dialog)
        self.Complete_str.setGeometry(QtCore.QRect(65, 20, 290, 30))
        self.Complete_str.setAlignment(QtCore.Qt.AlignCenter)
        self.Complete_str.setObjectName("Complete_str")
        self.File_Save = QtWidgets.QPushButton(Dialog)
        self.File_Save.setGeometry(QtCore.QRect(40, 70, 100, 37))
        self.File_Save.setObjectName("File_Save")
        self.File_Save.clicked.connect(lambda : self.File_Dir())
        self.File_Open = QtWidgets.QPushButton(Dialog)
        self.File_Open.setGeometry(QtCore.QRect(160, 70, 100, 37))
        self.File_Open.setObjectName("File_Open")
        self.File_Open.clicked.connect(lambda : self.File_choose())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("Dialog", "관리자 모드"))
        self.OK.setText(_translate("Dialog", "돌아가기"))
        self.File_Open.setText(_translate("Dialog", "파일 열기"))
        self.File_Save.setText(_translate("Dialog", "파일 저장"))
        self.Complete_str.setText(_translate("Dialog", "관리자모드로 진입하였습니다."))
    def File_choose(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None,"open File","","All Files(*)")
        if fname:
            self.File_path = fname[0]#파일 선택
            if user_upload(self.File_path):
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Save_Complete()
                self.ui.setupUi(self.window)
                self.window.show()#창전환
            else:
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Save_Error()
                self.ui.setupUi(self.window)
                self.window.show()#창전환
                            
    def File_Dir(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Folder')
        if fname:
            self.Dir_path = fname#파일 선택  
            if user_down(self.Dir_path+"/attendance.xlsx"):
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Save_Complete()
                self.ui.setupUi(self.window)
                self.window.show()#창전환
            else:
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Save_Error()
                self.ui.setupUi(self.window)
                self.window.show()#창전환
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_sign_in_complete()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
