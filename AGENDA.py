from tkinter import *
from tkinter import messagebox

v="#c557c6"
lc="#f2d374"

tela = Tk()
tela.title("Agenda Miau")
tela.geometry("380x500+0+0")
tela.resizable(width=False, height=False)

lb_nome = Label(tela,text="Nome",fg=v,font="Times 10")
lb_nome.place(width=80,height=30,x=10,y=70)
input_nome = Entry(tela, font="Times 10")
input_nome.place(width=70,height=40,x=90,y=70)

lb_telefone = Label(tela,text="Telefone",fg=v,font="Times 10")
lb_telefone.place(width=80,height=30,x=10,y=110)
input_telefone = Entry(tela, font="Times 10")
input_telefone.place(width=70,height=40,x=90,y=110)

lb_datan = Label(tela,text="Data Nascimento",fg=v,font="Times 10")
lb_datan.place(width=80,height=30,x=10,y=150)
input_datan = Entry(tela, font="Times 10")
input_datan.place(width=70,height=40,x=90,y=150)

lb_nacionalidade = Label(tela,text="Nacionalidade",fg=v,font="Times 10")
lb_nacionalidade.place(width=80,height=30,x=10,y=190)
input_nacionalidade = Entry(tela, font="Times 10")
input_nacionalidade.place(width=70,height=40,x=90,y=190)

lb_email = Label(tela,text="Email",fg=v,font="Times 10")
lb_email.place(width=80,height=30,x=10,y=230)
input_email = Entry(tela, font="Times 10")
input_email.place(width=70,height=40,x=90,y=230)

lb_nota = Label(tela,text="Nota Pessoal",fg=v,font="Times 10")
lb_nota.place(width=80,height=30,x=10,y=270)
input_nota = Entry(tela, font="Times 10")
input_nota.place(width=70,height=40,x=90,y=270)


lb_agenda= Label(tela,text="Agenda",fg=lc,font="Times 20 bold")
def adicionar():
    nome= input_nome.get()
    telefone = input_telefone.get()
    datan= input_datan.get()
    nacionalidade= input_nacionalidade.get()
    email = input_email.get()
    notap = input_nota.get()

    with open ("AgendaMiau.txt","a") as Arquivo:
        Arquivo.write(nome)
        Arquivo.write("\n")
        Arquivo.write(telefone)

    messagebox.showinfo("Agenda","Efetuado com sucesso! Agora sai daqui!")

    input_nome.delete('0', 'end')
    input_telefone.delete('0', 'end')
    input_datan.delete('0', 'end')
    input_nacionalidade.delete('0', 'end')
    input_email.delete('0', 'end')
    input_nota.delete('0','end')
    
button1 = Button(tela,text="Adicinar Pessoa",fg=v,font="Times 10 bold",command=adicionar)
button1.place(width=80,height=30,x=70,y=350)

tela.mainloop()
