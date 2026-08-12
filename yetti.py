#------------------------------------------4-misol
# import json
# from PyQt5.QtWidgets import *

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("Tasks Manger Lite")
#         self.setGeometry(100, 100, 500, 300)

#         self.vlayout = QVBoxLayout()
        
#         self.edit_t = QLineEdit()
#         self.edit_t.setPlaceholderText("Task nomi")

#         self.edit_s = QLineEdit()
#         self.edit_s.setPlaceholderText("Status (Done / Pending)")

#         self.edit_q = QLineEdit()
#         self.edit_q.setPlaceholderText("Qidruv")

#         self.btn_qoshish = QPushButton("Qo'shish")
#         self.btn_qoshish.clicked.connect(self.qosh)


#         self.btn_qidirish = QPushButton("Qidiridh")

#         self.btn_qidirish.clicked.connect(self.qid)


#         self.btn_um = QPushButton("Ummumiy son")
#         self.btn_um.clicked.connect(self.um)
#         self.label = QLabel()

#         self.vlayout.addWidget(self.edit_t)
#         self.vlayout.addWidget(self.edit_s)
#         self.vlayout.addWidget(self.edit_q)
#         self.vlayout.addWidget(self.btn_qoshish)
#         self.vlayout.addWidget(self.btn_qidirish)
#         self.vlayout.addWidget(self.btn_um)
#         self.vlayout.addWidget(self.label)

#         self.setLayout(self.vlayout)
#     def qosh(self):
#         task=self.edit_t.text()
#         status=self.edit_s.text()
#         if not task or not status:
#             QMessageBox.warning(self, "Xato","Barcha maydoni toldiring")
#             return
#         if len(task)<3:
#             QMessageBox.information(self, "Xato","Task juda qisqa")    
#             return
#         if not status in ["Done","Pending"]:
#             QMessageBox.warning(self, "Xato","Status xato")
#             return
        
#         with open("uyishi.json", "r") as f:
#          data=json.load(f)
#         data.append({"task": task,"status": status})


#         with open("uyishi.json", "w") as f:
#            json.dump(data,f,indent=4)

#         self.edit_t.clear()
#         self.edit_s.clear()

#         QMessageBox.information(self, "OK", "Task qo'shildi!") 

#     def qid(self):
#         qidr=self.edit_q.text()
#         self.edit_q.clear()
#         if qidr:
#          with open("uyishi.json", "r") as f:
#             task=json.load(f)
#             for i in task:
#                 if i["task"]==qidr:
#                    QMessageBox.information(self, "info", f"""Task: {i["task"]}
# Status: {i["status"]}""")
#                    return
#                 else:
#                     QMessageBox.warning(self, "Xato", "Qidiruv Topilmadi")            
   
#         else:   
#            QMessageBox.warning(self, "Xato", "Qidiruvga yozing")            
        
#     def um(self):
#         with open("uyishi.json", "r") as f:
#            data=json.load(f)
#            QMessageBox.information(self, "Info", f"Ummiy task soni: {len(data)}")            
        

# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()        



#----------------------------------------1-misol
# def unikal(sonlar:list):
#     son=[]
#     for i in sonlar:
#         if sonlar.count(i)==1:
#             son.append(i)
#     if len(son)<2:
#         return -1
#     return son[1]        

# print(unikal([1, 2, 2, 3, 3, 4]))        

#-----------------------------------------2-misol
# def yoqolgan(sonlar:list):
#     if not sonlar:
#         return -1
#     return len(sonlar)*(len(sonlar)+1)//2 - sum(sonlar)

# print(yoqolgan([ 8, 6, 5, 3, 4, 0, 1, 2]))

#-----------------------------------------3-misol
# def users(user:list):
#     phone=set()
#     for i in user:
#         for x in i["phones"]:
#          phone.add(x)
#     return phone    

# u = [
#     {"name": "Ali", "phones": ("111", "222")},
#     {"name": "Vali", "phones": ("222", "333")}
# ]

# print(users(u))

#---------------------------------------4-misol
# def students(student:list):
#     stunet_max=student[0]
#     for i in student:
#         if len(i["subjects"]) > len(stunet_max["subjects"]):
#             stunet_max=i
#     return stunet_max["name"]

# s = [
#     {"name": "Ali", "subjects": {"math", "physics"}},
#     {"name": "Vali", "subjects": {"math"}},
#     {"name": "Hasan", "subjects": {"math", "physics", "english"}}
# ]

# print(students(s))

#-----------------------------------------5-misol tor.sql faylda 