from tkinter import *
from tkinter import messagebox
v="c557c6"
lc="f2d374"
def adicionar():
    nome= input_nome.get()
    telefone = input_telefone.get()
    datan= input_datan.get()
    nacionalidade= input_nacionalidade.get()
    email = input_email.get()

    messagebox.showinfo("Agenda","Efetuado com sucesso! Agora sai daqui!")

    input_nome.delete('0', 'end')
    input_telefone.delete('0', 'end')
    input_datan.delete('0', 'end')
    input_nacionalidade.delete('0', 'end')
    input_email.delete('0', 'end')
adicionar()
tela = Tk()
tela.title("Agenda Miau")
tela.geometry("380x500+700x700")
tela.resizable(width=False, height=False)
tela.mainloop()

button1 = Button(tela,text="Adicinar Pessoa",fg=v,font="Times 10 bold")
button1.place(width=80,height=30,x=70,y=310)

lb_agenda= Label(tela,text="Agenda",fg=lc,font="Times 20 bold")
lb_nome = Label(tela,text="Nome",fg=v,font="Times 10")
lb_nome.place(width=80,height=30,x=70,y=40)
input_nome = Entry(tela, font="Times 10")
input_nome.place(width=70,height=40,x=60,y=30)