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
        self.button1 = tk.Button(self.menu_frame, text="Musica", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))
        self.button2 = tk.Button(self.menu_frame, text="Cinema", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))
        self.button3 = tk.Button(self.menu_frame, text="Teatro", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))
        self.button4 = tk.Button(self.menu_frame, text="Turismo", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))
        self.button5 = tk.Button(self.menu_frame, text="Contato", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))
        self.button6 = tk.Button(self.menu_frame, text="Registrar", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))
        self.button7 = tk.Button(self.menu_frame, text="Login", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Georgia", 14))

        #Organiza botões na horizontal
        self.button1.pack(side=LEFT, padx=10)
        self.button2.pack(side=LEFT, padx=10)
        self.button3.pack(side=LEFT, padx=10)
        self.button4.pack(side=LEFT, padx=10)
        self.button5.pack(side=LEFT, padx=10)
        self.button6.pack(side=LEFT, padx=10)
        self.button7.pack(side=LEFT, padx=10)

    def criar_caixa(self, master, nome_evento, data, dia, link):
        caixa = tk.Frame(master)
        caixa.pack(padx=3, pady=3, anchor="center")
        caixa.configure(bg="#1e192c")
        evento_label = tk.Label(caixa, text=nome_evento, font=("Georgia", 14), fg="white")
        evento_label.configure(bg="#1e192c")
        evento_label.pack(pady=20, padx=80, anchor="center")
        data_label = tk.Label(caixa, text=data, font=("Georgia", 12), fg="white")
        data_label.configure(bg="#1e192c")
        data_label.pack()
        dia_label = tk.Label(caixa, text=dia, font=("Georgia", 12), fg="white")
        dia_label.configure(bg="#1e192c")
        dia_label.pack()
        link_label = tk.Label(caixa, text="Saiba mais", font=("Georgia", 12), fg="white", cursor="hand2")
        link_label.configure(bg="#1e192c")
        link_label.pack(pady=10)
    
    

    def frame_principal(self): # frame principal
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=True)

       
        # estilo para as caixas
        style = ttk.Style()
        style.configure("TFrame", background="gray")

        # caixa 1
        caixa1 = ttk.Frame(style="TFrame")
        caixa1.pack(pady=20, padx=40, fill=Y, expand=True)
        self.criar_caixa(caixa1, "Evento 1", "01/01/2022", "Sábado", "https://www.site.com/evento1")

        # caixa 2
        caixa2 = ttk.Frame(style="TFrame")
        caixa2.pack(pady=20, padx=40, fill=Y, expand=True)
        self.criar_caixa(caixa2, "Evento 2", "02/01/2022", "Domingo", "https://www.site.com/evento2")

        # caixa 3
        caixa3 = ttk.Frame(style="TFrame")
        caixa3.pack(pady=20, padx=40, fill=Y, expand=True)
        self.criar_caixa(caixa3, "Evento 3", "03/01/2022", "Segunda", "https://www.site.com/evento3")

          
        

    def rodape(self): #rodapé
        self.footer = tk.Frame(self, bg="#1e192c", height=100)
        self.footer.pack(side=BOTTOM, fill=X)

        # texto do rodapé
        self.footer_text = Label(self.footer, text="Lafacult © 2023 - Todos os direitos reservados", font=("Georgia", 12), bg="#1e192c", fg="white")
        self.footer_text.pack(side=BOTTOM, pady=10)    

if __name__ == "__main__":
    app = Menu()
    app.mainloop()
