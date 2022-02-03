import tkinter as tk
from tkinter import *
from tkinter import messagebox
import data
from tkinter import messagebox

black = '#000000'
white = '#ffffff'
color1 = '#A9E1DF'
color2 = '#A9A5DF'




def register():
    window = tk.Tk()
    window.title('Cadastro')
    window.geometry('300x275')
    window.configure(bg=color1)
    window.resizable(False, False)


    def submit():
        if input_name_user.get() == "" or input_user.get() == "" or input_password.get() == "" or input_mail.get() == "":
            messagebox.showinfo(title="ERRO", message="Digite todos os dados") 
            return
        registro()
        input_name_user.delete(0, END)
        input_user.delete(0, END)
        input_password.delete(0, END)
        input_mail.delete(0, END)
        window.destroy()


    def registro():
        name = input_name_user.get()
        user = input_user.get()
        password = input_password.get()
        email = input_mail.get()
        query = "INSERT INTO login (name, user, password, email) VALUES ('"+name+"','"+user+"','"+password+"','"+email+"')"
        vcon = data.ConnectDB()
        data.insert(vcon, query)




    app_line = Label(window, text='', width=300, height=1, padx=0, relief='flat', anchor='center', font=('Arial 1'), bg=color1, fg=black)
    app_line.grid(column=0, row=1)


    name_user = Label(window, text='Nome', height=1, padx=0, relief='flat', anchor='center', font=('Arial 10 bold'), bg=color1, fg=black)
    name_user.place(x=10, y=40)
    input_name_user = Entry(window,text='digite seu nome', width=20, relief='solid', font=('Arial 10 bold'), justify='center', bg=white)
    input_name_user.place(x=80, y=40)

    user = Label(window, text='Usuário', height=1, padx=0, relief='flat', anchor='center', font=('Arial 10 bold'), bg=color1, fg=black)
    user.place(x=10, y=80)
    input_user = Entry(window,text='digite seu usuario', width=20, relief='solid', font=('Arial 10 bold'), justify='center', bg=white)
    input_user.place(x=80, y=80)

    

    login_password = Label(window, text='Senha', height=1, padx=0, relief='flat', anchor='center', font=('Arial 10 bold'), bg=color1, fg=black)
    login_password.place(x=10, y=120)
    input_password = Entry(window, show='*', text='digite sua senha', width=20, relief='solid', font=('Arial 10 bold'), justify='center', bg=white)
    input_password.place(x=80, y=120)

    mail = Label(window, text='E-mail', height=1, padx=0, relief='flat', anchor='center', font=('Arial 10 bold'), bg=color1, fg=black)
    mail.place(x=10, y=160)
    input_mail = Entry(window,text='digite seu e-mail', width=20, relief='solid', font=('Arial 10 bold'), justify='center', bg=white)
    input_mail.place(x=80, y=160)



    register_button = Button(window, command=submit, text='Enviar', width=30, height=1, overrelief=SOLID, relief='raised', border=0, anchor='center', font=('Arial 10 bold'), bg=color2, fg=white, cursor='hand2')
    register_button.place(x=30,y=230)




    window.mainloop()
