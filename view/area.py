import tkinter as tk
from tkinter import ttk, messagebox
from model.database import Database

#Ventana Superior
app = tk.Toplevel()

class Area(tk.Frame):
    def __init__(self, app):
        super().__init__(app, width=800, height=600)
        self.app = app
        self.id_area = None
        

    def createArea(self):
        #Label de area
        self.label_nombre = tk.Label(self, text='Nombre: ', font='Arial 12 bold', padx=10, pady=10)
        self.label_nombre.grid(row=0, column=0)

        #Entradas de campos
        self.area_nombre = tk.StringVar()
        self.entry_area = tk.Entry(self, width=50, font='Arial 12', textvariable=self.area_nombre)
        self.entry_area.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        #botones
        self.boton_nuevo = tk.Button(self, text='Nuevo', bg='#00a8cc', width=20, font='Arial 12 bold', fg='#03d2fe', cursor='hand2', activebackground='#35bd6f',
                                     command=self.ableData)
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar', bg='#45eba5', width=20, font='Arial 12 bold', fg='#4cffb3', cursor='hand2', activebackground='#3586df', 
                                       command=self.saveData)
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', bg='#fdc57b', width=20, font='Arial 12 bold', fg='#ffe2bd', cursor='hand2', activebackground='#e15370',
                                        command=self.unableData)
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def ableData(self):
        self.area_nombre.set('')
        self.entry_area.configure(state='normal')
        self.boton_guardar.configure(state='normal')
        self.boton_cancelar.configure(state='normal')

    def unableData(self):
        self.id_area = None
        self.area_nombre.set('')
        self.entry_area.configure(state='disabled')
        self.boton_guardar.configure(state='disabled')
        self.boton_cancelar.configure(state='disabled')
        
    def saveData(self):
        area = Database(self.area_nombre.get())
            
        if self.id_area == None:
                area.guardar()
        else:
                area.editar(self.id_area)
            
        self.createTable()
        self.unableData()

    def createTable(self):
        #Creamos la tabla
        self.tabla = ttk.Treeview(self, column = ('Nombre'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        #Scrollbar para > 10 registros
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        # Creamos sus encabezados
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')

        #iterar sobre los datos recuperados
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1]))
        
        #botones
        self.boton_editar = tk.Button(self, text='Editar', bg='#fcfa70', width=20, font='Arial 12 bold', fg='#fcfbad', cursor='hand2', activebackground='#35bd6f', command=self.editaData)
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text='Eliminar', bg='#ed6363', width=20, font='Arial 12 bold', fg='#ff6e6e', cursor='hand2', activebackground='#e15370', command=self.deleteData)
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
    
    def editData(self):
        try:
            self.id_area = self.tabla.item(self.tabla.selection())['text']
            self.area_nombre = self.tabla.item(self.tabla.selection())['values'][0]

            self.unableData()

            self.entry_area.insert(0, self.area_nombre)
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')

    def deleteData(self):
        try:
            self.id_area = self.tabla.item(self.tabla.selection())['text']
            Database.eliminar(self.id_area)
            self.createTable()
            self.id_area = None
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')