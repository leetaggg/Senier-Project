import requests
import mysql.connector
from mysql.connector import Error

def user_remove(user_name):
    try:
        url = 'http://39.124.26.132/Py_php/delete.php'
        name = {'uname':user_name}
        r = requests.post(url, data=name)
        print(r.text)
    except:
        print("요청 오류")

    try:
        connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

        cursor = connection.cursor(prepared = True)
        sql = 'DELETE FROM user WHERE userID = %s;'
        insert_sql = (user_name, )
        cursor.execute(sql, insert_sql)
        connection.commit()
        
        sql = 'DELETE FROM attend WHERE userID = %s;'
        insert_sql = (user_name, )
        cursor.execute(sql, insert_sql)
        connection.commit()
        
        print("업로드 완료")

    except mysql.connector.Error as error:
        print("업로드 실패 {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("접속 종료")



if __name__ == "__main__":
    name = input() # 삭제할 사람 학번 또는 이름
    user_remove(name)