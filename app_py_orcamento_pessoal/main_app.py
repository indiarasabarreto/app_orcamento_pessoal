from tkinter import *
from tkinter import Tk, ttk

#importando pillow
from PIL import Image, ImageTk


# cores
co0 = "#2e2d2b" #Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" # - ProFit
co6 = "#038cfc" # Azul
co7 = "#3fbfb9" # Verde
c08 = "#263138" # + Verde
co9 = "#e9edf5" # + Verde7
co10 = "#6e8jaj"
co11 = "#f2f4f2"

# criando janela

janela = Tk()
janela.title("")
janela.geometry('250x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')


# Frames
frame_cima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=300, height=90, bg=co1, relief="flat")
frame_meio.grid(row=1, column=0)

frame_baixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frame_baixo.grid(row=2, column=0)


# Logo ------------------------------------------------------------
app_ = Label(frame_cima, text='Orçamento', compound=LEFT, padx=5, relief='flat', anchor=NW, font=('Verdana 20'), bg=co1, fg=co4)

app_.place(x=0, y=0)

# abrindo imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1, fg=co4)

app_logo.place(x=160, y=0)

app_linha = Label(frame_cima, width=295, relief=FLAT, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)

app_linha.place(x=0, y=47)


# Função Calcular
def calcular():
    renda_mensal = float(e_valor.get())

    # Obtendo as percentagens
    obter_50_porcento = ( 40 / 100) * renda_mensal
    obter_30_porcento = ( 45 / 100) * renda_mensal
    obter_20_porcento = ( 10 / 100) * renda_mensal
    
    l_necessidades['text'] = ("R${:,.2f}".format(obter_50_porcento))
    l_gastos['text'] = ("R${:,.2f}".format(obter_30_porcento))
    l_poupanca['text'] = ("R${:,.2f}".format(obter_20_porcento))  


# Frame Meio -------------------------------------------------
app_ = Label(frame_meio, text='Renda Mensal', relief=FLAT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
app_.place(x=7, y=15)


e_valor = Entry(frame_meio, width=10, font=('Ivy 14'), justify='center', relief='solid')
e_valor.place(x=10, y=40)

b_calcular = Button(frame_meio, command=calcular, text='Calcular'.upper(), overrelief=RIDGE, anchor=NW, font=('Ivy 9'), bg=co1, fg=co0)
b_calcular.place(x=150, y=40)


# Frame Baixo ---------------------------------------------------
app_ = Label(frame_baixo, text='Seus valores de 50%, 30%, 20%', relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=co3, fg=co1)
app_.place(x=0, y=0)


# Total - Necessidades ---------------------------------------------------
l_total_necessidades = Label(frame_baixo, text='Necessidades', relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=co9, fg=co0)
l_total_necessidades.place(x=10, y=40)

l_necessidades = Label(frame_baixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
l_necessidades.place(x=10, y=75)


# Total - Gastos ---------------------------------------------------
l_total_gastos = Label(frame_baixo, text='Gastos', relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=co9, fg=co0)
l_total_gastos.place(x=10, y=115)

l_gastos = Label(frame_baixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
l_gastos.place(x=10, y=145)


# Total - Poupança ---------------------------------------------------
l_total_poupanca = Label(frame_baixo, text='Poupança', relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=co9, fg=co0)
l_total_poupanca.place(x=10, y=185)

l_poupanca = Label(frame_baixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
l_poupanca.place(x=10, y=215)


janela.mainloop()
