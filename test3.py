import pymysql

class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Wang12145",
            database="students"
        )
        self.cur = self.conn.cursor()

class Student:
    def __init__(self):
        self.db = DB()

    def add_student(self, name, age, sex):
        sql = "INSERT INTO student_info (name, age, sex) VALUES (%s, %s, %s)"
        self.db.cur.execute(sql, (name, age, sex))
        self.db.conn.commit()

    def delete_student(self, id):
        sql = "DELETE FROM student_info WHERE id=%s"
        self.db.cur.execute(sql, id)
        self.db.conn.commit()

    def update_student(self, id, name, age, sex):
        sql = "UPDATE student_info SET name=%s, age=%s, sex=%s WHERE id=%s"
        self.db.cur.execute(sql, (name, age, sex, id))
        self.db.conn.commit()

    def select_student(self):
        sql = "SELECT * FROM student_info"
        self.db.cur.execute(sql)
        result = self.db.cur.fetchall()
        return result

class UserInterface:
    def __init__(self):
        self.student = Student()

    def login(self):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        # TODO：校验用户名和密码是否正确

    def register(self):
        username = input("请输入用户名：")
        password1 = input("请输入密码：")
        password2 = input("请再次输入密码：")
        # TODO：检查两次输入的密码是否相同，如果相同则将用户信息添加到数据库中

    def add(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        sex = input("请输入性别：")
        self.student.add_student(name, age, sex)
        print("添加成功！")

    def delete(self):
        id = int(input("请输入要删除的学生的编号："))
        self.student.delete_student(id)
        print("删除成功！")

    def show(self):
        result = self.student.select_student()
        for row in result:
            print("编号：%d\t姓名：%s\t年龄：%d\t性别：%s" % (row[0], row[1], row[2], row[3]))

ui = UserInterface()
while True:
    print("请选择操作：\n1. 添加学生\n2. 删除学生\n3. 查看学生\n4. 退出")
    choice = input()
    if choice == "1":
        ui.add()
    elif choice == "2":
        ui.delete()
    elif choice == "3":
        ui.show()
    elif choice == "4":
        break
    else:
        print("输入有误，请重新输入。")