from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.hisob=""       

        self.v_main_lay = QVBoxLayout()
        self.h_lay1 = QHBoxLayout()
        self.h_lay2 = QHBoxLayout()
        self.h_lay3 = QHBoxLayout()
        self.h_lay4 = QHBoxLayout()


        self.lbl = QLabel()
        self.btn_1=QPushButton("1")
        self.btn_1.clicked.connect(self.bir)
        self.btn_2= QPushButton("2")
        self.btn_2.clicked.connect(self.ikki)
        self.btn_3=QPushButton("3")
        self.btn_3.clicked.connect(self.uch)
        self.btn_4=QPushButton("4")
        self.btn_4.clicked.connect(self.tor)
        self.btn_5=QPushButton("5")
        self.btn_5.clicked.connect(self.besh)
        self.btn_6=QPushButton("6")
        self.btn_6.clicked.connect(self.olti)
        self.btn_7=QPushButton("7")
        self.btn_7.clicked.connect(self.yeti)
        self.btn_8=QPushButton("8")
        self.btn_8.clicked.connect(self.sakkiz)
        self.btn_9=QPushButton("9")
        self.btn_9.clicked.connect(self.toqqiz)
        self.btn_0=QPushButton("0")
        self.btn_0.clicked.connect(self.nol)
        self.btn_x=QPushButton("x")
        self.btn_x.setStyleSheet("background-color: orange;")
        self.btn_x.clicked.connect(self.kopaytirish)
        self.btn_ayrish=QPushButton("-")
        self.btn_ayrish.setStyleSheet("background-color: orange;")
        self.btn_ayrish.clicked.connect(self.ayirish)
        self.btn_bolish=QPushButton("/")
        self.btn_bolish.setStyleSheet("background-color: orange;")
        self.btn_bolish.clicked.connect(self.bolish)
        self.btn_plus=QPushButton("+")
        self.btn_plus.setStyleSheet("background-color: orange;")
        self.btn_plus.clicked.connect(self.qoshish)
        self.btn_javob=QPushButton("=")
        self.btn_javob.setStyleSheet("background-color: orange;")
        self.btn_javob.clicked.connect(self.javob)
        self.btn_c=QPushButton("<---")
        self.btn_c.setStyleSheet("background-color: orange;")
        self.btn_c.clicked.connect(self.toza)

        self.setStyleSheet("""MyWindow {background-color: black;}""")
        self.lbl.setStyleSheet("color: white;")


        self.h_lay1.addWidget(self.btn_1)
        self.h_lay1.addWidget(self.btn_2)
        self.h_lay1.addWidget(self.btn_3)
        self.h_lay1.addWidget(self.btn_x)
        self.h_lay2.addWidget(self.btn_4)
        self.h_lay2.addWidget(self.btn_5)
        self.h_lay2.addWidget(self.btn_6)
        self.h_lay2.addWidget(self.btn_ayrish)
        self.h_lay3.addWidget(self.btn_7)
        self.h_lay3.addWidget(self.btn_8)
        self.h_lay3.addWidget(self.btn_9)
        self.h_lay3.addWidget(self.btn_bolish)
        self.h_lay4.addWidget(self.btn_c)
        self.h_lay4.addWidget(self.btn_0)
        self.h_lay4.addWidget(self.btn_plus)
        self.h_lay4.addWidget(self.btn_javob)


        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_lay1)
        self.v_main_lay.addLayout(self.h_lay2)
        self.v_main_lay.addLayout(self.h_lay3)
        self.v_main_lay.addLayout(self.h_lay4)
        

        self.setLayout(self.v_main_lay)

    def bir(self):
        self.hisob+="1"
        self.lbl.setText(f"{self.lbl.text()}{1}")
    def ikki(self):
        self.hisob+="2"
        self.lbl.setText(f"{self.lbl.text()}{2}")    
    def uch(self):
        self.hisob+="3"
        self.lbl.setText(f"{self.lbl.text()}{3}")
    def tor(self):
        self.hisob+="4"
        self.lbl.setText(f"{self.lbl.text()}{4}")    
    def besh(self):
        self.hisob+="5"
        self.lbl.setText(f"{self.lbl.text()}{5}")    
    def olti(self):
        self.hisob+="6"
        self.lbl.setText(f"{self.lbl.text()}{6}")         
    def yeti(self):
        self.hisob+="7"
        self.lbl.setText(f"{self.lbl.text()}{7}")
    def sakkiz(self):
        self.hisob+="8"
        self.lbl.setText(f"{self.lbl.text()}{8}")   
    def toqqiz(self):
        self.hisob+="9"
        self.lbl.setText(f"{self.lbl.text()}{9}")  
    def nol(self):
        self.hisob+="0"
        self.lbl.setText(f"{self.lbl.text()}{0}")      
    def kopaytirish(self):
        self.hisob+="*"
        self.lbl.setText(f"{self.lbl.text()}*")    
    def ayirish(self):
        self.hisob+="-"
        self.lbl.setText(f"{self.lbl.text()}-")  
    def qoshish(self):
        self.hisob+="+"
        self.lbl.setText(f"{self.lbl.text()}+")       
    def bolish(self):
        self.hisob+="/"
        self.lbl.setText(f"{self.lbl.text()}/")    
    def javob(self):
        self.lbl.clear() 
        self.lbl.setText(f"{self.lbl.text()}{eval(self.hisob)}")        
    def toza(self):
        self.hisob = self.hisob[:-1]
        self.lbl.setText(self.hisob)

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()