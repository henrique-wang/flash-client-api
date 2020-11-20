import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import datetime
import imutils
from imutils.video import VideoStream
import threading
import cv2
import os
import json
import requests
import numpy as np
import Item
import Cart

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

class Shopping_1(tk.Frame):

    def __init__(self, parent, controller):
        PICAMERA = False
        self.vs = VideoStream(usePiCamera=PICAMERA).start()
        self.outputPath = r'pages\photos'
        self.frame = None
        self.thread = None
        self.stopEvent = None

        # initialize the root window and image panel
        self.root = parent
        self.panel = None

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Após posicionar a bandeja na região delimitada, selecione 'Avançar'",
                          font=MEDIUMFONT)
        label.place(relx=0.5, rely=0.1, anchor='center')

        # button to show next shopping page
        # layout2
        button_next = tk.Button(self, text="Avançar", bg='blue', fg='white',
                                command=lambda: self.onClose("Shopping_2", controller, cancel=False))
        button_next.place(relx=0.89, rely=0.8, anchor='se')

        # button to cancel
        # layout2
        button_cancel = tk.Button(self, text="Cancelar Compra",
                                  command=lambda: self.cancel_shop(controller), bg='red', fg='white')
        button_cancel.place(relx=0.9, rely=0.85, anchor='se')

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

    def cancel_shop(self, controller):
        cancel = messagebox.askokcancel(title=None, message="Você realmente deseja cancelar a compra?")
        if cancel == True:
            self.onClose("Shopping_cancel", controller, cancel=True)

    def videoLoop(self):
        # DISCLAIMER:
        # I'm not a GUI developer, nor do I even pretend to be. This
        # try/except statement is a pretty ugly hack to get around
        # a RunTime error that Tkinter throws due to threading
        try:
            # keep looping over frames until we are instructed to stop
            while not self.stopEvent.is_set():
                # grab the frame from the video stream and resize it to
                # have a maximum width of 300 pixels
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=500)

                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)

                # if the panel is not None, we need to initialize it
                if self.panel is None:
                    self.panel = tk.Label(image=image)
                    self.panel.image = image
                    self.panel.place(relx=0.5, rely=0.25, anchor='n')

                # otherwise, simply update the panel
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image
        except RuntimeError as e:
            print("[INFO] caught a RuntimeError")

    def onClose(self, next_page, controller, cancel):
        if (cancel == False):
            # Save image
            ts = datetime.datetime.now()
            #  filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
            filename = "{}.jpg".format("CartPhoto")
            p = os.path.sep.join((self.outputPath, filename))
            # p = self.outputPath + filename

            # save the file
            cv2.imwrite(p, self.frame.copy())
            print("[INFO] saved {} on {}".format(filename, p))

            # YOLO Recognition
            if (controller.MODE == "TEST"):
                print ("TEST MODE")
                image = cv2.imread("pages/photos/bananas.jpg")
            else:
                print("APPLICATIONMODE")
                image = cv2.imread("pages/photos/CartPhoto.jpg")

            frame = cv2.resize(image, None, fx=0.4, fy=0.4)
            frame = frame.tolist()
            data = json.dumps(frame)
            res = requests.post('http://localhost:5000/api/prediction', json=data)

            if res.ok:
                res = res.json()
                product_list = res["cart"]["productList"]
                cart = Cart.Cart()
                for item in product_list:
                    itemName = item["name"]
                    itemQty = item["quantity"]
                    itemPrice = item["itemPrice"]
                    item_cart = Item.Item(itemName, itemQty, itemPrice)
                    print(item_cart.__str__())
                    cart.addItem(item_cart)
                    print(cart.__str__())
                controller.cart = cart


                recog_result = res["data"]
                controller.recog_result = cv2.UMat(np.array(recog_result, dtype=np.uint8))
                recog_path = os.path.sep.join((self.outputPath, "RecogResult.jpg"))
                cv2.imwrite(recog_path, controller.recog_result)
                print("[INFO] saved {}".format("RecogResult.jpg"))



        print("[INFO] closing...")
        self.stopEvent.set()
        self.vs.stop()
        self.panel.destroy()
        controller.show_frame(next_page)

    # third window frame page2