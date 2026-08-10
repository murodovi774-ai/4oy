import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,QHBoxLayout, QLabel, QMessageBox, QCheckBox,QRadioButton,QComboBox, QListWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size: 20px")
        self.v_main_lay = QVBoxLayout()
        self.h_clik_lay =QHBoxLayout()
        self.h_sh_lay =QHBoxLayout()
        self.h_t_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        
        self.lbl_jins = QLabel("Jins")
        self.lbl_shaxar = QLabel("Shaxarlar")
        self.lbl_tuman = QLabel("Tumanlar")
        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("Name...")

        self.edit_second = QLineEdit()
        self.edit_second.setPlaceholderText("Second...")

        self.edit_age = QLineEdit()
        self.edit_age.setPlaceholderText("Age...")
        
        self.r1 = QRadioButton("M")
        self.r1.setChecked(True)
        self.r2 = QRadioButton("F")
        
        self.cmb = QComboBox()
        self.cmb.addItems(["Andijon",
    "Buxoro",
    "Toshkent viloyati",
    "Jizzax",
    "Qashqadaryo",
    "Navoiy",
    "Namangan",
    "Samarqand",
    "Surxondaryo",
    "Sirdaryo",
    "Toshkent",
    "Farg'ona",
    "Xorazm"])
        
        self.cmb.activated[str].connect(self.tuman)
        self.tum = QComboBox()

        self.btn_submit = QPushButton("Submit")
        self.btn_submit.clicked.connect(self.submit)
        self.btn_Exit = QPushButton("Exit")
        self.btn_Exit.clicked.connect(exit)
        self.h_btn_lay.addWidget(self.btn_submit)
        self.h_btn_lay.addWidget(self.btn_Exit)





        self.v_main_lay.addWidget(self.edit_name)
        self.v_main_lay.addWidget(self.edit_second)
        self.v_main_lay.addWidget(self.edit_age)
        self.h_clik_lay.addWidget(self.lbl_jins)
        self.h_clik_lay.addWidget(self.r1)
        self.h_clik_lay.addWidget(self.r2)
        
        self.h_sh_lay.addWidget(self.lbl_shaxar)
        self.h_sh_lay.addWidget(self.cmb)

        self.h_t_lay.addWidget(self.lbl_tuman)
        self.h_t_lay.addWidget(self.tum)



    
        self.v_main_lay.addLayout(self.h_clik_lay)
        self.v_main_lay.addLayout(self.h_sh_lay)
        self.v_main_lay.addLayout(self.h_t_lay)
        self.v_main_lay.addLayout(self.h_btn_lay)
        self.setLayout(self.v_main_lay)




    def tuman(self,obj):
        self.tum.clear()
        self.dct={
    "Andijon": [
        "Andijon tumani",
        "Asaka",
        "Baliqchi",
        "Bo'ston",
        "Buloqboshi",
        "Izboskan",
        "Jalaquduq",
        "Marhamat",
        "Oltinko'l",
        "Paxtaobod",
        "Qo'rg'ontepa",
        "Shahrixon",
        "Ulug'nor",
        "Xo'jaobod"
    ],

    "Buxoro": [
        "Buxoro tumani",
        "G'ijduvon",
        "Jondor",
        "Kogon",
        "Olot",
        "Peshku",
        "Qorako'l",
        "Qorovulbozor",
        "Romitan",
        "Shofirkon",
        "Vobkent"
    ],

    "Jizzax": [
        "Arnasoy",
        "Baxmal",
        "Do'stlik",
        "Forish",
        "G'allaorol",
        "Jizzax tumani",
        "Mirzacho'l",
        "Paxtakor",
        "Sharof Rashidov",
        "Yangiobod",
        "Zafarobod",
        "Zarbdor"
    ],

    "Qashqadaryo": [
        "Chiroqchi",
        "Dehqonobod",
        "G'uzor",
        "Kasbi",
        "Kitob",
        "Koson",
        "Mirishkor",
        "Muborak",
        "Nishon",
        "Qamashi",
        "Qarshi tumani",
        "Shahrisabz",
        "Yakkabog'"
    ],

    "Navoiy": [
        "Karmana",
        "Konimex",
        "Navbahor",
        "Navoiy tumani",
        "Nurota",
        "Qiziltepa",
        "Tomdi",
        "Uchquduq",
        "Xatirchi"
    ],

    "Namangan": [
        "Chortoq",
        "Chust",
        "Kosonsoy",
        "Mingbuloq",
        "Namangan tumani",
        "Norin",
        "Pop",
        "To'raqo'rg'on",
        "Uchqo'rg'on",
        "Uychi",
        "Yangiqo'rg'on"
    ],

    "Samarqand": [
        "Bulung'ur",
        "Ishtixon",
        "Jomboy",
        "Kattaqo'rg'on tumani",
        "Kattaqo'rg'on shahri",
        "Narpay",
        "Nurobod",
        "Oqdaryo",
        "Paxtachi",
        "Pastdarg'om",
        "Payariq",
        "Samarqand tumani",
        "Toyloq",
        "Urgut"
    ],

    "Surxondaryo": [
        "Angor",
        "Bandixon",
        "Boysun",
        "Denov",
        "Jarqo'rg'on",
        "Muzrabot",
        "Oltinsoy",
        "Qiziriq",
        "Qumqo'rg'on",
        "Sariosiyo",
        "Sherobod",
        "Sho'rchi",
        "Termiz tumani",
        "Uzun"
    ],

    "Sirdaryo": [
        "Boyovut",
        "Guliston tumani",
        "Mirzaobod",
        "Oqoltin",
        "Sayxunobod",
        "Sardoba",
        "Sirdaryo tumani",
        "Xovos"
    ],

    "Toshkent viloyati": [
        "Bekobod",
        "Bo'ka",
        "Bo'stonliq",
        "Chinoz",
        "Ohangaron",
        "Oqqo'rg'on",
        "Parkent",
        "Piskent",
        "Quyi Chirchiq",
        "Toshkent tumani",
        "Uchqo'rg'on",
        "Yuqori Chirchiq",
        "Zangiota",
        "Yangiyo'l"
    ],

    "Farg'ona": [
        "Bag'dod",
        "Beshariq",
        "Buvayda",
        "Dang'ara",
        "Farg'ona tumani",
        "Furqat",
        "Oltiariq",
        "Qo'shtepa",
        "Quva",
        "Rishton",
        "So'x",
        "Toshloq",
        "Uchko'prik",
        "Yozyovon"
    ],

    "Xorazm": [
        "Bog'ot",
        "Gurlan",
        "Hazorasp",
        "Qo'shko'pir",
        "Shovot",
        "Tuproqqal'a",
        "Urganch tumani",
        "Xiva tumani",
        "Xonqa",
        "Yangiariq",
        "Yangibozor"
    ],

    "Qoraqalpog'iston Respublikasi": [
        "Amudaryo",
        "Beruniy",
        "Bo'zatov",
        "Chimboy",
        "Ellikqal'a",
        "Kegeyli",
        "Mo'ynoq",
        "Nukus tumani",
        "Qanliko'l",
        "Qo'ng'irot",
        "Qorao'zak",
        "Shumanay",
        "Taxtako'pir",
        "To'rtko'l",
        "Xo'jayli"
    ],

    "Toshkent": [
        "Bektemir",
        "Chilonzor",
        "Mirobod",
        "Mirzo Ulug'bek",
        "Olmazor",
        "Sergeli",
        "Shayxontohur",
        "Uchtepa",
        "Yakkasaroy",
        "Yashnobod",
        "Yunusobod",
        "Yangihayot"
    ]
    
}
        self.tum.addItems(self.dct[obj])
    def submit(self):
     name = self.edit_name.text()
     second = self.edit_second.text()
     age = self.edit_age.text()

     if self.r1.isChecked():
        jins = "M"
     elif self.r2.isChecked():
        jins = "F"
     else:
        jins = ""

     shahar = self.cmb.currentText()
     tuman = self.tum.currentText()

     if not name or not second or not age or not jins or not shahar or not tuman:
        QMessageBox.warning(
            self,
            "Ogohlantirish",
            "Iltimos, barcha maydonlarni to'liq to'ldiring!"
        )
        return

     user = {
        "name": name,
        "second": second,
        "age": age,
        "jins": jins,
        "shahar": shahar,
        "tuman": tuman
     }

     with open("test.json", "r+") as f:
        data = json.load(f)
        data.append(user)

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

     QMessageBox.information(
        self,
        "Muvaffaqiyatli",
        "Ma'lumotlaringiz saqlandi. Rahmat!"
     )

     self.edit_name.clear()
     self.edit_second.clear()
     self.edit_age.clear()

     self.r1.setChecked(False)
     self.r2.setChecked(False)

     self.cmb.setCurrentIndex(0)
     self.tum.clear()
                       


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()

