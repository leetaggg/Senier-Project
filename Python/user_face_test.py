from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import cvlib as cv
from Face_detection import *
from socket import *
from retinaface import RetinaFace as Re
from choose_student_name import Ui_choose_student_name
from datetime import timedelta, datetime
from DB.attendance import atd_upload
from Temp_error import Ui_Temp_error

save_img = None
cameraimg = None
Face_Area = []
ip = "172.18.9.7"
port = 1127
clientSocket = socket(AF_INET, SOCK_STREAM)    
#1clientSocket.connect((ip,port))                                    #####
send_data = None
recv_data = None
StudentID = None
dddown = 9            # 0.6 > x > 0.05 mask
ddup = 0            # 0.45 > x # nomask
distest = []
Thread_Pause = True
class Temp_data_send(QtCore.QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self, parent = None):
        super(Temp_data_send, self).__init__(parent)
        global Thread_Pause
    def run(self):
        global Face_Area
        while Thread_Pause:
            if len(Face_Area) == 4:
                send_data = str(Face_Area)#데이터 수신
                #print(str(Face_Area))
                #1clientSocket.send(send_data.encode())              #######
                time.sleep(0.5)
class Temp_data_recv(QtCore.QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self, parent = None):
        super(Temp_data_recv, self).__init__(parent)
        global Thread_Pause
    def run(self):
        while Thread_Pause:
            global recv_data
            #1recv_data = clientSocket.recv(1024)#데이터 수신                #######
            #1recv_data = recv_data.decode("utf-8")                          #######
            time.sleep(1)
class Temp_Data(QtCore.QThread):
    def __init__(self, parent=None):
        super(Temp_Data, self).__init__(parent)
        global recv_data
        global Thread_Pause
    signal = QtCore.pyqtSignal(str)
    def run(self):
        while Thread_Pause:
            self.signal.emit(str(recv_data))
            time.sleep(1)
class Name_Data(QtCore.QThread):
    def __init__(self, parent=None):
        super(Name_Data, self).__init__(parent)
        global StudentID
        global Thread_Pause
    signal = QtCore.pyqtSignal(str)
    def run(self):
        while Thread_Pause:
            #print("결과:" + StudentID)
            self.signal.emit(str(StudentID))
            time.sleep(0.5)
