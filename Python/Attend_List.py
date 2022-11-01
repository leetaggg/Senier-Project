from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import time
from DB.attendance import atd_check # 출석 데이터 and 학번데이터
""" 리스트중 NONE이 아닌것을 탐색하여 갯수를 파악한후 N주차 까지 출력
    for i in range(길이):
        if (index[i] == None):
            retrun
        else:
            value++"""
Window = None #이 창을 컨트롤 할수있는 포인터? 같은 개념
Week = ["1주차", "2주차", "3주차", "4주차", "5주차"]
class Waiting_Time(QtCore.QThread):
    Time_value = QtCore.pyqtSignal(int)
    def run(self):
        for i in range(5, -1, -1):
            self.Time_value.emit(i)
            time.sleep(1)
            #n초뒤에 창이 닫힙니다.
class Ui_User_Attend_List(object):
    def __init__(self, message):
        self.name = message
    def setupUi(self, Dialog):
        global Window
        Dialog.setObjectName("출석확인")
        Dialog.resize(400, 312)
        Window = Dialog
        self.count = 0
        self.Week = []
        self.Waiting_Thread = Waiting_Time()
        self.Waiting_Thread.Time_value.connect(self.Print_Time)
        self.Waiting_Thread.start()
        self.Student_ID_info = QtWidgets.QLabel(Dialog)
        self.Student_ID_info.setGeometry(QtCore.QRect(10, 10, 380, 20))
        self.Student_ID_info.setObjectName("Student_ID_info")
        self.Student_ID_info.setAlignment(Qt.AlignCenter)
        self.Waiting_info = QtWidgets.QLabel(Dialog)
        self.Waiting_info.setGeometry(QtCore.QRect(10, 280, 380, 20))
        self.Waiting_info.setObjectName("Waiting_info")
        self.Waiting_info.setAlignment(Qt.AlignCenter)
        self.Attend_data = atd_check(self.name)#학번에 해당하는 열을 불러온다.
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.isCornerButtonEnabled()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#수정이 불가능하게
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 380, 230))
        #self.tableWidget.setRowCount(5)  # 행 갯수 지정
        self.tableWidget.setColumnCount(1)  # 열갯수 지정
        self.tableWidget.setHorizontalHeaderLabels(self.Attend_data[0].split())  # 열 내용 지정
        self.tableWidget.setVerticalHeaderLabels(["1주차", "2주차", "3주차", "4주차", "5주차"])  # 행 항목 지정
        print(atd_check(self.name))
        """self.tableWidget.setRowHeight(0, 0.2 * 230)
        self.tableWidget.setRowHeight(1, 0.2 * 230)
        self.tableWidget.setRowHeight(2, 0.2 * 230)
        self.tableWidget.setRowHeight(3, 0.2 * 230)
        self.tableWidget.setRowHeight(4, 0.2 * 230)"""
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setObjectName("tableView")
        self.retranslateUi(Dialog)
        for i in range(1,len(self.Attend_data) + 1):
            if self.Attend_data[i] != None:
                self.count = self.count + 1;
                self.Week.append(Week[i - 1])
            else:
                break
        self.tableWidget.setRowCount(self.count)
        print(self.Week)
        self.tableWidget.setVerticalHeaderLabels(self.Week)
        for i in range(1,self.count + 1):
            if self.Attend_data[i] != None:
                self.tableWidget.setRowHeight(i -1, int(0.2 * 230))
                self.tableWidget.setItem(0, i - 1 , QTableWidgetItem(self.Attend_data[i]))
                item = self.tableWidget.item(i - 1,0)
                item.setTextAlignment(Qt.AlignCenter)
            else:
                break
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def Print_Time(self, Time):
        if Time == 0:
            Window.close()
        self.Waiting_info.setText(str(Time) + "초 뒤에 창이 닫힙니다.")
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Dialog.setWindowTitle(_translate("Form", "출석 확인"))
        self.Student_ID_info.setText(_translate("Form", str(self.name) + "님의 출석 현황입니다."))
        self.Waiting_info.setText(_translate("Form", "남은초"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_User_Attend_List()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
