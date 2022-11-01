import time
import sys
import pymysql
from threading import Thread
from datetime import datetime
EMULATE_HX711=False
weight = 0
referenceUnit = 1
user_id = ""
user_pw = ""

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()

hx = HX711(21, 20)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(467)
hx.reset()
hx.tare()
print("Tare done! Add weight now...")

def Login():
    global user_id, user_pw
    login_bool = True

    while login_bool:
        user_id = input("아이디를 입력해주세요 : ")
        user_pw = input("비밀번호를 입력해주세요 : ")
        con = pymysql.connect(host="123.215.162.92", user="kbuser", password="1234", db="kb", charset='utf8')
        cur = con.cursor()
        sql = "SELECT * FROM user WHERE userid = {0} AND password = {1};".format(user_id, user_pw)
        cur.execute(sql)
        con.commit()
        row = cur.fetchone()
        if row is not None:
            login_bool = False
            print("로그인에 성공했습니다.")
        else:
            print("아이디나 비밀번호가 틀립니다.")

    con.close()

def Send_Data(table, col):
    global weight, user_id
    con = pymysql.connect(host="123.215.162.92", user="kbuser", password="1234", db="kb", charset='utf8')
    cur = con.cursor()
    sql = "UPDATE {0} SET {1} = '{2}' WHERE userid = {3};".format(table, col, str(weight), user_id)
    cur.execute(sql)
    con.commit()
    con.close()
def Measure_Weight():
    global weight
    while True:
        weight = int(hx.get_weight(5))
        print(weight)
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
def Check_Time():
    while True:
        now = datetime.now()
        """print("년 : ", now.year)
        print("시 : ", now.hour)
        print("분 : ", now.minute)
        print("초 : ", now.second)"""
        month = str(now.month)
        day =  str(now.day)
        #print("현재 시간 : ", now.strftime('%Y-%m-%d %H:%M:%S'))
        #Send_Data(month+"mon","g"+'{:0>2}'.format(month)+'{:0>2}'.format(day))
        time.sleep(1)
if __name__ == "__main__":
    '''Login()'''
    get_weight = Thread(target = Measure_Weight)
    get_time = Thread(target = Check_Time)
    get_weight.start()
    get_time.start()
