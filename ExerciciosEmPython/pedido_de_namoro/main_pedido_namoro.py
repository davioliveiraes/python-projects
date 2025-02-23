import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

def move_button_1(event):
   if abs(event.x_root - button_1.winfo_rootx()) < 50 and abs(event.y_root - button_1.winfo_rooty()) < 50:
      x = random.randint(0, root.winfo_width() - button_1.winfo_width())
      y = random.randint(0, root.winfo_height() - button_1.winfo_height())
   button_1.place(x=x, y=y)

def order_accepted():
   messagebox.showinfo(
   
      'Eu te amo hoje e sempre <3', 'Você tomou a melhor decisão da sua vida'
   
   )

def request_denied():
   button_1.destroy()

root = tk.Tk()
root.title("PEDIDO DE NAMORO")
root.geometry('600x600')
root.configure(background='#8747A0')

margin = Canvas(root, width=600, bg='#8747A0', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = Label(root, bg='#8747A0', text='QUER NAMORAR COMIGO?', fg='#C29AF3', font=('Segoe', 30, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#B36DF5', command=request_denied, relief=RIDGE, bd=5, font=('Segoe', 10, 'bold'))
button_1.place(x=0, y=0)

root.bind('<Motion>', move_button_1)

button_2 = tk.Button(root, text='Sim', bg='#F517AD', relief=RIDGE, bd=5, command=order_accepted, font=('Segoe', 20, 'bold'))
button_2.pack()

image = PhotoImage(file=r"C:\Users\Davil\OneDrive\Documentos\Practice\Python\ExerciciosEmPython\pedido_de_namoro\coracaoFlecha.png")
label = Label(root, image=image, bg="#8747A0")
label.pack()

root.mainloop()
