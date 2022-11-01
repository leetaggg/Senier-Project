import mysql.connector
from mysql.connector import Error

def user_list():
    try:
        connection = mysql.connector.connect(host='39.124.26.132',
                                                database='student',
                                                user='root',
                                                password='123456')

        cursor = connection.cursor()
        sql = "SELECT userID, name FROM user;"

        cursor.execute(sql, )
        record = cursor.fetchall()
        row = []
        with open("C:/AHard/Project/DB/User_List.txt", "w") as f:
            for i in range(0, len(record)):
                f.write(str(record[i][0]) + "\n")
                f.write(str(record[i][1]) + "\n")
                    
    except mysql.connector.Error as error:
        print("연결 실패 {}".format(error))
        return False

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()