import tkinter as tk
from view.menu import Menu
#from view.dashboard import Dashboard


def main():
    #Ventana Principal
    app = tk.Tk()
    app.configure(bg='#142850', width=800, height=600)
    app.title('Sistema Estadístico Maranatha Infantil')
    app.iconbitmap('public/img/kids.ico')
    app.state('zoomed')
    Menu.createMenu(app)
    #dashboard = Dashboard(app)
    #dashboard.createDashboard()
    app.mainloop()


if __name__ == '__main__':
    main()
