#import sys
#sys.path.append("C:/xampp/htdocs/SEMI/model")
import tkinter as tk
from tkinter import ttk, messagebox
from model.semi import Areas


class Area:
    #Constructor
    def __init__(self, window = None):
        #Ventana secundaria
        self.window = tk.Toplevel()
        self.window.configure(width=800, height=600, bg="#142850")
        self.window.title("Sistema Estadístico Maranatha Infantil - Áreas")
        #marco
        marco = tk.Frame(self.window)
        marco.grid(row=0, column=0, sticky="nw")  
        #Id datos
        self.id = None
        self.sql = ''

        self.createArea()
        self.window.mainloop()
    
    def createArea(self):
        #Label de area
        self.label_nombre = tk.Label(self.marco, text='Nombre: ', font='Arial 12 bold', padx=10, pady=10)
        self.label_nombre.grid(row=0, column=0)

        #Entradas de campos
        self.area_nombre = tk.StringVar()
        self.entry_area = tk.Entry(self.marco, width=50, font='Arial 12', textvariable=self.area_nombre)
        self.entry_area.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        #botones
        self.boton_nuevo = tk.Button(self.marco, text='Nuevo', bg='#00a8cc', width=20, font='Arial 12 bold', fg='#03d2fe', cursor='hand2', activebackground='#35bd6f',
                                     command=self.ableData)
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self.marco, text='Guardar', bg='#45eba5', width=20, font='Arial 12 bold', fg='#4cffb3', cursor='hand2', activebackground='#3586df', 
                                       command=self.saveData)
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self.marco, text='Cancelar', bg='#fdc57b', width=20, font='Arial 12 bold', fg='#ffe2bd', cursor='hand2', activebackground='#e15370',
                                        command=self.unableData)
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def ableData(self):
        self.area_nombre.set('')
        self.entry_area.configure(state='normal')
        self.boton_guardar.configure(state='normal')
        self.boton_cancelar.configure(state='normal')

    def unableData(self):
        self.id = None
        self.area_nombre.set('')
        self.entry_area.configure(state='disabled')
        self.boton_guardar.configure(state='disabled')
        self.boton_cancelar.configure(state='disabled')
        
    def saveData(self):
        self.area = self.area_nombre.get()
            
        if self.id == None:
            Areas.create(nombre = self.area)
        else:
            Areas.save()
            
        self.createTable(self)
        self.unableData(self)

    def createTable(self):
        #Importar los datos de la tabla
        self.lista_areas = Areas.select().dict()
        
        #Creamos la tabla
        tabla = ttk.Treeview(self.marco, column = ('Nombre'))
        tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        #Scrollbar para > 10 registros
        scroll = ttk.Scrollbar(self.marco, orient='vertical', command=tabla.yview)
        scroll.grid(row=4, column=4, sticky='nse')
        tabla.configure(yscrollcommand=scroll.set)

        # Creamos sus encabezados
        tabla.heading('#0', text='ID')
        tabla.heading('#1', text='NOMBRE')

        #iterar sobre los datos recuperados
        for a in self.lista_areas:
            tabla.insert('', 0, text=a[0], values=(a[1]))
        
        #botones
        boton_editar = tk.Button(self.marcos, text='Editar', bg='#fcfa70', width=20, font='Arial 12 bold', fg='#fcfbad', cursor='hand2', activebackground='#35bd6f', command=self.editaData)
        boton_editar.grid(row=5, column=0, padx=10, pady=10)

        boton_eliminar = tk.Button(self.marcos, text='Eliminar', bg='#ed6363', width=20, font='Arial 12 bold', fg='#ff6e6e', cursor='hand2', activebackground='#e15370', command=self.deleteData)
        boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
    
    def editData(self):
        try:
            self.id = self.tabla.item(self.tabla.selection())['text']
            self.area_nombre = self.tabla.item(self.tabla.selection())['values'][0]

            self.unableData()

            self.entry_area.insert(0, self.area_nombre)
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')

    def deleteData(self):
        try:
            self.id = self.tabla.item(self.tabla.selection())['text']
            self.areas = Areas.get(Areas.id == self.id)
            self.areas.delete_instance()
            self.createTable()
            self.id = None
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')
