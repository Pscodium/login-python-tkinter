import tkinter as tk
from tkinter import *
from tkinter import ttk
from register import register
import data
from tkinter import messagebox

black = '#000000'
white = '#ffffff'
color1 = '#A9E1DF'
color2 = '#A9A5DF'




window = tk.Tk()
window.title("Login")
window.geometry("300x250")
window.configure(bg=color1)
window.resizable(False, False)



def consultar():
    try:
        user = usuario.get()
        password = senha.get()
        query = "SELECT * FROM login WHERE user='"+user+"' AND password='"+password+"'"
        vcon = data.ConnectDB()
        login = data.login(vcon, query)
        if login:
            messagebox.showinfo(title="ERRO", message="Sucesso")
        else:
            messagebox.showinfo(title="ERRO", message="Usuário ou Senha incorretos")
    except:
        messagebox.showinfo(title="ERRO", message="Usuário ou Senha incorretos")




usuario_lb = Label(window, text="Usuário", bg=color1, fg=black, font=('Arial 10 bold'))
usuario_lb.place(x=45, y=40)
usuario = Entry(window, width=25, bg=white, fg=black, highlightbackground=white, relief='solid', border=0)
usuario.place(x=45, y=60)

senha_lb = Label(window, text="Senha", bg=color1, fg=black, font=('Arial 10 bold'))
senha_lb.place(x=45, y=100)
senha = Entry(window, width=25, bg=white, fg=black, highlightbackground=white, relief='solid', border=0, show='*')
senha.place(x=45, y=120)

reg = Button(window, text='Crie sua Conta',command=register, border=0, width=15, bg=color1, fg=black, overrelief=SOLID, activebackground=color1, relief='solid', highlightbackground=color1, cursor='hand2', activeforeground=white)
reg.place(x=20, y=143)
log = Button(window, text='logar', font=('Arial 10 bold'), command=consultar, border=0, width=30, bg=color2, fg=white)
log.place(x=30, y=200)



window.mainloop()