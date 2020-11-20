import tkinter as tk
from tkinter import Frame
from tkinter import Button
from tkinter import messagebox
import threading
from Cart import Cart
from Item import Item

LARGE_FONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)
STRONG_FONT = ("verdana 12 bold")

class EditCartPage(Frame):
    def __init__(self, parent, controller):
        print("edit")
        tk.Frame.__init__(self, parent)

        # Line 1
        self.labelTest = tk.Label(text="Selecione o produto que deseja editar", font=('Helvetica', 12), fg='red')
        self.labelTest.place(relx=0.5, rely=0.1, anchor='center')

        # Dropdown
        self.productList = controller.cart.product_list
        productNameList = []
        for product in self.productList:
            productNameList.append(product.getName())

        self.selectedProduct = tk.StringVar(self)
        self.selectedProduct.set(self.productList[0].getName())

        self.lastSelectedProduct = self.selectedProduct.get()

        self.productInfo = self.getProductByName(self.selectedProduct.get())
        self.labelProductInfo = tk.Label(text=self.productInfo, font=('Helvetica', 12), fg='black')
        self.labelProductInfo.place(relx=0.5, rely=0.3, anchor='center')

        self.opt = tk.OptionMenu(self, self.selectedProduct, *productNameList)
        self.opt.config(width=50, font=('Helvetica', 12))
        self.opt.place(relx=0.5, rely=0.5, anchor='center')

        # SelectButton
        self.selectButton = Button(self, text="Selecionar",
                                command=lambda: self.nextPage(controller))
        self.selectButton.place(relx=0.8, rely=0.5, anchor='center')

        # BackButton
        self.backButton = Button(self, text="Voltar",
                                command=lambda: self.cancel_update(controller), fg = 'red')
        self.backButton.place(relx=0.8, rely=0.55, anchor='center')

        # AddProduct
        self.addButton = Button(self, text="Adicionar Produto",
                                command=lambda: self.addProduct(controller))
        self.addButton.place(relx=0.5, rely=0.55, anchor='center')

        # threading
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.updateSelectedProductInfo, args=())
        self.thread.start()

    def getProductByName(self, name):
        for product in self.productList:
            if product.getName() == name:
                return product
        return None

    def updateSelectedProductInfo(self):
        try:
            while not self.stopEvent.is_set():
                if self.lastSelectedProduct != self.selectedProduct.get():
                    self.productInfo = self.getProductByName(self.selectedProduct.get())
                    self.labelProductInfo.destroy()
                    self.labelProductInfo = tk.Label(text=self.productInfo, font=('Helvetica', 12), fg='black')
                    self.labelProductInfo.place(relx=0.5, rely=0.3, anchor='center')
                    self.lastSelectedProduct = self.selectedProduct.get()
        except RuntimeError as e:
            print("[INFO] caught a RuntimeError")

    def cancel_update(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Você deseja sair desta página?")
        if cancel == True:
            self.onClose()
            self.labelProductInfo.destroy()
            self.opt.destroy()
            self.labelTest.destroy()
            controller.show_frame("HomeClient")

    def nextPage(self, controller):
        self.onClose()
        self.labelProductInfo.destroy()
        self.opt.destroy()
        self.labelTest.destroy()
        controller.update_product = self.getProductByName(self.lastSelectedProduct)
        controller.show_frame("EditCartPage2")

    def addProduct(self, controller):
        self.onClose()
        self.labelProductInfo.destroy()
        self.opt.destroy()
        self.labelTest.destroy()
        controller.show_frame("AddProduct")

    def onClose(self):
        print("[INFO] closing...")
        self.stopEvent.set()