from conexion import ConexionDB
from tkinter import messagebox



def borrar_tabla(name: str):
    conexion = ConexionDB()

    if isinstance(name, str):
        sql = 'DROP TABLE ' + name

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('¡Borrar Tabla!', 'Se ha borrado exitosamente la tabla en la Base de Datos')
    except:
        messagebox.showerror('¡Borrar Tabla!', 'La tabla peliculas no existe en la Base de Datos')

class Database:
    def __init__(self, nombre):
        self.id_area = None
        self.nombre = nombre
    
    def __str__(self):
        return f'Database[{self.nombre}, {self.duracion}, {self.genero}]'

    def guardar(area):
        conexion = ConexionDB()
        
        sql = f"""INSERT INTO areas (nombre)
            VALUES('{area.nombre}')"""
        
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            messagebox.showinfo('Guardar Registro', 'Se ha guardado el registro exitosamente')
        except:
            messagebox.showerror('Error', 'No está creada la tabla en la Base de Datos')
    
    def listar():
        conexion = ConexionDB()

        lista_peliculas = []
        sql = 'SELECT * FROM peliculas'

        try:
            conexion.cursor.execute(sql)
            lista_peliculas = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            messagebox.showwarning('¡Advertencia', 'La tabla no existe en la base de datos')
        
        return lista_peliculas

    def editar(pelicula, id_pelicula):
        conexion = ConexionDB()

        sql = f"""UPDATE peliculas
                SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
                WHERE id_pelicula = '{id_pelicula}'"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            messagebox.showinfo('Actualización', 'Se ha actualizado exitosamente')
        except:
            messagebox.showwarning('Error', 'No se ha podido actualizar el registro')

    def eliminar(id_pelicula):
        conexion = ConexionDB()
        sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

        try:
            conexion.cursor.execute(sql)
            messagebox.askyesno('Borrar Registro', '¿Está seguro de Borrar el Registro?')
            conexion.cerrar()
        except:
            messagebox.showerror('Error', 'No se ha podido eliminar el Registro')
