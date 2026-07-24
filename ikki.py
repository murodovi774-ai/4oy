# class User:
#     def __init__(self,name:str,email:str,adres:str):
#         self.name=name
#         self.email=email
#         self.adres=adres
#     def get_name(self)->str:
#         return self.name  
#     def get_email(self)->str:
#         return self.email
#     def get_adres(self)->str:
#         return self.adres
#     def set_adres(self,new_adres)->None:
#         print("Adres yangilandi")
#         self.adres=new_adres
#     def __str__(self)->str:
#         return f"Name: {self.name}, email: {self.email}, adres: {self.adres}"
    
# u1=User("Izzat","murodovi774@gmail.com","Toshkent")
# print(u1)
# print(u1.get_name())
# print(u1.get_email())
# print(u1.get_adres())
# u1.set_adres("New york")
# print(u1.get_adres())

# class Customer(User):
#     def __init__(self, name, email, adres,cart:list[tuple[str,int,int]],balance:int):
#         super().__init__(name, email, adres)
#         self.cart=cart
#         self.balance=balance
#     def add_to_cart(self, product, qty, price) -> None:
#         if qty>0 and price>=0:
#             print("Maxsulot qo'shildi")
#             self.cart.append((product,qty,price))   
#         else:
#             print("Xato: qty > 0 va price >= 0 bo'lishi kerak")    
#     def clear_cart(self) -> None:
#         print("Savat tozalandi")
#         self.cart.clear()
#     def get_cart_total(self) -> int:
#         return sum(qty*price for _,qty,price in self.cart)   
#     def checkout(self) -> bool:
#         if self.balance>=sum(qty*price for _,qty,price in self.cart):
#             print("Xarid amalga oshdi")
#             self.balance-=sum(qty*price for _,qty,price in self.cart)
#             self.clear_cart()
#             print(f"Balansda qoldi: {self.balance}")
#             return True
#         else:
#             print("Mablag' yetarli emas")    
#             return False
#     def __str__(self):
#         return f"Customer: {self.name} (balance: {self.balance} so'm)"   

# c = Customer("Ali", "ali@mail.com", "Toshkent",[], balance=2_000_000)
# c.add_to_cart("Keyboard", 1, 300_000)
# c.add_to_cart("Mouse", 2, 150_000)
# print(c.get_cart_total())     # 600000
# print(c.checkout())           # True
# print(c)                      # Customer: Ali (balance: 1400000 so‘m)


            
# class Seller(User):
#     def __init__(self, name, email, adres,praduct:dict[str,int],reting:float):
#         super().__init__(name, email, adres)
#         self.praduct=praduct
#         self.reting=reting
#     def add_product(self, name, qty) -> None:
#         if qty>0:
#             self.praduct[name]=qty 
#             print("Maxsulot qo'shildi")   
#         else:
#             print("qty>0 bo'lishi kerak")
#     def remove_product(self, name) -> bool:
#         if name in self.praduct:
#             self.praduct.pop(name)
#             print("Maxsulot o'chirildi")
#             return True
#         else:
#             return False
#     def update_stock(self, name, delta_qty) -> bool:
#         if name not in self.praduct:
#             return False
#         elif self.praduct[name]+delta_qty <0:
#             return False
#         else:
#             self.praduct[name]+=delta_qty
#             return True
#     def get_stock(self) -> dict[str,int]:
#         return self.praduct
#     def __str__(self)->str:
#         return  f"Seller {self.name} (rating: {self.reting}, items: {sum(self.praduct.values())})"
# s = Seller("Gulbahor", "g@mail.com", "Samarqand",{}, reting=4.8)
# s.add_product("Keyboard", 10)
# s.update_stock("Keyboard", -3)
# print(s.get_stock())          # {'Keyboard': 7}
# print(s)                      # Seller: Gulbahor (rating: 4.8, items: 7)

#--------------------------------------------------------------1^3tasi

# class Person:
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number

#     def get_name(self):
#         return self.name

