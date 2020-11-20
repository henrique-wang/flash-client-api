import tkinter as tk
from pages.homepage import HomeClient
from pages.videopage import Shopping_1
from pages.recogpage import Shopping_2
from pages.cartpage import Shopping_3
from pages.thankspage import Shopping_4
from pages.cancelpage import Shopping_cancel
from pages.editcartpage import EditCartPage
from pages.editcart2page import EditCartPage2
from pages.addproductpage import AddProduct
from pages.addproduct2 import AddProduct2

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

recog_result = None

# Select which application mode do you want to use
# TEST mode -> recognizes objects from bananas.jpg
# APPLICATION mode -> recognizes objects from picture taken from webcam
MODE = "TEST"
#MODE = "APPLICATION"

class FlashMallClient(tk.Tk):

    # __init__ function for class FlashMallClient
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Cart Variables
        self.cart = None
        self.recog_result = None

        # Selected product for update
        self.update_product = None

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.curr_page = HomeClient(self.container, self)

        # to display the current frame passed as
        self.show_frame("HomeClient")

        # MODE
        self.MODE = MODE

    # parameter
    def show_frame(self, page):
        print("page", page )
        self.curr_page.destroy()
        if (page == "HomeClient"):
            self.curr_page = HomeClient(self.container, self)
        elif (page == "Shopping_1"):
            self.curr_page = Shopping_1(self.container, self)
        elif (page == "Shopping_2"):
            self.curr_page = Shopping_2(self.container, self)
        elif (page == "Shopping_3"):
            self.curr_page = Shopping_3(self.container, self)
        elif (page == "Shopping_4"):
            self.curr_page = Shopping_4(self.container, self)
        elif (page == "Shopping_cancel"):
            self.curr_page = Shopping_cancel(self.container, self)
        elif (page == "EditCartPage"):
            self.curr_page = EditCartPage(self.container, self)
        elif (page == "EditCartPage2"):
            self.curr_page = EditCartPage2(self.container, self)
        elif (page == "AddProduct"):
            self.curr_page = AddProduct(self.container, self)
        elif (page == "AddProduct2"):
            self.curr_page = AddProduct2(self.container, self)

        self.curr_page.grid(row=0, column=0, sticky="nsew")

def main():
    app = FlashMallClient()
    app.mainloop()
main()