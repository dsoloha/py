# Joe's Auto Shop
# Dan Soloha
# 10-20-2019

# pylint: disable=all

from tkinter import *

# Table of services containing their names and costs.
SERVICES = [('Oil Change', 30.00),
            ('Lube Job', 20.00),
            ('Radiator Flush', 40.00),
            ('Transmission Flush', 100.00),
            ("Inspection", 35.00),
            ("Muffler Replacement", 200.00),
            ("Tire Rotation", 20.00)]

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.main_window = root
        self.top_frame = Frame(self)
        self.bottom_frame = Frame(self)

        self.cb_vars = [IntVar() for _ in range(len(SERVICES))]

        self.cbs = [
            Checkbutton(
                self.top_frame,
                text="{}-${:.2f}".format(SERVICES[i][0], SERVICES[i][1]),
                variable=self.cb_vars[i])
            for i in range(len(self.cb_vars))
        ]

        for i in range(len(self.cbs)):
            self.cbs[i].pack()

        Button(self.bottom_frame,
        text="OK", command=self.show_choice
        ).pack(side="left")
        Button(self.bottom_frame,
        text="Quit", command=self.main_window.destroy
        ).pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

    def show_choice(self):
        popup_window = Toplevel()
        label_frame = LabelFrame(popup_window, text="Total Charges")
        label_frame.pack()
        total = sum(SERVICES[i][1] for i in range(len(self.cb_vars))
                    if self.cb_vars[i].get())
        Label(label_frame, text="${:.2f}".format(total)).pack()
        Button(popup_window,
        text="Okay", command=popup_window.destroy
        ).pack()
        root.wait_window(popup_window)

root = Tk()
app = Application(root)
app.master.title("Joe's Auto Shop")
app.mainloop()
