import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Wang12145',
    db='diandian',
    charset='utf8mb4',

)
cursor = conn.cursor()

class Student:
    def __init__(self, id,name,english,python):
        self.id = id
        self.name = name
        self.english = english
        self.python = python





def menu():
    print('==============学生信息管理系统======================')
    print('---------------功能菜单--------------------------')
    print('\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t5.显示所有学生信息')
    print('\t\t\t\t\t\t\t0.退出')


class ManagementSystem:
    def __init__(self):
        pass

    def add(self):
        while True:
            id = input('请输入id(如1001):')
            if not id:
                break
            name = str(input('请输入姓名：'))
            if not name:
                break
            try:
                english = int(input('请输入英语成绩：'))
                python = int(input('请输入python成绩：'))
            except:
                print('输入无效，不是整数，请重新输入')
                continue

            sql = "INSERT INTO students(id,name,english,python) VALUES (%s, %s, %s,%s)"
            values = (id,name,english,python)
            cursor.execute(sql, values)
            conn.commit()
            answer = input('是否继续添加？y/n')
            if answer == 'y':
                continue
            else:
                break


    def remove(self):
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        # result = cursor.fetchone()
        results = cursor.fetchall()
        # print(result)
        fl=0
        id = int(input("请输入要删除学生的ID："))
        for result in results:
            if id==result[0]:
                fl=1

        if fl==1:
            sql = "delete from students where id=%s"
            values = (id,)#########这里为什么要这样写？？
            cursor.execute(sql, values)
            conn.commit()
            print(f'id为{id}的学生信息已经删除')
        else:
            print(f'没有找到id为{id}的学生信息')
        while True:
            answer=input("是否要继续删除？y/n\n")
            if answer=='y':
                self.remove()
            else:
                break

        ###此处待更新，因为需要加一个是否继续删除的选项！！！！

        # if results:
        #     for result in results:
        #         student = Student(*result)
        #         # print(student.id)
        #         id=int(input("请输入要删除学生的ID："))
        #         # print(id)
        #         if id==student.id:############此处的students.id是什么？？？
        #             sql = "delete from students where id=%s"
        #             values = (student.id,)#########这里为什么要这样写？？
        #             cursor.execute(sql, values)
        #             conn.commit()
        #             print(f'id为{id}的学生信息已经删除')
        #         else:
        #             print(f'没有找到id为{id}的学生信息')
        #         answer=input("是否要继续删除？y/n\n")
        #         if answer=='y':
        #             continue
        #         else:
        #             break





    def update(self, student) :
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        results = cursor.fetchall()
        fl = 0
        id = int(input("请输入要更新学生的ID："))
        for result in results:
            if id == result[0]:
                fl = 1

        if fl==1:
            sql = "update students set name=%s,english=%s,python=%s"
            name = input("Name:")
            english = input("english : ")
            python = input("python: ")
            values = (name,english,python)
            cursor.execute(sql, values)
            conn.commit()
            print(f'id为{id}的学生信息已经更新')
        else:
            print(f'没有找到id为{id}的学生信息')

        while True:
            answer = input("是否要继续更新？y/n\n")
            if answer == 'y':
                self.update(student=Student)
            else:
                break


        # name = input("Name ({}): ".format(student.name))
        # age = int(input("Age ({}): ".format(student.age)))
        # grade = input("Grade ({}): ".format(student.grade))
        # sql = "UPDATE student SET name = %s, age = %s, grade = %s WHERE id = %s"
        # val = (name, age, grade, student.id)
        # cursor.execute(sql, val)
        # conn.commit()
        # print("成功更新学生信息!")

    def query(self,student):
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        results = cursor.fetchall()
        mode=input("按ID查找请输入1，按姓名查找请输入2:")
        if mode=='1':
            id=input("请输入学生ID:")
            sql="select name,english,python from students where id=%s;"
            values=id
            cursor.execute(sql,values)
            result = cursor.fetchone()
            conn.commit()
            print(result)
        elif mode=='2':
            name=input("请输入学生姓名")
            sql = "select id,english,python from students where name=%s;"
            values=name
            cursor.execute(sql,values)
            result=cursor.fetchone()
            conn.commit()
            print(result)
        else:
            print("您的输入有误，请重新输入")
        while True:
            answer = input("是否要继续查询？y/n\n")
            if answer == 'y':
                self.query(student=Student)
            else:
                break

        # for result in results:
        #     if id==student.id:
        #         print("ID: {}, Name: {}, Age: {}, Grade: {}".format(student.id, student.name, student.english, student.python))
        #     elif name==student.name:
        #         print("ID: {}, Name: {}, Age: {}, Grade: {}".format(student.id, student.name, student.english, student.python))




    def show(self):
        print("查看所有学生:")
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        results = cursor.fetchall()
        if results:
            for result in results:
                student = Student(*result)
                print(
                    "ID: {}, Name: {}, english: {}, python: {}".format(student.id, student.name, student.english, student.python))
        else:
            print("没有找到学生.")

    def main(self):
        while True:
            menu()
            choice=int(input('请选择'))
            if choice in [0,1,2,3,4,5]:
                if choice==0:
                    answer= input('你真的要退出系统吗？y/n')
                    if answer =='y':
                        print('谢谢你的使用！')
                        break
                    else:
                        continue
                elif  choice==1:
                    self.add()
                elif  choice==2:
                    self.query(student=Student)
                elif  choice==3:
                    self.remove()
                elif  choice==4:
                    self.update(student=Student)
                elif  choice==5:
                    self.show()
                else:
                    print("输入有误，请重新输入！")

system = ManagementSystem()
system.main()

