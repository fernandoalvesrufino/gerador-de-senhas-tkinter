from tkinter import *
import random
import string
import pyperclip as pc


janela = Tk()
janela.title('Gerador de Senhas')
janela.geometry('320x150')
janela.config(bg='#016064')
janela.resizable(width=False, height=False)

senha = []
tratar_senha = ''


def gerar_senha():
    global tratar_senha
    for i in range(3):
        for _ in range(6):
            senha.append(random.choice(string.digits + string.ascii_letters))
        if i != 2:
            senha.append('-')
        else:
            senha.append('')

    tratar_senha = "".join(senha)
    nova_senha['text'] = tratar_senha
    senha.clear()


def copiar_senha():
    global tratar_senha
    if tratar_senha == '':
        pc.copy('Nenhuma senha foi criada ainda!')
    else:
        pc.copy(tratar_senha)


label = Label(janela, text='GERADOR DE SENHAS', bg='#016064',
              fg='white', font='Arial 10 bold', height=1, width=30)
label.place(x=38, y=15)

nova_senha = Label(janela, text='', bg='white', fg='black',
                   font='Arial 14', height=2, width=23)
nova_senha.place(x=30, y=45)

botao = Button(janela, text='Gerar senha', command=gerar_senha, bg='white',
               fg='black', relief='raised', height=1, width=10, font='Arial 10 bold')
botao.place(x=60, y=105)

botao = Button(janela, text='Copiar senha', command=copiar_senha, bg='white',
               fg='black', relief='raised', height=1, width=10, font='Arial 10 bold')
botao.place(x=170, y=105)


janela.mainloop()
