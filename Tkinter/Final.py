####BIBLIOTECAS####
from tkinter import *
import customtkinter
from ligacao import *
from tkinter.messagebox import * #Biblioteca para janelas pre formatadas
from tkinter import filedialog

#Personalizar para tema escuro do customTkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


####FUNÇÕES####

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

def registar():
    # Cria a janela de novo registo
    jan2 = customtkinter.CTkToplevel()
    jan2.title("Novo Registo")
    jan2.geometry("300x250+780+330")
    jan2.lift()
    jan2.attributes("-topmost", True)
    jan2.after(10, lambda: jan2.attributes("-topmost", False))

    # Labels e campos de entrada
    label_user = customtkinter.CTkLabel(jan2, text="Novo Username")
    label_user.pack(pady=5)
    entry_user = customtkinter.CTkEntry(jan2, placeholder_text="Username")
    entry_user.pack(pady=5)

    label_pass = customtkinter.CTkLabel(jan2, text="Nova Password")
    label_pass.pack(pady=5)
    entry_pass = customtkinter.CTkEntry(jan2, placeholder_text="Password", show="*")
    entry_pass.pack(pady=5)

    # Função para inserir o novo utilizador na base de dados
    def inserir_utilizador():
        username = entry_user.get()
        password = entry_pass.get()

        if username and password:
            con = conexao()  # Conecta à base de dados
            cursor = con.cursor()
            try:
                # Inserir os dados na tabela login
                sql = "INSERT INTO login (nome, senha) VALUES (?, ?)"
                cursor.execute(sql, (username, password))
                con.commit()
                showinfo("Registo", "Novo utilizador registado com sucesso!")
                jan2.destroy()  # Fecha a janela de registo
            except Exception as e:
                showerror("Erro", f"Ocorreu um erro: {e}")
            finally:
                con.close()
        else:
            showwarning("Atenção", "Por favor, preencha todos os campos.")

    # Botão de registo
    botao_registar = customtkinter.CTkButton(jan2, text="Registar", fg_color="aquamarine4", hover_color="dark slate gray", command=inserir_utilizador)
    botao_registar.pack(pady=20)

    jan2.mainloop()


def entrar(): #liga à BD, obtem credenciais
    con = conexao()
    cursor = con.cursor()
    username = luser.get()
    password = lpass.get()
    sql =f"""select * from login where nome = '{username}' and senha = '{password}'"""
    cursor.execute(sql)
    resp = cursor.fetchone()
    if resp [2] == password:
        abrir_janela_importar_exportar()
    else:
        showerror("Erro de Login...", "Erro nas credênciais.\nVerifique o User e a Pass")
        limpar()



def abrir_janela_importar_exportar():
    jan3 = customtkinter.CTkToplevel()
    jan3.title("Importar/Exportar Ficheiros")
    jan3.geometry("300x250+710+350")
    jan3.lift()
    jan3.attributes("-topmost", True)
    jan3.after(10, lambda: jan3.attributes("-topmost", False))

    def importar():
        file = filedialog.askopenfile(mode="r", title="Selecionar Ficheiro para Importar")
        cont = file.readlines()
        con = conexao()
        cursor = con.cursor()
        cont.pop(0)  # Elimina a primeira linha que é a estrutura do ficheiro
        for line in cont:
            dados = line.strip().split(";")  # Divide a linha em campos
            # Verifica se o número de campos em 'dados' é o esperado (8 colunas no ficheiro)
            if len(dados) != 8:
                print(f"Linha ignorada por número incorreto de campos: {line}")
                continue  # Ignora linhas com o número de colunas incorreto
            # Remove o valor da coluna `no`, que corresponde à posição [1] em `dados`
            dados.pop(1)
            # Query sem a coluna `no`, que é preenchida automaticamente
            sql = """
                INSERT INTO clientes (nome, ncont, esaldo, morada, local, codpost, zona) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6]))

        con.commit()  # Efetiva a gravação dos dados na BD
        con.close()
        print("Importação concluída com sucesso!")
        showinfo("Importação", "Importação concluída com sucesso!")

    def exportar():
        file = filedialog.asksaveasfile(mode='w', defaultextension=".csv", title="Selecionar Ficheiro para Exportar")
        if file:
            con = conexao()  # Conecta à base de dados
            cursor = con.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()

            # Escrever os dados no arquivo
            for row in rows:
                # Converte cada linha  numa string separada por ponto e vírgula
                line = ';'.join(str(value) for value in row) + '\n'
                file.write(line)

            file.close()  # Fecha o arquivo
            cursor.close()  # Fecha o cursor
            con.close()  # Fecha a conexão
            print("Exportação concluída com sucesso!")
            showinfo("Exportação", "Exportação concluída com sucesso!")

    label = customtkinter.CTkLabel(jan3, text="Escolha uma opção:")
    label.pack(padx=10, pady=10)

    b_importar = customtkinter.CTkButton(jan3, text="Importar Ficheiro", fg_color="aquamarine4", hover_color="dark slate gray", command=importar)
    b_importar.pack(padx=10, pady=10)

    b_exportar = customtkinter.CTkButton(jan3, text="Exportar Ficheiro", fg_color="aquamarine4", hover_color="dark slate gray", command=exportar)
    b_exportar.pack(padx=10, pady=10)

    b_close = customtkinter.CTkButton(jan3, text="Fechar", fg_color="indian red", hover_color="brown4", command=lambda: janela_importar_exportar.destroy())
    b_close.pack(padx=10, pady=10)


#####JANELA PRINCIPAL####

janela = customtkinter.CTk()
janela.geometry("400x350+710+250") # 400x200 - tamanho da janela;  600+250 - onde aparece a janela no ecra
janela.title("Sistema de Login")


intro = customtkinter.CTkLabel(janela,text='Login')
intro.pack(padx=10, pady=10)

luser = customtkinter.CTkEntry(janela, placeholder_text='Insira username') #Etiqueta com o texto Username posicionado na janela
luser.pack(padx=10, pady=10)

lpass = customtkinter.CTkEntry(janela, placeholder_text='Insira password',show='*')
lpass.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela,text='Lembrar Senha')
checkbox.pack(anchor='center')


####BOTÕES####

blogin = customtkinter.CTkButton(janela, text="Login", fg_color="aquamarine4", hover_color="dark slate gray", command=entrar)
blogin.pack(padx=10, pady=10)

bclean = customtkinter.CTkButton(janela, text="Limpar", fg_color="gray43", hover_color="gray26", command= limpar)
bclean.place(relx=0.3, rely=0.7, anchor="center")

bnew = customtkinter.CTkButton(janela, text="Novo Registo", fg_color="gray43", hover_color="gray26", command=registar)
bnew.place(relx=0.7, rely=0.7, anchor="center")

bclose = customtkinter.CTkButton(janela, text="Fechar", fg_color="indian red", hover_color="brown4", command=lambda:janela.destroy())
bclose.place(relx=0.5, rely=0.9, anchor="center")


janela.mainloop()

