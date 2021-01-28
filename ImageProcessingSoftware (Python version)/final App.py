
import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
from tkinter import messagebox as mBox
from PIL import Image, ImageTk
import cv2
from pylab import *
from matplotlib import path
import matplotlib.cm as cm
from matplotlib.widgets import Slider
from tkinter import filedialog
import numpy as np
from matplotlib.image import imread
from scipy import ndimage as ndi

from skimage.morphology import watershed
from skimage.feature import peak_local_max

from skimage.transform import (hough_line, hough_line_peaks,
                               probabilistic_hough_line)
from skimage.feature import canny
from skimage import data

import matplotlib.pyplot as plt
from matplotlib import cm

import tkinter.scrolledtext as tkst
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.path import Path
from matplotlib.widgets import LassoSelector
from collections import deque
import matplotlib.image as mpimg

### Functions
def OPEN():
    global Original_Image
    global Dimension_Number
    global Original_image_Size
    root1.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("jpeg files", "*.jpg"),("png files", "*.png"),("tif files", "*.TIF"), ("all files", "*.*")))
    Original_Image = Image.open(root1.filename)
    Original_Image=np.array(Original_Image)
    Original_image_Size = np.shape(Original_Image)
    print(len(Original_image_Size))


    a1 = np.shape(Original_Image)
    a1 = str(a1)
    tk.Label(root1, text='Dimensions: ').place(x=0,y=0)
    v_dim = tk.StringVar(root1, value=a1)
    e = tk.Entry(root1, textvariable=v_dim)
    e.place(x=70, y=0)



    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    def RGB_Show():
        root2 = tk.Toplevel()
        root2.geometry('600x600')

        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        image = Original_Image
        image = Image.fromarray(image)
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(root2, image=photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill=tk.BOTH, expand='YES')

        root2.mainloop()

    def ShowChoice():
        a = int(v1.get())
        root2 = tk.Toplevel()
        root2.geometry('600x600')

        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        image = Original_Image[:, :, a]
        image = Image.fromarray(image)
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(root2, image=photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill=tk.BOTH, expand='YES')

        root2.mainloop()

    def ShowChoiceOneBand():
        root2 = tk.Toplevel()
        root2.geometry('600x600')

        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo  # avoid garbage collection

        image = Original_Image
        image = Image.fromarray(image)
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(root2, image=photo)
        label.bind('<Configure>', resize_image)
        label.pack(fill=tk.BOTH, expand='YES')

    tk.Label(root1, text="""Choose your favourite view:""", justify=tk.LEFT, padx=20).place(x=0,y=20)

    if len(Original_image_Size) > 2:
        v1 = tk.StringVar()
        v1.set("L")  # initialize
        z=20
        for val, Dimension_Number in enumerate(Dimension_Number):
            z=z+20
            b = tk.Radiobutton(root1, text=Dimension_Number, padx=20, variable=v1, value=val, command=ShowChoice)
            b.place(x=0,y=z)
        if Original_image_Size[2] == 3:
            RGB_btn = tk.Button(root1, bg='#000000', fg='#b7f731', text='   RGB   ', padx=20, bd='5', command=RGB_Show)
            RGB_btn.place(x=0,y=20+z)
    else:
        z=20
        b = tk.Radiobutton(root1, text="Band 1", padx=20, value=1, command=ShowChoiceOneBand)
        b.place(x=0,y=z+20)

    def Staticks():
        root3 = tk.Tk()
        if len(Original_image_Size) > 2:
            a_staticks = int(v1.get())
            img_staticks = Original_Image[:, :, a_staticks]

            Min = np.min(img_staticks)
            Min = str(Min)
            tk.Label(root3, text='Minimum: ').grid(row=0, column=0)
            v_min = tk.StringVar(root3, value=Min)
            e_min = tk.Entry(root3, textvariable=v_min)
            e_min.grid(row=0, column=1)

            Max = np.max(img_staticks)
            Max = str(Max)
            tk.Label(root3, text='Maximum: ').grid(row=1, column=0)
            v_Max = tk.StringVar(root3, value=Max)
            e_Max = tk.Entry(root3, textvariable=v_Max)
            e_Max.grid(row=1, column=1)

            Mean = np.mean(img_staticks)
            Mean = str(Mean)
            tk.Label(root3, text='Maximum: ').grid(row=2, column=0)
            v_Mean = tk.StringVar(root3, value=Mean)
            e_Mean = tk.Entry(root3, textvariable=v_Mean)
            e_Mean.grid(row=2, column=1)

            STD = np.std(img_staticks)
            STD = str(STD)
            tk.Label(root3, text='Standard Diversion: ').grid(row=3, column=0)
            v_STD = tk.StringVar(root3, value=STD)
            e_STD = tk.Entry(root3, textvariable=v_STD)
            e_STD.grid(row=3, column=1)

            SUM = np.sum(img_staticks)
            SUM = str(SUM)
            tk.Label(root3, text='Total: ').grid(row=4, column=0)
            v_SUM = tk.StringVar(root3, value=SUM)
            e_SUM = tk.Entry(root3, textvariable=v_SUM)
            e_SUM.grid(row=4, column=1)
        else:
            img_staticks = Original_Image

            Min = np.min(img_staticks)
            Min = str(Min)
            tk.Label(root3, text='Minimum: ').grid(row=0, column=0)
            v_min = tk.StringVar(root3, value=Min)
            e_min = tk.Entry(root3, textvariable=v_min)
            e_min.grid(row=0, column=1)

            Max = np.max(img_staticks)
            Max = str(Max)
            tk.Label(root3, text='Maximum: ').grid(row=1, column=0)
            v_Max = tk.StringVar(root3, value=Max)
            e_Max = tk.Entry(root3, textvariable=v_Max)
            e_Max.grid(row=1, column=1)

            Mean = np.mean(img_staticks)
            Mean = str(Mean)
            tk.Label(root3, text='Maximum: ').grid(row=2, column=0)
            v_Mean = tk.StringVar(root3, value=Mean)
            e_Mean = tk.Entry(root3, textvariable=v_Mean)
            e_Mean.grid(row=2, column=1)

            STD = np.std(img_staticks)
            STD = str(STD)
            tk.Label(root3, text='Standard Diversion: ').grid(row=3, column=0)
            v_STD = tk.StringVar(root3, value=STD)
            e_STD = tk.Entry(root3, textvariable=v_STD)
            e_STD.grid(row=3, column=1)

            SUM = np.sum(img_staticks)
            SUM = str(SUM)
            tk.Label(root3, text='Total: ').grid(row=4, column=0)
            v_SUM = tk.StringVar(root3, value=SUM)
            e_SUM = tk.Entry(root3, textvariable=v_SUM)
            e_SUM.grid(row=4, column=1)

        root3.mainloop()

    Quick_Staticks_btn = tk.Button(root1, bg='#000000', fg='#b7f731', text='Staticks', padx=20, bd='5',
                                   command=Staticks)
    Quick_Staticks_btn.place(x=0,y=z+50)


def Show_Histogram1():
    root4 = tk.Toplevel()
    root4.geometry("1800x900")
    root4.configure(background='white')
    root4.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root4,
        bg='#808000'
    )
    frame1.place(x=0, y=200)
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
"""\
At this menu You can see the Image Histogram
in two different method(Bar and Plot).
you can see:
- Histogram Of special band
- all bands histogram( if image has more than a band)
- commulative Histogram of each bands.
for using this option on the application at first you should
select your special band from the "list top of the page" and then 
press button of your own option.

""")

    def Show_Histogram2():
        if len(Original_image_Size) > 2:
            a_Histogram = int(numberChosen1.get())
            img = Original_Image[:, :, a_Histogram - 1]
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])

            fig = plt.Figure(figsize=(13, 7),facecolor='w')

            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720,y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax1.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax1.set_facecolor("#2E2E2E")
            ax2.set_facecolor("#2E2E2E")

            fig.subplots_adjust(bottom=0.25)
            ax1.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_Histogram))
            ax2.plot(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_Histogram))

            ax1.set_title("Band"+str(a_Histogram)+" Histogram", fontsize=12, color="#333533")
            ax2.set_title("Band" + str(a_Histogram) + " Histogram", fontsize=12, color="#333533")

            ax1.legend(loc='best')
            ax2.legend(loc='best')


            fig.canvas.draw_idle()




        else:
            img = Original_Image
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])

            fig = plt.Figure(figsize=(13, 7), facecolor='w')

            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax1.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax1.set_facecolor("#2E2E2E")
            ax2.set_facecolor("#2E2E2E")

            fig.subplots_adjust(bottom=0.25)
            ax1.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1))
            ax2.plot(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1))

            ax1.set_title("Band" + str(1) + " Histogram", fontsize=12, color="#333533")
            ax2.set_title("Band" + str(1) + " Histogram", fontsize=12, color="#333533")

            ax1.legend(loc='best')
            ax2.legend(loc='best')

            fig.canvas.draw_idle()


    def ALL_BANDS():

        color = ('b', 'g', 'r')
        fig = plt.Figure(figsize=(13, 7))
        canvas = FigureCanvasTkAgg(fig, root4)
        canvas.get_tk_widget().place(x=200, y=0)

        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        ax1.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
        ax1.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
        ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
        ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

        ax1.set_facecolor("#2E2E2E")
        ax2.set_facecolor("#2E2E2E")

        toolbarFrame = tk.Frame(master=root4)
        toolbarFrame.place(x=720, y=600)

        ax1.set_title("Histogram")
        ax2.set_title("Histogram")

        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        toolbar.update()

        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)

        canvas.mpl_connect("key_press_event", on_key_press)

        fig.subplots_adjust(bottom=0.25)
        k=0
        for i, col in enumerate(color):
            k=1+k
            hist_RGB = cv2.calcHist([Original_Image], [i], None, [256], [0, 256])
            ax1.bar(range(256), hist_RGB.ravel(), color=col,label="Band"+str(k))
            ax2.plot(range(256), hist_RGB.ravel(), color=col,label="Band"+str(k))

            ax1.legend(loc='best')
            ax2.legend(loc='best')

            fig.canvas.draw_idle()

    def CumulativeHistogram():
        if len(Original_image_Size) > 2:
            a_CumulativeHistogr = int(numberChosen1.get())
            img = Original_Image[:, :, a_CumulativeHistogr - 1]
            CumulativeHist = cv2.calcHist([img], [0], None, [256], [0, 256])
            CDF = CumulativeHist.cumsum()

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax1.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax1.set_facecolor("#2E2E2E")
            ax2.set_facecolor("#2E2E2E")

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.bar(range(256), CDF.ravel(),color="gold",label="Band"+str(a_CumulativeHistogr)+"Commulative Histogram")
            ax1.bar(range(256), CumulativeHist.ravel(),color="magenta",label="Band"+str(a_CumulativeHistogr))
            ax2.plot(range(256), CDF.ravel(),color="gold",label="Band"+str(a_CumulativeHistogr)+"Commulative Histogram")
            ax2.plot(range(256), CumulativeHist.ravel(),color="magenta",label="Band"+str(a_CumulativeHistogr))

            ax1.legend(loc='best')
            ax2.legend(loc='best')

            ax1.set_title("Band" + str(a_CumulativeHistogr) + "Comulative Histogram", fontsize=12, color="#333533")
            ax2.set_title("Band" + str(a_CumulativeHistogr) + "Comulative Histogram", fontsize=12, color="#333533")

            fig.canvas.draw_idle()

        else:
            img = Original_Image
            CumulativeHist = cv2.calcHist([img], [0], None, [256], [0, 256])
            CDF = CumulativeHist.cumsum()

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax1.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax1.set_facecolor("#2E2E2E")
            ax2.set_facecolor("#2E2E2E")

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.bar(range(256), CDF.ravel(), color="gold", label="Band" + str(1))
            ax1.bar(range(256), CumulativeHist.ravel(), color="magenta", label="Band" + str(1))
            ax2.plot(range(256), CDF.ravel(), color="gold", label="Band" + str(1))
            ax2.plot(range(256), CumulativeHist.ravel(), color="magenta", label="Band" + str(1))

            ax1.legend(loc='best')
            ax2.legend(loc='best')

            ax1.set_title("Band" + str(1) + "Comulative Histogram", fontsize=12, color="#333533")
            ax2.set_title("Band" + str(1) + "Comulative Histogram", fontsize=12, color="#333533")

            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:

        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root4, text="Choose a band:").place(x=0,y=0)
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root4, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.place(x=0, y=30)
        numberChosen1.current(0)
        if Original_image_Size[2] == 3:
            RGB_btn = tk.Button(root4, bg='#000000', fg='#b7f731', text='   show hist   ', padx=20, bd='5',
                                command=Show_Histogram2)
            RGB_btn.place(x=0, y=60)
            RGB_btn1 = tk.Button(root4, bg='#000000', fg='#b7f731', text='   All Bands   ', padx=20, bd='5',
                                 command=ALL_BANDS)
            RGB_btn1.place(x=0, y=90)
            Cumsum_btn = tk.Button(root4, bg='#000000', fg='#b7f731', text='Cumulative histogram', padx=20, bd='5',
                                   command=CumulativeHistogram)
            Cumsum_btn.place(x=0, y=120)

        def Quit():
           root4.quit()
           root4.destroy()



        button = tk.Button(master=root4, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                            bd='5', command=Quit)
        button.place(x=0, y=150)


    else:
        tk.Label(root4, text="Choose a band:").place(x=0,y=0)
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root4, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.place(x=0, y=30)
        numberChosen1.current(0)
        btn1 = tk.Button(root4, bg='#000000', fg='#b7f731', text='   show hist   ', padx=20, bd='5',
                         command=Show_Histogram2)
        btn1.place(x=0, y=60)
        Cumsum_btn = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Cumulative histogram   ', padx=20,
                               bd='5', command=CumulativeHistogram)
        Cumsum_btn.place(x=0, y=90)


        def Quit():
           root4.quit()
           root4.destroy()



        button = tk.Button(master=root4, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                            bd='5', command=Quit)
        button.place(x=0, y=120)

    root4.mainloop()



def Equalization():
    root4 = tk.Toplevel()
    root4.geometry("1800x900")
    root4.configure(background='white')
    root4.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root4,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
"""\
At this menu You can equalize the Image Histogram
for using this option on the application at first you should
select your special band from the "list top of the page" and then 
press "Equalize" button.
if you want save output image use the "Save Equalized Image" botton.

""")

    def EqualizationOneBand():
        if len(Original_image_Size) > 2:
            a_Histogram = int(numberChosen1.get())
            img = Original_Image[:, :, a_Histogram - 1]
            img2 = cv2.equalizeHist(img)

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)
            fig.subplots_adjust(bottom=0.25)

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)



            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')
            ax1.grid(False)
            ax2.grid(False)

            a_Histogram = int(numberChosen1.get())
            img = Original_Image[:, :, a_Histogram - 1]
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(1)+"Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Band" + str(1)+"Equalized Histogram")

            ax3.legend(loc='best')


            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")
            ax2.set_title(" Equalized Image", fontsize=12, color="#333533")


            fig.canvas.draw_idle()

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', img2)
                f.close()

            btnw = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Save Equalized Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)


        else:
            img = Original_Image
            img2 = cv2.equalizeHist(img)

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)
            fig.subplots_adjust(bottom=0.25)

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')
            ax1.grid(False)
            ax2.grid(False)


            img = Original_Image
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(1) + "Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Band" + str(1) + "Equalized Histogram")

            ax3.legend(loc='best')

            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")
            ax2.set_title(" Equalized Image", fontsize=12, color="#333533")


            fig.canvas.draw_idle()

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))


                if f is None:
                    return

                filename = f.name



                cv2.imwrite(str(filename)+'.jpg',img2)
                f.close()
            btnw = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Save Equalized Image   ', padx=20, bd='5',
                            command=SaveI)
            btnw.place(x=1000, y=0)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root4, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root4, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Equalize   ', padx=20, bd='5',
                        command=EqualizationOneBand)
        btn.pack(anchor='w')

    else:
        tk.Label(root4, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root4, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Equalize   ', padx=20, bd='5',
                         command=EqualizationOneBand)
        btn1.pack(anchor='w')

    def Quit():
        root4.quit()
        root4.destroy()

    button = tk.Button(master=root4, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root4.mainloop()


def Binning():
    root5 = tk.Tk()
    tk.Label(root5, text='Enter number of distinct values in image: ').grid(row=0, column=0)
    entry1 = tk.Entry(root5, width=10)
    entry1.grid(row=0, column=1)
    tk.Label(root5, text='Enter number of bins: ').grid(row=1, column=0)
    entry2 = tk.Entry(root5, width=10)
    entry2.grid(row=1, column=1)
    root5.configure(background='white')
    root5.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
    def CalBin():
        e1 = entry1.get()
        e1 = int(e1)
        e2 = entry2.get()
        e2 = int(e2)
        Bin_size = int(e1 / e2)
        tk.Label(root5, text='Your image bin size is: ').grid(row=3, column=0)
        v = tk.StringVar(root5, value=Bin_size)
        e = tk.Entry(root5, textvariable=v)
        e.grid(row=3, column=1)

    btn_bin = tk.Button(root5, bg='#000000', fg='#b7f731', text='   Calculate Bin Size   ', padx=20, bd='5',
                        command=CalBin)
    btn_bin.grid(row=2, column=0)


    root5.mainloop()


def clahe():
    root7 = tk.Toplevel()
    root7.configure(background='white')
    root7.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
    root7.geometry("1800x900")

    frame1 = tk.Frame(
        master=root7,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
"""\
At this menu You can improve contrast of the Image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Clahe" button. if you want save output image use the "Save CLAHE Image" botton. CLAHE means Contras Limited Adaptive Histogram Adjustment.

""")

    def clahe1():
        if len(Original_image_Size) > 2:
            a_clahe = int(numberChosen1.get())
            img = Original_Image[:, :, a_clahe - 1]
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16, 16))
            img2 = clahe.apply(img)

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root7)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)
            fig.subplots_adjust(bottom=0.25)

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            toolbarFrame = tk.Frame(master=root7)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')

            a_clahe = int(numberChosen1.get())
            img = Original_Image[:, :, a_clahe - 1]
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(a_clahe) + " Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Band" + str(a_clahe) + " Contrast Limited Adaptive Histogram Adjustment")

            ax3.legend(loc='best')

            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")
            ax2.set_title("Contrast Limited Adaptive Histogram Adjustment", fontsize=12, color="#333533")

            fig.canvas.draw_idle()


            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))


                if f is None:
                    return

                filename = f.name



                cv2.imwrite(str(filename)+'.jpg',img2)
                f.close()
            btnw = tk.Button(root7, bg='#000000', fg='#b7f731', text='   Save CLAHE Image   ', padx=20, bd='5',
                            command=SaveI)
            btnw.place(x=1000, y=0)

        else:
            img = Original_Image
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16, 16))
            img2 = clahe.apply(img)
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root7)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)
            fig.subplots_adjust(bottom=0.25)

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            toolbarFrame = tk.Frame(master=root7)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')


            img = Original_Image
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(1) + " Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold",
                     label="Band" + str(1) + " Contrast Limited Adaptive Histogram Adjustment")

            ax3.legend(loc='best')

            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")
            ax2.set_title("Contrast Limited Adaptive Histogram Adjustment", fontsize=12, color="#333533")

            fig.canvas.draw_idle()

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', img2)
                f.close()

            btnw = tk.Button(root7, bg='#000000', fg='#b7f731', text='   Save CLAHE Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1100, y=0)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root7, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root7, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root7, bg='#000000', fg='#b7f731', text='   CLAHE   ', padx=20, bd='5', command=clahe1)
        btn.pack(anchor='w')

    else:
        tk.Label(root7, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root7, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root7, bg='#000000', fg='#b7f731', text='   CLAHE   ', padx=20, bd='5', command=clahe1)
        btn1.pack(anchor='w')


    def Quit():
        root7.quit()
        root7.destroy()

    button = tk.Button(master=root7, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root7.mainloop()


def Brightness():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
At this menu You can Increase Image Brightness. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button to choose your own band then you can use Slider to increase brightness or use entry box and enter a number to set as brightness (slider and entry box do same work). if you want save output image use the "Save Processed Image" botton.
                
                    """)


    def Brightness1():

        if len(Original_image_Size) > 2:
            a_Brightness = int(numberChosen1.get())
            img = Original_Image[:, :, a_Brightness - 1]
            img = np.array(img)
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title(" HiBrightness", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time = Slider(ax1_value, 'Brightness:', 0, 255, valinit=0,color='red')

            def DrawPlot():
                E11 = float(E1.get())
                q = E11 + img

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if q[i, j] > 255:
                            q[i, j] = 255

                ax1.imshow(q, cmap='gray')
                ax1.set_title(" Processed Image", fontsize=12, color="#333533")
                y = E11 + x
                p = str(E11)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Processed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=500, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Brightness:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=260, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=650)
            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn1.place(x=460, y=650)

            def update(val):

                pos = float(s_time.val)
                q = pos + img

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if q[i, j] > 255:
                            q[i, j] = 255
                ax1.imshow(q, cmap='gray')
                ax1.set_title(" Processed Image", fontsize=12, color="#333533")
                y = pos + x
                p = str(pos)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Processed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=500, y=0)

                fig.canvas.draw_idle()

            x = np.arange(0, 256, 1)
            y = x
            ax2.plot(x, y)
            ax2.plot(x, y, label="c={0}".format(s_time.val))
            ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))
            s_time.on_changed(update)
        else:
            img = Original_Image
            img = np.array(img)
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title(" Brightness", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time = Slider(ax1_value, 'Brightness:', 0, 255, valinit=0, color='red')

            def DrawPlot():
                E11 = float(E1.get())
                q = E11 + img

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if q[i, j] > 255:
                            q[i, j] = 255

                ax1.imshow(q, cmap='gray')
                ax1.set_title(" Processed Image", fontsize=12, color="#333533")
                y = E11 + x
                p = str(E11)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Processed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=500, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Brightness:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=260, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=650)
            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn1.place(x=460, y=650)

            def update(val):

                pos = float(s_time.val)
                q = pos + img

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if q[i, j] > 255:
                            q[i, j] = 255
                ax1.imshow(q, cmap='gray')
                ax1.set_title(" Processed Image", fontsize=12, color="#333533")
                y = pos + x
                p = str(pos)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Processed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=500, y=0)

                fig.canvas.draw_idle()

            x = np.arange(0, 256, 1)
            y = x
            ax2.plot(x, y)
            ax2.plot(x, y, label="c={0}".format(s_time.val))
            ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))
            s_time.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Brightness1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Brightness1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()




def Clamping():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
we usually use this menu when we are processed an image and it got the unusual value if you use image without any process on it application return itself and not diffrent between output and input.Increase Image Brightness. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Clamping" button to process. if you want save output image use the "Save Processed Image" botton.

                    """)

    def Clamping1():

        if len(Original_image_Size) > 2:
            a_Clamping = int(numberChosen1.get())
            img = Original_Image[:, :, a_Clamping - 1]
            img = np.array(img)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if img[i, j] > 255:
                        img[i, j] = 255
                    elif img[i, j] < 0:
                        img[i, j] = 0
                    else:
                        pass
            img2 = img
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)

            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax3.cla()

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            ax2.set_title(" Processed Image", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', img2)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Processed Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)



            img = Original_Image[:, :, a_Clamping - 1]
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(a_Clamping) + " Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Clampped Image" + " Histogram")
            ax3.legend(loc='best')

            fig.canvas.draw_idle()
        else:
            img = Original_Image
            img = np.array(img)
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if img[i, j] > 255:
                        img[i, j] = 255
                    elif img[i, j] < 0:
                        img[i, j] = 0
                    else:
                        pass
            img2=img
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)

            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax3.cla()

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            ax2.set_title(" Processed Image", fontsize=12, color="#333533")
            ax1.set_title(" Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', img2)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Processed Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)

            img = Original_Image
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(1) + " Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Clampped Image" + " Histogram")
            ax3.legend(loc='best')

            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Clamping   ', padx=20, bd='5',
                        command=Clamping1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Clamping   ', padx=20, bd='5',
                         command=Clamping1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()



