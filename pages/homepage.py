import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

class HomeClient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Home Client
        label_Welcome = ttk.Label(self, text="Bem vindo ao FlashMall", font=LARGEFONT)
        label_Welcome.place(relx=0.5, rely=0.3, anchor='center')

        label_Instruc = ttk.Label(self, text="Para iniciar a compra, clique no botão 'Iniciar Compra'",
                                  font=LARGEFONT)
        label_Instruc.place(relx=0.5, rely=0.4, anchor='center')

        button_shopping1 = tk.Button(self, text="Iniciar Compra", height=5, width=15, bg='#ffb3fe',
                                     command=lambda: controller.show_frame("Shopping_1"))
        button_shopping1.place(relx=0.5, rely=0.7, anchor='center')