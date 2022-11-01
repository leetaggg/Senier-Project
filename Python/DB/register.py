import mysql.connector
from mysql.connector import Error

def register(id, password, name, grade):
    try:
        connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

        cursor = connection.cursor(prepared = True)
        sql = 'INSERT INTO user (userID, userPassword, name, grade, renewal) VALUES (%s, %s, %s, %s, 3);'
        insert_sql = (id, password, name, grade)
        cursor.execute(sql, insert_sql)
        connection.commit()
        
        sql = 'INSERT INTO attend (userID) VALUES (%s);'
        insert_sql = (id, )
        cursor.execute(sql, insert_sql)
        connection.commit()
        
        print("업로드 완료")

    except mysql.connector.Error as error:
        print("업로드 실패")
        error = str(error)
        if(error == "Error while executing statement: Duplicate entry '" + id + "' for key 'user.PRIMARY'"):
            print("중복된 사용자입니다.")

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("접속 종료")



