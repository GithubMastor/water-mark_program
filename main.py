import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import subprocess


winder = tk.Tk()
winder.iconbitmap('favicon.ico')
winder.geometry("450x450")  # Size of the window
winder.title('          watermark-program')
winder.configure(bg='#FFFFFF')
my_font1=('times', 18, 'bold')
label1 = tk.Label(winder,text='',width=30,font=my_font1)
label1.configure(bg='#FFFFFF')
label1.grid(row=1,column=1,columnspan=4)
button1 = tk.Button(winder, text='Browse Files',width=20,command = lambda:upload_file())
btn_img = Image.open('button_upload-image.png')
imz = ImageTk.PhotoImage(btn_img)
button1.configure(image=imz, width=imz.width(), bg='#FFFFFF',borderwidth=0)
button1.grid(row=2,column=1,columnspan=4, padx=10, pady=10)
btna_img = Image.open('button_apply-watermark.png')
ima = ImageTk.PhotoImage(btna_img)


def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select
    filename = tk.filedialog.askopenfilename(multiple=False,filetypes=f_types)
    img = Image.open(filename)
    imgx = 220
    imgy = round((220/img.size[0])*img.size[1])
    img = img.resize((imgx, imgy))  # new width & height
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(winder)
    e1.grid(row=4, column=2, columnspan=2)
    e1.image = img
    e1['image'] = img

    search_button = Button(text="Apply Watermark", width=30, command=lambda: watermarker(filename))
    search_button.configure(image=ima, width=ima.width(), bg='#FFFFFF',borderwidth=0)
    search_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

def imgpath(path):
    name = path.split('/')[-1]
    name = name.split('.')
    loc = path.split('/')[0:-1]
    new_path = '/'.join(loc) + '/'
    name[1] = new_path
    return name

def watermarker(imz):
    image = Image.open(imz)
    draw = ImageDraw.Draw(image)
    txt = "watermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\nwatermark -- watermark -- watermark -- watermark -- watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --watermark -- watermark -- watermark --\n\n\n"
    fontsize = round(image.size[1] / 25)
    font = ImageFont.truetype("arial.ttf", fontsize)
    draw.text((10, 25), txt, fill=(0, 0, 0, 127), font=font)
    imgnmz = imgpath(image.filename)
    image.show('wtrmrk_' + imgnmz[0])
    image.save(imgnmz[1] + 'wtrmrk_' + imgnmz[0] + '.jpg')



winder.mainloop()  # Keep the window open