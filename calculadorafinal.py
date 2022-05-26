import tkinter
expr = ""

def limpiar():
    global expr
    expr = ""
    eq.set(expr)
    return


def apretar(num):
    global expr
    expr = expr + str(num)
    eq.set(expr)
    return


def calc():
    global expr

    tot = str(eval(expr))
    eq.set(tot)

    expr = tot
    return


def agregar_botones(gui):
    # Fila 1
    boton_limpiar = tkinter.Button(gui, text=" AC ", fg="black", bg="red",
                                   command=lambda: limpiar(), height=2, width=14)
    boton_limpiar.grid(row=4, column=0, columnspan=4, padx=5, pady=5 )
    boton_div = tkinter.Button(gui, text=" / ", fg="white", bg="orange",
                                   command=lambda: apretar("/"), height=2, width=5)
    boton_div.grid(row=4, column=3, padx=5, pady=5)

    # Fila 2
    bot7 = tkinter.Button(gui, text=' 7 ', fg='black', bg='dodger blue',
                     command=lambda: apretar(7), height=2, width=5)
    bot7.grid(row=5, column=0, padx=5, pady=5)
    bot8 = tkinter.Button(gui, text=' 8 ', fg='black', bg='dodger blue',
                     command=lambda: apretar(8), height=2, width=5)
    bot8.grid(row=5, column=1, padx=5, pady=5)
    bot9 = tkinter.Button(gui, text=' 9 ', fg='black', bg='dodger blue',
                     command=lambda: apretar(9), height=2, width=5)
    bot9.grid(row=5, column=2, padx=5, pady=5)
    bot_mult = tkinter.Button(gui, text=' X ', fg='white', bg='orange',
                     command=lambda: apretar("*"), height=2, width=5)
    bot_mult.grid(row=5, column=3, padx=5, pady=5)

    # Fila 3
    bot4 = tkinter.Button(gui, text=' 4 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(4), height=2, width=5)
    bot4.grid(row=6, column=0, padx=5, pady=5)
    bot5 = tkinter.Button(gui, text=' 5 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(5), height=2, width=5)
    bot5.grid(row=6, column=1, padx=5, pady=5)
    bot6 = tkinter.Button(gui, text=' 6 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(6), height=2, width=5)
    bot6.grid(row=6, column=2, padx=5, pady=5)
    bot_men = tkinter.Button(gui, text=' - ', fg='white', bg='orange',
                     command=lambda: apretar("-"), height=2, width=5)
    bot_men.grid(row=6, column=3, padx=5, pady=5)

    # Fila 4
    bot1 = tkinter.Button(gui, text=' 1 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(1), height=2, width=5)
    bot1.grid(row=7, column=0, padx=5, pady=5)
    bot2 = tkinter.Button(gui, text=' 2 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(2), height=2, width=5)
    bot2.grid(row=7, column=1, padx=5, pady=5)
    bot3 = tkinter.Button(gui, text=' 3 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(3), height=2, width=5)
    bot3.grid(row=7, column=2, padx=5, pady=5)
    bot_mas = tkinter.Button(gui, text=' + ', fg='white', bg='orange',
                     command=lambda: apretar("+"), height=2, width=5)
    bot_mas.grid(row=7, column=3, padx=5, pady=5)

    # Fila 5
    bot0 = tkinter.Button(gui, text=' 0 ', fg='black', bg='dodger blue',
                          command=lambda: apretar(0), height=2, width=13)
    bot0.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
    bot_punto = tkinter.Button(gui, text=' . ', fg='black', bg='dodger blue',
                          command=lambda: apretar("."), height=2, width=5)
    bot_punto.grid(row=8, column=2, padx=5, pady=5)
    bot_mas = tkinter.Button(gui, text=' = ', fg='white', bg='orange',
                     command=lambda: calc(), height=2, width=5)
    bot_mas.grid(row=8, column=3, padx=5, pady=5)

# Código Principal
if __name__ == "__main__":
    gui = tkinter.Tk()
    gui.configure(background="honeydew4")
    gui.title("Calculadora CASIO")
    gui.geometry("300x300")

    eq = tkinter.StringVar()

    campo_exp = tkinter.Entry(gui, textvariable=eq, font=("Calibri 20"))
    campo_exp.grid(columnspan=4, padx=5, pady=5)

    agregar_botones(gui)

    gui.mainloop()