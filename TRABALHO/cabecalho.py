from tkinter import *

class Menu(Tk):
    def __init__(self):
        super().__init__() 
        self.janela_principal()
        self.cabecalho()
        #self.frame_principal()
        self.rodape()
        
    # janela principal
    def janela_principal(self):        
        self.title("Lafaiete Cultural")
        self.geometry("1310x740")
        self.resizable(False,False)

    # cabeçalho
    def cabecalho(self):    
        
        self.header = Frame(self, bg="#1e192c", height=100)
        self.header.pack(side=TOP, fill=X)

        # nome do app e logo
        self.logo = PhotoImage(file="TRABALHO/Imagens/logo.png")
        self.app_logo = Label(self.header, image=self.logo, bg="#1e192c")
        self.app_logo.grid(row=0, column=0, padx=20)

        # frame para os botões do menu
        self.menu_frame = Frame(self.header, bg="#1e192c")
        self.menu_frame.grid(row=0, column=2, padx=490)

        # Botões do menu 
        self.button1 = Button(self.menu_frame, text="Musica", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button2 = Button(self.menu_frame, text="Cinema", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button3 = Button(self.menu_frame, text="Teatro", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button4 = Button(self.menu_frame, text="Turismo", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button5 = Button(self.menu_frame, text="Contato", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button6 = Button(self.menu_frame, text="Registrar", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))
        self.button7 = Button(self.menu_frame, text="Login", command="", highlightthickness=0, bd=0, bg="#1e192c", fg="white", font=("Arial", 14))

        #Organiza botões na horizontal
        self.button1.pack(side=LEFT, padx=10)
        self.button2.pack(side=LEFT, padx=10)
        self.button3.pack(side=LEFT, padx=10)
        self.button4.pack(side=LEFT, padx=10)
        self.button5.pack(side=LEFT, padx=10)
        self.button6.pack(side=LEFT, padx=10)
        self.button7.pack(side=LEFT, padx=10)


    def rodape(self): #rodapé
        self.footer = Frame(self, bg="#1e192c", height=100)
        self.footer.pack(side=BOTTOM, fill=X)

        # texto do rodapé
        self.footer_text = Label(self.footer, text="Lafacult © 2023 - Todos os direitos reservados", font=("Arial", 12), bg="#1e192c", fg='white')
        self.footer_text.pack(side=BOTTOM, pady=10)

if __name__ == '__main__':
    app = Menu()
    app.mainloop()


# def frame_principal(self): # frame principal
#         self.main_frame = Frame(self)
#         self.main_frame.pack(side=TOP, fill=BOTH, expand=True)

#         # frame com barra de rolagem
#         scrollable_frame = Frame(self.main_frame)
#         scrollable_frame.pack(side=LEFT, fill=BOTH, expand=True)

#         # barra de rolagem
#         scrollbar = Scrollbar(scrollable_frame, orient="vertical", bg="#1e192c")
#         scrollbar.pack(side=RIGHT, fill=Y)

#         # texto modelo
#         sample_text = Text(scrollable_frame, yscrollcommand=scrollbar.set, font=("Arial", 14), bg="white", fg="black")
#         sample_text.insert(END, 'dskjfsdkjhf')
#         sample_text.pack(side=LEFT, fill=BOTH, expand=True)

#         # vincula a barra de rolagem ao texto
#         scrollbar.config(command=sample_text.yview)