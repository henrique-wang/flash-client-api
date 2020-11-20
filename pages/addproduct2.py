import tkinter as tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from Item import Item

LARGE_FONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)
STRONG_FONT = ("verdana 12 bold")
LARGE_FONT = ("Verdana", 12)
BRANCO = "#fff"

class AddProduct2(Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent, bg=BRANCO)

        self.label = Label(self, text="Selecione a quantidade deste produto", font=LARGE_FONT, bg=BRANCO, relief="groove")
        self.namel = Label(self, text="Nome do Produto:", font="Verdana 10", bg=BRANCO, relief="groove")
        self.quantityl = Label(self, text="Quantidade do Produto:", font="Verdana 10", bg=BRANCO, relief="groove")

        self.name = Label(self, text=controller.update_product.getName(), font=LARGE_FONT, bg=BRANCO, relief="groove")
        self.quantity = Entry(self)
        self.quantity.insert(0, 0)

        self.label.place(relx=0.5, rely=0.2, anchor='center')
        self.namel.place(relx=0.4, rely=0.3, anchor='center')
        self.quantityl.place(relx=0.4, rely=0.35, anchor='center')
        import tkinter as tk

        self.name.place(relx=0.5, rely=0.3, anchor='center')
        self.quantity.place(relx=0.55, rely=0.35, anchor='center')

        self.grid_columnconfigure(3, weight=1)

        self.backButton = Button(self, text="Voltar",
                                 command=lambda: self.cancel_update(controller))
        self.backButton.place(relx=0.4, rely=0.4, anchor='center')

        self.nextButton = Button(self, text="Confirmar",
                                 command=lambda: self.editInfo(controller))
        self.nextButton.place(relx=0.6, rely=0.4, anchor='center')

    def editInfo(self, controller):
        new_product_info = Item(controller.update_product.getName(), self.quantity.get(), controller.update_product.getPrice())
        controller.cart.addItem(new_product_info)
        self.nextPage(controller)

    def cancel_update(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Você deseja sair desta página?")
        if cancel == True:
            self.onClose()
            self.labelProductInfo.destroy()
            self.opt.destroy()
            self.labelTest.destroy()
            controller.update_product = None
            controller.show_frame("EditCartPage")

    def nextPage(self, controller):
        controller.update_product = None
        controller.show_frame("Shopping_3")
