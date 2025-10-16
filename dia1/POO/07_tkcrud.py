from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

class TkAlumno:
    
    def __init__(self,app):
        self.app = app
        self.app.title("CRUD Alumnos")
        self.app.geometry("640x480")
        
        frame = LabelFrame(self.app, text="Datos del Alumno")
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        
        ### DNI ###
        self.lb_dni = Label(frame, text="DNI: ")
        self.lb_dni.grid(row=1,column=0, pady=10, padx=10)
        self.txt_dni = Entry(frame)
        self.txt_dni.grid(row=1,column=1, pady=10, padx=10)
        
        ##### NOMBRE ####
        lb_nombre = Label(frame,text='NOMBRE : ')
        lb_nombre.grid(row=2,column=0, pady=10, padx=10)
        self.txt_nombre = Entry(frame)
        self.txt_nombre.grid(row=2,column=1, pady=10, padx=10)

        ##### EMAIL ####
        lb_email = Label(frame,text='EMAIL : ')
        lb_email.grid(row=3,column=0, pady=10, padx=10)
        self.txt_email = Entry(frame)
        self.txt_email.grid(row=3,column=1, pady=10, padx=10)
        
        ### TABLA DE ALUMNOS ###
        self.tree = Treeview(app)
        self.tree["columns"] = ("DNI","NOMBRE","EMAIL")
        
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("DNI", anchor=W, width=120)
        self.tree.column("NOMBRE", anchor=W, width=200)
        self.tree.column("EMAIL", anchor=W, width=200)
        
        self.tree.heading("#0", text="id")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("NOMBRE", text="NOMBRE")
        self.tree.heading("EMAIL", text="EMAIL")
        
        self.tree.grid(row=5,column=0,pady=20, padx=20)
        
        ### BOTONES ###
        self.btn_insertar = Button(frame,text="Insertar Nuevo Alumno", command=self.insertar_alumno)
        self.btn_insertar.grid(row=4,column=0,columnspan=2)
        
        self.btn_eliminar = Button(frame,text='Eliminar Alumno',command=self.eliminar_alumno)
        self.btn_eliminar.grid(row=5,column=0,columnspan=2)
    
    def insertar_alumno(self):
        dni = self.txt_dni.get()
        nombre = self.txt_nombre.get()
        email = self.txt_email.get()
        
        nuevo_alumno = (dni,nombre,email)
        self.tree.insert('',END,values=nuevo_alumno)
        
    def eliminar_alumno(self):
        seleccion = self.tree.selection()
        if seleccion:
            for item in seleccion:
                self.tree.delete(item)
        else:
            messagebox.showerror('alerta','Por favor seleciones un registro')
        
app = Tk()

if __name__ == "__main__":
    app_alumno = TkAlumno(app)
    app.mainloop()