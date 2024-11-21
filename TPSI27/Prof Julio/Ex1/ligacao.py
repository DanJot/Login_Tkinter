import pyodbc as pbd

def conexao():
    driver = "odbc driver 17 for sql server"
    servidor = "AUD-PORT-012\\SQLEXPRESS" #Está na pagina inicial do SQL Server, duas \\ senao \S significa outra coisa
    basedados = "proj27"
    utilizador = "sa"
    password = "z43VGYT@Iu"

    try:
        con = pbd.connect(f"DRIVER={driver};SERVER={servidor};DATABASE={basedados};UID={utilizador};PWD={password}")
        print("Conexão feita com sucesso")
        return con

    except:
        return False