def Inverting():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu returns Invert image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Inverting" button to process. if you want save output image use the "Save Invert Image" botton.

                    """)

    def Inverting1():

        if len(Original_image_Size) > 2:
            a_Inverting = int(numberChosen1.get())
            img = Original_Image[:, :, a_Inverting - 1]
            img = np.array(img)
            img2 = np.array(img)
            Max = np.max(img2)
            for i in range(img2.shape[0]):
                for j in range(img2.shape[1]):
                    img2[i, j] = Max - img2[i, j]

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)

            ax3.set_title(" Histogram", fontsize=12, color="#333533")
            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            ax2.set_title("Invert Image", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')


            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', img2)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)

            img = Original_Image[:, :, a_Inverting - 1]
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(a_Inverting) + " Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Inverted Image" + " Histogram")
            ax3.legend(loc='best')
            fig.canvas.draw_idle()
        else:
            img = Original_Image
            img = np.array(img)
            img2 = np.array(img)
            Max = np.max(img2)
            for i in range(img2.shape[0]):
                for j in range(img2.shape[1]):
                    img2[i, j] = Max - img2[i, j]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)

            ax3.set_title(" Histogram", fontsize=12, color="#333533")

            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax3.set_facecolor("#2E2E2E")

            ax2.set_title("Invert Image", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img2, cmap='gray')

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', img2)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)

            img = Original_Image
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            hist_img1 = cv2.calcHist([img2], [0], None, [256], [0, 256])

            ax3.plot(range(256), hist_img.ravel(), color="magenta", label="Band" + str(1) + " Histogram")
            ax3.plot(range(256), hist_img1.ravel(), color="gold", label="Inverted Image" + " Histogram")
            ax3.legend(loc='best')
            fig.canvas.draw_idle()


    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Inverting   ', padx=20, bd='5',
                        command=Inverting1)
        btn.pack(anchor='w')


    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Inverting   ', padx=20, bd='5',
                         command=Inverting1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def Tresholding():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu returns Tresholded image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can use slider to treshold your image. if you want to save output image use the "Save Tresholded Image" botton.

                    """)


    def Tresholding1():
        if len(Original_image_Size) > 2:
            global imgT
            a_Tresholding = int(numberChosen1.get())
            imgT = Original_Image[:, :, a_Tresholding - 1]

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)


            ax2.set_title(" Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(imgT, cmap='gray')

            hist_img = cv2.calcHist([imgT], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_Tresholding)+"Histogram")



            ax2.axvline(x=0,label="Treshold", color='r')
            ax2.legend(loc='best')


            fig.canvas.draw_idle()

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time = Slider(ax1_value, 'Tresholding:', 0, 255, valinit=0,color='r')

            def update(val):
                ax2.cla()

                hist_img = cv2.calcHist([imgT], [0], None, [256], [0, 256])
                a_Tresholding = int(numberChosen1.get())
                ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_Tresholding)+"Histogram")
                ax2.axvline(x=int(s_time.val),label="Treshold", color='r')


                img = Original_Image[:, :, a_Tresholding - 1]
                img = np.array(img)
                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i, j] > s_time.val:
                            img[i, j] = 255
                        else:
                            img[i, j] = 0
                img3 = img
                ax1.imshow(img3, cmap='gray')

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Tresholding Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img3)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Tresholded Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)


                fig.canvas.draw_idle()

            s_time.on_changed(update)
        else:

            imgT = Original_Image

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title(" Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(imgT, cmap='gray')

            hist_img = cv2.calcHist([imgT], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")

            ax2.axvline(x=0, label="Treshold", color='r')
            ax2.legend(loc='best')

            fig.canvas.draw_idle()

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time = Slider(ax1_value, 'Tresholding:', 0, 255, valinit=0, color='r')

            def update(val):
                ax2.cla()

                hist_img = cv2.calcHist([imgT], [0], None, [256], [0, 256])

                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")
                ax2.axvline(x=int(s_time.val), label="Treshold", color='r')

                img = Original_Image
                img = np.array(img)
                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i, j] > s_time.val:
                            img[i, j] = 255
                        else:
                            img[i, j] = 0
                img3 = img
                ax1.imshow(img3, cmap='gray')

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Tresholding Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img3)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Tresholded Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            s_time.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Tresholding1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Tresholding1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def IntensityWindowing():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu returns strech image histogram between minimum and maximum. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can use slider to set minimum and maximum number for streching also you can enter your own number in entry box and then press "Set" button. both of them do same work. if you want to save output image use the "Save streched Image" botton.

                    """)

    def IntensityWindowing1():
        if len(Original_image_Size) > 2:
            global imgI
            a_IntensityWindowing = int(numberChosen1.get())
            imgI = Original_Image[:, :, a_IntensityWindowing - 1]

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)

            ax2.set_title(" Image Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")
            ax3.set_facecolor("#2E2E2E")


            ax3.set_title("Streched Histogram", fontsize=12, color="#333533")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=680)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(imgI, cmap='gray')

            hist_imgI = cv2.calcHist([imgI], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_imgI.ravel(), color="#d1ae45", label="Band" + str(a_IntensityWindowing) + "Histogram")
            ax2.legend(loc='best')

            fig.canvas.draw_idle()
            L1 = tk.Label(root8, text="From:")
            L1.place(x=0, y=650)
            E1 = tk.Entry(root8, bd=2)
            E1.place(x=40, y=650)

            L2 = tk.Label(root8, text="to:")
            L2.place(x=0, y=680)
            E2 = tk.Entry(root8, bd=2)
            E2.place(x=25, y=680)

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Fromm:', 0, 255, valinit=0,color='r')

            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'To:', 0, 255, valinit=0,color='g')

            def IntensityWindowing2():
                ax2.cla()
                ax1.cla()
                ax3.cla()

                hist_imgI = cv2.calcHist([imgI], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgI.ravel(), color="#d1ae45", label="Band" + str(a_IntensityWindowing) + "Histogram")

                ax2.axvline(x=float(E1.get()),label="From", color='r')
                ax2.axvline(x=float(E2.get()),label="To", color='g')
                ax2.legend(loc='best')

                img = Original_Image[:, :, a_IntensityWindowing - 1]
                img = np.array(img)
                Max = np.max(img)
                global E11
                E11 = float(E1.get())
                E22 = float(E2.get())

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i, j] < float(E1.get()):
                            img[i, j] = 0
                        elif img[i, j] > float(E2.get()):
                            img[i, j] = Max
                        else:
                            img[i, j] = Max * ((img[i, j] - E11 / (E22 - E11)))
                img3 = img
                ax1.imshow(img3, cmap='gray')

                hist_img3 = cv2.calcHist([img3], [0], None, [256], [0, 256])
                ax3.bar(range(256), hist_img3.ravel(), color="#d1ae45", label="Streched Histogram")
                ax3.legend(loc='best')
                ax1.set_title("Streched Image", fontsize=12, color="#333533")
                ax2.set_title(" Image Histogram", fontsize=12, color="#333533")
                ax3.set_title("Streched Histogram", fontsize=12, color="#333533")
                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
                ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");


                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img3)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Streched Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            def update(val):
                ax2.cla()
                ax1.cla()
                ax3.cla()

                hist_imgI = cv2.calcHist([imgI], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgI.ravel(),color="#d1ae45", label="Band" + str(a_IntensityWindowing) + "Histogram")

                ax2.axvline(x=float(s_time1.val),label="From", color='r')
                ax2.axvline(x=float(s_time2.val),label="To", color='g')

                img = Original_Image[:, :, a_IntensityWindowing - 1]
                img = np.array(img)
                Max = np.max(img)
                global E11
                E11 = float(s_time1.val)
                E22 = float(s_time2.val)

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i, j] < float(s_time1.val):
                            img[i, j] = 0
                        elif img[i, j] > float(s_time2.val):
                            img[i, j] = Max
                        else:
                            img[i, j] = Max * ((img[i, j] - E11 / (E22 - E11)))
                img3 = img
                ax1.imshow(img3, cmap='gray')

                ax1.set_title("Streched Image", fontsize=12, color="#333533")
                ax2.set_title(" Image Histogram", fontsize=12, color="#333533")
                ax3.set_title("Streched Histogram", fontsize=12, color="#333533")
                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
                ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                hist_img3 = cv2.calcHist([img3], [0], None, [256], [0, 256])
                ax3.bar(range(256), hist_img3.ravel(), color="#d1ae45", label="Streched Histogram")
                ax3.legend(loc='best')


                ax2.legend(loc='best')
                ax3.legend(loc='best')



                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img3)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Streched Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                             command=IntensityWindowing2)
            btn1.place(x=0, y=750)

            s_time1.on_changed(update)
            s_time2.on_changed(update)
        else:
            imgI = Original_Image

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(212)

            ax2.set_title(" Image Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
            ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")
            ax3.set_facecolor("#2E2E2E")

            ax3.set_title("Streched Histogram", fontsize=12, color="#333533")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=680)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(imgI, cmap='gray')

            hist_imgI = cv2.calcHist([imgI], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_imgI.ravel(), color="#d1ae45",
                    label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')

            fig.canvas.draw_idle()
            L1 = tk.Label(root8, text="From:")
            L1.place(x=0, y=650)
            E1 = tk.Entry(root8, bd=2)
            E1.place(x=40, y=650)

            L2 = tk.Label(root8, text="to:")
            L2.place(x=0, y=680)
            E2 = tk.Entry(root8, bd=2)
            E2.place(x=25, y=680)

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Fromm:', 0, 255, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'To:', 0, 255, valinit=0, color='g')

            def IntensityWindowing2():
                ax2.cla()
                ax1.cla()
                ax3.cla()

                hist_imgI = cv2.calcHist([imgI], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgI.ravel(), color="#d1ae45",
                        label="Band" + str(1) + "Histogram")

                ax2.axvline(x=float(E1.get()), label="From", color='r')
                ax2.axvline(x=float(E2.get()), label="To", color='g')
                ax2.legend(loc='best')

                img = Original_Image
                img = np.array(img)
                Max = np.max(img)
                global E11
                E11 = float(E1.get())
                E22 = float(E2.get())

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i, j] < float(E1.get()):
                            img[i, j] = 0
                        elif img[i, j] > float(E2.get()):
                            img[i, j] = Max
                        else:
                            img[i, j] = Max * ((img[i, j] - E11 / (E22 - E11)))
                img3 = img
                ax1.imshow(img3, cmap='gray')

                hist_img3 = cv2.calcHist([img3], [0], None, [256], [0, 256])
                ax3.bar(range(256), hist_img3.ravel(), color="#d1ae45", label="Streched Histogram")
                ax3.legend(loc='best')
                ax1.set_title("Streched Image", fontsize=12, color="#333533")
                ax2.set_title(" Image Histogram", fontsize=12, color="#333533")
                ax3.set_title("Streched Histogram", fontsize=12, color="#333533")
                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
                ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img3)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Streched Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            def update(val):
                ax2.cla()
                ax1.cla()
                ax3.cla()

                hist_imgI = cv2.calcHist([imgI], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgI.ravel(), color="#d1ae45",
                        label="Band" + str(1) + "Histogram")

                ax2.axvline(x=float(s_time1.val), label="From", color='r')
                ax2.axvline(x=float(s_time2.val), label="To", color='g')

                img = Original_Image
                img = np.array(img)
                Max = np.max(img)
                global E11
                E11 = float(s_time1.val)
                E22 = float(s_time2.val)

                for i in range(img.shape[0]):
                    for j in range(img.shape[1]):
                        if img[i, j] < float(s_time1.val):
                            img[i, j] = 0
                        elif img[i, j] > float(s_time2.val):
                            img[i, j] = Max
                        else:
                            img[i, j] = Max * ((img[i, j] - E11 / (E22 - E11)))
                img3 = img
                ax1.imshow(img3, cmap='gray')

                ax1.set_title("Streched Image", fontsize=12, color="#333533")
                ax2.set_title(" Image Histogram", fontsize=12, color="#333533")
                ax3.set_title("Streched Histogram", fontsize=12, color="#333533")
                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
                ax3.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax3.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                hist_img3 = cv2.calcHist([img3], [0], None, [256], [0, 256])
                ax3.bar(range(256), hist_img3.ravel(), color="#d1ae45", label="Streched Histogram")
                ax3.legend(loc='best')


                ax2.legend(loc='best')
                ax3.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img3)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Streched Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                             command=IntensityWindowing2)
            btn1.place(x=0, y=750)

            s_time1.on_changed(update)
            s_time2.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=IntensityWindowing1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=IntensityWindowing1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def LogTr():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu returns Transformed image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can use slider to set constant value for transform logarithm. also you can enter your own number in entry box and then press "Set" button. both of them do same work. if you want to save output image use the "Save Logarithm Transformed Image" botton.

                    """)

    def LogTr1():
        if len(Original_image_Size) > 2:
            a_LogTr = int(numberChosen1.get())
            img = Original_Image[:, :, a_LogTr - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title(" Logarithm Transform", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");


            ax2.set_facecolor("#2E2E2E")




            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            img = np.double(img)
            nimg = img / 255
            img2 = np.log1p(1 + nimg)

            img2 = np.uint8(img2)

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time = Slider(ax1_value, 'Constant:', 0, 300, valinit=0,color='r')

            def DrawPlot():
                E11 = float(E1.get())
                q = E11 * np.log1p(1 + nimg)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = E11 * np.log1p(1 + x)
                p = str(E11)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                ax1.set_title("Logarithm Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Logarithm Transformed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Constant:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=270, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=650)
            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn1.place(x=440, y=650)

            def update(val):

                pos = float(s_time.val)
                q = pos * np.log1p(1 + nimg)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = pos * np.log1p(1 + x)
                p = str(pos)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))


                ax1.set_title("Logarithm Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Logarithm Transformed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            x = np.arange(0, 256, 1)
            y = np.log1p(1 + x)
            ax2.plot(x, y)
            ax2.plot(x, y, label="c={0}".format(s_time.val))
            ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))
            s_time.on_changed(update)
        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title(" Logarithm Transform", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            img = np.double(img)
            nimg = img / 255
            img2 = np.log1p(1 + nimg)

            img2 = np.uint8(img2)

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time = Slider(ax1_value, 'Constant:', 0, 300, valinit=0, color='r')

            def DrawPlot():
                E11 = float(E1.get())
                q = E11 * np.log1p(1 + nimg)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = E11 * np.log1p(1 + x)
                p = str(E11)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                ax1.set_title("Logarithm Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Logarithm Transformed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Constant:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=270, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=650)
            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn1.place(x=440, y=650)

            def update(val):

                pos = float(s_time.val)
                q = pos * np.log1p(1 + nimg)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = pos * np.log1p(1 + x)
                p = str(pos)
                ax2.plot(x, y, label=p)
                ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))

                ax1.set_title("Logarithm Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Logarithm Transformed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            x = np.arange(0, 256, 1)
            y = np.log1p(1 + x)
            ax2.plot(x, y)
            ax2.plot(x, y, label="c={0}".format(s_time.val))
            ax2.legend(loc='upper left', prop={'size': 7}, bbox_to_anchor=(1, 1))
            s_time.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=LogTr1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=LogTr1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def PowerTr():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu returns Transformed image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can use slider to set constant value and power value for power transform. also you can enter your own numbers in entry box and then press "Set" button. both of them do same work. if you want to save output image use the "Save power Transformed Image" botton.

                    """)

    def PowerTr1():
        if len(Original_image_Size) > 2:
            a_PowTr = int(numberChosen1.get())
            img = Original_Image[:, :, a_PowTr - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Power Transform", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=740, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            img = np.double(img)
            nimg = img / 255
            img2 = np.log1p(1 + nimg)

            img2 = np.uint8(img2)

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Constant', 0, 300, valinit=0,color='r')
            s_time2 = Slider(ax2_value, 'Power', 0, 30, valinit=0,color='g')

            def DrawPlot():
                E11 = float(E1.get())
                E22 = float(E2.get())
                q = E11 * (nimg ** E22)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = E11 * (x ** E22)
                p1 = round(E11)
                p2 = round(E22)
                p1 = str(E11)
                p2 = str(E22)
                ax2.plot(x, y, label=['C=' + p1, 'P=' + p2])
                ax2.legend(loc='upper left', prop={'size': 8}, bbox_to_anchor=(1, 1))

                ax1.set_title("Power Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Power Transformed Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="C:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=240, y=700)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=260, y=700)

            L2 = tk.Label(root8, text="Power:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=390, y=700)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=440, y=700)
            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn2.place(x=570, y=700)

            def update(val):

                pos1 = float(s_time1.val)
                pos2 = float(s_time2.val)
                q = pos1 * (nimg ** pos2)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = pos1 * (x ** pos2)
                pos1 = round(pos1)
                pos2 = round(pos2)
                p1 = str(pos1)
                p2 = str(pos2)
                ax2.plot(x, y, label=['C=' + p1, 'P=' + p2])
                ax2.legend(loc='upper left', prop={'size': 8}, bbox_to_anchor=(1, 1))

                ax1.set_title("Power Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Power Transformed Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            x = np.arange(0, 256, 1)
            y = x ** 2
            ax2.plot(x, y)
            ax2.plot(x, y, label=['C=1', 'P=2'])
            ax2.legend(loc='upper left', prop={'size': 8}, bbox_to_anchor=(1, 1))

            s_time1.on_changed(update)
            s_time2.on_changed(update)


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Power Transform", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=740, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            img = np.double(img)
            nimg = img / 255
            img2 = np.log1p(1 + nimg)

            img2 = np.uint8(img2)

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Constant', 0, 300, valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Power', 0, 30, valinit=0, color='g')

            def DrawPlot():
                E11 = float(E1.get())
                E22 = float(E2.get())
                q = E11 * (nimg ** E22)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = E11 * (x ** E22)
                p1 = round(E11)
                p2 = round(E22)
                p1 = str(E11)
                p2 = str(E22)
                ax2.plot(x, y, label=['C=' + p1, 'P=' + p2])
                ax2.legend(loc='upper left', prop={'size': 8}, bbox_to_anchor=(1, 1))

                ax1.set_title("Power Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Power Transformed Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="C:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=240, y=700)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=260, y=700)

            L2 = tk.Label(root8, text="Power:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=390, y=700)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=440, y=700)
            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn2.place(x=570, y=700)

            def update(val):

                pos1 = float(s_time1.val)
                pos2 = float(s_time2.val)
                q = pos1 * (nimg ** pos2)
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                y = pos1 * (x ** pos2)
                pos1 = round(pos1)
                pos2 = round(pos2)
                p1 = str(pos1)
                p2 = str(pos2)
                ax2.plot(x, y, label=['C=' + p1, 'P=' + p2])
                ax2.legend(loc='upper left', prop={'size': 8}, bbox_to_anchor=(1, 1))

                ax1.set_title("Power Transformed Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Power Transformed Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            x = np.arange(0, 256, 1)
            y = x ** 2
            ax2.plot(x, y)
            ax2.plot(x, y, label=['C=1', 'P=2'])
            ax2.legend(loc='upper left', prop={'size': 8}, bbox_to_anchor=(1, 1))

            s_time1.on_changed(update)
            s_time2.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=PowerTr1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=PowerTr1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')



    root8.mainloop()


def ACA():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Automatic contrast adjustment. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can use slider to set minimum value and maximum value for automatic contrast adjustment. also you can enter your own numbers in entry box and then press "Set" button. both of them do same work. if you want to save output image use the "Save output Image" botton.

                    """)


    def ACA1():
        if len(Original_image_Size) > 2:
            a_ACA1 = int(numberChosen1.get())
            img = Original_Image[:, :, a_ACA1 - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=760, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Minimum', 0, 300, valinit=0,color='r')
            s_time2 = Slider(ax2_value, 'Maximum', 0, 30, valinit=0,color='g')

            def DrawPlot():
                ax2.cla()
                E11 = float(E1.get())
                E22 = float(E2.get())
                q = E11 + (img - np.min(img)) * ((E22 - E11) / (np.max(img) - np.min(img)))
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(),color="magenta",label="Automatic Contrast Adjustment Image Histogram")
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",label="Band"+str(a_ACA1))

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax1.set_title("Automatic Contrast Adjustment Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Output Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Min:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=230, y=700)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=270, y=700)

            L2 = tk.Label(root8, text="Max:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=405, y=700)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=440, y=700)
            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn2.place(x=570, y=700)

            def update(val):
                ax2.cla()
                pos1 = s_time1.val
                pos2 = s_time2.val
                q = pos1 + (img - np.min(img)) * ((pos2 - pos1) / (np.max(img) - np.min(img)))
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Automatic Contrast Adjustment Image Histogram")
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(a_ACA1))

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax1.set_title("Automatic Contrast Adjustment Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Output Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(),color="gold",label="Band"+str(a_ACA1))
            ax2.legend(loc='best')

            s_time1.on_changed(update)
            s_time2.on_changed(update)


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=760, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Minimum', 0, 300, valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Maximum', 0, 30, valinit=0, color='g')

            def DrawPlot():
                ax2.cla()
                E11 = float(E1.get())
                E22 = float(E2.get())
                q = E11 + (img - np.min(img)) * ((E22 - E11) / (np.max(img) - np.min(img)))
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Automatic Contrast Adjustment Image Histogram")
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1))

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax1.set_title("Automatic Contrast Adjustment Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Output Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Min:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=230, y=700)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=270, y=700)

            L2 = tk.Label(root8, text="Max:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=405, y=700)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=440, y=700)
            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=DrawPlot)
            btn2.place(x=570, y=700)

            def update(val):
                ax2.cla()
                pos1 = s_time1.val
                pos2 = s_time2.val
                q = pos1 + (img - np.min(img)) * ((pos2 - pos1) / (np.max(img) - np.min(img)))
                q = np.uint8(q)
                ax1.imshow(q, cmap='gray')
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Automatic Contrast Adjustment Image Histogram")
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1))

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax1.set_title("Automatic Contrast Adjustment Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Output Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1))
            ax2.legend(loc='best')

            s_time1.on_changed(update)
            s_time2.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=ACA1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=ACA1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def HisogramMatching():
    root8 = tk.Toplevel()

    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for maching histogram of two images. for using this option on the application at first you should select your special band for the source image from the "list top of the page" and then press "Select Band" button then appears "Open" button that You can use it for open template image and by "select band" button under that button you can select your special band for template image then two histogram will be matched. if you want to save output image use the "Save Matched Image" botton.

                    """)

    def HisogramMatching1():
        if len(Original_image_Size) > 2:
            a_HistogramMatching = int(numberChosen1.get())
            img = Original_Image[:, :, a_HistogramMatching - 1]

            def OpenTemplate():
                global Template_Image
                root8.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                            filetypes=(
                                                                ("jpeg files", "*.jpg"), ("all files", "*.*")))
                Template_Image = imread(root8.filename)

                a3 = np.shape(Template_Image)
                Template_Image_Size = np.shape(Template_Image)

                def HistogramMatching2():
                    if len(Template_Image_Size) > 2:
                        a_HistogramMatching2 = int(numberChosen11.get())
                        img2 = Template_Image[:, :, a_HistogramMatching2 - 1]
                        template = img2
                        source = img

                        def hist_match(source, template):
                            oldshape = source.shape
                            source = source.ravel()
                            template = template.ravel()

                            # get the set of unique pixel values and their corresponding indices and
                            # counts
                            s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                                                    return_counts=True)
                            t_values, t_counts = np.unique(template, return_counts=True)

                            # take the cumsum of the counts and normalize by the number of pixels to
                            # get the empirical cumulative distribution functions for the source and
                            # template images (maps pixel value --> quantile)
                            s_quantiles = np.cumsum(s_counts).astype(np.float64)
                            s_quantiles /= s_quantiles[-1]
                            t_quantiles = np.cumsum(t_counts).astype(np.float64)
                            t_quantiles /= t_quantiles[-1]

                            # interpolate linearly to find the pixel values in the template image
                            # that correspond most closely to the quantiles in the source image
                            interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

                            return interp_t_values[bin_idx].reshape(oldshape)

                        matched = hist_match(source, template)

                        def ecdf(x):
                            """convenience function for computing the empirical CDF"""
                            vals, counts = np.unique(x, return_counts=True)
                            ecdf = np.cumsum(counts).astype(np.float64)
                            ecdf /= ecdf[-1]
                            return vals, ecdf

                        x1, y1 = ecdf(source.ravel())
                        x2, y2 = ecdf(template.ravel())
                        x3, y3 = ecdf(matched.ravel())

                        fig = plt.Figure(figsize=(13, 7))
                        canvas = FigureCanvasTkAgg(fig, root8)
                        canvas.get_tk_widget().place(x=200, y=0)
                        gs = plt.GridSpec(2, 3)
                        ax1 = fig.add_subplot(gs[0, 0])
                        ax2 = fig.add_subplot(gs[0, 1], sharex=ax1, sharey=ax1)
                        ax3 = fig.add_subplot(gs[0, 2], sharex=ax1, sharey=ax1)
                        ax4 = fig.add_subplot(gs[1, :])
                        ax4.set_facecolor("#2E2E2E")

                        for aa in (ax1, ax2, ax3):
                            aa.set_axis_off()

                        ax1.imshow(source, cmap=plt.cm.gray)
                        ax1.set_title('Source')
                        ax2.imshow(template, cmap=plt.cm.gray)
                        ax2.set_title('template')
                        ax3.imshow(matched, cmap=plt.cm.gray)
                        ax3.set_title('Matched')

                        ax4.plot(x1, y1 * 100, '-r', lw=3, label='Source',color='gold')
                        ax4.plot(x2, y2 * 100, '-k', lw=3, label='Template',color='magenta')
                        ax4.plot(x3, y3 * 100, '--r', lw=3, label='Matched',color='g')
                        ax4.set_xlim(x1[0], x1[-1])
                        ax4.set_xlabel('Pixel value')
                        ax4.set_ylabel('Cumulative %')
                        ax4.set_title("Histogram", fontsize=12, color="#333533")
                        ax4.legend(loc='best')

                        def SaveI():
                            f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                            if f is None:
                                return

                            filename = f.name

                            cv2.imwrite(str(filename) + '.jpg', matched)
                            f.close()

                        btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save matched Image   ', padx=20,
                                         bd='5',
                                         command=SaveI)
                        btnw.place(x=1200, y=0)

                        fig.canvas.draw_idle()

                    else:
                        img2 = Template_Image
                        template = img2
                        source = img

                        def hist_match(source, template):
                            oldshape = source.shape
                            source = source.ravel()
                            template = template.ravel()

                            # get the set of unique pixel values and their corresponding indices and
                            # counts
                            s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                                                    return_counts=True)
                            t_values, t_counts = np.unique(template, return_counts=True)

                            # take the cumsum of the counts and normalize by the number of pixels to
                            # get the empirical cumulative distribution functions for the source and
                            # template images (maps pixel value --> quantile)
                            s_quantiles = np.cumsum(s_counts).astype(np.float64)
                            s_quantiles /= s_quantiles[-1]
                            t_quantiles = np.cumsum(t_counts).astype(np.float64)
                            t_quantiles /= t_quantiles[-1]

                            # interpolate linearly to find the pixel values in the template image
                            # that correspond most closely to the quantiles in the source image
                            interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

                            return interp_t_values[bin_idx].reshape(oldshape)

                        matched = hist_match(source, template)

                        def ecdf(x):
                            """convenience function for computing the empirical CDF"""
                            vals, counts = np.unique(x, return_counts=True)
                            ecdf = np.cumsum(counts).astype(np.float64)
                            ecdf /= ecdf[-1]
                            return vals, ecdf

                        x1, y1 = ecdf(source.ravel())
                        x2, y2 = ecdf(template.ravel())
                        x3, y3 = ecdf(matched.ravel())

                        fig = plt.Figure(figsize=(13, 7))
                        canvas = FigureCanvasTkAgg(fig, root8)
                        canvas.get_tk_widget().place(x=200, y=0)
                        gs = plt.GridSpec(2, 3)
                        ax1 = fig.add_subplot(gs[0, 0])
                        ax2 = fig.add_subplot(gs[0, 1], sharex=ax1, sharey=ax1)
                        ax3 = fig.add_subplot(gs[0, 2], sharex=ax1, sharey=ax1)
                        ax4 = fig.add_subplot(gs[1, :])
                        ax4.set_facecolor("#2E2E2E")

                        for aa in (ax1, ax2, ax3):
                            aa.set_axis_off()

                        ax1.imshow(source, cmap=plt.cm.gray)
                        ax1.set_title('Source')
                        ax2.imshow(template, cmap=plt.cm.gray)
                        ax2.set_title('template')
                        ax3.imshow(matched, cmap=plt.cm.gray)
                        ax3.set_title('Matched')

                        ax4.plot(x1, y1 * 100, '-r', lw=3, label='Source', color='gold')
                        ax4.plot(x2, y2 * 100, '-k', lw=3, label='Template', color='magenta')
                        ax4.plot(x3, y3 * 100, '--r', lw=3, label='Matched', color='g')
                        ax4.set_xlim(x1[0], x1[-1])
                        ax4.set_xlabel('Pixel value')
                        ax4.set_ylabel('Cumulative %')
                        ax4.set_title("Histogram", fontsize=12, color="#333533")
                        ax4.legend(loc='best')

                        def SaveI():
                            f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                            if f is None:
                                return

                            filename = f.name

                            cv2.imwrite(str(filename) + '.jpg', matched)
                            f.close()

                        btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save matched Image   ', padx=20,
                                         bd='5',
                                         command=SaveI)
                        btnw.place(x=1200, y=0)

                        fig.canvas.draw_idle()


                if len(Template_Image_Size) > 2:
                    Dimension_Number1 = []
                    Dimension_Number1_int = []
                    for x11 in range(Template_Image.shape[2]):
                        Dimension_Number1_int.append(x11 + 1)
                        Dimension_Number1.append(("Band ", x11 + 1))

                else:
                    Dimension_Number1 = [("Band", 1)]

                if len(Template_Image_Size) > 2:
                    ttk.Label(root8, text="Choose a band:").pack(anchor='w')
                    number11 = tk.StringVar()
                    numberChosen11 = ttk.Combobox(root8, width=12, textvariable=number11)
                    numberChosen11['values'] = (Dimension_Number1_int)
                    numberChosen11.pack(anchor='w')
                    numberChosen11.current(0)
                    btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                                    command=HistogramMatching2)
                    btn.pack(anchor='w')

                else:
                    tk.Label(root8, text="Choose a band:").pack(anchor='w')
                    number11 = tk.StringVar()
                    numberChosen11 = ttk.Combobox(root8, width=12, textvariable=number11)
                    numberChosen11['values'] = "1"
                    numberChosen11.pack(anchor='w')
                    numberChosen11.current(0)
                    btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                                     command=HistogramMatching2)
                    btn1.pack(anchor='w')

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Open   ', padx=20, bd='5',
                            command=OpenTemplate)
            btn.pack(anchor='w')


        else:
            img = Original_Image

            def OpenTemplate():
                global Template_Image
                root8.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                            filetypes=(
                                                                ("jpeg files", "*.jpg"), ("all files", "*.*")))
                Template_Image = imread(root8.filename)

                a3 = np.shape(Template_Image)
                Template_Image_Size = np.shape(Template_Image)

                def HistogramMatching2():
                    if len(Template_Image_Size) > 2:
                        a_HistogramMatching2 = int(numberChosen11.get())
                        img2 = Template_Image[:, :, a_HistogramMatching2 - 1]
                        template = img2
                        source = img

                        def hist_match(source, template):
                            oldshape = source.shape
                            source = source.ravel()
                            template = template.ravel()

                            # get the set of unique pixel values and their corresponding indices and
                            # counts
                            s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                                                    return_counts=True)
                            t_values, t_counts = np.unique(template, return_counts=True)

                            # take the cumsum of the counts and normalize by the number of pixels to
                            # get the empirical cumulative distribution functions for the source and
                            # template images (maps pixel value --> quantile)
                            s_quantiles = np.cumsum(s_counts).astype(np.float64)
                            s_quantiles /= s_quantiles[-1]
                            t_quantiles = np.cumsum(t_counts).astype(np.float64)
                            t_quantiles /= t_quantiles[-1]

                            # interpolate linearly to find the pixel values in the template image
                            # that correspond most closely to the quantiles in the source image
                            interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

                            return interp_t_values[bin_idx].reshape(oldshape)

                        matched = hist_match(source, template)

                        def ecdf(x):
                            """convenience function for computing the empirical CDF"""
                            vals, counts = np.unique(x, return_counts=True)
                            ecdf = np.cumsum(counts).astype(np.float64)
                            ecdf /= ecdf[-1]
                            return vals, ecdf

                        x1, y1 = ecdf(source.ravel())
                        x2, y2 = ecdf(template.ravel())
                        x3, y3 = ecdf(matched.ravel())

                        fig = plt.Figure(figsize=(13, 7))
                        canvas = FigureCanvasTkAgg(fig, root8)
                        canvas.get_tk_widget().place(x=200, y=0)
                        gs = plt.GridSpec(2, 3)
                        ax1 = fig.add_subplot(gs[0, 0])
                        ax2 = fig.add_subplot(gs[0, 1], sharex=ax1, sharey=ax1)
                        ax3 = fig.add_subplot(gs[0, 2], sharex=ax1, sharey=ax1)
                        ax4 = fig.add_subplot(gs[1, :])
                        ax4.set_facecolor("#2E2E2E")

                        for aa in (ax1, ax2, ax3):
                            aa.set_axis_off()

                        ax1.imshow(source, cmap=plt.cm.gray)
                        ax1.set_title('Source')
                        ax2.imshow(template, cmap=plt.cm.gray)
                        ax2.set_title('template')
                        ax3.imshow(matched, cmap=plt.cm.gray)
                        ax3.set_title('Matched')

                        ax4.plot(x1, y1 * 100, '-r', lw=3, label='Source', color='gold')
                        ax4.plot(x2, y2 * 100, '-k', lw=3, label='Template', color='magenta')
                        ax4.plot(x3, y3 * 100, '--r', lw=3, label='Matched', color='g')
                        ax4.set_xlim(x1[0], x1[-1])
                        ax4.set_xlabel('Pixel value')
                        ax4.set_ylabel('Cumulative %')
                        ax4.set_title("Histogram", fontsize=12, color="#333533")
                        ax4.legend(loc='best')

                        def SaveI():
                            f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                            if f is None:
                                return

                            filename = f.name

                            cv2.imwrite(str(filename) + '.jpg', matched)
                            f.close()

                        btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save matched Image   ', padx=20,
                                         bd='5',
                                         command=SaveI)
                        btnw.place(x=1200, y=0)

                        fig.canvas.draw_idle()
                    else:
                        img2 = Template_Image
                        template = img2
                        source = img

                        def hist_match(source, template):
                            oldshape = source.shape
                            source = source.ravel()
                            template = template.ravel()

                            # get the set of unique pixel values and their corresponding indices and
                            # counts
                            s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                                                    return_counts=True)
                            t_values, t_counts = np.unique(template, return_counts=True)

                            # take the cumsum of the counts and normalize by the number of pixels to
                            # get the empirical cumulative distribution functions for the source and
                            # template images (maps pixel value --> quantile)
                            s_quantiles = np.cumsum(s_counts).astype(np.float64)
                            s_quantiles /= s_quantiles[-1]
                            t_quantiles = np.cumsum(t_counts).astype(np.float64)
                            t_quantiles /= t_quantiles[-1]

                            # interpolate linearly to find the pixel values in the template image
                            # that correspond most closely to the quantiles in the source image
                            interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

                            return interp_t_values[bin_idx].reshape(oldshape)

                        matched = hist_match(source, template)

                        def ecdf(x):
                            """convenience function for computing the empirical CDF"""
                            vals, counts = np.unique(x, return_counts=True)
                            ecdf = np.cumsum(counts).astype(np.float64)
                            ecdf /= ecdf[-1]
                            return vals, ecdf

                        x1, y1 = ecdf(source.ravel())
                        x2, y2 = ecdf(template.ravel())
                        x3, y3 = ecdf(matched.ravel())

                        fig = plt.Figure(figsize=(13, 7))
                        canvas = FigureCanvasTkAgg(fig, root8)
                        canvas.get_tk_widget().place(x=200, y=0)
                        gs = plt.GridSpec(2, 3)
                        ax1 = fig.add_subplot(gs[0, 0])
                        ax2 = fig.add_subplot(gs[0, 1], sharex=ax1, sharey=ax1)
                        ax3 = fig.add_subplot(gs[0, 2], sharex=ax1, sharey=ax1)
                        ax4 = fig.add_subplot(gs[1, :])
                        ax4.set_facecolor("#2E2E2E")

                        for aa in (ax1, ax2, ax3):
                            aa.set_axis_off()

                        ax1.imshow(source, cmap=plt.cm.gray)
                        ax1.set_title('Source')
                        ax2.imshow(template, cmap=plt.cm.gray)
                        ax2.set_title('template')
                        ax3.imshow(matched, cmap=plt.cm.gray)
                        ax3.set_title('Matched')

                        ax4.plot(x1, y1 * 100, '-r', lw=3, label='Source', color='gold')
                        ax4.plot(x2, y2 * 100, '-k', lw=3, label='Template', color='magenta')
                        ax4.plot(x3, y3 * 100, '--r', lw=3, label='Matched', color='g')
                        ax4.set_xlim(x1[0], x1[-1])
                        ax4.set_xlabel('Pixel value')
                        ax4.set_ylabel('Cumulative %')
                        ax4.set_title("Histogram", fontsize=12, color="#333533")
                        ax4.legend(loc='best')

                        def SaveI():
                            f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                            if f is None:
                                return

                            filename = f.name

                            cv2.imwrite(str(filename) + '.jpg', matched)
                            f.close()

                        btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save matched Image   ', padx=20,
                                         bd='5',
                                         command=SaveI)
                        btnw.place(x=1200, y=0)

                        fig.canvas.draw_idle()

                if len(Template_Image_Size) > 2:
                    Dimension_Number1 = []
                    Dimension_Number1_int = []
                    for x11 in range(Template_Image.shape[2]):
                        Dimension_Number1_int.append(x11 + 1)
                        Dimension_Number1.append(("Band ", x11 + 1))

                else:
                    Dimension_Number1 = [("Band", 1)]

                if len(Template_Image_Size) > 2:
                    ttk.Label(root8, text="Choose a band:").pack(anchor='w')
                    number11 = tk.StringVar()
                    numberChosen11 = ttk.Combobox(root8, width=12, textvariable=number11)
                    numberChosen11['values'] = (Dimension_Number1_int)
                    numberChosen11.pack(anchor='w')
                    numberChosen11.current(0)
                    btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                                    command=HistogramMatching2)
                    btn.pack(anchor='w')

                else:
                    tk.Label(root8, text="Choose a band:").pack(anchor='w')
                    number11 = tk.StringVar()
                    numberChosen11 = ttk.Combobox(root8, width=12, textvariable=number11)
                    numberChosen11['values'] = "1"
                    numberChosen11.pack(anchor='w')
                    numberChosen11.current(0)
                    btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                                     command=HistogramMatching2)
                    btn1.pack(anchor='w')

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Open   ', padx=20, bd='5',
                            command=OpenTemplate)
            btn.pack(anchor='w')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=HisogramMatching1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=HisogramMatching1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def AverageFilter():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Averaging filter. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You should enter the size of your kernel in entry box and then press "Apply" button. if you want to save output image use the "Save Filtered Image" botton.

                    """)

    def AveragingFilter1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=850, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def AverageFiltering2():
                ax2.cla()
                E11 = int(E1.get())
                E22 = int(E2.get())
                kernel_3 = np.ones((E11, E22), np.float32) / (E11 * E22)

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(),color="gold", label="Band" + str(a_AverageFiltering)+"Histogram")
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(),color="magenta", label="Filtered Image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Row:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=350, y=600)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=380, y=600)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=520, y=600)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=570, y=600)
            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=AverageFiltering2)
            btn2.place(x=680, y=600)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(a_AverageFiltering)+"Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=850, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def AverageFiltering2():
                ax2.cla()
                E11 = int(E1.get())
                E22 = int(E2.get())
                kernel_3 = np.ones((E11, E22), np.float32) / (E11 * E22)

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered Image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Row:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=350, y=600)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=380, y=600)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=520, y=600)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=570, y=600)
            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=AverageFiltering2)
            btn2.place(x=680, y=600)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBAvrageFil():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=850, y=600)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def AverageFiltering2():
                    ax2.cla()
                    E11 = int(E1.get())
                    E22 = int(E2.get())
                    kernel_3 = np.ones((E11, E22), np.float32) / (E11 * E22)

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')

                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax1.set_title("Filtred Image", fontsize=12, color="#333533")

                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")


                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label= "Filtered Image Histogram")
                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                L1 = tk.Label(root8, text="Row:", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=350, y=600)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=380, y=600)

                L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
                L2.place(x=520, y=600)
                E2 = tk.Entry(root8, bd=5)
                E2.place(x=570, y=600)
                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                                 command=AverageFiltering2)
                btn2.place(x=680, y=600)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")
                ax2.legend(loc='best')

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBAvrageFil)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=AveragingFilter1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").place(x=0, y=0)
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=AveragingFilter1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def GaussianFilter():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for gaussian filter. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You should enter the size of your kernel in entry box and then press "Apply" button and finaly by slider you can control the sigma X and sigma Y value. if you want to save output image use the "Save Filtered Image" botton.

                    """)

    def GaussianFilter1():
        if len(Original_image_Size) > 2:
            a_GaussianFilter = int(numberChosen1.get())
            img = Original_Image[:, :, a_GaussianFilter - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=850, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.15, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Sigma X', 0, 30, valinit=0,color='r')
            s_time2 = Slider(ax2_value, 'Sigma Y', 0, 30, valinit=0,color='g')

            def GaussianFilter3():
                global t1
                t1 = int(E1.get())

            def GaussianFilter2(val):
                ax2.cla()
                q = cv2.GaussianBlur(img, (t1, t1), s_time1.val, s_time2.val)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold", label= "Band"+str(a_GaussianFilter)+" Histogram")
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label= "Filtered Image Histogram")
                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Kernel Size(odd number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=350, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=495, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=GaussianFilter3)
            btn2.place(x=620, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label= "Band"+str(a_GaussianFilter)+" Histogram")
            ax2.legend(loc='best')

            s_time1.on_changed(GaussianFilter2)
            s_time2.on_changed(GaussianFilter2)


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=850, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Sigma X', 0, 30, valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Sigma Y', 0, 30, valinit=0, color='g')

            def GaussianFilter3():
                global t1
                t1 = int(E1.get())

            def GaussianFilter2(val):
                ax2.cla()
                q = cv2.GaussianBlur(img, (t1, t1), s_time1.val, s_time2.val)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + " Histogram")
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered Image Histogram")
                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Kernel Size(odd number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=350, y=700)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=495, y=700)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=GaussianFilter3)
            btn2.place(x=620, y=700)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1) + " Histogram")
            ax2.legend(loc='best')

            s_time1.on_changed(GaussianFilter2)
            s_time2.on_changed(GaussianFilter2)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBGaussFil():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                fig.subplots_adjust(bottom=0.25)

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=850, y=700)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                ax1.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
                s_time1 = Slider(ax1_value, 'Sigma X', 0, 30, valinit=0)
                s_time2 = Slider(ax2_value, 'Sigma Y', 0, 30, valinit=0)

                def GaussianFilter3():
                    global t1
                    t1 = int(E1.get())

                def GaussianFilter2(val):
                    ax2.cla()
                    q = cv2.GaussianBlur(img, (t1, t1), s_time1.val, s_time2.val)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="R", label="Band" + str(1) + " Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + " Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + " Histogram")


                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")
                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)


                    fig.canvas.draw_idle()

                L1 = tk.Label(root8, text="Kernel Size(odd number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=350, y=700)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=495, y=700)

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                                 command=GaussianFilter3)
                btn2.place(x=620, y=700)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="R", label="Band" + str(1) + " Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(),  color="g", label="Band" + str(2) + " Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + " Histogram")

                ax2.legend(loc='best')

                s_time1.on_changed(GaussianFilter2)
                s_time2.on_changed(GaussianFilter2)

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBGaussFil)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=GaussianFilter1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=GaussianFilter1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def MedianFilter():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Median filter. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You should enter the size of your kernel in entry box and then press "Apply" button. if you want to save output image use the "Save Filtered Image" botton.

                    """)


    def MedianFilter1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=850, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def MedianFilter2():
                ax2.cla()
                E11 = int(E1.get())

                q = cv2.medianBlur(img, E11)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band"+str(a_AverageFiltering)+"Histogram")
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered Image Histogram")

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Kernel Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=550, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=MedianFilter2)
            btn2.place(x=680, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band"+str(a_AverageFiltering)+"Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=850, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def MedianFilter2():
                ax2.cla()
                E11 = int(E1.get())

                q = cv2.medianBlur(img, E11)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")
                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered Image Histogram")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Kernel Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=550, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=MedianFilter2)
            btn2.place(x=680, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBMedianFil():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=850, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def MedianFilter2():
                    ax2.cla()
                    E11 = int(E1.get())

                    q = cv2.medianBlur(img, E11)
                    ax1.imshow(q, cmap='gray')

                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel() ,color="r", label="Band1 Histogram")

                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band2 Histogram")

                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band3 Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")
                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                L1 = tk.Label(root8, text="Kernel Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=400, y=650)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=550, y=650)

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                                 command=MedianFilter2)
                btn2.place(x=680, y=650)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band1 Histogram")

                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band2 Histogram")

                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band3 Histogram")
                ax2.legend(loc='best')


            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBMedianFil)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=MedianFilter1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=MedianFilter1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def UDK():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for any kernel. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You should enter the size of your kernel in entry box and then press "Apply" button then appears a matrix that you should define your value kernel then press "Set" Button. if you want to save output image use the "Save Filtered Image" botton.

                    """)


    def UDK1():
        if len(Original_image_Size) > 2:
            a_UDK = int(numberChosen1.get())
            img = Original_Image[:, :, a_UDK - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def UDK2():
                root9 = tk.Tk()
                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def UDK3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))
                    Kernel = np.array(Kernel)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.filter2D(img, -1, Kernel)
                    ax1.imshow(q, cmap='gray')
                    ax2.cla()
                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img.ravel(), color="gold",
                             label="Band" + str(a_UDK) + "Histogram")
                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered Image Histogram")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()


                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=UDK3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            L1 = tk.Label(root8, text="Rows(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=515, y=650)

            L2 = tk.Label(root8, text="Column(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=650, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=750, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1', command=UDK2)
            btn2.place(x=860, y=650)
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(),color="gold",
                             label="Band" + str(a_UDK) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def UDK2():
                root9 = tk.Tk()
                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def UDK3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))
                    Kernel = np.array(Kernel)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.filter2D(img, -1, Kernel)
                    ax1.imshow(q, cmap='gray')
                    ax2.cla()
                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img.ravel(), color="gold",
                             label="Band" + str(1) + "Histogram")
                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered Image Histogram")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=UDK3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            L1 = tk.Label(root8, text="Rows(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=515, y=650)

            L2 = tk.Label(root8, text="Column(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=650, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=750, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1', command=UDK2)
            btn2.place(x=860, y=650)
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                     label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:

            def RGBUDK():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def UDK2():
                    root9 = tk.Tk()
                    root9.configure(background='white')
                    root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

                    height = int(E1.get())
                    width = int(E2.get())
                    rows = []
                    for i in range(height):  # Rows
                        cols = []
                        for j in range(width):  # Columns
                            b = tk.Entry(root9, text="")
                            b.grid(row=i, column=j)
                            cols.append(b)
                        rows.append(cols)

                    def UDK3():
                        global Kernel
                        Kernel = []
                        for row in rows:
                            for col in row:
                                Kernel.append(float(col.get()))
                        Kernel = np.array(Kernel)
                        Kernel = np.reshape(Kernel, (height, width))
                        ax2.cla()
                        q = cv2.filter2D(img, -1, Kernel)
                        ax1.imshow(q, cmap='gray')

                        hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                        ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band1 Histogram")

                        hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                        ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band2 Histogram")

                        hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                        ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band3 Histogram")

                        ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                        ax2.set_title("Histogram", fontsize=12, color="#333533")


                        hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                        ax2.plot(range(256), hist_q.ravel(),  color="gold", label="Filtered Image Histogram")
                        ax2.legend(loc='best')

                        def SaveI():
                            f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                            if f is None:
                                return

                            filename = f.name

                            cv2.imwrite(str(filename) + '.jpg', q)
                            f.close()

                        btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                         bd='5',
                                         command=SaveI)
                        btnw.place(x=400, y=0)

                        fig.canvas.draw_idle()

                    btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                     command=UDK3)
                    btn1.grid(row=height + 1, column=0)
                    root9.mainloop()

                L1 = tk.Label(root8, text="Rows(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=400, y=650)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=515, y=650)

                L2 = tk.Label(root8, text="Column(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L2.place(x=650, y=650)
                E2 = tk.Entry(root8, bd=5)
                E2.place(x=750, y=650)

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1', command=UDK2)
                btn2.place(x=860, y=650)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band1 Histogram")

                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band2 Histogram")

                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band3 Histogram")

                ax2.legend(loc='best')

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBUDK)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=UDK1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").placepack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=UDK1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Laplacian():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Laplacian filtering. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You can use two Button "Without Diameter Direcion" and "Diameter Direction" for laplacian filtering. if you want to save output image use the "Save Filtered Image" botton.

                    """)

    def Laplacian1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Laplacian2():
                ax2.cla()

                kernel_3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')

                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band"+str(a_AverageFiltering)+ " Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(),color="magenta", label="Filtered Image Histogram(Without Diameter Direction)")

                ax1.set_title("Filtered Image(Without Diameter Direction)", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            def Laplacian4():
                ax2.cla()

                kernel_3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + " Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Filtered Image Histogram(Diameter Direction)")

                ax1.set_title("Filtered Image(Diameter Direction)", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Without Diameter Direction   ', padx=20,
                             bd='1', command=Laplacian2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Diameter Direction   ', padx=20, bd='1',
                             command=Laplacian4)
            btn3.place(x=720, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(),color="gold", label="Band"+str(a_AverageFiltering)+"Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_title("Histogram", fontsize=12, color="#333533")

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Laplacian2():
                ax2.cla()

                kernel_3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')

                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + " Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Filtered Image Histogram(Without Diameter Direction)")

                ax1.set_title("Filtered Image(Without Diameter Direction)", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            def Laplacian4():
                ax2.cla()

                kernel_3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + " Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Filtered Image Histogram(Diameter Direction)")

                ax1.set_title("Filtered Image( Diameter Direction)", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Without Diameter Direction   ', padx=20,
                             bd='1', command=Laplacian2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Diameter Direction   ', padx=20, bd='1',
                             command=Laplacian4)
            btn3.place(x=720, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBLaplacian():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)



                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def Laplacian2():
                    ax2.cla()
                    kernel_3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')

                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")

                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")

                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(1) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram(Without Diameter Direction)")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                def Laplacian4():
                    ax2.cla()

                    kernel_3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')

                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")

                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")

                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(1) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold",
                             label="Filtered Image Histogram(Diameter Direction)")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    ax2.legend(loc='best')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)
                    fig.canvas.draw_idle()

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Without Diameter Direction   ', padx=20,
                                 bd='1', command=Laplacian2)
                btn2.place(x=530, y=650)
                btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Diameter Direction   ', padx=20, bd='1',
                                 command=Laplacian4)
                btn3.place(x=720, y=650)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")

                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")

                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(1) + "Histogram")

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBLaplacian)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Laplacian1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Laplacian1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def SIE():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Simplified Image Enhancement. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You can use two Button "Without Diameter Direcion" and "Diameter Direction" for Processing. if you want to save output image use the "Save Filtered Image" botton.

                    """)


    def SIE1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def SIE2():
                ax2.cla()

                kernel_3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")


                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label= "Filtered Image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def SIE4():
                ax2.cla()

                kernel_3 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Filtered Image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Without Diameter Direction   ', padx=20,
                             bd='1', command=SIE2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Diameter Direction   ', padx=20, bd='1',
                             command=SIE4)
            btn3.place(x=720, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(a_AverageFiltering) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def SIE2():
                ax2.cla()

                kernel_3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Filtered Image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def SIE4():
                ax2.cla()

                kernel_3 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta",
                         label="Filtered Image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Without Diameter Direction   ', padx=20,
                             bd='1', command=SIE2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Diameter Direction   ', padx=20, bd='1',
                             command=SIE4)
            btn3.place(x=720, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBSIE():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def SIE2():
                    ax2.cla()
                    kernel_3 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')

                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def SIE4():
                    ax2.cla()

                    kernel_3 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter In X Direction   ', padx=20,
                                 bd='1', command=SIE2)
                btn2.place(x=530, y=650)
                btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter in Y direction   ', padx=20, bd='1',
                                 command=SIE4)
                btn3.place(x=720, y=650)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBSIE)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SIE1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SIE1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Robertz():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Robertz filtering. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You can use two Button "Filter in X Direcion" and "Filter in Y Direction" for Robertz filtering. if you want to save output image use the "Save Filtered Image" botton.

                    """)

    def Robertz1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Robertz2():
                ax2.cla()

                kernel_3 = np.array([[-1, 0], [0, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel() , color="gold", label="Band" + str(a_AverageFiltering) + "Histogram")


                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)


                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Robertz4():
                ax2.cla()

                kernel_3 = np.array([[0, -1], [1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter In X Direction   ', padx=20,
                             bd='1', command=Robertz2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter in Y direction   ', padx=20, bd='1',
                             command=Robertz4)
            btn3.place(x=720, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel() , color="gold", label="Band" + str(a_AverageFiltering) + "Histogram")
            ax2.legend(loc='best')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Robertz2():
                ax2.cla()

                kernel_3 = np.array([[-1, 0], [0, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Robertz4():
                ax2.cla()

                kernel_3 = np.array([[0, -1], [1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter In X Direction   ', padx=20,
                             bd='1', command=Robertz2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter in Y direction   ', padx=20, bd='1',
                             command=Robertz4)
            btn3.place(x=720, y=650)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBRobertz():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def Robertz2():
                    ax2.cla()
                    kernel_3 = np.array([[-1, 0], [0, 1]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')

                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                    ax2.set_title("Histogram", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Robertz4():
                    ax2.cla()

                    kernel_3 = np.array([[0, -1], [1, 0]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()


                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter In X Direction   ', padx=20,
                                 bd='1', command=Robertz2)
                btn2.place(x=530, y=650)
                btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Filter in Y direction   ', padx=20, bd='1',
                                 command=Robertz4)
                btn3.place(x=720, y=650)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBRobertz)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Robertz1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Robertz1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def Prewitt():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Prewitt filtering. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You can use four Button "Horizontal" ,"Vertical" , "NE" and "NW" for Prewitt filtering. if you want to save output image use the "Save Filtered Image" botton.

                    """)

    def Prewitt1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Prewitt2():
                ax2.cla()
                kernel_3 = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Prewitt4():
                ax2.cla()
                kernel_3 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Prewitt5():
                ax2.cla()
                kernel_3 = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Prewitt6():
                ax2.cla()
                kernel_3 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Horizontal   ', padx=20, bd='1',
                             command=Prewitt2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Vertical   ', padx=20, bd='1',
                             command=Prewitt4)
            btn3.place(x=630, y=650)
            btn21 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NE   ', padx=20, bd='1', command=Prewitt5)
            btn21.place(x=530, y=700)
            btn31 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NW   ', padx=20, bd='1', command=Prewitt6)
            btn31.place(x=630, y=700)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Prewitt2():
                ax2.cla()
                kernel_3 = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Prewitt4():
                ax2.cla()
                kernel_3 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Prewitt5():
                ax2.cla()
                kernel_3 = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Prewitt6():
                ax2.cla()
                kernel_3 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Horizontal   ', padx=20, bd='1',
                             command=Prewitt2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Vertical   ', padx=20, bd='1',
                             command=Prewitt4)
            btn3.place(x=630, y=650)
            btn21 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NE   ', padx=20, bd='1', command=Prewitt5)
            btn21.place(x=530, y=700)
            btn31 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NW   ', padx=20, bd='1', command=Prewitt6)
            btn31.place(x=630, y=700)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                     label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBPrewitt():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def Prewitt2():
                    ax2.cla()
                    kernel_3 = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Prewitt4():
                    ax2.cla()
                    kernel_3 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Prewitt5():
                    ax2.cla()
                    kernel_3 = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Prewitt6():
                    ax2.cla()
                    kernel_3 = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])
                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Horizontal   ', padx=20, bd='1',
                                 command=Prewitt2)
                btn2.place(x=530, y=650)
                btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Vertical   ', padx=20, bd='1',
                                 command=Prewitt4)
                btn3.place(x=630, y=650)
                btn21 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NE   ', padx=20, bd='1',
                                  command=Prewitt5)
                btn21.place(x=530, y=700)
                btn31 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NW   ', padx=20, bd='1',
                                  command=Prewitt6)
                btn31.place(x=630, y=700)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBPrewitt)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Prewitt1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Prewitt1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Sobel():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Sobel filtering. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You can use four Button "Horizontal" ,"Vertical" , "NE" and "NW" for Sobel filtering. if you want to save output image use the "Save Filtered Image" botton.

                    """)


    def Sobel1():
        if len(Original_image_Size) > 2:
            a_AverageFiltering = int(numberChosen1.get())
            img = Original_Image[:, :, a_AverageFiltering - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Sobel2():
                ax2.cla()

                kernel_3 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Sobel4():
                ax2.cla()

                kernel_3 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Sobel5():
                ax2.cla()

                kernel_3 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Sobel6():
                ax2.cla()

                kernel_3 = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_AverageFiltering) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Horizontal   ', padx=20, bd='1',
                             command=Sobel2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Vertical   ', padx=20, bd='1',
                             command=Sobel4)
            btn3.place(x=630, y=650)
            btn21 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NE   ', padx=20, bd='1', command=Sobel5)
            btn21.place(x=530, y=700)
            btn31 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NW   ', padx=20, bd='1', command=Sobel6)
            btn31.place(x=630, y=700)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                     label="Band" + str(a_AverageFiltering) + "Histogram")

            ax2.legend(loc='best')
            fig.canvas.draw_idle()


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Sobel2():
                ax2.cla()

                kernel_3 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Sobel4():
                ax2.cla()

                kernel_3 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Sobel5():
                ax2.cla()

                kernel_3 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            def Sobel6():
                ax2.cla()

                kernel_3 = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

                q = cv2.filter2D(img, -1, kernel_3)
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Horizontal   ', padx=20, bd='1',
                             command=Sobel2)
            btn2.place(x=530, y=650)
            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Vertical   ', padx=20, bd='1',
                             command=Sobel4)
            btn3.place(x=630, y=650)
            btn21 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NE   ', padx=20, bd='1', command=Sobel5)
            btn21.place(x=530, y=700)
            btn31 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NW   ', padx=20, bd='1', command=Sobel6)
            btn31.place(x=630, y=700)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                     label="Band" + str(1) + "Histogram")

            ax2.legend(loc='best')
            fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBSobel():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                def Sobel2():
                    ax2.cla()

                    kernel_3 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Sobel4():
                    ax2.cla()

                    kernel_3 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Sobel5():
                    ax2.cla()

                    kernel_3 = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                def Sobel6():
                    ax2.cla()

                    kernel_3 = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

                    q = cv2.filter2D(img, -1, kernel_3)
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Horizontal   ', padx=20, bd='1',
                                 command=Sobel2)
                btn2.place(x=530, y=650)
                btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Vertical   ', padx=20, bd='1',
                                 command=Sobel4)
                btn3.place(x=630, y=650)
                btn21 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NE   ', padx=20, bd='1',
                                  command=Sobel5)
                btn21.place(x=530, y=700)
                btn31 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   NW   ', padx=20, bd='1',
                                  command=Sobel6)
                btn31.place(x=630, y=700)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBSobel)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Sobel1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Sobel1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def USM():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Unsharp masking. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button or select all bands by press "All Bands" Button then You should enter kernel size in entry box and press "Apply" then control parameters by sliders. if you want to save output image use the "Save Filtered Image" botton.

                    """)


    def USM1():
        if len(Original_image_Size) > 2:
            a_USM = int(numberChosen1.get())
            img = Original_Image[:, :, a_USM - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.08, 0.78, 0.03])
            ax3_value = fig.add_axes([0.12, 0.12, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'K', 0, 30, valinit=0,color='r')
            s_time2 = Slider(ax2_value, 'Sigma X', 0, 30, valinit=0,color='g')
            s_time3 = Slider(ax3_value, 'Sigma Y', 0, 30, valinit=0,color='b')

            def USM3():
                global t1
                t1 = int(E1.get())

            def USM2(val):
                ax2.cla()
                b = cv2.GaussianBlur(img, (t1, t1), s_time2.val, s_time3.val)
                K = int(s_time1.val)
                gmask = img - b
                q = img + K * gmask
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(a_USM) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Kernel Size(odd number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=320, y=720)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=480, y=720)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1', command=USM3)
            btn2.place(x=630, y=720)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                     label="Band" + str(a_USM) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

            s_time1.on_changed(USM2)
            s_time2.on_changed(USM2)
            s_time3.on_changed(USM2)


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Histogram", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=1000, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.08, 0.78, 0.03])
            ax3_value = fig.add_axes([0.12, 0.12, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'K', 0, 30, valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Sigma X', 0, 30, valinit=0, color='g')
            s_time3 = Slider(ax3_value, 'Sigma Y', 0, 30, valinit=0, color='b')

            def USM3():
                global t1
                t1 = int(E1.get())

            def USM2(val):
                ax2.cla()
                b = cv2.GaussianBlur(img, (t1, t1), s_time2.val, s_time3.val)
                K = int(s_time1.val)
                gmask = img - b
                q = img + K * gmask
                ax1.imshow(q, cmap='gray')
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img.ravel(), color="gold",
                         label="Band" + str(1) + "Histogram")

                hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_q.ravel(), color="magenta", label="Filtered image Histogram")

                ax1.set_title("Filtered Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            L1 = tk.Label(root8, text="Kernel Size(odd number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=320, y=720)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=480, y=720)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1', command=USM3)
            btn2.place(x=630, y=720)

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.plot(range(256), hist_img.ravel(), color="gold",
                     label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')
            fig.canvas.draw_idle()

            s_time1.on_changed(USM2)
            s_time2.on_changed(USM2)
            s_time3.on_changed(USM2)

    if len(np.shape(Original_Image)) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBUSM():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Histogram", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=1000, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.08, 0.78, 0.03])
                ax3_value = fig.add_axes([0.12, 0.12, 0.78, 0.03])
                s_time1 = Slider(ax1_value, 'K', 0, 30, valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Sigma X', 0, 30, valinit=0, color='g')
                s_time3 = Slider(ax3_value, 'Sigma Y', 0, 30, valinit=0, color='b')

                def USM3():
                    global t1
                    t1 = int(E1.get())

                def USM2(val):
                    ax2.cla()
                    b = cv2.GaussianBlur(img, (t1, t1), s_time2.val, s_time3.val)
                    K = int(s_time1.val)
                    gmask = img - b
                    q = img + K * gmask
                    ax1.imshow(q, cmap='gray')
                    hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                    hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                    hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                    ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                    hist_q = cv2.calcHist([q], [0], None, [256], [0, 256])
                    ax2.plot(range(256), hist_q.ravel(), color="gold", label="Filtered Image Histogram")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    ax2.legend(loc='best')
                    fig.canvas.draw_idle()

                L1 = tk.Label(root8, text="Kernel Size(odd number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=320, y=720)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=480, y=720)

                btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1', command=USM3)
                btn2.place(x=630, y=720)

                hist_img0 = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.plot(range(256), hist_img0.ravel(), color="r", label="Band" + str(1) + "Histogram")
                hist_img1 = cv2.calcHist([img], [1], None, [256], [0, 256])
                ax2.plot(range(256), hist_img1.ravel(), color="g", label="Band" + str(2) + "Histogram")
                hist_img2 = cv2.calcHist([img], [2], None, [256], [0, 256])
                ax2.plot(range(256), hist_img2.ravel(), color="b", label="Band" + str(3) + "Histogram")

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

                s_time1.on_changed(USM2)
                s_time2.on_changed(USM2)
                s_time3.on_changed(USM2)

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBUSM)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=USM1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=USM1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def SAP():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for add nise to image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can control salt and pepper by slider. if you want to save noisy image you can use "save noisy image"
                    """)


    def SAP1():
        if len(Original_image_Size) > 2:
            a_SAP = int(numberChosen1.get())
            img = Original_Image[:, :, a_SAP - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)



            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img,cmap='gray')


            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Salt:', 0, 1, valinit=0,color='r')

            channel_2 = np.atleast_1d(img)
            noisy = np.zeros_like(channel_2)

            def update(val):

                s_and_p = np.random.rand(img.shape[0], img.shape[1])
                salt = s_and_p > s_time1.val
                pepper = s_and_p < 1 - s_time1.val
                for i in range(channel_2.shape[0] * channel_2.shape[1]):
                    if salt.ravel()[i] == 1:
                        noisy.ravel()[i] = 255
                    elif pepper.ravel()[i] == 1:
                        noisy.ravel()[i] = 0
                    else:
                        noisy.ravel()[i] = channel_2.ravel()[i]

                ax2.imshow(noisy, cmap='gray')

                S = s_time1.val
                P = 1 - s_time1.val
                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Noisy Image(Salt="+str(S)+",Pepper="+str(P), fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', noisy)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Noisy Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Salt:', 0, 1, valinit=0, color='r')

            channel_2 = np.atleast_1d(img)
            noisy = np.zeros_like(channel_2)

            def update(val):

                s_and_p = np.random.rand(img.shape[0], img.shape[1])
                salt = s_and_p > s_time1.val
                pepper = s_and_p < 1 - s_time1.val
                for i in range(channel_2.shape[0] * channel_2.shape[1]):
                    if salt.ravel()[i] == 1:
                        noisy.ravel()[i] = 255
                    elif pepper.ravel()[i] == 1:
                        noisy.ravel()[i] = 0
                    else:
                        noisy.ravel()[i] = channel_2.ravel()[i]

                ax2.imshow(noisy, cmap='gray')

                S = s_time1.val
                P = 1 - s_time1.val
                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Noisy Image(Salt=" + str(S) + ",Pepper=" + str(P), fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', noisy)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Noisy Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SAP1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SAP1)
        btn1.pack(anchor='w')





    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def GNoise():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for add nise to image. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can control gaussian noise parameters by sliders. if you want to save noisy image you can use "save noisy image"
                    """)

    def GNoise1():
        if len(Original_image_Size) > 2:
            a_GNoise = int(numberChosen1.get())
            img = Original_Image[:, :, a_GNoise - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Mean:', 0, 200, valinit=0,color='r')

            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Sigma:', 0, 200, valinit=0,color='g')

            def update(val):

                gauss_noise = np.random.normal(s_time1.val, s_time2.val, (img.shape[0], img.shape[1]))

                g_noisy = img + gauss_noise

                ax2.imshow(g_noisy, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Noisy Image", fontsize=12, color="#333533")


                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', g_noisy)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Noisy   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Mean:', 0, 200, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Sigma:', 0, 200, valinit=0, color='g')

            def update(val):

                gauss_noise = np.random.normal(s_time1.val, s_time2.val, (img.shape[0], img.shape[1]))

                g_noisy = img + gauss_noise

                ax2.imshow(g_noisy, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Noisy Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', g_noisy)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Noisy Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=GNoise1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=GNoise1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Wrap():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image padding. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can control pading parameters by sliders. if you want to save noisy image you can use "save padded image"
                    """)

    def Wrap1():
        if len(Original_image_Size) > 2:
            a_Wrap = int(numberChosen1.get())
            img = Original_Image[:, :, a_Wrap - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0,color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0,color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0,color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0,color='gold')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_WRAP)
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_WRAP)
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBWrap():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')
                ax2.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
                s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

                ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
                s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

                ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
                s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

                ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

                def update(val):
                    q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                           cv2.BORDER_WRAP)
                    ax2.imshow(q, cmap='gray')

                    ax1.set_title("Original Image", fontsize=12, color="#333533")
                    ax2.set_title("Padded Image", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(update)
                s_time2.on_changed(update)
                s_time3.on_changed(update)
                s_time4.on_changed(update)

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBWrap)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=Wrap1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Wrap1)
        btn1.pack(anchor='w')




    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def Reflect():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image padding. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can control pading parameters by sliders. if you want to save noisy image you can use "save padded image"
                    """)

    def Reflect1():
        if len(Original_image_Size) > 2:
            a_Reflect = int(numberChosen1.get())
            img = Original_Image[:, :, a_Reflect - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')


            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_REFLECT)
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_REFLECT)
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBReflect():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')
                ax2.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
                s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

                ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
                s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

                ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
                s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

                ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

                def update(val):
                    q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                           cv2.BORDER_REFLECT)
                    ax2.imshow(q, cmap='gray')

                    ax1.set_title("Original Image", fontsize=12, color="#333533")
                    ax2.set_title("Padded Image", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(update)
                s_time2.on_changed(update)
                s_time3.on_changed(update)
                s_time4.on_changed(update)

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBReflect)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Reflect1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Reflect1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Replicate():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.placepack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image padding. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can control pading parameters by sliders. if you want to save noisy image you can use "save padded image"
                    """)

    def Replicate1():
        if len(Original_image_Size) > 2:
            a_Reflect = int(numberChosen1.get())
            img = Original_Image[:, :, a_Reflect - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_REPLICATE)
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_REPLICATE)
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBReplicate():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')
                ax2.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
                s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

                ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
                s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

                ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
                s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

                ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

                def update(val):
                    q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                           cv2.BORDER_REPLICATE)
                    ax2.imshow(q, cmap='gray')

                    ax1.set_title("Original Image", fontsize=12, color="#333533")
                    ax2.set_title("Padded Image", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(update)
                s_time2.on_changed(update)
                s_time3.on_changed(update)
                s_time4.on_changed(update)

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBReplicate)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Replicate1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Replicate1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Constant():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image padding. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then You can control pading parameters by sliders. if you want to save noisy image you can use "save padded image"
                    """)

    def Constant1():
        if len(Original_image_Size) > 2:
            a_Reflect = int(numberChosen1.get())
            img = Original_Image[:, :, a_Reflect - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

            ax5_value = fig.add_axes([0.12, 0.13, 0.78, 0.03])
            s_time5 = Slider(ax5_value, 'Constant:', 0, 255, valinit=0,color='magenta')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_CONSTANT, int(s_time5.val))
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)
            s_time5.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

            ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

            ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
            s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

            ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

            ax5_value = fig.add_axes([0.12, 0.13, 0.78, 0.03])
            s_time5 = Slider(ax5_value, 'Constant:', 0, 255, valinit=0, color='magenta')

            def update(val):
                q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                       cv2.BORDER_CONSTANT, int(s_time5.val))
                ax2.imshow(q, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Padded Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)
            s_time3.on_changed(update)
            s_time4.on_changed(update)
            s_time5.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        if len(Original_image_Size) == 3:
            def RGBConstant():
                img = Original_Image
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')
                ax2.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.01, 0.78, 0.03])
                s_time1 = Slider(ax1_value, 'Top:', 0, 500, valinit=0, color='r')

                ax2_value = fig.add_axes([0.12, 0.04, 0.78, 0.03])
                s_time2 = Slider(ax2_value, 'Right:', 0, 500, valinit=0, color='g')

                ax3_value = fig.add_axes([0.12, 0.07, 0.78, 0.03])
                s_time3 = Slider(ax3_value, 'Bottom:', 0, 500, valinit=0, color='b')

                ax4_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                s_time4 = Slider(ax4_value, 'Left:', 0, 500, valinit=0, color='gold')

                ax5_value = fig.add_axes([0.12, 0.13, 0.78, 0.03])
                s_time5 = Slider(ax5_value, 'Constant:', 0, 255, valinit=0, color='magenta')

                def update(val):
                    q = cv2.copyMakeBorder(img, int(s_time1.val), int(s_time3.val), int(s_time4.val), int(s_time2.val),
                                           cv2.BORDER_CONSTANT, int(s_time5.val))
                    ax2.imshow(q, cmap='gray')

                    ax1.set_title("Original Image", fontsize=12, color="#333533")
                    ax2.set_title("Padded Image", fontsize=12, color="#333533")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Padded Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(update)
                s_time2.on_changed(update)
                s_time3.on_changed(update)
                s_time4.on_changed(update)
                s_time5.on_changed(update)

            btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   All Band   ', padx=20, bd='5',
                            command=RGBConstant)
            btn.pack(anchor='w')
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Constant1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Constant1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def IFT():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image fourier transform. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can use slider to fix a constant value for logarithm transform. if you want to save fourier image you can use "save  fourier Image" buttons.
                    """)

    def IFT1():
        if len(Original_image_Size) > 2:
            a_GNoise = int(numberChosen1.get())
            img = Original_Image[:, :, a_GNoise - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(223)
            ax4 = fig.add_subplot(224)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Foutier Transform Without Shift", fontsize=12, color="#333533")

            ax3.set_title("Foutier Transform", fontsize=12, color="#333533")
            ax4.set_title("Foutier Transform", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            a1 = np.log(np.abs(f))
            a2 = np.log(np.abs(fshift))

            ax1.imshow(img, cmap='gray')
            ax2.imshow(a1, cmap='gray')
            ax3.imshow(a2, cmap='gray')
            ax4.imshow(a2, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Constant:', 0, 200, valinit=0,color='r')

            def update(val):
                q1 = s_time1.val * np.log1p(1 + fshift, dtype=complex)
                q1 = np.uint8(q1)

                q2 = s_time1.val * np.log1p(1 + f, dtype=complex)
                q2 = np.uint8(q2)

                ax2.imshow(q2, cmap='gray')
                ax4.imshow(q1, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Fourier Transform Without Shift(By logarithm Transformatin)", fontsize=12, color="#333533")

                ax3.set_title("Fourier Transform", fontsize=12, color="#333533")
                ax4.set_title("Fourier Transform(By logarithm Transformation)", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q1)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image(without shift)   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=0)


                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q2)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=720)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(223)
            ax4 = fig.add_subplot(224)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Foutier Transform Without Shift", fontsize=12, color="#333533")

            ax3.set_title("Foutier Transform", fontsize=12, color="#333533")
            ax4.set_title("Foutier Transform", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            a1 = np.log(np.abs(f))
            a2 = np.log(np.abs(fshift))

            ax1.imshow(img, cmap='gray')
            ax2.imshow(a1, cmap='gray')
            ax3.imshow(a2, cmap='gray')
            ax4.imshow(a2, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Constant:', 0, 200, valinit=0, color='r')

            def update(val):
                q1 = s_time1.val * np.log1p(1 + fshift, dtype=complex)
                q1 = np.uint8(q1)

                q2 = s_time1.val * np.log1p(1 + f, dtype=complex)
                q2 = np.uint8(q2)

                ax2.imshow(q2, cmap='gray')
                ax4.imshow(q1, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Fourier Transform Without Shift(By logarithm Transformatin)", fontsize=12,
                              color="#333533")

                ax3.set_title("Fourier Transform", fontsize=12, color="#333533")
                ax4.set_title("Fourier Transform(By logarithm Transformation)", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q1)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image(without shift)   ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=0)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q2)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=720)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=IFT1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=IFT1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def HPF():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image fourier transform. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select an area by drawing shape on fourier image then process will be done. if you want to save fourier image you can use "save  filtered Image" button.
                    """)



    def HPF1():
        if len(Original_image_Size) > 2:
            a_HPF = int(numberChosen1.get())
            img = Original_Image[:, :, a_HPF - 1]

            def onselect(verts):
                p = path.Path(verts)
                ind = p.contains_points(v)
                fshift.flat[ind] = 0
                f_ishift = np.fft.ifftshift(fshift)
                img_back = np.fft.ifft2(f_ishift)
                img_back = np.abs(img_back)

                ax2.imshow(img_back, cmap='gray')

                ax2.set_title("Filtered Image", fontsize=12, color="#333533")
                ax1.set_title("Foutier Transform ", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img_back)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)


                fig.canvas.draw_idle()

            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = np.log(np.abs(fshift))

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax1.imshow(magnitude_spectrum, cmap='gray')

            ax2 = fig.add_subplot(122)
            ax2.imshow(img, cmap='gray')

            ax2.set_title("Original Image", fontsize=12, color="#333533")
            ax1.set_title("Foutier Transform ", fontsize=12, color="#333533")



            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            lasso = LassoSelector(ax1, onselect)

            length_y = img.shape[0]  # Number of rows
            length_x = img.shape[1]  # Number of cols
            v = np.zeros((length_x * length_y, 2), dtype=np.int)  # Creates zero array

            # For y
            a = np.array(range(0, length_x))
            y = np.tile(a, length_y)

            # For x
            b = np.array(range(0, length_y))
            x = np.repeat(b, length_x)

            v[:, 0] = x
            v[:, 1] = y

            root8.mainloop()

        else:
            img = Original_Image

            def onselect(verts):
                p = path.Path(verts)
                ind = p.contains_points(v)
                fshift.flat[ind] = 0
                f_ishift = np.fft.ifftshift(fshift)
                img_back = np.fft.ifft2(f_ishift)
                img_back = np.abs(img_back)

                ax2.imshow(img_back, cmap='gray')

                ax2.set_title("Filtered Image", fontsize=12, color="#333533")
                ax1.set_title("Foutier Transform ", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img_back)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Filtered Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = np.log(np.abs(fshift))

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax1.imshow(magnitude_spectrum, cmap='gray')

            ax2 = fig.add_subplot(122)
            ax2.imshow(img, cmap='gray')

            ax2.set_title("Original Image", fontsize=12, color="#333533")
            ax1.set_title("Foutier Transform ", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            lasso = LassoSelector(ax1, onselect)

            length_y = img.shape[0]  # Number of rows
            length_x = img.shape[1]  # Number of cols
            v = np.zeros((length_x * length_y, 2), dtype=np.int)  # Creates zero array

            # For y
            a = np.array(range(0, length_x))
            y = np.tile(a, length_y)

            # For x
            b = np.array(range(0, length_y))
            x = np.repeat(b, length_x)

            v[:, 0] = x
            v[:, 1] = y

            root8.mainloop()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=HPF1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=HPF1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()




def LPFMask():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image fourier transform. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can use slider to fix a constant value for logarithm transform. if you want to save fourier image you can use "save  fourier Image" buttons.
                    """)

    def LPFMask1():
        if len(Original_image_Size) > 2:
            a_LPFMask = int(numberChosen1.get())
            img = Original_Image[:, :, a_LPFMask - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(223)
            ax4 = fig.add_subplot(224)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Foutier Transform Without Shift", fontsize=12, color="#333533")

            ax3.set_title("Foutier Transform", fontsize=12, color="#333533")
            ax4.set_title("Foutier Transform", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax2.imshow(img, cmap='gray')

            ax3.imshow(img, cmap='gray')

            ax4.imshow(img, cmap='gray')


            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Constant:', 0,  int(img.shape[0]/2), valinit=0,color='r')

            def update(val):
                dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
                dft_shift = np.fft.fftshift(dft)

                magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)  # center

                # Circular LPF mask, center circle is 1, remaining all zeros
                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)

                mask = np.zeros((rows, cols, 2), np.uint8)
                r = s_time1.val
                center = [crow, ccol]
                x, y = np.ogrid[:rows, :cols]
                mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
                mask[mask_area] = 1

                # apply mask and inverse DFT
                fshift = dft_shift * mask
                ax3.cla()

                fshift_mask_mag = 2000 * np.log10(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

                f_ishift = np.fft.ifftshift(fshift)
                img_back = cv2.idft(f_ishift)
                img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

                ax1.imshow(img, cmap='gray')

                ax2.imshow(magnitude_spectrum, cmap='gray')

                ax3.imshow(fshift_mask_mag, cmap='gray')

                ax4.imshow(img_back, cmap='gray')


                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("After FFT", fontsize=12,
                              color="#333533")

                ax3.set_title("FFT + Mask", fontsize=12, color="#333533")
                ax4.set_title("After FFT Inverse", fontsize=12, color="#333533")




                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img_back)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=720)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(223)
            ax4 = fig.add_subplot(224)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Foutier Transform Without Shift", fontsize=12, color="#333533")

            ax3.set_title("Foutier Transform", fontsize=12, color="#333533")
            ax4.set_title("Foutier Transform", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax2.imshow(img, cmap='gray')

            ax3.imshow(img, cmap='gray')

            ax4.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'Constant:', 0, int(img.shape[0] / 2), valinit=0, color='r')

            def update(val):
                dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
                dft_shift = np.fft.fftshift(dft)

                magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)  # center

                # Circular LPF mask, center circle is 1, remaining all zeros
                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)

                mask = np.zeros((rows, cols, 2), np.uint8)
                r = s_time1.val
                center = [crow, ccol]
                x, y = np.ogrid[:rows, :cols]
                mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
                mask[mask_area] = 1

                # apply mask and inverse DFT
                fshift = dft_shift * mask
                ax3.cla()

                fshift_mask_mag = 2000 * np.log10(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

                f_ishift = np.fft.ifftshift(fshift)
                img_back = cv2.idft(f_ishift)
                img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

                ax1.imshow(img, cmap='gray')

                ax2.imshow(magnitude_spectrum, cmap='gray')

                ax3.imshow(fshift_mask_mag, cmap='gray')

                ax4.imshow(img_back, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("After FFT", fontsize=12,
                              color="#333533")

                ax3.set_title("FFT + Mask", fontsize=12, color="#333533")
                ax4.set_title("After FFT Inverse", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img_back)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=720)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=LPFMask1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=LPFMask1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()




def HPFMask():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image fourier transform. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can use slider to fix a constant value for logarithm transform. if you want to save fourier image you can use "save  fourier Image" buttons.
                    """)

    def HPFMask1():
        if len(Original_image_Size) > 2:
            a_HPFMask = int(numberChosen1.get())
            img = Original_Image[:, :, a_HPFMask - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(223)
            ax4 = fig.add_subplot(224)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Foutier Transform Without Shift", fontsize=12, color="#333533")

            ax3.set_title("Foutier Transform", fontsize=12, color="#333533")
            ax4.set_title("Foutier Transform", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax2.imshow(img, cmap='gray')

            ax3.imshow(img, cmap='gray')

            ax4.imshow(img, cmap='gray')


            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'R(in):', 0,  int(img.shape[0]/2), valinit=0,color='r')
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'R(Out):', 0, int(img.shape[0] / 2), valinit=0, color='r')

            def update(val):
                dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
                dft_shift = np.fft.fftshift(dft)
                ax3.cla()
                magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)  # center

                # Concentric BPF mask,with are between the two cerciles as one's, rest all zero's.
                rows, cols = img.shape
                crow = int(rows / 2)
                ccol = int(cols / 2)

                mask = np.zeros((rows, cols, 2), np.uint8)


                r_in = int(s_time1.val)
                r_out = int(s_time2.val)

                center = [crow, ccol]
                x, y = np.ogrid[:rows, :cols]

                mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                                           ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
                mask[mask_area] = 1

                # apply mask and inverse DFT
                fshift = dft_shift * mask

                fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

                f_ishift = np.fft.ifftshift(fshift)
                img_back = cv2.idft(f_ishift)
                img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

                ax1.imshow(img, cmap='gray')

                ax2.imshow(magnitude_spectrum, cmap='gray')

                ax3.imshow(fshift_mask_mag, cmap='gray')

                ax4.imshow(img_back, cmap='gray')


                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("After FFT", fontsize=12,
                              color="#333533")

                ax3.set_title("FFT + Mask", fontsize=12, color="#333533")
                ax4.set_title("After FFT Inverse", fontsize=12, color="#333533")




                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img_back)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=720)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(221)
            ax2 = fig.add_subplot(222)
            ax3 = fig.add_subplot(223)
            ax4 = fig.add_subplot(224)

            ax1.set_title("Original Image", fontsize=12, color="#333533")
            ax2.set_title("Foutier Transform Without Shift", fontsize=12, color="#333533")

            ax3.set_title("Foutier Transform", fontsize=12, color="#333533")
            ax4.set_title("Foutier Transform", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax2.imshow(img, cmap='gray')

            ax3.imshow(img, cmap='gray')

            ax4.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            s_time1 = Slider(ax1_value, 'R(in):', 0, int(img.shape[0] / 2), valinit=0, color='r')
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])
            s_time2 = Slider(ax2_value, 'R(Out):', 0, int(img.shape[0] / 2), valinit=0, color='r')

            def update(val):
                dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
                dft_shift = np.fft.fftshift(dft)
                ax3.cla()
                magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

                rows, cols = img.shape
                crow, ccol = int(rows / 2), int(cols / 2)  # center

                # Concentric BPF mask,with are between the two cerciles as one's, rest all zero's.
                rows, cols = img.shape
                crow = int(rows / 2)
                ccol = int(cols / 2)

                mask = np.zeros((rows, cols, 2), np.uint8)

                r_in = int(s_time1.val)
                r_out = int(s_time2.val)

                center = [crow, ccol]
                x, y = np.ogrid[:rows, :cols]

                mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                                           ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
                mask[mask_area] = 1

                # apply mask and inverse DFT
                fshift = dft_shift * mask

                fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

                f_ishift = np.fft.ifftshift(fshift)
                img_back = cv2.idft(f_ishift)
                img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

                ax1.imshow(img, cmap='gray')

                ax2.imshow(magnitude_spectrum, cmap='gray')

                ax3.imshow(fshift_mask_mag, cmap='gray')

                ax4.imshow(img_back, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("After FFT", fontsize=12,
                              color="#333533")

                ax3.set_title("FFT + Mask", fontsize=12, color="#333533")
                ax4.set_title("After FFT Inverse", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img_back)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Fourier Image   ', padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1100, y=720)

                fig.canvas.draw_idle()

            s_time1.on_changed(update)
            s_time2.on_changed(update)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=HPFMask1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=HPFMask1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()




def Sequential():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for icolor image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)

    def Sequential1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.title("Original Image")
            plt.colorbar()

            course = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map="+cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)




        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")

            plt.colorbar()

            course = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Sequential1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Sequential1)
        btn1.pack(anchor='w')




    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Sequential2():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for color image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)

    def Sequential21():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                      'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                      'hot', 'afmhot', 'gist_heat', 'copper']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)




        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
                      'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                      'hot', 'afmhot', 'gist_heat', 'copper']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Sequential21)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Sequential21)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Diverging():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for color image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)



    def Diverging1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                      'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)




        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                      'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)



    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Diverging1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Diverging1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Cyclic():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for color image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)




    def Cyclic1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['twilight', 'twilight_shifted', 'hsv']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)


                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)






        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['twilight', 'twilight_shifted', 'hsv']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)



    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Cyclic1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Cyclic1)
        btn1.pack(anchor='w')




    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Qualitative():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for color image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)



    def Qualitative1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                      'Dark2', 'Set1', 'Set2', 'Set3',
                      'tab10', 'tab20', 'tab20b', 'tab20c']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)




        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                      'Dark2', 'Set1', 'Set2', 'Set3',
                      'tab10', 'tab20', 'tab20b', 'tab20c']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)



    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Qualitative1)
        btn.placepack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Qualitative1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Miscellaneouse():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for color image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)



    def Miscellaneouse1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                      'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
                      'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)




        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                      'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
                      'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Miscellaneouse1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Miscellaneouse1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def PUS():
    root8 = tk.Tk()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for color image processing. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can select special color from the list and then press "Set" Button. if you want to save fourier image you can use "save  output Image" button.
                    """)


    def PUS1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]

            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)




        else:
            img = Original_Image
            fig = plt.figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.draw()
            canvas.get_tk_widget().place(x=200, y=0)

            color_map = plt.imshow(img, cmap="gray")
            plt.colorbar()

            course = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
            cb = ttk.Combobox(root8, values=course, width=10)
            cb.place(x=0, y=200)

            def ColorPr():
                fig = plt.figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.draw()
                canvas.get_tk_widget().place(x=200, y=0)
                color_map = plt.imshow(img, cmap=cb.get())
                plt.title("color map=" + cb.get())
                plt.colorbar()

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=800, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save output Image  ',
                                 padx=20,
                                 bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

            butn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=ColorPr)
            butn.place(x=0, y=300)
            plt.title("Original Image")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=800, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)



    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=PUS1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=PUS1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def Erosion():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save fourier image you can use "save  erroded Image" button.
                    """)



    def Erosion1():
        if len(Original_image_Size) > 2:
            a_Sequential = int(numberChosen1.get())
            img = Original_Image[:, :, a_Sequential - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')


            def Erosion2():
                root9 = tk.Tk()
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Erosion3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))
                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))


                    q = cv2.erode(img, Kernel, iterations=1)
                    ax2.imshow(q, cmap='gray')

                    ax2.set_title("Eroded Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Erodded Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)


                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Erosion3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Erosion2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Erosion2():
                root9 = tk.Tk()
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Erosion3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))
                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.erode(img, Kernel, iterations=1)
                    ax2.imshow(q, cmap='gray')

                    ax2.set_title("Eroded Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Erodded Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Erosion3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Erosion2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Erosion1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Erosion1)
        btn1.pack(anchor='w')
    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()

def Dilation():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save fourier image you can use "save  dilated Image" button.
                    """)


    def Dilation1():
        if len(Original_image_Size) > 2:
            a_Dilation = int(numberChosen1.get())
            img = Original_Image[:, :, a_Dilation - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Dilation2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Dilation3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.dilate(img, Kernel, iterations=1)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Dilated Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Dilated Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Dilation3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Dilation2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Dilation2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Dilation3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.dilate(img, Kernel, iterations=1)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Dilated Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Dilated Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Dilation3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Dilation2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Dilation1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Dilation1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')
    root8.mainloop()


def Opening():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save fourier image you can use "save  opening Image" button.
                    """)



    def Opening1():
        if len(Original_image_Size) > 2:
            a_Dilation = int(numberChosen1.get())
            img = Original_Image[:, :, a_Dilation - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Opening2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Opening3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_OPEN, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Opening")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Opening Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Opening3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Opening2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Opening2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Opening3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_OPEN, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Opening")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Opening Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Opening3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Opening2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Opening1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Opening1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()

def MG():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save fourier image you can use "save  Morphological gradient Image" button.
                    """)



    def MG1():
        if len(Original_image_Size) > 2:
            a_Closing = int(numberChosen1.get())
            img = Original_Image[:, :, a_Closing - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def MG2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def MG3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Morphological Gradient")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Morphological Gradient Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=MG3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=MG2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def MG2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def MG3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Morphological Gradient")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Morphological Gradient Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=MG3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=MG2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=MG1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=MG1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Closing():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.placepack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save fourier image you can use "save  closing Image" button.
                    """)


    def Closing1():
        if len(Original_image_Size) > 2:
            a_Closing = int(numberChosen1.get())
            img = Original_Image[:, :, a_Closing - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Closing2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Closing3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_CLOSE, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Closing")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Closing Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Closing3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Closing2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def Closing2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def Closing3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_CLOSE, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Closing")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Closing Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=Closing3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=Closing2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Closing1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Closing1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def TH():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save output image you can use "save  Top hat Image" button.
                    """)



    def TH1():
        if len(Original_image_Size) > 2:
            a_TH = int(numberChosen1.get())
            img = Original_Image[:, :, a_TH - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def TH2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def TH3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Top Hat")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Top Hat Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=TH3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=TH2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def TH2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def TH3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Top Hat")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Top Hat Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=TH3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=TH2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=TH1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=TH1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def BH():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save output image you can use "save  black hat Image" button.
                    """)


    def BH1():
        if len(Original_image_Size) > 2:
            a_TH = int(numberChosen1.get())
            img = Original_Image[:, :, a_TH - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def BH2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def BH3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Black Hat")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Black Hat Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=BH3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=BH2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def BH2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def BH3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))

                    q = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, Kernel)
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Black Hat")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Black Hat Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=BH3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=BH2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=BH1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=BH1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def BE():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save output image you can use "save  Boundary Extraction Image" button.
                    """)



    def BE1():
        if len(Original_image_Size) > 2:
            a_BE = int(numberChosen1.get())
            img = Original_Image[:, :, a_BE - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def BE2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def BE3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))
                    erosion = cv2.erode(img, Kernel, iterations=1)
                    q = img - erosion
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Boundary Extracion")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Boundary Extraction Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=BE3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=BE2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')


        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            def BE2():
                root9 = tk.Tk()

                root9.configure(background='white')
                root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                ax2.cla()
                height = int(E1.get())
                width = int(E2.get())
                rows = []
                for i in range(height):  # Rows
                    cols = []
                    for j in range(width):  # Columns
                        b = tk.Entry(root9, text="")
                        b.grid(row=i, column=j)
                        cols.append(b)
                    rows.append(cols)

                def BE3():
                    global Kernel
                    Kernel = []
                    for row in rows:
                        for col in row:
                            Kernel.append(float(col.get()))

                    Kernel = np.array(Kernel, np.uint8)
                    Kernel = np.reshape(Kernel, (height, width))
                    erosion = cv2.erode(img, Kernel, iterations=1)
                    q = img - erosion
                    ax2.imshow(q, cmap='gray')
                    ax2.set_title("Boundary Extracion")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Boundary Extraction Image  ',
                                     padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=1000, y=0)

                    fig.canvas.draw_idle()

                btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                 command=BE3)
                btn1.grid(row=height + 1, column=0)
                root9.mainloop()

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=900, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            L1 = tk.Label(root8, text="Rows:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=400, y=650)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=440, y=650)

            L2 = tk.Label(root8, text="Column:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=570, y=650)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=630, y=650)

            btn2 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Apply   ', padx=20, bd='1',
                             command=BE2)
            btn2.place(x=730, y=650)

            ax2.imshow(img, cmap='gray')
            ax2.set_title('Original Image')
            ax1.set_title('Original Image')

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=BE1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=BE1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Skel():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Morphological operations. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you should enter size of kernel and then press "Apply" Button then a matrix will be appears that you should fill it then press "Set" button. if you want to save output image you can use "save  Skeletonize Image" button.
                    """)



    def Skel1():
        if len(Original_image_Size) > 2:
            a_BE = int(numberChosen1.get())
            img = Original_Image[:, :, a_BE - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            size = np.size(img)
            skel = np.zeros(img.shape, np.uint8)

            ret, img = cv2.threshold(img, 127, 255, 0)
            element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            done = False

            while (not done):
                eroded = cv2.erode(img, element)
                temp = cv2.dilate(eroded, element)
                temp = cv2.subtract(img, temp)
                skel = cv2.bitwise_or(skel, temp)
                img = eroded.copy()

                zeros = size - cv2.countNonZero(img)
                if zeros == size:
                    done = True

            ax2.imshow(skel, cmap='gray')
            ax2.set_title('Skeletonize')
            ax1.set_title('Original Image')

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=600, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', skel)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Skel Image  ',
                             padx=20,
                             bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            size = np.size(img)
            skel = np.zeros(img.shape, np.uint8)

            ret, img = cv2.threshold(img, 127, 255, 0)
            element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
            done = False

            while (not done):
                eroded = cv2.erode(img, element)
                temp = cv2.dilate(eroded, element)
                temp = cv2.subtract(img, temp)
                skel = cv2.bitwise_or(skel, temp)
                img = eroded.copy()

                zeros = size - cv2.countNonZero(img)
                if zeros == size:
                    done = True

            ax2.imshow(skel, cmap='gray')
            ax2.set_title('Skeletonize')
            ax1.set_title('Original Image')

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=600, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', skel)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Skel Image  ',
                             padx=20,
                             bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=Skel1)
        btn.pack(anchor='w')
    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Skel1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def Canny():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for Image segmantation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then you can control Canny Parametrs by sliders. if you want to save output image you can use "save  Segmented Image" button.
                    """)



    def Canny1():
        if len(Original_image_Size) > 2:
            a_Canny = int(numberChosen1.get())
            img = Original_Image[:, :, a_Canny - 1]
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)



            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=670)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

            s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')



            def Canny2(val):
                ax2.cla()
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_Canny)+"Histogram")

                ax2.axvline(x=int(s_time1.val), color='r',label="Minimum")
                ax2.axvline(x=int(s_time2.val), color='g',label="Maximum")

                ax2.legend(loc='best')

                q = cv2.Canny(img, int(s_time1.val), int(s_time2.val))
                ax1.imshow(q, cmap='gray')





                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_Canny)+"Histogram")

            ax2.legend(loc='best')

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', q)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Segmented Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=400, y=0)

            s_time1.on_changed(Canny2)
            s_time2.on_changed(Canny2)



        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=670)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

            s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

            def Canny2(val):
                ax2.cla()
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")

                ax2.axvline(x=int(s_time1.val), color='r', label="Minimum")
                ax2.axvline(x=int(s_time2.val), color='g', label="Maximum")

                ax2.legend(loc='best')

                q = cv2.Canny(img, int(s_time1.val), int(s_time2.val))
                ax1.imshow(q, cmap='gray')
                global q1
                q1=q

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")

            ax2.legend(loc='best')

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', q1)
                f.close()

            btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Segmented Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=400, y=0)

            s_time1.on_changed(Canny2)
            s_time2.on_changed(Canny2)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Canny1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Canny1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def MT():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then appears five buttons that specific that kind of tresholding select one of them and then you can control tresholding parameters ny sliders. if you want to save output image you can use "save  segmented Image" button.
                    """)



    def MT1():
        if len(Original_image_Size) > 2:
            a_ST = int(numberChosen1.get())
            img = Original_Image[:, :, a_ST - 1]

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)



            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=670)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(img,cmap='gray')
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_ST)+"Histogram")
            ax2.legend(loc='best')

            def BT():




                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0,color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0,color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r',label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g',label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')

                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_BINARY)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()


                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def BTI():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')



                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_BINARY_INV)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()


                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def TRUNC():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')


                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_TRUNC)
                    ax1.imshow(q, cmap='gray')


                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()


                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def TOZERO():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')


                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_TOZERO)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()


                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def TOZERO_INV():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')




                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_TOZERO_INV)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()


                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            btn5 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Binary Tresholding   ', padx=20, bd='5',
                             command=BT)
            btn5.place(x=0, y=100)
            btn6 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Inverse Binary Tresholding   ', padx=20,
                             bd='5', command=BTI)
            btn6.place(x=0, y=130)
            btn7 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Trunic Tresholding   ', padx=20, bd='5',
                             command=TRUNC)
            btn7.place(x=0, y=160)
            btn8 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   To zero Tresholding   ', padx=20, bd='5',
                             command=TOZERO)
            btn8.place(x=0, y=190)
            btn8 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Inverse To zero Tresholding   ', padx=20,
                             bd='5', command=TOZERO_INV)
            btn8.place(x=0, y=220)

        else:
            img = Original_Image
            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            fig.subplots_adjust(bottom=0.25)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=670)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(img, cmap='gray')
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')

            def BT():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")

                    ax2.legend(loc='best')

                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_BINARY)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def BTI():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')

                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_BINARY_INV)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def TRUNC():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')

                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_TRUNC)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def TOZERO():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')

                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_TOZERO)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def TOZERO_INV():

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()

                    ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                    ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                    ax2.set_facecolor("#2E2E2E")

                    ax2.set_title("Histogram", fontsize=12, color="#333533")
                    ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                    ax2.axvline(x=int(s_time1.val), color='r', label='Minimum')
                    ax2.axvline(x=int(s_time2.val), color='g', label='Maximum')

                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(a_ST) + "Histogram")

                    ax2.legend(loc='best')

                    ret, q = cv2.threshold(img, int(s_time1.val), int(s_time2.val), cv2.THRESH_TOZERO_INV)
                    ax1.imshow(q, cmap='gray')

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            btn5 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Binary Tresholding   ', padx=20, bd='5',
                             command=BT)
            btn5.place(x=0, y=100)
            btn6 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Inverse Binary Tresholding   ', padx=20,
                             bd='5', command=BTI)
            btn6.place(x=0, y=130)
            btn7 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Trunic Tresholding   ', padx=20, bd='5',
                             command=TRUNC)
            btn7.place(x=0, y=160)
            btn8 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   To zero Tresholding   ', padx=20, bd='5',
                             command=TOZERO)
            btn8.place(x=0, y=190)
            btn8 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Inverse To zero Tresholding   ', padx=20,
                             bd='5', command=TOZERO_INV)
            btn8.place(x=0, y=220)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=MT1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=MT1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')



    root8.mainloop()


def AT():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then appears two buttons that specific that kind of tresholding select one of them and enter block size and then you can control tresholding parameters ny sliders. if you want to save output image you can use "save  segmented Image" button.
                    """)



    def AT1():
        if len(Original_image_Size) > 2:
            a_AT = int(numberChosen1.get())
            img = Original_Image[:, :, a_AT - 1]

            def BT():
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=700)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Constant', 0, 20, valinit=1,color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0,color='g')

                def Canny2(val):
                    ax2.cla()
                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                            label="Band" + str(a_AT) + "Histogram")
                    ax2.axvline(x=int(s_time2.val), color='r',label="Maximum")
                    ax2.legend(loc='best')

                    q = cv2.adaptiveThreshold(img, int(s_time2.val), cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                              int(E1.get()), int(s_time1.val))
                    ax1.imshow(q, cmap='gray')
                    ax1.set_title("Segmented Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                        label="Band" + str(a_AT) + "Histogram")

                L1 = tk.Label(root8, text="Block Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=230, y=700)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=360, y=700)

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def BTI():
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=700)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Constant', 0, 20, valinit=1, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')


                def Canny2(val):
                    ax2.cla()
                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                            label="Band" + str(a_AT) + "Histogram")
                    ax2.axvline(x=int(s_time2.val), color='r', label="Maximum")
                    ax2.legend(loc='best')

                    q = cv2.adaptiveThreshold(img, int(s_time2.val), cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, int(E1.get()), int(s_time1.val))
                    ax1.imshow(q, cmap='gray')
                    ax1.set_title("Segmented Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)


                    fig.canvas.draw_idle()

                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                        label="Band" + str(a_AT) + "Histogram")

                L1 = tk.Label(root8, text="Block Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=230, y=700)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=360, y=700)

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            btn5 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Mean Treshold Adaptive   ', padx=20,
                             bd='5', command=BT)
            btn5.place(x=0, y=100)
            btn6 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Gaussian Treshold Adaptive   ', padx=20,
                             bd='5', command=BTI)
            btn6.place(x=0, y=130)


        else:
            img = Original_Image

            def BT():
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=700)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Constant', 0, 20, valinit=1, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()
                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                            label="Band" + str(1) + "Histogram")
                    ax2.axvline(x=int(s_time2.val), color='r', label="Maximum")
                    ax2.legend(loc='best')

                    q = cv2.adaptiveThreshold(img, int(s_time2.val), cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                              int(E1.get()), int(s_time1.val))
                    ax1.imshow(q, cmap='gray')
                    ax1.set_title("Segmented Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                        label="Band" + str(1) + "Histogram")

                L1 = tk.Label(root8, text="Block Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=230, y=700)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=360, y=700)

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            def BTI():
                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Original Image", fontsize=12, color="#333533")

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=700)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(img, cmap='gray')

                ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
                ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

                s_time1 = Slider(ax1_value, 'Constant', 0, 20, valinit=1, color='r')
                s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

                def Canny2(val):
                    ax2.cla()
                    hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                    ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                            label="Band" + str(1) + "Histogram")
                    ax2.axvline(x=int(s_time2.val), color='r', label="Maximum")
                    ax2.legend(loc='best')

                    q = cv2.adaptiveThreshold(img, int(s_time2.val), cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, int(E1.get()), int(s_time1.val))
                    ax1.imshow(q, cmap='gray')
                    ax1.set_title("Segmented Image")

                    def SaveI():
                        f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                        if f is None:
                            return

                        filename = f.name

                        cv2.imwrite(str(filename) + '.jpg', q)
                        f.close()

                    btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20,
                                     bd='5',
                                     command=SaveI)
                    btnw.place(x=400, y=0)

                    fig.canvas.draw_idle()

                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45",
                        label="Band" + str(1) + "Histogram")

                L1 = tk.Label(root8, text="Block Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
                L1.place(x=230, y=700)
                E1 = tk.Entry(root8, bd=5)
                E1.place(x=360, y=700)

                s_time1.on_changed(Canny2)
                s_time2.on_changed(Canny2)

            btn5 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Mean Treshold Adaptive   ', padx=20,
                             bd='5', command=BT)
            btn5.place(x=0, y=100)
            btn6 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Gaussian Treshold Adaptive   ', padx=20,
                             bd='5', command=BTI)
            btn6.place(x=0, y=130)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=AT1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=AT1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def OT():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then enter block size and then you can control tresholding parameters by sliders. if you want to save output image you can use "save  segmented Image" button.
                    """)



    def OT1():
        if len(Original_image_Size) > 2:
            a_OT = int(numberChosen1.get())
            img = Original_Image[:, :, a_OT - 1]

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)


            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

            s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0,color='r')
            s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0,color='g')

            def Canny2(val):
                ax2.cla()
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_OT)+"Histogram")
                ax2.axvline(x=int(s_time2.val), color='g',label="Maximum")
                ax2.axvline(x=int(s_time1.val), color='r', label="Minimum")

                blur = cv2.GaussianBlur(img, (int(E1.get()), int(E1.get())), 0)
                ret3, q = cv2.threshold(blur, int(s_time1.val), int(s_time2.val),
                                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Treshhold Image", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax1.imshow(q, cmap='gray')

                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_OT)+"Histogram")
            ax2.legend(loc='best')


            L1 = tk.Label(root8, text="Block Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=200, y=720)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=720)

            s_time1.on_changed(Canny2)
            s_time2.on_changed(Canny2)




        else:
            img = Original_Image

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533")
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533")

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])
            ax2_value = fig.add_axes([0.12, 0.05, 0.78, 0.03])

            s_time1 = Slider(ax1_value, 'Minimum Value', 0, np.max(img), valinit=0, color='r')
            s_time2 = Slider(ax2_value, 'Maximum Value', 0, np.max(img), valinit=0, color='g')

            def Canny2(val):
                ax2.cla()
                hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")
                ax2.axvline(x=int(s_time2.val), color='g', label="Maximum")
                ax2.axvline(x=int(s_time1.val), color='r', label="Minimum")

                blur = cv2.GaussianBlur(img, (int(E1.get()), int(E1.get())), 0)
                ret3, q = cv2.threshold(blur, int(s_time1.val), int(s_time2.val),
                                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Treshhold Image", fontsize=12, color="#333533")

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax1.imshow(q, cmap='gray')

                ax2.legend(loc='best')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', q)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')

            L1 = tk.Label(root8, text="Block Size(Odd Number):", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=200, y=720)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=720)

            s_time1.on_changed(Canny2)
            s_time2.on_changed(Canny2)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=OT1)
        btn.place(x=0, y=60)

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=OT1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root8.mainloop()


def VT():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then appears two buttons ("set SubDivided" and "set SubDividedH")  enter row size and column size then press one of the butons.if you want to treshold to each part use "set" button that appears a matrix as size size as divided image that you shold fill it by numbers that each number belongs to specefic divided image for tresholding.
                    """)



    def VT1():
        if len(Original_image_Size) > 2:
            a_VT = int(numberChosen1.get())
            img = Original_Image[:, :, a_VT - 1]
            img = np.array(img)

            fig = plt.Figure(figsize=(13, 7))
            ax1 = fig.add_subplot(121)
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1.imshow(img, cmap='gray')

            ax2 = fig.add_subplot(122)
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_VT)+"Histogram")
            ax2.legend(loc='best')

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.canvas.draw_idle()

            def SubDivided():
                row = int(E1.get())
                column = int(E2.get())
                fig, ax = plt.subplots(row, column, figsize=(13, 7), sharex='col', sharey='row')


                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                Size = np.shape(img)

                q1 = int(Size[0] / row)
                q2 = int(Size[1] / column)

                for i in range(row):
                    for j in range(column):
                        w = img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2]
                        ax[i, j].imshow(img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2], cmap='gray')
                        ax[i,j].set_title("Image("+str(i+1)+","+str(j+1)+")", fontsize=12, color="#333533")
                        fig.canvas.draw_idle()

            def SubDividedH():
                row1 = int(E1.get())
                column1 = int(E2.get())
                fig, ax = plt.subplots(row1, column1, figsize=(13, 7), sharex='col', sharey='row')





                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                Size = np.shape(img)

                q1 = int(Size[0] / row1)
                q2 = int(Size[1] / column1)

                for i in range(row1):
                    for j in range(column1):
                        w = img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2]
                        hist_img = cv2.calcHist([w], [0], None, [256], [0, 256])
                        ax[i, j].bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_VT)+"Histogram")
                        ax[i, j].set_title("Histogram(" + str(i+1) + "," + str(j+1) + ")", fontsize=12, color="#333533")
                        ax[i,j].set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                        ax[i,j].set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                        ax[i,j].set_facecolor("#2E2E2E")
                        ax[i,j].legend(loc='best')

                        fig.canvas.draw_idle()

                def BE2():
                    root9 = tk.Tk()
                    root9.configure(background='white')
                    root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                    ax2.cla()
                    height = int(E1.get())
                    width = int(E2.get())
                    rows = []
                    for i in range(height):  # Rows
                        cols = []
                        for j in range(width):  # Columns
                            b = tk.Entry(root9, text="")
                            b.grid(row=i, column=j)
                            cols.append(b)
                        rows.append(cols)

                    def BE3():
                        global Kernel
                        Kernel = []
                        for row in rows:
                            for col in row:
                                Kernel.append(float(col.get()))
                        Kernel = np.array(Kernel)
                        Kernel = np.reshape(Kernel, (row1, column1))

                        for i in range(Kernel.shape[0]):
                            for j in range(Kernel.shape[1]):
                                w = img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2]
                                for i1 in range(w.shape[0]):
                                    for j1 in range(w.shape[1]):
                                        if w[i1, j1] > Kernel[i, j]:
                                            w[i1, j1] = 255
                                        else:
                                            w[i1, j1] = 0
                                ax[i, j].imshow(w, cmap='gray')
                                ax[i,j].axvline(x=int(Kernel[i,j]),color='r',label="Treshold")
                                ax[i,j].legend(loc='best')

                    btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                     command=BE3)
                    btn1.grid(row=height + 1, column=0)
                    root9.mainloop()

                btn4 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=BE2)
                btn4.place(x=0, y=200)

            L1 = tk.Label(root8, text="Row > 1:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=200, y=720)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=720)

            L2 = tk.Label(root8, text="Column Size > 1:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=200, y=750)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=330, y=750)

            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   set SudDivided   ', padx=20, bd='5',
                             command=SubDivided)
            btn1.place(x=0, y=90)

            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   set SudDividedH   ', padx=20, bd='5',
                             command=SubDividedH)
            btn1.place(x=0, y=130)



        else:
            img = Original_Image
            img = np.array(img)

            fig = plt.Figure(figsize=(13, 7))
            ax1 = fig.add_subplot(121)
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1.imshow(img, cmap='gray')

            ax2 = fig.add_subplot(122)
            hist_img = cv2.calcHist([img], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=720)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.canvas.draw_idle()

            def SubDivided():
                row = int(E1.get())
                column = int(E2.get())
                fig, ax = plt.subplots(row, column, figsize=(13, 7), sharex='col', sharey='row')

                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                Size = np.shape(img)

                q1 = int(Size[0] / row)
                q2 = int(Size[1] / column)

                for i in range(row):
                    for j in range(column):
                        w = img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2]
                        ax[i, j].imshow(img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2], cmap='gray')
                        ax[i, j].set_title("Image(" + str(i + 1) + "," + str(j + 1) + ")", fontsize=12, color="#333533")
                        fig.canvas.draw_idle()

            def SubDividedH():
                row1 = int(E1.get())
                column1 = int(E2.get())
                fig, ax = plt.subplots(row1, column1, figsize=(13, 7), sharex='col', sharey='row')

                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=720)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                Size = np.shape(img)

                q1 = int(Size[0] / row1)
                q2 = int(Size[1] / column1)

                for i in range(row1):
                    for j in range(column1):
                        w = img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2]
                        hist_img = cv2.calcHist([w], [0], None, [256], [0, 256])
                        ax[i, j].bar(range(256), hist_img.ravel(), color="#d1ae45",
                                     label="Band" + str(1) + "Histogram")
                        ax[i, j].set_title("Histogram(" + str(i + 1) + "," + str(j + 1) + ")", fontsize=12,
                                           color="#333533")
                        ax[i, j].set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                        ax[i, j].set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                        ax[i, j].set_facecolor("#2E2E2E")
                        ax[i, j].legend(loc='best')

                        fig.canvas.draw_idle()

                def BE2():
                    root9 = tk.Tk()
                    root9.configure(background='white')
                    root9.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")
                    ax2.cla()
                    height = int(E1.get())
                    width = int(E2.get())
                    rows = []
                    for i in range(height):  # Rows
                        cols = []
                        for j in range(width):  # Columns
                            b = tk.Entry(root9, text="")
                            b.grid(row=i, column=j)
                            cols.append(b)
                        rows.append(cols)

                    def BE3():
                        global Kernel
                        Kernel = []
                        for row in rows:
                            for col in row:
                                Kernel.append(float(col.get()))
                        Kernel = np.array(Kernel)
                        Kernel = np.reshape(Kernel, (row1, column1))

                        for i in range(Kernel.shape[0]):
                            for j in range(Kernel.shape[1]):
                                w = img[i * q1:(i + 1) * q1, j * q2:(j + 1) * q2]
                                for i1 in range(w.shape[0]):
                                    for j1 in range(w.shape[1]):
                                        if w[i1, j1] > Kernel[i, j]:
                                            w[i1, j1] = 255
                                        else:
                                            w[i1, j1] = 0
                                ax[i, j].imshow(w, cmap='gray')
                                ax[i, j].axvline(x=int(Kernel[i, j]), color='r', label="Treshold")
                                ax[i, j].legend(loc='best')

                    btn1 = tk.Button(root9, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5',
                                     command=BE3)
                    btn1.grid(row=height + 1, column=0)
                    root9.mainloop()

                btn4 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Set   ', padx=20, bd='5', command=BE2)
                btn4.place(x=0, y=200)

            L1 = tk.Label(root8, text="Row > 1:", bg='#000000', fg='#b7f731', bd=5)
            L1.place(x=200, y=720)
            E1 = tk.Entry(root8, bd=5)
            E1.place(x=330, y=720)

            L2 = tk.Label(root8, text="Column Size > 1:", bg='#000000', fg='#b7f731', bd=5)
            L2.place(x=200, y=750)
            E2 = tk.Entry(root8, bd=5)
            E2.place(x=330, y=750)

            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   set SudDivided   ', padx=20, bd='5',
                             command=SubDivided)
            btn1.place(x=0, y=90)

            btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   set SudDividedH   ', padx=20, bd='5',
                             command=SubDividedH)
            btn1.place(x=0, y=130)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=VT1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=VT1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def SGT():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then appears a button that if you use it Mean value used for initial value oterwise you can control Initial value by sliders. if you want to save output image you can use "save  segmented Image" button.
                    """)



    def SGT1():
        if len(Original_image_Size) > 2:
            a_SGT = int(numberChosen1.get())
            img = Original_Image[:, :, a_SGT - 1]
            img = np.array(img)




            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])

            s_time1 = Slider(ax1_value, 'Initial Value', 0, np.max(img), valinit=0,color='r')

            def InitialT(val):
                imgInitial = img
                ax2.cla()

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                hist_imgInitial = cv2.calcHist([Original_Image[:, :, a_SGT - 1]], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgInitial.ravel(),color="#d1ae45",label="Band"+str(a_SGT)+"Histogram")

                ax2.axvline(x=int(s_time1.val), color='r', label="Initial Value")



                T = [int(s_time1.val)]
                i1 = 0
                delta = 1
                while np.abs(delta) > 0.00000001:

                    g1 = []
                    g2 = []
                    for i in range(imgInitial.shape[0]):
                        for j in range(imgInitial.shape[1]):
                            if imgInitial[i, j] > T[i1]:
                                g1.append(imgInitial[i, j])
                            else:
                                g2.append(imgInitial[i, j])
                    g1 = np.array(g1)
                    g2 = np.array(g2)
                    m1 = np.mean(g1)
                    m2 = np.mean(g2)
                    T1 = (m1 + m2) / 2
                    T.append(T1)
                    i1 = i1 + 1
                    delta = T[i1] - T[i1 - 1]
                    delta = np.array(delta)
                ax2.axvline(x=T[i1], color='g', label="Final Value")

                for i in range(imgInitial.shape[0]):
                    for j in range(imgInitial.shape[1]):
                        if imgInitial[i, j] > T[i1]:
                            imgInitial[i, j] = 255
                        else:
                            imgInitial[i, j] = 0

                ax1.imshow(imgInitial, cmap='gray')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', imgInitial)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([Original_Image[:, :, a_SGT - 1]], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(),color="#d1ae45",label="Band"+str(a_SGT)+"Histogram")
            ax2.legend(loc='best')

            def MeanT():
                imgMean = img
                ax2.cla()
                hist_imgMean = cv2.calcHist([Original_Image[:, :, a_SGT - 1]], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgMean.ravel(),color="#d1ae45",label="Band"+str(a_SGT)+"Histogram")



                T = [np.mean(imgMean)]
                ax2.axvline(x=T, color='r',label="Mean As Initial Value")
                i1 = 0
                delta = 1
                while np.abs(delta) > 0.00000001:

                    g1 = []
                    g2 = []
                    for i in range(imgMean.shape[0]):
                        for j in range(imgMean.shape[1]):
                            if imgMean[i, j] > T[i1]:
                                g1.append(imgMean[i, j])
                            else:
                                g2.append(imgMean[i, j])
                    g1 = np.array(g1)
                    g2 = np.array(g2)
                    m1 = np.mean(g1)
                    m2 = np.mean(g2)
                    T1 = (m1 + m2) / 2
                    T.append(T1)
                    i1 = i1 + 1
                    delta = T[i1] - T[i1 - 1]
                    delta = np.array(delta)
                ax2.axvline(x=T[i1], color='g',label="Final value")
                ax2.legend(loc='best')
                for i in range(imgMean.shape[0]):
                    for j in range(imgMean.shape[1]):
                        if imgMean[i, j] > T[i1]:
                            imgMean[i, j] = 255
                        else:
                            imgMean[i, j] = 0

                ax1.imshow(imgMean, cmap='gray')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', imgMean)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Use Mean As Initial Value   ', padx=20,
                             bd='5', command=MeanT)
            btn3.place(x=0, y=200)

            s_time1.on_changed(InitialT)





        else:
            img = Original_Image
            img = np.array(img)

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
            ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

            ax2.set_facecolor("#2E2E2E")

            ax2.set_title("Histogram", fontsize=12, color="#333533")
            ax1.set_title("Original Image", fontsize=12, color="#333533")

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=650)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')

            ax1_value = fig.add_axes([0.12, 0.1, 0.78, 0.03])

            s_time1 = Slider(ax1_value, 'Initial Value', 0, np.max(img), valinit=0, color='r')

            def InitialT(val):
                imgInitial = img
                ax2.cla()

                ax2.set_xlabel("Value", labelpad=15, fontsize=12, color="#333533");
                ax2.set_ylabel("Frequency", labelpad=15, fontsize=12, color="#333533");

                ax2.set_facecolor("#2E2E2E")

                ax2.set_title("Histogram", fontsize=12, color="#333533")
                ax1.set_title("Segmented Image", fontsize=12, color="#333533")

                hist_imgInitial = cv2.calcHist([Original_Image], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgInitial.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")

                ax2.axvline(x=int(s_time1.val), color='r', label="Initial Value")

                T = [int(s_time1.val)]
                i1 = 0
                delta = 1
                while np.abs(delta) > 0.00000001:

                    g1 = []
                    g2 = []
                    for i in range(imgInitial.shape[0]):
                        for j in range(imgInitial.shape[1]):
                            if imgInitial[i, j] > T[i1]:
                                g1.append(imgInitial[i, j])
                            else:
                                g2.append(imgInitial[i, j])
                    g1 = np.array(g1)
                    g2 = np.array(g2)
                    m1 = np.mean(g1)
                    m2 = np.mean(g2)
                    T1 = (m1 + m2) / 2
                    T.append(T1)
                    i1 = i1 + 1
                    delta = T[i1] - T[i1 - 1]
                    delta = np.array(delta)
                ax2.axvline(x=T[i1], color='g', label="Final Value")

                for i in range(imgInitial.shape[0]):
                    for j in range(imgInitial.shape[1]):
                        if imgInitial[i, j] > T[i1]:
                            imgInitial[i, j] = 255
                        else:
                            imgInitial[i, j] = 0

                ax1.imshow(imgInitial, cmap='gray')
                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', imgInitial)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                ax2.legend(loc='best')
                fig.canvas.draw_idle()

            hist_img = cv2.calcHist([Original_Image], [0], None, [256], [0, 256])
            ax2.bar(range(256), hist_img.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")
            ax2.legend(loc='best')

            def MeanT():
                imgMean = img
                ax2.cla()
                hist_imgMean = cv2.calcHist([Original_Image], [0], None, [256], [0, 256])
                ax2.bar(range(256), hist_imgMean.ravel(), color="#d1ae45", label="Band" + str(1) + "Histogram")

                T = [np.mean(imgMean)]
                ax2.axvline(x=T, color='r', label="Mean As Initial Value")
                i1 = 0
                delta = 1
                while np.abs(delta) > 0.00000001:

                    g1 = []
                    g2 = []
                    for i in range(imgMean.shape[0]):
                        for j in range(imgMean.shape[1]):
                            if imgMean[i, j] > T[i1]:
                                g1.append(imgMean[i, j])
                            else:
                                g2.append(imgMean[i, j])
                    g1 = np.array(g1)
                    g2 = np.array(g2)
                    m1 = np.mean(g1)
                    m2 = np.mean(g2)
                    T1 = (m1 + m2) / 2
                    T.append(T1)
                    i1 = i1 + 1
                    delta = T[i1] - T[i1 - 1]
                    delta = np.array(delta)
                ax2.axvline(x=T[i1], color='g', label="Final value")
                ax2.legend(loc='best')
                for i in range(imgMean.shape[0]):
                    for j in range(imgMean.shape[1]):
                        if imgMean[i, j] > T[i1]:
                            imgMean[i, j] = 255
                        else:
                            imgMean[i, j] = 0

                ax1.imshow(imgMean, cmap='gray')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', imgMean)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=400, y=0)

                fig.canvas.draw_idle()

            btn3 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Use Mean As Initial Value   ', padx=20,
                             bd='5', command=MeanT)
            btn3.place(x=0, y=200)

            s_time1.on_changed(InitialT)

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SGT1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SGT1)
        btn1.pack(anchor='w')


    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def Watershed():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then image will be segmented. if you want to save output image you can use "save  segmented Image" button.
                    """)


    def Watershed1():
        if len(Original_image_Size) > 2:
            a_Watershed = int(numberChosen1.get())
            img = Original_Image[:, :, a_Watershed - 1]
            img = np.array(img)

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)
            ax1.set_title("Original Image")
            ax2.set_title("Watershed Segmentation")

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')
            fig.canvas.draw_idle()

            class Watershed(object):
                MASK = -2
                WSHD = 0
                INIT = -1
                INQE = -3

                def __init__(self, levels=256):
                    self.levels = levels

                # Neighbour (coordinates of) pixels, including the given pixel.
                def _get_neighbors(self, height, width, pixel):
                    return np.mgrid[
                           max(0, pixel[0] - 1):min(height, pixel[0] + 2),
                           max(0, pixel[1] - 1):min(width, pixel[1] + 2)
                           ].reshape(2, -1).T

                def apply(self, image):
                    current_label = 0
                    flag = False
                    fifo = deque()

                    height, width = image.shape
                    total = height * width
                    labels = np.full((height, width), self.INIT, np.int32)

                    reshaped_image = image.reshape(total)
                    # [y, x] pairs of pixel coordinates of the flattened image.
                    pixels = np.mgrid[0:height, 0:width].reshape(2, -1).T
                    # Coordinates of neighbour pixels for each pixel.
                    neighbours = np.array([self._get_neighbors(height, width, p) for p in pixels])
                    if len(neighbours.shape) == 3:
                        # Case where all pixels have the same number of neighbours.
                        neighbours = neighbours.reshape(height, width, -1, 2)
                    else:
                        # Case where pixels may have a different number of pixels.
                        neighbours = neighbours.reshape(height, width)

                    indices = np.argsort(reshaped_image)
                    sorted_image = reshaped_image[indices]
                    sorted_pixels = pixels[indices]

                    # self.levels evenly spaced steps from minimum to maximum.
                    levels = np.linspace(sorted_image[0], sorted_image[-1], self.levels)
                    level_indices = []
                    current_level = 0

                    # Get the indices that deleimit pixels with different values.
                    for i in range(total):
                        if sorted_image[i] > levels[current_level]:
                            # Skip levels until the next highest one is reached.
                            while sorted_image[i] > levels[current_level]: current_level += 1
                            level_indices.append(i)
                    level_indices.append(total)

                    start_index = 0
                    for stop_index in level_indices:
                        # Mask all pixels at the current level.
                        for p in sorted_pixels[start_index:stop_index]:
                            labels[p[0], p[1]] = self.MASK
                            # Initialize queue with neighbours of existing basins at the current level.
                            for q in neighbours[p[0], p[1]]:
                                # p == q is ignored here because labels[p] < WSHD
                                if labels[q[0], q[1]] >= self.WSHD:
                                    labels[p[0], p[1]] = self.INQE
                                    fifo.append(p)
                                    break

                        # Extend basins.
                        while fifo:
                            p = fifo.popleft()
                            # Label p by inspecting neighbours.
                            for q in neighbours[p[0], p[1]]:
                                # Don't set lab_p in the outer loop because it may change.
                                lab_p = labels[p[0], p[1]]
                                lab_q = labels[q[0], q[1]]
                                if lab_q > 0:
                                    if lab_p == self.INQE or (lab_p == self.WSHD and flag):
                                        labels[p[0], p[1]] = lab_q
                                    elif lab_p > 0 and lab_p != lab_q:
                                        labels[p[0], p[1]] = self.WSHD
                                        flag = False
                                elif lab_q == self.WSHD:
                                    if lab_p == self.INQE:
                                        labels[p[0], p[1]] = self.WSHD
                                        flag = True
                                elif lab_q == self.MASK:
                                    labels[q[0], q[1]] = self.INQE
                                    fifo.append(q)

                        # Detect and process new minima at the current level.
                        for p in sorted_pixels[start_index:stop_index]:
                            # p is inside a new minimum. Create a new label.
                            if labels[p[0], p[1]] == self.MASK:
                                current_label += 1
                                fifo.append(p)
                                labels[p[0], p[1]] = current_label
                                while fifo:
                                    q = fifo.popleft()
                                    for r in neighbours[q[0], q[1]]:
                                        if labels[r[0], r[1]] == self.MASK:
                                            fifo.append(r)
                                            labels[r[0], r[1]] = current_label

                        start_index = stop_index

                    return labels

            if __name__ == "__main__":


                w = Watershed()
                image = img
                image = np.array(image)
                labels = w.apply(image)

                ax2.imshow(labels, cmap='Paired', interpolation='nearest')

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', labels)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()





        else:
            img = Original_Image
            img = np.array(img)

            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root8)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(121)
            ax2 = fig.add_subplot(122)

            toolbarFrame = tk.Frame(master=root8)
            toolbarFrame.place(x=720, y=700)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            fig.subplots_adjust(bottom=0.25)
            ax1.set_title("Original Image")
            ax2.set_title("Watershed Segmentation")

            fig.subplots_adjust(bottom=0.25)

            ax1.imshow(img, cmap='gray')
            ax2.imshow(img, cmap='gray')
            fig.canvas.draw_idle()

            class Watershed(object):
               MASK = -2
               WSHD = 0
               INIT = -1
               INQE = -3

               def __init__(self, levels=256):
                  self.levels = levels

               # Neighbour (coordinates of) pixels, including the given pixel.
               def _get_neighbors(self, height, width, pixel):
                  return np.mgrid[
                         max(0, pixel[0] - 1):min(height, pixel[0] + 2),
                         max(0, pixel[1] - 1):min(width, pixel[1] + 2)
                         ].reshape(2, -1).T

               def apply(self, image):
                  current_label = 0
                  flag = False
                  fifo = deque()

                  height, width = image.shape
                  total = height * width
                  labels = np.full((height, width), self.INIT, np.int32)

                  reshaped_image = image.reshape(total)
                  # [y, x] pairs of pixel coordinates of the flattened image.
                  pixels = np.mgrid[0:height, 0:width].reshape(2, -1).T
                  # Coordinates of neighbour pixels for each pixel.
                  neighbours = np.array([self._get_neighbors(height, width, p) for p in pixels])
                  if len(neighbours.shape) == 3:
                     # Case where all pixels have the same number of neighbours.
                     neighbours = neighbours.reshape(height, width, -1, 2)
                  else:
                     # Case where pixels may have a different number of pixels.
                     neighbours = neighbours.reshape(height, width)

                  indices = np.argsort(reshaped_image)
                  sorted_image = reshaped_image[indices]
                  sorted_pixels = pixels[indices]

                  # self.levels evenly spaced steps from minimum to maximum.
                  levels = np.linspace(sorted_image[0], sorted_image[-1], self.levels)
                  level_indices = []
                  current_level = 0

                  # Get the indices that deleimit pixels with different values.
                  for i in range(total):
                     if sorted_image[i] > levels[current_level]:
                        # Skip levels until the next highest one is reached.
                        while sorted_image[i] > levels[current_level]: current_level += 1
                        level_indices.append(i)
                  level_indices.append(total)

                  start_index = 0
                  for stop_index in level_indices:
                     # Mask all pixels at the current level.
                     for p in sorted_pixels[start_index:stop_index]:
                        labels[p[0], p[1]] = self.MASK
                        # Initialize queue with neighbours of existing basins at the current level.
                        for q in neighbours[p[0], p[1]]:
                           # p == q is ignored here because labels[p] < WSHD
                           if labels[q[0], q[1]] >= self.WSHD:
                              labels[p[0], p[1]] = self.INQE
                              fifo.append(p)
                              break

                     # Extend basins.
                     while fifo:
                        p = fifo.popleft()
                        # Label p by inspecting neighbours.
                        for q in neighbours[p[0], p[1]]:
                           # Don't set lab_p in the outer loop because it may change.
                           lab_p = labels[p[0], p[1]]
                           lab_q = labels[q[0], q[1]]
                           if lab_q > 0:
                              if lab_p == self.INQE or (lab_p == self.WSHD and flag):
                                 labels[p[0], p[1]] = lab_q
                              elif lab_p > 0 and lab_p != lab_q:
                                 labels[p[0], p[1]] = self.WSHD
                                 flag = False
                           elif lab_q == self.WSHD:
                              if lab_p == self.INQE:
                                 labels[p[0], p[1]] = self.WSHD
                                 flag = True
                           elif lab_q == self.MASK:
                              labels[q[0], q[1]] = self.INQE
                              fifo.append(q)

                     # Detect and process new minima at the current level.
                     for p in sorted_pixels[start_index:stop_index]:
                        # p is inside a new minimum. Create a new label.
                        if labels[p[0], p[1]] == self.MASK:
                           current_label += 1
                           fifo.append(p)
                           labels[p[0], p[1]] = current_label
                           while fifo:
                              q = fifo.popleft()
                              for r in neighbours[q[0], q[1]]:
                                 if labels[r[0], r[1]] == self.MASK:
                                    fifo.append(r)
                                    labels[r[0], r[1]] = current_label

                     start_index = stop_index

                  return labels

            if __name__ == "__main__":
               w = Watershed()
               image = img
               image = np.array(image)
               labels = w.apply(image)

               ax2.imshow(labels, cmap='Paired', interpolation='nearest')

               def SaveI():
                   f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                   if f is None:
                       return

                   filename = f.name

                   cv2.imwrite(str(filename) + '.jpg', labels)
                   f.close()

               btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                                command=SaveI)
               btnw.place(x=1000, y=0)

               fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                        command=Watershed1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                         command=Watershed1)
        btn1.pack(anchor='w')



    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')


    root8.mainloop()


