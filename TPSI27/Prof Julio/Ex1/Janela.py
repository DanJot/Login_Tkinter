#Bibliotecas:
from tkinter import *
import customtkinter
from ligacao import *
from tkinter.messagebox import * #Biblioteca para janelas pre formatadas


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Funçoes
def limpar():
    luser.delete(0,END)
    lpass.delete(0,END)
    luser.focus()

def abandonar(nome):
    #jan.deiconify()#volta a mostrar janela
    nome.destroy()

def leitura():
    nome = luser.get() #lê o que está na entry
    senha = lpass.get()
    print(f"O username é {nome}")
    print(f"A pass é {senha}")

def registar(): #criar nova janela com campos da tabela login na BD(id,user,pass)
    # jan.iconify()#esconde na barra de tarefas
    # jan.withdraw()#esquece que existe a janela
    jan2 = Toplevel()
    b = customtkinter.CTkButton(jan2,text="texto",
               command=lambda:abandonar(jan2)).pack()
    jan2.mainloop()

def entrar(): #liga à BD, obtem credenciais
    con = conexao()
    cursor = con.cursor()
    username = luser.get()
    password = lpass.get()
    sql =f"""select * from login where nome like '{username}' and senha like '{password}'"""
    cursor.execute(sql)
    resp = cursor.fetchone()
    if resp == None:
        #dá msg de erro
        showerror("Erro de Login...", "Erro nas credênciais.\nVerifque o user e a pass")
        limpar()
    else:
        janela=Toplevel()
        janela.mainloop()




janela = customtkinter.CTk()
janela.geometry("400x350+600+250") # 400x200 - tamanho da janela;  600+250 - onde aparece a janela no ecra
janela.title("Sistema de Login")

intro = customtkinter.CTkLabel(janela,text='Login')
intro.pack(padx=10, pady=10)

luser = customtkinter.CTkEntry(janela, placeholder_text='Insira username') #Etiqueta com o texto Username posicionado na janela
luser.pack(padx=10, pady=10)

lpass = customtkinter.CTkEntry(janela, placeholder_text='Insira password',show='*')
lpass.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela,text='Lembrar Senha')
checkbox.pack(anchor='center')

#Botões

blogin = customtkinter.CTkButton(janela, text="Login", fg_color="aquamarine4", hover_color="dark slate gray", command=entrar)
blogin.pack(padx=10, pady=10)

bclean = customtkinter.CTkButton(janela, text="Limpar", fg_color="gray43", hover_color="gray26", command= limpar)
bclean.place(relx=0.3, rely=0.7, anchor="center")

bnew = customtkinter.CTkButton(janela, text="Novo Registo", fg_color="gray43", hover_color="gray26", command=registar)
bnew.place(relx=0.7, rely=0.7, anchor="center")

bclose = customtkinter.CTkButton(janela, text="Fechar", fg_color="indian red", hover_color="brown4", command=lambda:janela.destroy())
bclose.place(relx=0.5, rely=0.9, anchor="center")


janela.mainloop()

