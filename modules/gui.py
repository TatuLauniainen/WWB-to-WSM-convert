from tkinter import *
from tkinter import filedialog

import main


class GUI:
    def __init__(self):
        """
        Creates the graphical user interface for the program and initializes the necessary variables
        """
        self.__mainwindow = Tk()
        self.__mainwindow.geometry("480x240")
        self.__frame = Frame(self.__mainwindow, relief='sunken')
        self.__frame.grid(sticky="we")
        self.__frame.grid_rowconfigure(0, weight=1)
        self.__frame.grid_columnconfigure(0, weight=1)
        self.__mainwindow.grid_rowconfigure(0, weight=1)
        self.__mainwindow.grid_columnconfigure(0, weight=1)

        self.__mainwindow.title("WWB to WSM Converter")

        self.__WSM_path = ""
        self.__WWB_path = ""

        self.__open_WSM_button = Button(self.__frame, text="Select WSM template", command=self.open_WSM)
        self.__open_WWB_button = Button(self.__frame, text="Select WWB inventory", command=self.open_WWB)
        self.__convert_button = Button(self.__frame, text="Convert frequencies", command=self.convert,
                                       bg="#44e359", fg="black")

        self.__chosen_WSM = Label(self.__frame, text="No file selected")
        self.__chosen_WWB = Label(self.__frame, text="No file selected")

        self.__open_WSM_button.grid(row=1, column=0)
        self.__chosen_WSM.grid(row=2, column=0)
        self.__open_WWB_button.grid(row=3, column=0)
        self.__chosen_WWB.grid(row=4, column=0)
        self.__convert_button.grid(row=5, column=0)

        self.__mainwindow.mainloop()

    def open_WSM(self):
        """
        Creates an Open dialog and updates the self.__WSM_path variable with the selected filepath
        """
        self.__WSM_path = filedialog.askopenfilename(parent=self.__mainwindow, title="Select WSM file...",
                                                     initialfile="/Users/pvvmsktekniikka/Desktop/20220528_testi.wsm",
                                                     filetypes=[("WSM files", "*.wsm")])

        self.__chosen_WSM.configure(text=f"Selected file: {self.__WSM_path}")

    def open_WWB(self):
        """
        Creates an Open dialog and updates the self.__WWB_path with the selected filepath
        """
        self.__WWB_path = filedialog.askopenfilename(parent=self.__mainwindow, title="Select WWB file...",
                                                     initialdir="~/Documents/Shure/Inventory/",
                                                     filetypes=[(".inv files", "*.inv")])

        self.__chosen_WWB.configure(text=f"Selected file: {self.__WWB_path}")

    def convert(self):
        main.main(self.__WWB_path, self.__WSM_path)
