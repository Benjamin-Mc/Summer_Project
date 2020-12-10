#Testing the output generation into a pdf

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from tkinter import *
from tkinter import filedialog

def output_data():
    with PdfPages(r'C:\Users\benja\Documents\Test Analysis.pdf') as export_pdf:
        a = np.array(range(5))
        b = [21, 22, 23, 24, 25]

        plt.subplot(2, 2, 1)
        plt.plot(a, b)
        plt.title("Test Data - 1")
        plt.xlabel('x')
        plt.ylabel('y')

        a -= 10
        plt.subplot(2, 2, 2)
        plt.plot(b, a)
        plt.title("Test Data - 2")
        plt.xlabel('x')
        plt.ylabel('y')

        export_pdf.savefig()
        plt.close()

def browse(n):
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\benja\\Documents\\", filetypes=(("text files", "*.txt"),))
    if n==1:
        sample_file.set(filename)
    else:
        background_file.set(filename)

def close_program():
    root.destroy()

if __name__ == '__main__':

    root = Tk()
    root.title("Linear Flow Fluorescence Analysis")
    root.geometry("650x200")
    root.grid_columnconfigure(0, weight=1)

    sample_file = StringVar()
    background_file = StringVar()

    frame1 = Frame(root)
    frame1.grid(row=0, column=0)

    title = Label(frame1, text="Linear Flow Fluorescence Analysis", font=(None, 13))
    title.grid(row=0, column=1, padx=10, pady=10)

    frame2 = Frame(root, relief=RAISED, borderwidth=1)
    frame2.grid(row=1, column=0, padx=8, pady=6, sticky=W+E)

    fnlbl = Label(frame2, text="Select Sample Measurement", font=(None, 11))
    fnlbl.grid(row=1, column=1, padx=28, pady=6, sticky=W)

    xnlbl = Label(frame2, text="Select Background Measurement", font=(None, 11))
    xnlbl.grid(row=3, column=1, padx=28, pady=6, sticky=W)

    input_box1 = Entry(frame2, textvariable=sample_file, width=40)
    input_box1.grid(row=1, column=2, padx=12)

    input_box2 = Entry(frame2, textvariable=background_file, width=40)
    input_box2.grid(row=3, column=2, padx=12)

    but1 = Button(frame2, text="Browse", command=lambda: browse(1))
    but1.grid(row=1, column=3)
    but2 = Button(frame2, text="Browse", command=lambda: browse(2))
    but2.grid(row=3, column=3)

    frame3 = Frame(root)
    frame3.grid(row=5, column=0)

    but3 = Button(frame3, text="Start", command=output_data)
    but3.grid(row=5, column=0, padx=10, pady=10)

    but4 = Button(frame3, text="Close", command=close_program)
    but4.grid(row=5, column=1)

    root.mainloop()