def Watershed2():
   root8 = tk.Toplevel()
   root8.geometry("1800x900")
   root8.configure(background='white')
   root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

   frame1 = tk.Frame(
       master=root8,
       bg='#808000'
   )
   frame1.pack(anchor='w')
   editArea = tkst.ScrolledText(
       master=frame1,
       wrap=tk.WORD,
       width=20,
       height=10
   )
   # Don't use widget.place(), use pack or grid instead, since
   # They behave better on scaling the window -- and you don't
   # have to calculate it manually!
   editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
   editArea.configure(font=('Franklin Gothic Demi Cond', 11))
   # Adding some text, to see if scroll is working as we expect it
   editArea.insert(tk.INSERT,
                   """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then image will be segmented. if you want to save output image you can use "save  segmented Image" button.
                   """)


   def Watershed21():
      if len(Original_image_Size) > 2:
         a_Watershed = int(numberChosen1.get())
         img = Original_Image[:, :, a_Watershed - 1]
         img = np.array(img)

         fig = plt.Figure(figsize=(13, 7))
         canvas = FigureCanvasTkAgg(fig, root8)
         canvas.get_tk_widget().place(x=200, y=0)

         ax1 = fig.add_subplot(131)
         ax2 = fig.add_subplot(132)
         ax3 = fig.add_subplot(133)

         fig.subplots_adjust(bottom=0.25)

         toolbarFrame = tk.Frame(master=root8)
         toolbarFrame.place(x=720, y=700)

         toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
         toolbar.update()

         def on_key_press(event):
             print("you pressed {}".format(event.key))
             key_press_handler(event, canvas, toolbar)

         canvas.mpl_connect("key_press_event", on_key_press)


         image = img

         # Now we want to separate the two objects in image
         # Generate the markers as local maxima of the distance to the background
         distance = ndi.distance_transform_edt(image)
         local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
                                     labels=image)
         markers = ndi.label(local_maxi)[0]
         labels = watershed(-distance, markers, mask=image)



         ax1.imshow(image, cmap=plt.cm.gray)
         ax1.set_title('Overlapping objects')
         ax2.imshow(-distance, cmap=plt.cm.gray)
         ax2.set_title('Distances')
         ax3.imshow(labels, cmap=plt.cm.nipy_spectral)
         ax3.set_title('Separated objects')

         def SaveI():
             f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

             if f is None:
                 return

             filename = f.name

             cv2.imwrite(str(filename) + '.jpg', labels)
             f.close()

         btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                          command=SaveI)
         btnw.place(x=1000, y=0)


         fig.tight_layout()

         fig.canvas.draw_idle()




      else:
         img = Original_Image
         img = np.array(img)

         fig = plt.Figure(figsize=(13, 7))
         canvas = FigureCanvasTkAgg(fig, root8)
         canvas.get_tk_widget().place(x=200, y=0)

         ax1 = fig.add_subplot(131)
         ax2 = fig.add_subplot(132)
         ax3 = fig.add_subplot(133)

         fig.subplots_adjust(bottom=0.25)

         toolbarFrame = tk.Frame(master=root8)
         toolbarFrame.place(x=720, y=700)

         toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
         toolbar.update()

         def on_key_press(event):
             print("you pressed {}".format(event.key))
             key_press_handler(event, canvas, toolbar)

         canvas.mpl_connect("key_press_event", on_key_press)



         image = img

         # Now we want to separate the two objects in image
         # Generate the markers as local maxima of the distance to the background
         distance = ndi.distance_transform_edt(image)
         local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
                                     labels=image)
         markers = ndi.label(local_maxi)[0]
         labels = watershed(-distance, markers, mask=image)

         ax1.imshow(image, cmap=plt.cm.gray)
         ax1.set_title('Overlapping objects')
         ax2.imshow(-distance, cmap=plt.cm.gray)
         ax2.set_title('Distances')
         ax3.imshow(labels, cmap=plt.cm.nipy_spectral)
         ax3.set_title('Separated objects')

         def SaveI():
             f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

             if f is None:
                 return

             filename = f.name

             cv2.imwrite(str(filename) + '.jpg', labels)
             f.close()

         btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Invert Image   ', padx=20, bd='5',
                          command=SaveI)
         btnw.place(x=1000, y=0)

         fig.tight_layout()

         fig.canvas.draw_idle()


   if len(Original_image_Size) > 2:
      Dimension_Number = []
      Dimension_Number_int = []
      for x1 in range(Original_Image.shape[2]):
         Dimension_Number_int.append(x1 + 1)
         Dimension_Number.append(("Band ", x1 + 1))

   else:
      Dimension_Number = [("Band", 1)]

   if len(Original_image_Size) > 2:
      ttk.Label(root8, text="Choose a band:").pack(anchor='w')
      number1 = tk.StringVar()
      numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
      numberChosen1['values'] = (Dimension_Number_int)
      numberChosen1.pack(anchor='w')
      numberChosen1.current(0)

      btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                      command=Watershed21)
      btn.pack(anchor='w')

   else:
      tk.Label(root8, text="Choose a band:").pack(anchor='w')
      number1 = tk.StringVar()
      numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
      numberChosen1['values'] = "1"
      numberChosen1.pack(anchor='w')
      numberChosen1.current(0)
      btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5',
                       command=Watershed21)
      btn1.pack(anchor='w')

   def Quit():
       root8.quit()
       root8.destroy()

   button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                      bd='5', command=Quit)
   button.pack(anchor='w')

   root8.mainloop()



