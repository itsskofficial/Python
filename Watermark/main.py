from io import BytesIO
import tkinter
from tkinter import NW, messagebox
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont

def image_file():
    file=askopenfile(mode='rb',filetypes=[('JPG File', '*.jpg'),('PNG File','*.png')])
    if file is not None:
        img_bytes=file.read()
        stream = BytesIO(img_bytes)
        img = Image.open(stream).convert("RGB")
        stream.close()
        img.save(fp="userimage.jpg")
        watermark_page()
    else:
        messagebox.showerror('Upload error','No such file found')

def watermark_page():
    global canvas1
    global label1
    global button1
    global button2
    global canvas2
    global image_on_canvas
    canvas1.destroy()
    label1.destroy()
    button1.destroy()
    canvas2 = tkinter.Canvas(screen, height=300, width=300, bg="black")
    canvas2.place(x=100, y=50)
    img=Image.open("userimage.jpg")
    print(img)
    resized_img=img.resize((300,300),Image.ANTIALIAS)
    new_img=ImageTk.PhotoImage(image=resized_img)
    print(new_img)
    resized_img.save(fp='resizedimage.jpg')
    screen.new_img=new_img
    image_on_canvas=canvas2.create_image((0,0),image=new_img,anchor=tkinter.NW)
    button2=tkinter.Button(screen,text="Watermark image",command=watermark_image)
    button2.place(x=200,y=400)

def watermark_image():
    img=Image.open("resizedimage.jpg")
    base=img.convert("RGBA")
    text=Image.new("RGBA",base.size,(255,255,255,0))
    d=ImageDraw.Draw(text)
    fnt = ImageFont.truetype("arial.ttf", 40)
    d.text((0,0),"SK",font=fnt, fill=(255,255,255,128))
    out=Image.alpha_composite(base,text)
    final_out=out.convert("RGB")
    final_out.save(fp='finalimage.jpg')
    final_page()

def final_page():
    global canvas2
    global button2
    global image_on_canvas
    img=Image.open('finalimage.jpg')
    final_img=ImageTk.PhotoImage(image=img)
    screen.final_img=final_img
    canvas2.itemconfig(image_on_canvas,image=final_img)
    button2.config(text="Download image", command=download_image)

def download_image():
    img=Image.open('finalimage.jpg')
    img.save(fp=r"C:/Users/sarth/Downloads/watermarked_image.jpg")
    screen.quit()
    
screen = tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas1 = tkinter.Canvas(screen, height=100, width=100, bg="black")
canvas1.place(x=200, y=50)
logo=Image.open("logo.jpg")
print(logo)
resized_logo=logo.resize((100,100),Image.ANTIALIAS)
new_logo=ImageTk.PhotoImage(image=resized_logo)
print(new_logo)
canvas1.create_image((0, 0), image=new_logo, anchor=tkinter.NW)
label1 = tkinter.Label(screen, text="Get your image watermarked", font=('Montserrat 10 bold'))
label1.place(x=155, y=200)
button1=tkinter.Button(screen,text="Upload image",command=image_file)
button1.place(x=205,y=250)
screen.mainloop()