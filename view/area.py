import sys
sys.path.append("C:/xampp/htdocs/SEMI/model")
import tkinter as tk
from tkinter import ttk, messagebox
from database import Database


def DesplegarAreas():
    #Ventana Superior
    window = tk.Toplevel()
    window.configure(width=800, height=600, bg="#142850")
    window.title("Sistema Estadístico Maranatha Infantil - Áreas")

    #marco
    marco = tk.Frame(window)
    marco.grid(row=0, column=0, sticky="nw")      
    
    def createArea():
        #Label de area
        label_nombre = tk.Label(marco, text='Nombre: ', font='Arial 12 bold', padx=10, pady=10)
        label_nombre.grid(row=0, column=0)

        #Entradas de campos
        area_nombre = tk.StringVar()
        entry_area = tk.Entry(marco, width=50, font='Arial 12', textvariable=area_nombre)
        entry_area.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        #botones
        boton_nuevo = tk.Button(marco, text='Nuevo', bg='#00a8cc', width=20, font='Arial 12 bold', fg='#03d2fe', cursor='hand2', activebackground='#35bd6f',
                                     command=ableData)
        boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        boton_guardar = tk.Button(marco, text='Guardar', bg='#45eba5', width=20, font='Arial 12 bold', fg='#4cffb3', cursor='hand2', activebackground='#3586df', 
                                       command=saveData)
        boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        boton_cancelar = tk.Button(marco, text='Cancelar', bg='#fdc57b', width=20, font='Arial 12 bold', fg='#ffe2bd', cursor='hand2', activebackground='#e15370',
                                        command=unableData)
        boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def ableData(s):
        area_nombre.set('')
        entry_area.configure(state='normal')
        boton_guardar.configure(state='normal')
        boton_cancelar.configure(state='normal')

    def unableData(s):
        id_area = None
        area_nombre.set('')
        entry_area.configure(state='disabled')
        boton_guardar.configure(state='disabled')
        boton_cancelar.configure(state='disabled')
        
    def saveData(s):
        area = Database(area_nombre.get())
            
        if id_area == None:
                area.guardar()
        else:
                area.editar(id_area)
            
        createTable()
        unableData()

    def createTable(s):
        #Importar los datos de la tabla


        #Creamos la tabla
        tabla = ttk.Treeview(s, column = ('Nombre'))
        tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        #Scrollbar para > 10 registros
        scroll = ttk.Scrollbar(s, orient='vertical', command=tabla.yview)
        scroll.grid(row=4, column=4, sticky='nse')
        tabla.configure(yscrollcommand=scroll.set)

        # Creamos sus encabezados
        tabla.heading('#0', text='ID')
        tabla.heading('#1', text='NOMBRE')

        #iterar sobre los datos recuperados
        for p in lista_peliculas:
            tabla.insert('', 0, text=p[0], values=(p[1]))
        
        #botones
        boton_editar = tk.Button(s, text='Editar', bg='#fcfa70', width=20, font='Arial 12 bold', fg='#fcfbad', cursor='hand2', activebackground='#35bd6f', command=editaData)
        boton_editar.grid(row=5, column=0, padx=10, pady=10)

        boton_eliminar = tk.Button(s, text='Eliminar', bg='#ed6363', width=20, font='Arial 12 bold', fg='#ff6e6e', cursor='hand2', activebackground='#e15370', command=deleteData)
        boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
    
    def editData(s):
        try:
            id_area = tabla.item(tabla.selection())['text']
            area_nombre = tabla.item(tabla.selection())['values'][0]

            unableData()

            entry_area.insert(0, area_nombre)
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')

    def deleteData(s):
        try:
            id_area = tabla.item(tabla.selection())['text']
            Database.eliminar(id_area)
            createTable()
            id_area = None
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')

    window.mainloop()