def SAS():
    root8 = tk.Toplevel()
    root8.geometry("1800x900")
    root8.configure(background='white')
    root8.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root8,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then image will be segmented. if you want to save output image you can use "save  segmented Image" button.
                    """)


    def SAS1():
        if len(Original_image_Size) > 2:
            a_SAS = int(numberChosen1.get())
            img = Original_Image[:, :, a_SAS - 1]
            img = np.array(img)

            class Point(object):
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

            def getX(self):
                return self.x

            def getY(self):
                return self.y

            class Node:
                def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight, location):
                    self.mean_val = val
                    self.isLeaf = isLeaf
                    self.topLeft = topLeft
                    self.topRight = topRight
                    self.bottomLeft = bottomLeft
                    self.bottomRight = bottomRight
                    self.location = location

            class Solution:
                def __init__(self, image, total_mean, total_max, total_min):
                    self.image = image
                    self.total_mean = total_mean
                    self.total_max = total_max
                    self.total_min = total_min

                def construct(self, picture, location):

                    root = Node(None, False, None, None, None, None, location)

                    if picture.shape[0] == 1:
                        root.isLeaf = True
                        root.mean_val = picture.mean()
                        self.color(location, root.mean_val)

                    elif self.stop_split(picture):  # 
                        root.isLeaf = True
                        root.mean_val = picture.mean()
                        self.color(location, root.mean_val)

                    else:  # 
                        height = picture.shape[0]
                        width = picture.shape[1]
                        halfheight = height // 2
                        halfwidth = width // 2  #
                        root.isLeaf = False  #
                        # print(height, width, halfheight, halfwidth)

                        # 
                        # 
                        base_start_x = location[0].x
                        base_start_y = location[0].y
                        base_end_x = location[1].x
                        base_end_y = location[1].y

                        root.topLeft = self.construct(picture[:halfheight, :halfwidth],
                                                      [Point(base_start_x, base_start_y),
                                                       Point(base_start_x + halfheight,
                                                             base_start_y + halfwidth)])
                        root.topRight = self.construct(picture[:halfheight, halfwidth:],
                                                       [Point(base_start_x, base_start_y + halfwidth),
                                                        Point(base_start_x + halfheight, base_end_y)])
                        root.bottomLeft = self.construct(picture[halfheight:, :halfwidth],
                                                         [Point(base_start_x + halfheight, base_start_y),
                                                          Point(base_end_x, base_start_y + halfwidth)])
                        root.bottomRight = self.construct(picture[halfheight:, halfwidth:],
                                                          [Point(base_start_x + halfheight,
                                                                 base_start_y + halfwidth),
                                                           Point(base_end_x, base_end_y)])
                    return root

                def stop_split(self, iim):
                    if iim.max() - iim.min() <= 10:
                        return True
                    else:
                        return False

                def color(self, location, mean_val):
                    first_point = location[0]
                    second_point = location[1]
                    print(first_point.x, first_point.y, ' to ', second_point.x, second_point.y)
                    if mean_val <= self.total_mean:
                        for i in range(first_point.x, second_point.x):
                            for j in range(first_point.y, second_point.y):
                                self.image[i][j] = self.total_max
                    else:
                        for i in range(first_point.x, second_point.x):
                            for j in range(first_point.y, second_point.y):
                                self.image[i][j] = self.total_min

            if __name__ == '__main__':
                # import Image
                im = img
                im_shape = im.shape
                height = im_shape[0]
                width = im_shape[1]
                print('the shape of image :', im_shape)

                init_locate = [Point(0, 0), Point(height, width)]  # 
                # 
                zpd = Solution(im, im.mean(), im.max(), im.min())

                zpd.construct(im, init_locate)

                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(Original_Image[:, :, a_SAS - 1], cmap='gray')

                ax2.imshow(zpd.image, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Segmanted Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', zpd.img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()








        else:
            img = Original_Image
            img = np.array(img)

            class Point(object):
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

            def getX(self):
                return self.x

            def getY(self):
                return self.y

            class Node:
                def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight, location):
                    self.mean_val = val
                    self.isLeaf = isLeaf
                    self.topLeft = topLeft
                    self.topRight = topRight
                    self.bottomLeft = bottomLeft
                    self.bottomRight = bottomRight
                    self.location = location

            class Solution:
                def __init__(self, image, total_mean, total_max, total_min):
                    self.image = image
                    self.total_mean = total_mean
                    self.total_max = total_max
                    self.total_min = total_min

                def construct(self, picture, location):

                    root = Node(None, False, None, None, None, None, location)

                    if picture.shape[0] == 1:
                        root.isLeaf = True
                        root.mean_val = picture.mean()
                        self.color(location, root.mean_val)

                    elif self.stop_split(picture):  # 
                        root.isLeaf = True
                        root.mean_val = picture.mean()
                        self.color(location, root.mean_val)

                    else:  # 
                        height = picture.shape[0]
                        width = picture.shape[1]
                        halfheight = height // 2
                        halfwidth = width // 2  #  // 
                        root.isLeaf = False  #
                        # print(height, width, halfheight, halfwidth)

                        # 
                        # 
                        base_start_x = location[0].x
                        base_start_y = location[0].y
                        base_end_x = location[1].x
                        base_end_y = location[1].y

                        root.topLeft = self.construct(picture[:halfheight, :halfwidth],
                                                      [Point(base_start_x, base_start_y),
                                                       Point(base_start_x + halfheight,
                                                             base_start_y + halfwidth)])
                        root.topRight = self.construct(picture[:halfheight, halfwidth:],
                                                       [Point(base_start_x, base_start_y + halfwidth),
                                                        Point(base_start_x + halfheight, base_end_y)])
                        root.bottomLeft = self.construct(picture[halfheight:, :halfwidth],
                                                         [Point(base_start_x + halfheight, base_start_y),
                                                          Point(base_end_x, base_start_y + halfwidth)])
                        root.bottomRight = self.construct(picture[halfheight:, halfwidth:],
                                                          [Point(base_start_x + halfheight,
                                                                 base_start_y + halfwidth),
                                                           Point(base_end_x, base_end_y)])
                    return root

                def stop_split(self, iim):
                    if iim.max() - iim.min() <= 10:
                        return True
                    else:
                        return False

                def color(self, location, mean_val):
                    first_point = location[0]
                    second_point = location[1]
                    print(first_point.x, first_point.y, ' to ', second_point.x, second_point.y)
                    if mean_val <= self.total_mean:
                        for i in range(first_point.x, second_point.x):
                            for j in range(first_point.y, second_point.y):
                                self.image[i][j] = self.total_max
                    else:
                        for i in range(first_point.x, second_point.x):
                            for j in range(first_point.y, second_point.y):
                                self.image[i][j] = self.total_min

            if __name__ == '__main__':
                # import Image
                im = img
                im_shape = im.shape
                height = im_shape[0]
                width = im_shape[1]
                print('the shape of image :', im_shape)

                init_locate = [Point(0, 0), Point(height, width)]  # 
                # 
                zpd = Solution(im, im.mean(), im.max(), im.min())

                zpd.construct(im, init_locate)

                fig = plt.Figure(figsize=(13, 7))
                canvas = FigureCanvasTkAgg(fig, root8)
                canvas.get_tk_widget().place(x=200, y=0)

                ax1 = fig.add_subplot(121)
                ax2 = fig.add_subplot(122)

                toolbarFrame = tk.Frame(master=root8)
                toolbarFrame.place(x=720, y=650)

                toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
                toolbar.update()

                def on_key_press(event):
                    print("you pressed {}".format(event.key))
                    key_press_handler(event, canvas, toolbar)

                canvas.mpl_connect("key_press_event", on_key_press)

                fig.subplots_adjust(bottom=0.25)

                ax1.imshow(Original_Image, cmap='gray')

                ax2.imshow(zpd.image, cmap='gray')

                ax1.set_title("Original Image", fontsize=12, color="#333533")
                ax2.set_title("Segmanted Image", fontsize=12, color="#333533")

                def SaveI():
                    f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                    if f is None:
                        return

                    filename = f.name

                    cv2.imwrite(str(filename) + '.jpg', zpd.img)
                    f.close()

                btnw = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Save Segmented Image   ', padx=20, bd='5',
                                 command=SaveI)
                btnw.place(x=1000, y=0)

                fig.canvas.draw_idle()

    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)

        btn = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SAS1)
        btn.pack(anchor='w')

    else:
        tk.Label(root8, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root8, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root8, bg='#000000', fg='#b7f731', text='   Select Band   ', padx=20, bd='5', command=SAS1)
        btn1.pack(anchor='w')

    def Quit():
        root8.quit()
        root8.destroy()

    button = tk.Button(master=root8, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')




    root8.mainloop()


def HOUGH():
    root4 = tk.Toplevel()
    root4.geometry("1800x900")
    root4.configure(background='white')
    root4.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

    frame1 = tk.Frame(
        master=root4,
        bg='#808000'
    )
    frame1.pack(anchor='w')
    editArea = tkst.ScrolledText(
        master=frame1,
        wrap=tk.WORD,
        width=20,
        height=10
    )
    # Don't use widget.place(), use pack or grid instead, since
    # They behave better on scaling the window -- and you don't
    # have to calculate it manually!
    editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    editArea.configure(font=('Franklin Gothic Demi Cond', 11))
    # Adding some text, to see if scroll is working as we expect it
    editArea.insert(tk.INSERT,
                    """\
