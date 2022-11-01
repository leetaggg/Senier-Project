import mysql.connector
from mysql.connector import Error
from numpy import rec

def atd_upload(id, week, attendance):

    try:
        connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

        cursor = connection.cursor(prepared = True)
        sql = 'UPDATE attend SET {0} = %s WHERE userID = %s;'.format(week)

        data = (attendance, id)
        cursor.execute(sql, data)
        connection.commit()

    except mysql.connector.Error as error:
        print("업로드 실패 {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

            
def atd_check(userid):
    try:
        connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

        cursor = connection.cursor(prepared = True)
        sql = 'SELECT * from attend WHERE userID = %s;'

        data = (userid, )
        cursor.execute(sql, data)
        record = cursor.fetchall()
        atd_li = []
        for i in range(0, len(record[0])):
            atd_li.append(record[0][i])
        return atd_li

    except mysql.connector.Error as error:
        print("업로드 실패 {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("접속 종료")


