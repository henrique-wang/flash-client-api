import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import cv2

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

class Shopping_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Recognition Result
        photo = cv2.imread(r"pages\photos\RecogResult.jpg")
        photo = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(photo)
        [imageSizeWidth, imageSizeHeight] = image.size
        image = image.resize((imageSizeWidth*2, imageSizeHeight*2))
        image = ImageTk.PhotoImage(image)
        self.panel = tk.Label(image=image)
        self.panel.image = image
        self.panel.place(relx=0.5, rely=0.25, anchor='n')

        # First Line
        label_1 = ttk.Label(self, text="Por favor, verifique os itens presentes em seu carrinho.",
                            font=MEDIUMFONT)
        label_1.place(relx=0.5, rely=0.05, anchor='center')

        # Second Line
        label_2 = ttk.Label(self, text="Caso tenha algum erro, selecione 'Tirar foto novamente'.",
                            font=MEDIUMFONT)
        label_2.place(relx=0.5, rely=0.1, anchor='center')

        # Third Line
        label_3 = ttk.Label(self, text="Caso contrário, clique em 'confirmar'.",
                            font=MEDIUMFONT)
        label_3.place(relx=0.5, rely=0.15, anchor='center')

        # button to show next payment page
        button_next = tk.Button(self, text="Avançar", bg='blue', fg='white',
                                command=lambda: self.next_page("Shopping_3", controller))
        button_next.place(relx=0.89, rely=0.8, anchor='se')

        # button to cancel
        button_cancel = tk.Button(self, text="Cancelar Compra",
                                  command=lambda: self.cancel_shop(controller), bg='red', fg='white')
        button_cancel.place(relx=0.9, rely=0.85, anchor='se')

        # button to return to photo page
        button_next = tk.Button(self, text="Tirar foto novamente", bg='green', fg='white',
                                command=lambda: self.return_videopage(controller))
        button_next.place(relx=0.91, rely=0.9, anchor='se')

    def cancel_shop(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Você realmente deseja cancelar a compra?")
        if cancel == True:
            self.panel.destroy()
            controller.show_frame("Shopping_cancel")

    def next_page(self, nextPage, controller):
        self.panel.destroy()
        controller.show_frame(nextPage)

    def return_videopage(self, controller):
        controller.cart = None
        self.next_page("Shopping_1", controller)