import pymysql


def connect():
    return pymysql.connect(
        host="localhost",
        user="vinayak",
        port=3306,
        password="3553",
        database="test",
        cursorclass=pymysql.cursors.DictCursor,
    )


def getAllStudents():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def getStudentRecord(rollNumber):
    connection = connect()
    cursor = connection.cursor()
    command_to_execute = f"SELECT * FROM students WHERE ROLL={rollNumber};"
    cursor.execute(command_to_execute)
    rows = cursor.fetchone()
    cursor.close()
    connection.close()
    return rows


def insertRecord(roll, name, gender, contact, dob, address):
    # Auto-generated SQL script #202108191721
    connection = connect()
    cursor = connection.cursor()
    command_to_execute = f"INSERT INTO test.students (ROLL,NAME,GENDER,CONTACT,DOB,ADDRESS) VALUES ({int(roll)},'{name}','{gender}','{contact}','{dob}','{address}');"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()


def removeRecord(rollNumber):
    connection = connect()
    cursor = connection.cursor()
    command_to_execute = f"DELETE FROM test.students WHERE ROLL={rollNumber.get()};"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()


def updateRecord(roll, name, gender, contact, dob, address):
    connection = connect()
    cursor = connection.cursor()
    command_to_execute = f"UPDATE test.students SET NAME='{name}',GENDER='{gender}',CONTACT='{contact}',DOB='{dob}',ADDRESS='{address}' WHERE ROLL={roll};"
    cursor.execute(command_to_execute)
    connection.commit()
    connection.close()
