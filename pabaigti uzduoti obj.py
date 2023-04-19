
from tkinter import *

class Users:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    def get_user_info(self):
        return self.name + self.last_name

class Student(Users):

    def __init__(self,name, last_name, student_code):
        super().__init__(name, last_name)
        self.student_code = student_code
    def get_user_info(self):
        return self.name + last_name + student_code

class Admin(Users):

    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.admin_name = name
        self.admin_last_name = admin_last_name

    def get_user_info(self):
        return self.admin_name + admin_last_name

class Guest(Users):
    pass


stud = Student("A", "ZB", 546)
users = []

"""
Uzduotis 1: Sukurti klasę User, kuri turi properties: name, last_name.
Klasė turi funkciją get_user_info(), kuri gražina (return): vartotojo vardą ir pavardę

Uzduotis 2:
Sukurti klases Student, Admin, Guest, kurios paveldi iš User klasės
Student klasė turi papildomą property: student_code

Student klasė turi perrašyti get_user_info() metodą. 
Nauja funkcija turi gražinti (return): vartotojo vardą, pavardę, studento_kodą
"""

def add_student():
    vardas = name_field.get()
    pavarde = last_name_field.get()
    print( f"Pridedam studenta {vardas} {pavarde}" )

    # Pridėti studentą į users listą, su vardu, pavarde, ir atsitiktinai parinktu studento kodu

def add_admin():
    vardas = name_field.get()
    vartotojas = pavarde = last_name_field.get()
    # Pridėti admin vartotoją su vardu ir pavarde

def show_users():
    for user in users:
        # Uzduotis: iskviesti funkciją, kuri gražintų pilną vartotojo informaciją
        # Gautą informaciją atspausdinti (print)
        pass

window = Tk()
window.geometry( "300x400" )

name_lbl = Label( window, text="Vardas: " )
name_field = Entry( window )

last_name_lbl = Label( window, text="Pavarde: " )
last_name_field = Entry( window )

btn = Button(window, text="Pridėti studentą", command=add_student )
btn2 = Button(window, text="Pridėti administratorių", command=add_admin )
btn3 = Button(window, text="Rodyti vartotojus", command=show_users )

name_lbl.grid( row = 0, column = 0 )
name_field.grid( row = 0, column = 1 )
last_name_lbl.grid( row = 1, column = 0 )
last_name_field.grid( row = 1, column = 1 )

btn.grid( row = 2, column = 0 )
btn2.grid( row = 2, column = 1 )
btn3.grid( row = 3, column = 0 )
window.mainloop()