from tkinter import *
from tkinter import messagebox

v = "#c557c6"
lc = "#f2d374"
r = "#1F2880"

tela = Tk()
tela.title("Agenda Miau")
tela.geometry("380x500+0+0")
tela.resizable(width=False, height=False)

lb_nome = Label(tela, text="Nome", fg=v, font="Times 10")
lb_nome.place(width=80, height=30, x=10, y=60)
input_nome = Entry(tela, font="Times 10")
input_nome.place(width=150, height=40, x=90, y=60)

lb_telefone = Label(tela, text="Telefone", fg=v, font="Times 10")
lb_telefone.place(width=80, height=30, x=10, y=110)
input_telefone = Entry(tela, font="Times 10")
input_telefone.place(width=150, height=40, x=90, y=110)

lb_datan = Label(tela, text="Nascimento", fg=v, font="Times 10")
lb_datan.place(width=80, height=30, x=10, y=160)
input_datan = Entry(tela, font="Times 10")
input_datan.place(width=150, height=40, x=90, y=160)

lb_nacionalidade = Label(tela, text="Nacionalidade", fg=v, font="Times 10")
lb_nacionalidade.place(width=80, height=30, x=10, y=210)
input_nacionalidade = Entry(tela, font="Times 10")
input_nacionalidade.place(width=150, height=40, x=90, y=210)

lb_email = Label(tela, text="Email", fg=v, font="Times 10")
lb_email.place(width=80, height=30, x=10, y=260)
input_email = Entry(tela, font="Times 10")
input_email.place(width=150, height=40, x=90, y=260)

lb_nota = Label(tela, text="Nota Pessoal", fg=v, font="Times 10")
lb_nota.place(width=80, height=30, x=10, y=310)
input_nota = Entry(tela, font="Times 10")
input_nota.place(width=150, height=40, x=90, y=310)

lb_agenda = Label(tela, text="Agenda", fg=lc, font="Times 20 bold")
lb_agenda.place(width=80, height=30, x=60, y=15)

def adicionar():
    nome = input_nome.get()
    telefone = input_telefone.get()
    datan = input_datan.get()
    nacionalidade = input_nacionalidade.get()
    email = input_email.get()
    notap = input_nota.get()

    with open("AgendaMiau.txt", "a") as Arquivo:
        Arquivo.write(nome)
        Arquivo.write("\n")
        Arquivo.write(telefone)
        Arquivo.write("\n")
        Arquivo.write(datan)
        Arquivo.write("\n")
        Arquivo.write(nacionalidade)
        Arquivo.write("\n")
        Arquivo.write(email)
        Arquivo.write("\n")
        Arquivo.write(notap)

    messagebox.showinfo("Agenda", "Efetuado com sucesso! Agora sai daqui!")

    input_nome.delete('0', 'end')
    input_telefone.delete('0', 'end')
    input_datan.delete('0', 'end')
    input_nacionalidade.delete('0', 'end')
    input_email.delete('0', 'end')
    input_nota.delete('0', 'end')
def pesquisar():
    nome = input_nome.get()
    with open("AgendaMiau.txt", "r") as a:
        for linha in a:
            if nome in linha:
                telefone = (a.readline())
                nascimento = (a.readline())
                nacionalidade = (a.readline())
                email = (a.readline())
                nota = (a.readline())
                l_nome_busca = Label(tela, text=linha, font="Times 10", anchor="w")
                l_nome_busca.place(width=80, height=30, x=10, y=330)
                l_telefone_busca = Label(tela, text=linha, font="Times 10", anchor="w")
                l_telefone_busca.place(width=80, height=30, x=10, y=350)
                l_nascimento_busca = Label(tela, text=linha, font="Times 10", anchor="w")
                l_nascimento_busca.place(width=80, height=30, x=10, y=370)
                l_nacionalidade_busca = Label(tela, text=linha, font="Times 10", anchor="w")
                l_nacionalidade_busca.place(width=80, height=30, x=10, y=390)
                l_email_busca = Label(tela, text=linha, font="Times 10", anchor="w")
                l_email_busca.place(width=80, height=30, x=10, y=410)
                l_nota_busca = Label(tela, text=linha, font="Times 10", anchor="w")
                l_nota_busca.place(width=80, height=30, x=10, y=430)
                messagebox.showinfo("Agenda","Pessoa Encontrada! AGORA FECHA ESTA JANELA!")
            else:
                messagebox.showerror("Agenda","Pessoa Não Encontrada! Vê lá o que tens errado! >:(")
                break

button1 = Button(tela, text="Adicinar Pessoa", fg=r, font="Times 10 bold", command=adicionar)
button1.place(width=100, height=30, x=70, y=380)

button2 = Button(tela, text="Pesquisar", fg=r, font="Times 10 bold", command=pesquisar)
button2.place(width=70, height=30, x=250, y=380)

tela.mainloop()