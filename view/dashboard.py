from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from database.database import *


class Dashboard(Frame):
    def __init__(self, app=None):
        super().__init__(app, width=800, height=600)
        self.app = app
        #Scrollbar
        self.h = ttk.Scrollbar(self.app, orient=HORIZONTAL)
        self.v = ttk.Scrollbar(self.app, orient=VERTICAL)
        # Canvas adjuntar scrollbar
        self.canvas = Canvas(self.app, yscrollcommand=self.v.set, xscrollcommand=self.h.set)
        self.h['command'] = self.canvas.xview
        self.v['command'] = self.canvas.yview
        self.createDashboard()


    def createDashboard(self):
        '''Reset the scroll region to encompass the inner frame'''
        def onFrameConfigure(canvas): 
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        #Marco contenedor
        self.marco = Frame(self.canvas, bg='#142850')
        
        #Empaquetado del canvas
        self.v.pack(side="right", fill="y")
        self.h.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((8,6), window=self.marco, anchor="nw")

        # Etiqueta de título
        self.encabezado = Label(self.marco, text="Tablero", font="Arial 36 bold", fg='white', bg='#142850')
        self.encabezado.grid(row=0, column=0, padx=20, pady=10)

        plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color=["#00a8cc", "#45eba5", "#fdc57b", "#fcfa70", "#ed6363", "#ffe2bd", "#ff6e6e", "#fcfbad"])
        
        # Gráfico Salón Cuna y Gateo
        self.fg1, self.ax1 = plt.subplots()
        self.ax1.bar(cuna_gateo.keys(), cuna_gateo.values())
        self.ax1.set_title("Maternal: Salón Cuna y Gateo")
        self.ax1.set_xlabel("Servidores-Infantes")
        self.ax1.set_ylabel("Cantidad")

        # Gráfico Total Maternal
        self.fg2, self.ax2 = plt.subplots()
        self.ax2.bar(total.keys(), total.values())
        self.ax2.set_title("Maternal: Total Servidores, Niños y Niñas")
        self.ax2.set_xlabel("Servidores-Infantes")
        self.ax2.set_ylabel("Cantidad")

        # Gráfico Otros Servidores
        self.explode = (0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1)
        self.fg3, self.ax3 = plt.subplots()
        self.ax3.pie(otras_areas.values(), explode=self.explode, labels=otras_areas.keys(), shadow=True, startangle=90)
        self.ax3.set_title("Servidores Otras Áreas")

        #Función lambda
        self.marco.bind("<Configure>", lambda event, canvas=self.canvas: onFrameConfigure(canvas))

        # Despliegue de gráficos
        self.canvas1 = FigureCanvasTkAgg(self.fg1, self.marco)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().grid(row=1, column=0, padx=20, pady=20)

        self.canvas2 = FigureCanvasTkAgg(self.fg2, self.marco)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().grid(row=2, column=0, padx=20, pady=20)

        self.canvas3 = FigureCanvasTkAgg(self.fg3, self.marco)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().grid(row=3, column=0, padx=20, pady=20)


        #Tabla de Datos
        #Encabezado tabla salón cuna y gateo
        self.tabla = ttk.Treeview(self.marco, column=('niños', 'niñas', 'maestra', 'auxiliar', 'colaborador'))
        self.tabla.grid(row=1, column=1, sticky='nse')
        self.tabla.heading('#0', text='NIÑOS')
        self.tabla.heading('#1', text='NIÑAS')
        self.tabla.heading('#2', text='MAESTRAS')
        self.tabla.heading('#3', text='AUXILIARES')
        self.tabla.heading('#4', text='COLABORADORES')

        #iterar sobre los datos recuperados
        self.salon = {}
        self.salon = cuna_gateo
        for d in self.salon.values():
            self.tabla.insert('',0, values=(d))
            