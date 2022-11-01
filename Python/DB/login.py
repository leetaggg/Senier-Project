import mysql.connector
from mysql.connector import Error
from sqlalchemy import true

a = ""
def login(id, password):
    global a
    a = ""
    try:
        connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

        cursor = connection.cursor()

        sql = "SELECT renewal FROM user WHERE userID = %s && userPassword = %s;"
        cursor.execute(sql, (id, password))
        record = cursor.fetchall()
        for row in record:
            a = row[0]  
    except mysql.connector.Error as error:
        print("연결 실패 {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("접속 종료")
    
    if a == 4:
        return True
    else:
        return False
