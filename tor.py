import pymysql

class MySQL:
    
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()
    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user='root',
            password='1234'
        )
        self.c = self.db.cursor()
    def CreateDB(self):
        self.c.execute('''CREATE DATABASE IF NOT EXISTS Restaran''')
        self.c.execute('''USE Restaran''')
    def CreateTB(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS FASFOOD(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(50),Address VARCHAR(100),maxFoodPrice INT,minFoodPrice INT,employeesCount INT,experience INT )''')
    def Insert(self,name,adris,maxp,minp,x_soni,t_yil):
        self.c.execute(f'''INSERT INTO FASFOOD(name,Address,maxFoodPrice,minFoodPrice,employeesCount,experience) VALUES("{name}","{adris}",{maxp},{minp},{x_soni},{t_yil})''')
        self.db.commit()
    def misol_1(self):
        self.c.execute('''SELECT * FROM FASFOOD WHERE NAME LIKE "M%R" ORDER BY maxFoodPrice''')    
        return self.c.fetchall()
    def misol_2(self):
        self.c.execute('''SELECT NAME FROM FASFOOD ORDER BY mINFoodPrice LIMIT 3''')
        return self.c.fetchall()
    def misol_3(self):
        self.c.execute('''SELECT NAME,maxFoodPrice FROM FASFOOD ORDER BY experience DESC LIMIT 4''')
        return self.c.fetchall()
m1=MySQL()
# for i in range(int(input("Nechta restaran "))):
#     m1.Insert(input("Name "),input("Adres "),int(input("Max_p ")),int(input("Min_p ")),int(input("Xodim_soni" )),int(input("T_yil ")))

# for i in m1.misol_1():
#     print(i)

# for i in m1.misol_2():
#     print(i)

# for i in m1.misol_3():
#     print(i)