#     def get_id(self):
#         return self.id_number

#     def __str__(self):
#         return f"Person: {self.name} (#{self.id_number})"


# class Patient(Person):
#     def __init__(self, name, id_number):
#         super().__init__(name, id_number)
#         self.diagnoses = []
#         self.bill = 0

#     def add_diagnosis(self, text):
#         self.diagnoses.append(text)

#     def add_charge(self, amount):
#         if amount > 0:
#             self.bill += amount
#         else:
#             print("Xato")

#     def pay(self, amount):
#         if amount <= 0:
#             return False

#         if amount >= self.bill:
#             self.bill = 0
#         else:
#             self.bill -= amount

#         return True

#     def get_balance(self):
#         return self.bill

#     def print_history(self):
#         print("Bemor:", self.name)
#         print("ID:", self.id_number)
#         print("Tashxislar:")

#         for i in self.diagnoses:
#             print(i)

#         print("Qarz:", self.bill)

#     def __str__(self):
#         return f"Patient: {self.name}"


# class Doctor(Person):
#     def __init__(self, name, id_number, specialty):
#         super().__init__(name, id_number)
#         self.specialty = specialty
#         self.schedule = {}

#     def add_slot(self, day, time):
#         if day not in self.schedule:
#             self.schedule[day] = []

#         if time not in self.schedule[day]:
#             self.schedule[day].append(time)

#     def book_slot(self, day, time):
#         if day in self.schedule:
#             if time in self.schedule[day]:
#                 self.schedule[day].remove(time)
#                 return True
#         return False

#     def available_slots(self, day):
#         if day in self.schedule:
#             return self.schedule[day]
#         return []

#     def __str__(self):
#         return f"Dr. {self.name} ({self.specialty})"
    
# p = Patient("Aziz", "AB1234567")
# p.add_diagnosis("ORVI")
# p.add_charge(150_000)
# p.add_charge(80_000)
# print(p.get_balance())  # 230000
# p.pay(100_000)
# print(p.get_balance())  # 130000
# p.print_history()

# d = Doctor("Gulrux", "CD7654321", specialty="Cardiologist")
# d.add_slot("Mon", "09:00")
# d.add_slot("Mon", "09:30")
# print(d.book_slot("Mon", "09:00"))  # True
# print(d.book_slot("Mon", "09:00"))  # False
# print(d.available_slots("Mon"))     # ["09:30"]
# print(d) # Dr.Gulrux (Cardiologist)    

#-----------------------------------------------------2-3tasi^

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def get_title(self):
        return self.title

    def get_teacher(self):
        return self.teacher

    def enroll(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
            return True
        return False

    def drop(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            return True
        return False

    def __str__(self):
        return f"Course: {self.title} ({self.teacher})"

class OnlineCourse(Course):
    def __init__(self, title, teacher, url, max_students):
        super().__init__(title, teacher)
        self.url = url
        self.max_students = max_students

    def enroll(self, student_name):
        if len(self.students) < self.max_students:
            return super().enroll(student_name)
        return False

    def get_room(self):
        return f"Virtual: {self.url}"

class OfflineCourse(Course):
    def __init__(self, title, teacher, room, capacity):
        super().__init__(title, teacher)
        self.room = room
        self.capacity = capacity

    def enroll(self, student_name):
        if len(self.students) < self.capacity:
            return super().enroll(student_name)
        return False

    def get_room(self):
        return f"Room: {self.room}"
    
o = OnlineCourse("Python Basics", "Guzal", url="https://nt.uz/py", max_students=2)
print(o.enroll("Ali"))      # True
print(o.enroll("Vali"))     # True
print(o.enroll("Karim"))    # False (to‘ldi)
print(o.get_room())         # Virtual: https://nt.uz/py

f = OfflineCourse("Algorithms", "Dilshod", room="B-203", capacity=1)
print(f.enroll("Soliha"))   # True
print(f.enroll("Nodir"))    # False
print(f.get_room())         # Room: B-203
print(f)    