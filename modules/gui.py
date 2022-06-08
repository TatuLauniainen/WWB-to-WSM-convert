from tkinter import *
from tkinter import filedialog


class GUI:
    def __init__(self):
        """
        Creates the graphical user interface for the program and initializes the necessary variables
        """
        self.__mainwindow = Tk()
        self.__mainwindow.title("WWB to WSM Converter")

        self.__open_WSM_button = Button(self.__mainwindow, text="Select WSM template", command=self.open_WSM)
        self.__open_WWB_button = Button(self.__mainwindow, text="Select WWB inventory", command=self.open_WWB)
        self.__convert_button = Button(self.__mainwindow, text="Convert frequencies", command=self.convert)

        self.__open_WSM_button.pack()
        self.__open_WWB_button.pack()
        self.__convert_button.pack()

        self.__mainwindow.mainloop()

    def open_WSM(self):
        """
        Creates an Open dialog and returns the selected filename
        :return: str, selected filename
        """
        filedialog.askopenfilename(parent=self.__mainwindow, title="Select WSM file...",
                                   initialdir="~/Documents/WSM/Configuration",
                                   filetypes=[("WSM files", "*.wsm")])

        # TODO: Update the open_WSM_button label with the chosen filename

    def open_WWB(self):
        """
        Creates an Open dialog and returns the selected filename
        :return: str, selected filename
        """
        filedialog.askopenfilename(parent=self.__mainwindow, title="Select WWB file...",
                                   initialdir="~/Documents/Shure/Inventory",
                                   filetypes=[(".inv files", "*.inv")])

        # TODO: Update the open_WWB_button label with the chosen filename

    def convert(self):
        pass


GUI()