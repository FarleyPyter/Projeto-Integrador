from customtkinter import *
from tkinter import messagebox
import requests
import urllib.request
import sys
from PIL import Image
import random
import numpy
import time

janela = CTk()
janela.resizable(False,False)
janela.geometry('1310x740')

label = CTkLabel(janela, text='',font = ('arial ',25,'bold'),text_color = ('black'))
label.pack(pady=5)

#arquivo = open('DescricaoEventos.txt')#descicao dos eventos aqui

#salvando eventos dentro de um dicionario
eventos =[
    {    
    'nome':'Pânico 5',
    'categoria':'cinema',
    'Google maps':'https://goo.gl/maps/FeGpg5mmvfsehYTEA',
    'descrição': 'Pânico 6, sessão todos os dias ás 21:30',
    'imagem':'https://lh3.googleusercontent.com/p/AF1QipPerSg67foBpcHhNEPtcXLWQ8Oh0WBVHnShk3qe=w1080-h608-p-k-no-v0'
    },
    
    {
    'nome':'St. Patrick´s Day ',
    'categoria':'show',
    'Google maps':'bit.ly/3ngEITi',
    'descrição': '1 abr - 2023 • 15:00 > 2 abr - 2023 • 02:00',
    'imagem':'https://img.cancaonova.com/cnimages/canais/uploads/sites/2/2022/03/S%C3%A3o-Patr%C3%ADcio-300x300.png'
    
    },
    {
    'imagem':'http://s.glbimg.com/jo/g1/f/original/2011/03/19/sao_patricio_1.jpg'
    }

]



link = eventos[0]['imagem']
try:
    urllib.request.urlretrieve(link, "evento.jpeg")  #abrir imagem do evento
except:
    erro = sys.exc_info()
    messagebox.showerror('evento.jpeg', erro)
else:
    foto = CTkImage(light_image=Image.open('evento.jpeg'), dark_image=Image.open('evento.jpeg'), size=(380, 250)) #colocando a imagem no label
    label.configure(image=foto)
    

def salvar_imagens():
    for i, evento in enumerate(eventos):
        link = evento['imagem']
        try:
            urllib.request.urlretrieve(link, f"evento{i}.jpeg")  #abrir imagem do evento
        except:
            erro = sys.exc_info()
            messagebox.showerror(f"evento{i}.jpeg", erro)
            mostrar_imagens(evento[i])


def mostrar_imagens():
    foto = CTkImage(light_image=Image.open(f"evento{i}.jpeg"), dark_image=Image.open(f"evento{i}.jpeg"), size=(380, 250)) #colocando a imagem no label
    label.configure(image=foto)
            
    
        
        




botao_direita = CTkButton(janela,text='->',font=('Arial', 40, 'bold'),width=150,command=salvar_imagens)
botao_direita.pack()
janela.mainloop()