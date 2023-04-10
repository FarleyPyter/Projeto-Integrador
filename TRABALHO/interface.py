from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import ttk

class Menu(CTk):
    def __init__(self):
        super().__init__() 
        self.janela_principal()
        self.cabecalho()
        self.frame_principal()
        self.rodape()
    
    # janela principal
    def janela_principal(self):        
        self.title("Lafaiete Cultural")
        self.geometry("1310x740")
        self.resizable(False,False)

    # cabeçalho
    def cabecalho(self):    
        
        self.header = tk.Frame(self, bg="#1e192c", height=100)
        self.header.pack(side=TOP, fill=X)

        # nome do app e logo
        self.logo = tk.PhotoImage(file="TRABALHO\Imagens\logo.png")
        self.logo_label = tk.Label(self.header, image=self.logo, bg="#1e192c")
        self.logo_label.grid(row=0, column=0, padx=20)

        # frame para os botões do menu
        self.menu_frame = tk.Frame(self.header, bg="#1e192c")
        self.menu_frame.grid(row=0, column=2, padx=490)

        # Botões do menu 
        self.button1 = tk.Button(self.menu_frame, text="Musica", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button2 = tk.Button(self.menu_frame, text="Cinema", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button3 = tk.Button(self.menu_frame, text="Teatro", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button4 = tk.Button(self.menu_frame, text="Turismo", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button5 = tk.Button(self.menu_frame, text="Contato", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button6 = tk.Button(self.menu_frame, text="Registrar", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button7 = tk.Button(self.menu_frame, text="Login", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))

        #Organiza botões na horizontal
        self.button1.pack(side=LEFT, padx=10)
        self.button2.pack(side=LEFT, padx=10)
        self.button3.pack(side=LEFT, padx=10)
        self.button4.pack(side=LEFT, padx=10)
        self.button5.pack(side=LEFT, padx=10)
        self.button6.pack(side=LEFT, padx=10)
        self.button7.pack(side=LEFT, padx=10)

    def criar_caixa(self, master, nome_evento, data, dia, link, texto):
        caixa = tk.Frame(master)
        caixa.pack(padx=3, pady=3)
        caixa.configure(bg="#1e192c")
        evento_frame = tk.Frame(caixa, bg="#1e192c")
        evento_frame.pack(side=TOP, pady=20)
        evento_label = tk.Label(evento_frame, text=nome_evento, font=("Georgia", 14), fg="white")
        evento_label.configure(bg="#1e192c")
        evento_label.pack(side=TOP, anchor="center")
        data_label = tk.Label(evento_frame, text=data, font=("Georgia", 16), fg="white")
        data_label.configure(bg="#1e192c")
        data_label.pack(side=TOP)
        dia_label = tk.Label(caixa, text=dia, font=("Georgia", 16), fg="white")
        dia_label.configure(bg="#1e192c")
        dia_label.pack()
        link_frame = tk.Frame(caixa, bg="#1e192c")
        link_frame.pack(pady=20)
        link_label = tk.Label(link_frame, text="Saiba mais", font=("Georgia", 12), fg="white", cursor="hand2")
        link_label.pack(side=LEFT)
        link_label.configure(bg="#1e192c")
        texto_label = tk.Label(link_frame, text=texto, font=("Georgia", 12), fg="white")
        texto_label.configure(bg="#1e192c")
        texto_label.pack(side=LEFT, padx=10)

    def frame_principal(self): # frame principal
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=True)

       
        # estilo para as caixas
        style = ttk.Style()
        style.configure("TFrame", background="gray")

        # caixa 1
        caixa1 = ttk.Frame(style="TFrame")
        caixa1.pack(pady=20, padx=40, fill=Y, expand=True)
        self.criar_caixa(caixa1, "Evento 1", "01/01/2022", "Sábado", "https://www.site.com/evento1", "A arte é uma forma de expressão que transcende as barreiras da linguagem e da cultura. Ela nos permite explorar nossas emoções e ideias de maneiras únicas e pessoais. Através da arte, podemos nos conectar com os outros e com o mundo ao nosso redor.")

        # caixa 2
        caixa2 = ttk.Frame(style="TFrame")
        caixa2.pack(pady=20, padx=40, fill=Y, expand=True)
        self.criar_caixa(caixa2, "Evento 2", "02/01/2022", "Domingo", "https://www.site.com/evento2", "A cultura é a essência da nossa identidade coletiva. Ela nos conecta com nossas raízes e nos ajuda a entender de onde viemos. Através da cultura, podemos celebrar nossas diferenças e encontrar pontos em comum. Ela nos ensina a respeitar e valorizar a diversidade.")

        # caixa 3
        caixa3 = ttk.Frame(style="TFrame")
        caixa3.pack(pady=20, padx=40, fill=Y, expand=True)
        self.criar_caixa(caixa3, "Evento 3", "03/01/2022", "Segunda", "https://www.site.com/evento3", "A música é uma linguagem universal que transcende as fronteiras culturais e geográficas. Ela nos permite expressar nossas emoções e nos conecta com os outros de maneiras profundas e significativas. Através da música, podemos encontrar conforto, inspiração e alegria.")

          
        

    def rodape(self): #rodapé
        self.footer = tk.Frame(self, bg="#1e192c", height=100)
        self.footer.pack(side=BOTTOM, fill=X)

        # texto do rodapé
        self.footer_text = Label(self.footer, text="Lafacult © 2023 - Todos os direitos reservados", font=("Arial", 12), bg="#1e192c", fg="white")
        self.footer_text.pack(side=BOTTOM, pady=10)    

if __name__ == "__main__":
    app = Menu()
    app.mainloop()
