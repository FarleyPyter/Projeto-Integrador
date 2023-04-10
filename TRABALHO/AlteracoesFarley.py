import tkinter as tk
import sqlite3

# janela principal
window = tk.Tk()
window.title("Lafaiete Cultural")
window.geometry("1200x800")

# cabeçalho 

header = tk.Frame(window, bg="lightblue", height=100)
header.pack(side=tk.TOP, fill=tk.X)

#nome do app e logo

app_name = tk.Label(header, text="Lafaiete Cultural", font=("Arial", 24, "bold"))
logo = tk.PhotoImage(file="TRABALHO\Imagens\logo.png")
app_logo = tk.Label(header, image=logo)
app_name.grid(row=0, column=1)
app_logo.grid(row=0, column=0)

#menu lateral 
menu = tk.Frame(window, bg="white", width=200)
menu.pack(side=tk.LEFT, fill=tk.Y)

# Botões do menu 
button1 = tk.Button(menu, text="Quem somos", command="")
button2 = tk.Button(menu, text="Mural Cultural", command="")
button3 = tk.Button(menu, text="Pesquisar", command="")
button4 = tk.Button(menu, text="Cadastrar", command="")
button5 = tk.Button(menu, text="Login", command="")
button6 = tk.Button(menu, text="Contato", command="")
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)
button6.pack(pady=10)

#rodapé
footer = tk.Frame(window, bg="darkblue", height=50)
footer.pack(side=tk.BOTTOM, fill=tk.X)

info = tk.Label(footer, text="Lafaiete Cultural © 2023 - Todos os direitos reservados", fg="white")
info.pack()

#frame para exibir o mural cultural
mural = tk.Frame(window, bg="lightgray")
mural.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#títulos, as datas e as descrições das atividades culturais
title1 = tk.Label(mural, text="Exposição de arte", font=("Arial", 18, "bold"))
date1 = tk.Label(mural, text="De 01/04/2023 a 30/04/2023", font=("Arial", 14))
desc1 = tk.Label(mural, text="Venha apreciar as obras de artistas locais no Museu da Cidade.", font=("Arial", 12))
title2 = tk.Label(mural, text="Show musical", font=("Arial", 18, "bold"))
date2 = tk.Label(mural, text="Dia 15/04/2023 às 20:00", font=("Arial", 14))
desc2 = tk.Label(mural, text="Não perca o show da banda Rock'n'Roll no Teatro Municipal.", font=("Arial", 12))
title3 = tk.Label(mural, text="Feira de livros", font=("Arial", 18, "bold"))
date3 = tk.Label(mural, text="De 21/04/2023 a 23/04/2023", font=("Arial", 14))
desc3 = tk.Label(mural, text="Aproveite a oportunidade de comprar livros novos e usados na Praça Central.", font=("Arial", 12))

title1.grid(row=0, column=0, padx=10, pady=10)
date1.grid(row=1, column=0, padx=10)
desc1.grid(row=2, column=0, padx=10)
title2.grid(row=0, column=1, padx=10, pady=10)
date2.grid(row=1, column=1, padx=10)
desc2.grid(row=2, column=1, padx=10)
title3.grid(row=0, column=2, padx=10, pady=10)
date3.grid(row=1, column=2, padx=10)
desc3.grid(row=2, column=2, padx=10)

#banco de dados para armazenar as informações dos usuários que se cadastrarem no nosso app

def create_db():
    conn = sqlite3.connect("lafaiete.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
    conn.commit()
    conn.close()

create_db()    

#receber os dados do usuário que se cadastrar no nosso app e inserir esses dados na tabela users do banco de dados
def register():
    conn = sqlite3.connect("lafaiete.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name_entry.get(), email_entry.get(), password_entry.get()))
        conn.commit()
        tk.messagebox.showinfo(title="Sucesso", message="Usuário cadastrado com sucesso!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    except sqlite3.Error as e:
        tk.messagebox.showerror(title="Erro", message=f"Ocorreu um erro ao cadastrar o usuário: {e}")
    finally:
        conn.close()

"""  # Botão de cadastro na janela de login
register_button = tk.Button(login_window, text="Cadastrar", command=create_register_window)
register_button.pack() 

#janela para o usuário se cadastrar no nosso app. 
def create_register_window():
    register_window = tk.Toplevel(window)

    # adicionar os entrys
    name_entry = tk.Entry(register_window)
    email_entry = tk.Entry(register_window)
    password_entry = tk.Entry(register_window, show="*")

    # criar as labels
    name_label = tk.Label(register_window, text="Nome")
    email_label = tk.Label(register_window, text="E-mail")
    password_label = tk.Label(register_window, text="Senha")

    # posicionar os elementos
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    email_label.grid(row=1, column=0)
    email_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)

    # criar o botão de cadastro
    register_button = tk.Button(register_window, text="Cadastrar", command=register)
    register_button.grid(row=3, column=1)

    #Associar a função `create_register_window` ao botão "Cadastrar" do menu principal.
    button4 = tk.Button(menu, text="Cadastrar", command=create_register_window)


# recebe o email e a senha do usuário e verificar se esses dados estão corretos no banco de dados. 
def login():
    conn = sqlite3.connect("lafaiete.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password FROM users WHERE email = ?", (email_entry.get(),))
        result = cursor.fetchone()
        if result is not None and result[0] == password_entry.get():
            tk.messagebox.showinfo(title="Sucesso", message="Usuário logado com sucesso!")
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            tk.messagebox.showerror(title="Erro", message="Email ou senha incorretos!")
    except sqlite3.Error as e:
        tk.messagebox.showerror(title="Erro", message=f"Ocorreu um erro ao logar o usuário: {e}")
    finally:
        conn.close()

# janela para o usuário se logar no nosso app    
def create_login_window():
    login_window = tk.Toplevel()
    login_window.title("Logar")
    login_window.geometry("300x150")
    email_label = tk.Label(login_window, text="Email:")
    email_entry = tk.Entry(login_window)
    password_label = tk.Label(login_window, text="Senha:")
    password_entry = tk.Entry(login_window, show="*")
    login_button = tk.Button(login_window, text="Logar", command=login)    
    email_label.grid(row=0, column=0, padx=10, pady=10)
    email_entry.grid(row=0, column=1, padx=10)
    password_label.grid(row=1, column=0, padx=10)
    password_entry.grid(row=1, column=1, padx=10)
    login_button.grid(row=2, columnspan=2, pady=10)
    
    #associar a função `create_login_window` ao botão "Logar" do menu principal
    button3 = tk.Button(menu, text="Logar", command=create_login_window) """

window.mainloop()
