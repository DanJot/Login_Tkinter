
from tkinter import *
from tkinter.ttk import *


jan = Tk()
jan.geometry("400x350+600+250")

cores = IntVar()
paises = IntVar()

r1 = Radiobutton(jan, text="Preto", value=1, variable=cores)
r2 = Radiobutton(jan, text="Branco", value=2, variable=cores)
r3 = Radiobutton(jan, text="Rosa", value=3, variable=cores)

r4 = Radiobutton(jan, text="Portugal", value=1, variable=paises)
r5 = Radiobutton(jan, text="Brasil", value=2, variable=paises)


combo = Combobox(jan, values=["Ana", "Pedro"], state="readonly") #readonly não permite escrever na caixa de escolha
combo.pack()

r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()

jan.mainloop()