class FrameGrabber(QtCore.QThread):
    def __init__(self, parent=None):
        super(FrameGrabber, self).__init__(parent)
        self.cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        self.star = time.time()
        self.DB_Path =  DB_Path
        self.default_PKL = default_PKL
        self.score = 0
    signal = QtCore.pyqtSignal(QtGui.QImage)
    def run(self):
        global Face_Area, StudentID,embedding_list_No,embedding_list_Ma, save_img, cameraimg
        StudentID = None
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        while True:
            ret, img = self.cap.read()
            if ret:
                detector = RetinaFace(0)
                save_imgone = img
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                faces = detector(img)
                #print(faces)
                if not faces == []:
                    box, landmarks, self.score = faces[0]
                if self.score >= 0.93:
                    end = time.time()
                    c = end - self.star
                    box = box.astype(np.int)
                    cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), color=(255, 0, 0), thickness=2)
                    
                    '''
                    b = box[3] + box[1]
                    b = b / 100 * 50
                    boximg = cv2.rectangle(img, (box[0], int(b)), (box[2], box[3]), color=(255, 255, 255), thickness=-1)'''
                    
                    Face_Area = box[0], box[1], box[2], box[3]
                    #cv2.imshow("", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
                    #cv2.putText(img, Final_Path, (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
                    
                    # 얼굴인식
                    
                    if c > 5:
                        
                        #df = DE.find(img_path=img, db_path=self.DB_Path, enforce_detection=False)
                        df = DE.find(img_path=img, db_path=self.DB_Path, enforce_detection=False)
                        save_img = save_imgone
                        
                        # 마스크 시 얼굴인식
                        try:
                            img_dis = df.iloc[0][1] 
                            if img_dis < dddown and img_dis > ddup:
                                dflist = []
                                all_number = None
                                df_count = 0
                                while len(dflist) < 10 or len(dflist) < len(df) - 1 :
                                    all_number = re.sub(r'[^0-9]', '', df.identity[df_count])
                                    rank_number = int(all_number) % 1000
                                    rank_number = format(rank_number, '03')
                                    id_number = df.identity[df_count].replace("_"+ rank_number + ".jpg", "")
                                    all_number = re.sub(r'[^0-9]', '', id_number)
                                    Final_id = int(all_number) % 100000000
                                    if dflist.count(Final_id) == 3:
                                        df_count += 1
                                        continue
                                    else:
                                        dflist.append(Final_id)
                                        df_count +=1
                                print(dflist)
                                    
                                
                                '''Name_Path = df.iloc[0]
                                First_Path = os.path.dirname(Name_Path[0])
                                First_Path = First_Path.replace("\\", "/")
                                Final_Path = First_Path.replace(default.Mask_DB_Path +"/", "")
                                Final_Path = Final_Path.replace(default.NoMask_DB_Path + "/", ")"'''
                                    
                                aaa = dflist
                                aaa.reverse()
                                result = list(set(aaa))
                                total_list = []
                                for l in result:
                                    ranking = list(filter(lambda x: aaa[x] == l, range(len(aaa))))
                                    total_list.append(sum(ranking))
                                    

                                list_index = total_list.index(max(total_list))
                                result[list_index]
                                id_str = df[df['identity'].str.contains(str(result))]
                                
                                First_Path = os.path.dirname(id_str.iloc[0][0])   
                                for (root, directories, files) in os.walk(First_Path):
                                    for file in files:
                                        if '.jpg' in file:
                                            file_path = os.path.join(root, file)
                                StudentID = result
                                print("학번은 : " + str(StudentID))
                                cameraimg = img_save(file_path)
                                #print(cameraimg)
                                #이미지 저장
                                #cv2.imwrite(cameraimg, save_img)
                                
                                # 사진 저장된 파일 리스트에 저장
                                '''if self.DB_Path == default.NoMask_DB_Path:
                                    #print(self.DB_Path)
                                    embedding_list_No.append(cameraimg)
                                else: 
                                    #print(self.DB_Path)
                                    embedding_list_Ma.append(cameraimg)'''
                                    
                                a = StudentID + "  거리값  " + str(round(img_dis, 3))     # 나중에 지울 것 $$$$$
                                print(a)                        
                                distest.append(a)                          # 나중에 지울 것 $$$$$
                                

                                
                            # 얼굴 매칭 실패 시
                            # 캠 멈춰서 가리기        
                            else:
                                print("unknown")
                                StudentID = "unknown"
                        except:
                            print("얼굴 인식 안됨")
                            StudentID = "얼굴 인식 안됨"
                        self.star = time.time()
                    
                        
                       
                else:
                    self.star = time.time()
            #print(c)
            #print(end - start) # 시간
            try:
                image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
                self.signal.emit(image)
            except:
                continue
           
    #save_pickle()  #파일 피클파일 추가하기(갱신)

    def stop(self):
        save_pickle()

        self.cap.release()
        cv2.destroyAllWindows()
class Face_Status(QtCore.QThread):
    def __init__(self, parent=None):
        super(Face_Status, self).__init__(parent)
    Face_value = QtCore.pyqtSignal(bool)
    def run(self):
        global StudentID
        while True:
            if StudentID in ("unknown","얼굴 인식 안됨", None ):
                self.Face_value.emit(False)
            else:
                self.Face_value.emit(True)
            time.sleep(1)
