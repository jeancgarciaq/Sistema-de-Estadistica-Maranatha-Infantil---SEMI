import tkinter as tk
from view.area import Area

class Menu(tk.Menu):

    def __init__(self, app = None):
        self.app = app

    #Método Menú
    def createMenu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        inicio = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Inicio', menu=inicio)
        inicio.add_command(label='Áreas', command=Area.createArea)
        inicio.add_command(label='Salones')
        inicio.add_command(label='Salir', command=self.quit)

        enseñanza = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Enseñanza', menu=enseñanza)
        enseñanza.add_command(label='Edición')
        enseñanza.add_command(label='Búsqueda')

        otrasareas = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Otras áreas', menu=otrasareas)
        otrasareas.add_command(label='Edición')
        otrasareas.add_command(label='Búsqueda')

        logistica = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Logística', menu=logistica)
        logistica.add_command(label='Edición')
        logistica.add_command(label='Búsqueda')

        recepcion = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Recepción', menu=recepcion)
        recepcion.add_command(label='Edición')
        recepcion.add_command(label='Búsqueda')

        aula = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Aulas', menu=aula)
        aula.add_command(label='Edición')
        aula.add_command(label='Búsqueda')

        donaciones = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Donaciones', menu=donaciones)
        donaciones.add_command(label='Edición')
        donaciones.add_command(label='Búsqueda')

        comida = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Comidas repartidas', menu=comida)
        comida.add_command(label='Edición')
        comida.add_command(label='Búsqueda')

        ayuda = tk.Menu(menu, bg='#142850', fg='white', activebackground='#00a8cc', activeforeground='#fcfa70', font='Arial 10', tearoff=0)
        menu.add_cascade(label='Ayuda', menu=ayuda)
        ayuda.add_command(label='Manual')
        ayuda.add_command(label='Acerca de SEMI')
        