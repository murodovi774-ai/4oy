#------------------------------------------------------2
# class kompiuter:
#     def __init__(self,nomi,ram,narx,pratsesor):
#         self.nomi=nomi
#         self.ram=ram
#         self.narx=narx
#         self.pratsesor=pratsesor
#     def upgred_ram(self,new_ram):
#         print("Ram qo'shildi")
#         self.ram=new_ram    
#         self.komp_ram()
        
#     def komp_ram(self):
#         if self.ram >=8 and self.ram<=16:
#             print("Ram yetarli ")
#             print(f"{self.nomi} {self.ram} {self.narx} {self.pratsesor}")
#         else:
#             print("Ram kamlik qildi kuchaytirasizmi necha Gb qilamiz")
#             self.upgred_ram(int(input()))        

# lst = [kompiuter(input(), int(input()),int(input()),input()) for i in range(int(input("nechta kompiuter")))]          
# for i in lst:
#     i.komp_ram()   
#---------------------------------------------------3
# class user:
#     def __init__(self,nomi,ism,familya,tugulgan_sana):
#         self.nomi=nomi
#         self.ism=ism
#         self.familya=familya
#         self.tugulgan_sana=tugulgan_sana
#     def user_info(self):
#         print(f"Nomi:{self.nomi} Ism Fsmilya:{self.ism.title()+" "+self.familya.title()} Gmail:{self.ism+self.familya+self.tugulgan_sana[-4::]+"@gmail.com"}")    

# u1=user("izzat3733","izzat","murodov","12.10.2007")
# u1.user_info()

#------------------------------------------------1

# class Kitob:
#     def __init__(self, nomi, mualliflari, narxi, nashriyoti):
#         self.nomi = nomi
#         self.mualliflari = mualliflari
#         self.narxi = narxi
#         self.nashriyoti = nashriyoti
#     def info(self):
#         if "A" <= self.nashriyoti[0].upper() <= "H":
#             print(f"{self.nomi} {self.mualliflari} {self.narxi} so'm: {self.nashriyoti}")
#         else:
#             print("Bunday kitob yo'q")
# lst=[Kitob(input("Nomi "),input("Mualiflari "),int(input("Narxi ")),input("Nashiryoti ")) for i in range(int(input("Nechta kitob ")))]            
# for i in lst:
#     i.info()