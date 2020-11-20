import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

class Shopping_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # First Line
        label_1 = ttk.Label(self, text="Carrinho",
                            font=MEDIUMFONT)
        label_1.place(relx=0.5, rely=0.05, anchor='center')

        # Second Line
        cart_text = self.cart_text(controller)
        label_2 = ttk.Label(self, text=cart_text,
                            font=MEDIUMFONT)
        label_2.place(relx=0.5, rely=0.5, anchor='center')

        # button to show next payment page
        button_next = tk.Button(self, text="Finalizar Pagamento", bg='blue', fg='white',
                                command=lambda: controller.show_frame("Shopping_4"))
        button_next.place(relx=0.5, rely=0.8, anchor='s')

        # button to cancel
        button_cancel = tk.Button(self, text="Cancelar Compra",
                                  command=lambda: self.cancel_shop(controller), bg='red', fg='white')
        button_cancel.place(relx=0.9, rely=0.8, anchor='se')

        # Button to edit cart
        button_edit = tk.Button(self, text="Edit Cart",
                                  command=lambda: controller.show_frame("EditCartPage"))
        button_edit.place(relx=0.9, rely=0.84, anchor='se')

    def cancel_shop(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Você realmente deseja cancelar a compra?")
        if cancel == True:
            controller.show_frame("Shopping_cancel")

    def cart_text(self, controller):
        text = controller.cart.__str__()
        return text