class Ui_user_face(object):
    def __init__(self, day, week):
        self.daylist = day
        self.weeklist = week
    def setupUi(self, Dialog):
        Dialog.setObjectName("출석")
        Dialog.resize(660, 600)
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.grabber = FrameGrabber()
        self.Temp_data_R = Temp_data_recv()
        self.Temp_data_S = Temp_data_send()
        self.temp = Temp_Data()
        self.name = Name_Data()
        self.Face_result = Face_Status()
        self.Face_result.Face_value.connect(self.Button_Status)
        self.temp.signal.connect(self.updateTemp)
        self.name.signal.connect(self.updateName)
        self.grabber.signal.connect(self.updateFrame)
        self.grabber.start()
        self.Temp_data_R.start()
        self.Temp_data_S.start()
        self.temp.start()
        self.name.start()
        self.Face_result.start()
        self.Video = QtWidgets.QLabel(Dialog)
        self.Video.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.Video.setText("")
        self.Video.setObjectName("Video")
        self.Temp = QtWidgets.QLabel(Dialog)
        self.Temp.setGeometry(QtCore.QRect(10, 500, 315, 40))
        self.Temp.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        self.Temp.setFont(font)
        self.Temp.setObjectName("Temp")
        self.Name = QtWidgets.QLabel(Dialog)
        self.Name.setGeometry(QtCore.QRect(335, 500, 315, 40))
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Attend = QtWidgets.QPushButton(Dialog)
        self.Attend.setGeometry(QtCore.QRect(10, 550, 205, 40))
        self.Attend.setObjectName("Attend")
        self.Attend.clicked.connect(lambda : self.choose())
        self.Back = QtWidgets.QPushButton(Dialog)
        self.Back.setGeometry(QtCore.QRect(440, 550, 205, 40))
        self.Back.setObjectName("Back")
        self.Back.clicked.connect(lambda: self.close_video(Dialog))
        self.Change = QtWidgets.QPushButton(Dialog)
        self.Change.setGeometry(QtCore.QRect(225, 550, 205, 40))
        self.Change.setObjectName("Change")
        self.Change.clicked.connect(lambda : self.swap())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        global recv_data
        Dialog.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "출석"))
        self.Temp.setText(_translate("Dialog", "체온 :" + " " + str(recv_data)))
        #1print(recv_data)
        self.Name.setText(_translate("Dialog", "학번 :"))
        self.Attend.setText(_translate("Dialog", "출석하기"))
        self.Back.setText(_translate("Dialog", "돌아가기"))
        self.Change.setText(_translate("Dialog", "2차 인증(마스크 O)"))
    def updateFrame(self, image):
        self.Video.setPixmap(QtGui.QPixmap.fromImage(image))
    def updateTemp(self, temp):
        self.Temp.setText("체온 :" + " " + temp + "℃")
    def updateName(self, name):
        #print(name)
        self.Name.setText("학번 :" + " " + name)
    def close_video(self,Dialog):#출석중 찍은 사진 피클파일 갱신
        
        self.grabber.stop() #비디오 멈춤
        Dialog.close()
    def choose(self):#출석중 사진 찍기
        #여기에 DB 출석 함수 넣기c
        global StudentID, save_img, cameraimg, recv_data
        weeklist = ["weekone", "weektwo", "weekthree", "weekfour", "weekfive"]
        curr = datetime.now()
        temp = float(recv_data)
        if int(temp) >= 30:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Temp_error(recv_data)
            self.ui.setupUi(self.window)
            self.window.show()#창전환
        else:
            try:
                currlimit = self.weeklist[self.daylist.index(curr.date())] - curr

                if currlimit > timedelta(seconds= -1):
                    if currlimit  > timedelta(hours= 3):
                        print("너무 일찍 출석")
                    else:
                        print("출석")
                        print(self.daylist.index(curr.date())+1)
                        atd_upload(StudentID, weeklist[self.daylist.index(curr.date())], "출석")
                elif currlimit > timedelta(hours= -3):
                    '''if currlimit > timedelta(minutes = -30):
                        print("지각")
                    else:'''
                    print("지각")
                    print(self.daylist.index(curr.date())+1)
                    atd_upload(StudentID, weeklist[self.daylist.index(curr.date())], "지각")
                else:
                    print("결석")
                    print(self.daylist.index(curr.date())+1) 
                    atd_upload(StudentID, weeklist[self.daylist.index(curr.date())], "결석")
            except:
                print("기간아님")
            self.window = QtWidgets.QDialog()
            self.ui = Ui_choose_student_name(StudentID, cameraimg, save_img)
            self.ui.setupUi(self.window)
            self.window.show()#창전환
    def swap(self):
        global dddown
        if self.grabber.DB_Path == default.Mask_DB_Path:
            self.Change.setText("2차 인증(마스크 X)")
            self.grabber.DB_Path = default.NoMask_DB_Path
            dddown = 0.45             
        else:
            self.grabber.DB_Path = default.Mask_DB_Path
            self.Change.setText("2차 인증(마스크 O)")
            dddown = 0.6             
        print(self.grabber.DB_Path)
    def Button_Status(self, status):
        if status:
            self.Attend.setEnabled(True)
        else:
            self.Attend.setEnabled(False)

def test(test_list):            # 나중에 지울 것 $$$$$
    global distest,DB_Path
    with open('test.txt','a',encoding='UTF-8') as f:
        f.write(DB_Path+'\n')
        for test in test_list:
            f.write(test+'\n') 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_user_face()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