this menu use for image segmentation. for using this option on the application at first you should select your special band from the "list top of the page" and then press "Select Band" button then image will be segmented. if you want to save output image you can use "save  segmented Image" button.
                    """)


    def HOUGHOneBand():
        if len(Original_image_Size) > 2:
            a_Hough = int(numberChosen1.get())
            image = Original_Image[:, :, a_Hough - 1]





            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(231)
            ax2 = fig.add_subplot(232)
            ax3 = fig.add_subplot(233)
            ax4 = fig.add_subplot(234)
            ax5 = fig.add_subplot(235)
            ax6 = fig.add_subplot(236)

            fig.subplots_adjust(bottom=0.25)

            image=np.array(image)

            idx = np.arange(25, 75)
            image[idx[::-1], idx] = 255
            image[idx, idx] = 255

            # Classic straight-line Hough transform
            h, theta, d = hough_line(image)

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(image, cmap=cm.gray)
            ax1.set_title('Input image')
            ax1.set_axis_off()

            ax2.imshow(np.log(1 + h),
                       extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
                       cmap=cm.gray, aspect=1 / 1.5)
            ax2.set_title('Hough transform')
            ax2.set_xlabel('Angles (degrees)')
            ax2.set_ylabel('Distance (pixels)')
            ax2.axis('image')

            ax3.imshow(image, cmap=cm.gray)
            for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
                y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
                y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)
                ax3.plot((0, image.shape[1]), (y0, y1), '-r')
            ax3.set_xlim((0, image.shape[1]))
            ax3.set_ylim((image.shape[0], 0))
            ax3.set_axis_off()
            ax3.set_title('Detected lines')

            plt.tight_layout()

            # Line finding using the Probabilistic Hough Transform

            edges = canny(image, 2, 1, 25)
            lines = probabilistic_hough_line(edges, threshold=10, line_length=5,
                                             line_gap=3)

            # Generating figure 2

            ax4.imshow(image, cmap=cm.gray)
            ax4.set_title('Input image')

            ax5.imshow(edges, cmap=cm.gray)
            ax5.set_title('Canny edges')

            Q=edges * 0

            ax6.imshow(Q)
            for line in lines:
                p0, p1 = line
                ax6.plot((p0[0], p1[0]), (p0[1], p1[1]))
            ax6.set_xlim((0, image.shape[1]))
            ax6.set_ylim((image.shape[0], 0))
            ax6.set_title('Probabilistic Hough')



            plt.tight_layout()



            fig.canvas.draw_idle()

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', Q)
                f.close()

            btnw = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Save Straight line Hough transformed Image   ', padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)


        else:
            image = Original_Image


            fig = plt.Figure(figsize=(13, 7))
            canvas = FigureCanvasTkAgg(fig, root4)
            canvas.get_tk_widget().place(x=200, y=0)

            ax1 = fig.add_subplot(231)
            ax2 = fig.add_subplot(232)
            ax3 = fig.add_subplot(233)
            ax4 = fig.add_subplot(234)
            ax5 = fig.add_subplot(235)
            ax6 = fig.add_subplot(236)

            fig.subplots_adjust(bottom=0.25)

            image = np.array(image)

            idx = np.arange(25, 75)
            image[idx[::-1], idx] = 255
            image[idx, idx] = 255

            # Classic straight-line Hough transform
            h, theta, d = hough_line(image)

            toolbarFrame = tk.Frame(master=root4)
            toolbarFrame.place(x=720, y=600)

            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()

            def on_key_press(event):
                print("you pressed {}".format(event.key))
                key_press_handler(event, canvas, toolbar)

            canvas.mpl_connect("key_press_event", on_key_press)

            ax1.imshow(image, cmap=cm.gray)
            ax1.set_title('Input image')
            ax1.set_axis_off()

            ax2.imshow(np.log(1 + h),
                       extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
                       cmap=cm.gray, aspect=1 / 1.5)
            ax2.set_title('Hough transform')
            ax2.set_xlabel('Angles (degrees)')
            ax2.set_ylabel('Distance (pixels)')
            ax2.axis('image')

            ax3.imshow(image, cmap=cm.gray)
            for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
                y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
                y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)
                ax3.plot((0, image.shape[1]), (y0, y1), '-r')
            ax3.set_xlim((0, image.shape[1]))
            ax3.set_ylim((image.shape[0], 0))
            ax3.set_axis_off()
            ax3.set_title('Detected lines')

            plt.tight_layout()

            # Line finding using the Probabilistic Hough Transform

            edges = canny(image, 2, 1, 25)
            lines = probabilistic_hough_line(edges, threshold=10, line_length=5,
                                             line_gap=3)

            # Generating figure 2

            ax4.imshow(image, cmap=cm.gray)
            ax4.set_title('Input image')

            ax5.imshow(edges, cmap=cm.gray)
            ax5.set_title('Canny edges')

            Q = edges * 0

            ax6.imshow(Q)
            for line in lines:
                p0, p1 = line
                ax6.plot((p0[0], p1[0]), (p0[1], p1[1]))
            ax6.set_xlim((0, image.shape[1]))
            ax6.set_ylim((image.shape[0], 0))
            ax6.set_title('Probabilistic Hough')

            plt.tight_layout()

            fig.canvas.draw_idle()

            def SaveI():
                f = filedialog.asksaveasfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

                if f is None:
                    return

                filename = f.name

                cv2.imwrite(str(filename) + '.jpg', Q)
                f.close()

            btnw = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Save Straight line Hough transformed Image   ',
                             padx=20, bd='5',
                             command=SaveI)
            btnw.place(x=1000, y=0)


            fig.canvas.draw_idle()



            btnw.place(x=1000, y=0)



    if len(Original_image_Size) > 2:
        Dimension_Number = []
        Dimension_Number_int = []
        for x1 in range(Original_Image.shape[2]):
            Dimension_Number_int.append(x1 + 1)
            Dimension_Number.append(("Band ", x1 + 1))

    else:
        Dimension_Number = [("Band", 1)]

    if len(Original_image_Size) > 2:
        ttk.Label(root4, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root4, width=12, textvariable=number1)
        numberChosen1['values'] = (Dimension_Number_int)
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn = tk.Button(root4, bg='#000000', fg='#b7f731', text='  Straight line Hough transform  ', padx=20, bd='5',
                        command=HOUGHOneBand)
        btn.pack(anchor='w')

    else:
        tk.Label(root4, text="Choose a band:").pack(anchor='w')
        number1 = tk.StringVar()
        numberChosen1 = ttk.Combobox(root4, width=12, textvariable=number1)
        numberChosen1['values'] = "1"
        numberChosen1.pack(anchor='w')
        numberChosen1.current(0)
        btn1 = tk.Button(root4, bg='#000000', fg='#b7f731', text='   Straight line Hough transform   ', padx=20, bd='5',
                         command=HOUGHOneBand)
        btn1.pack(anchor='w')

    def Quit():
        root4.quit()
        root4.destroy()

    button = tk.Button(master=root4, bg='#000000', fg='#b7f731', text='       Quit        ', padx=20,
                       bd='5', command=Quit)
    button.pack(anchor='w')

    root4.mainloop()








root1 = tk.Tk()





root1.geometry("1920x1080")
img = ImageTk.PhotoImage(file='logo.png')
root1.tk.call('wm', 'iconphoto', root1._w, img)


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('Title.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root1, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=tk.BOTH, expand = 'YES')




root1.title("Khaje Nasir Toosi University of technology Image Processing Software(KNTUIPS)")

menubar1 = tk.Menu(root1)

filemenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))
filemenu.add_command(label="New", command=OPEN)
filemenu.add_command(label="Open", command=OPEN)
filemenu.add_command(label="Save", command=OPEN)
filemenu.add_command(label="Save as...", command=OPEN)
filemenu.add_command(label="Close", command=OPEN)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root1.quit)
menubar1.add_cascade(label="File", menu=filemenu)

Histogrammenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))

Histogrammenu.add_command(label="Show Histogram", command=Show_Histogram1)
Histogrammenu.add_command(label="Histogram Equalization", command=Equalization)
Histogrammenu.add_command(label="Binning", command=Binning)
Histogrammenu.add_command(label="CLAHE", command=clahe)
Histogrammenu.add_command(label="Brightness", command=Brightness)
Histogrammenu.add_command(label="Automatic Contrast Adjustment", command=ACA)
Histogrammenu.add_command(label="Histogram Matching", command=HisogramMatching)

menubar1.add_cascade(label="Histogram", menu=Histogrammenu)

Transformationmenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))
upoint = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))
Transformationmenu.add_cascade(label="Point Operation", menu=upoint)
upoint.add_command(label="Clamping", command=Clamping)
upoint.add_command(label="Inverting Image", command=Inverting)
upoint.add_command(label="Thresholding", command=Tresholding)
upoint.add_command(label="Intensity Windowing", command=IntensityWindowing)

uTransformation = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))
Transformationmenu.add_cascade(label="Gray Level Transformation", menu=uTransformation)
uTransformation.add_command(label="Logaritm Transformation", command=LogTr)
uTransformation.add_command(label="Power Transformation", command=PowerTr)

menubar1.add_cascade(label="Operation", menu=Transformationmenu)

Filteringmenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))
Spatial = tk.Menu(menubar1, tearoff=0)
Filteringmenu.add_cascade(label="Spatial Filtering", menu=Spatial)
Spatial.add_command(label="Averaging Filter", command=AverageFilter)
Spatial.add_command(label="Gaussian Filtering", command=GaussianFilter)
Spatial.add_command(label="Median Filtering", command=MedianFilter)

Sharpening = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))
Filteringmenu.add_cascade(label="Sharpening Filtering", menu=Sharpening)
Sharpening.add_command(label="Laplacian", command=Laplacian)
Sharpening.add_command(label="Simplified Image Enhancement", command=SIE)
Sharpening.add_command(label="Robertz Filtering", command=Robertz)
Sharpening.add_command(label="Prewitt Filtering", command=Prewitt)
Sharpening.add_command(label="Sobel Filtering", command=Sobel)
Filteringmenu.add_command(label="User Define Kernel", command=UDK)
Filteringmenu.add_command(label="Unsharp Masking", command=USM)

menubar1.add_cascade(label="Filtering", menu=Filteringmenu)

Noisemenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))

Noisemenu.add_command(label="Salt And Pepper", command=SAP)
Noisemenu.add_command(label="Gaussian Noise", command=GNoise)

menubar1.add_cascade(label="Noise", menu=Noisemenu)

Padmenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4,activeforeground='red2',fg='blue',bg='thistle4',font=('Franklin Gothic Demi Cond', 11))

Padmenu.add_command(label="Wrap", command=Wrap)
Padmenu.add_command(label="Reflect", command=Reflect)
Padmenu.add_command(label="Replicate", command=Replicate)
Padmenu.add_command(label="Constant", command=Constant)

menubar1.add_cascade(label="Padding", menu=Padmenu)

Frequencymenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))

Frequencymenu.add_command(label="Image Fourier Transform", command=IFT)
Frequencymenu.add_command(label="Custom High Pass Filtering", command=HPF)
Frequencymenu.add_command(label="Low pass Filter", command=LPFMask)
Frequencymenu.add_command(label="Band Pass Filter", command=HPFMask)

menubar1.add_cascade(label="Frequency", menu=Frequencymenu)

colormenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))

colormenu.add_command(label="Sequential", command=Sequential)
colormenu.add_command(label="Sequential2", command=Sequential2)
colormenu.add_command(label="Diverging", command=Diverging)
colormenu.add_command(label="Cyclic", command=Cyclic)
colormenu.add_command(label="Qualitative", command=Qualitative)
colormenu.add_command(label="Miscellaneouse", command=Miscellaneouse)
colormenu.add_command(label="Perceptually Uniform Sequential", command=PUS)

menubar1.add_cascade(label="Color Processing", menu=colormenu)

mormenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))

mormenu.add_command(label="Erosion", command=Erosion)
mormenu.add_command(label="Dilation", command=Dilation)
mormenu.add_command(label="Opening", command=Opening)
mormenu.add_command(label="Closing", command=Closing)
mormenu.add_command(label="Morphological Gradient", command=MG)
mormenu.add_command(label="Top Hat", command=TH)
mormenu.add_command(label="Black Hat", command=BH)
mormenu.add_command(label="Boundary Extraction", command=BE)
mormenu.add_command(label="Skeletonize", command=Skel)

menubar1.add_cascade(label="Morphological Operations", menu=mormenu)

segmenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))

Edge = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))
segmenu.add_cascade(label="Edge Detection", menu=Edge)
Edge.add_command(label="Robertz", command=Robertz)
Edge.add_command(label="Prewitt", command=Prewitt)
Edge.add_command(label="Sobel", command=Sobel)
Edge.add_command(label="Canny", command=Canny)
Edge.add_command(label="Straight line Hough transform", command=HOUGH)

trmenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))
segmenu.add_cascade(label="Tresholding", menu=trmenu)
trmenu.add_command(label="Simple Tresholding", command=Tresholding)
trmenu.add_command(label="Multiple Tresholding", command=MT)
trmenu.add_command(label="Adaptive Tresholding", command=AT)
trmenu.add_command(label="Otsu's Thresholding", command=OT)
trmenu.add_command(label="Variable Thresholding", command=VT)
trmenu.add_command(label="Simple Global Thresholding", command=SGT)

regionmenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))
segmenu.add_cascade(label="Region Base Segmentation", menu=regionmenu)
regionmenu.add_command(label="Splitting And Merging Segmentation", command=SAS)
regionmenu.add_command(label="Watershed", command=Watershed)
regionmenu.add_command(label="Seprate to abject by watershed", command=Watershed2)

menubar1.add_cascade(label="Segmentation", menu=segmenu)

editmenu = tk.Menu(menubar1, tearoff=0,activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))
editmenu.add_command(label="Undo", command=OPEN)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=OPEN)
editmenu.add_command(label="Copy", command=OPEN)
editmenu.add_command(label="Paste", command=OPEN)
editmenu.add_command(label="Delete", command=OPEN)
editmenu.add_command(label="Select All", command=OPEN)

menubar1.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar1, tearoff=0, activeborderwidth=4, activeforeground='red2', fg='blue', bg='thistle4', font=('Franklin Gothic Demi Cond', 11))
helpmenu.add_command(label="Help Index", command=OPEN)

helpmenu.add_command(label="About...", command=OPEN)
menubar1.add_cascade(label="Help", menu=helpmenu)

root1.config(menu=menubar1)
root1.mainloop()

