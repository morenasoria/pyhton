from tkinter import Tk, Menu, messagebox, simpledialog, Text, Button
import pandas as pd

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.namearchivo='/home/quintob/Documentos/rodrigo lenis/programacion/clasesmenu.xlsx'
        self.estudiantes = pd.read_excel(self.namearchivo)
        print(self.namearchivo)
        

        self.text_area= Text(master,wrap='word',height=20,width=60)
        self.text_area.pack(side='left',fill='both',expand=True)

    def create_menu(self):
        # Crear la barra de menú
        barra_menus = Menu(self.master)
       
    
        # Crear el menú "Excel"
        menu_calculo=Menu(barra_menus,tearoff=0)
        menu_excel = Menu(barra_menus, tearoff=0)
        menu_salir = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Exel", menu=menu_excel)
        barra_menus.add_cascade(label="Calculo",menu=menu_calculo)
        barra_menus.add_cascade(label="Salir", menu=menu_salir,command=self.salir )

        # Agregar opciones al menú "Excel"
        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)

        menu_calculo.add_command(label="Lpromedios", command=self.promedio)
        menu_calculo.add_command(label="Lmedia", command=self.mediana)
        menu_calculo.add_command(label="Lmoda", command=self.moda)
        menu_salir.add_command(label="salir", command=self.master.quit)   
          
        # Configurar la barra de menú en la ventana principal
        self.master.config(menu=barra_menus)

    def clear_text_area(self):
        self.text_area.delete(1.0,'end')

    def show_all(self):
        print(self.estudiantes)
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes))
    

    def promedio(self):
        estu=self.estudiantes
        promedio=estu["edad"].mean()
        messagebox.showinfo("Promedio:"," El promedio es:"+str(promedio))

    def mediana(self):
        estu=self.estudiantes
        mediana=estu["edad"].median()
        messagebox.showinfo("Mediana:","la mediana es iguak a:"+str(mediana))
    
    def moda(self):
        estu=self.estudiantes
        moda=estu["nombre"].mode()
        messagebox.showinfo("moda:","la moda es:"+str(moda))
        

    

    def show_name(self):
        mayores= self.estudiantes.query("edad>=18")
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["nombre"]))
            


    def show_over_18(self):
        mayores= self.estudiantes.query("edad>=18")
        self.clear_text_area()
        self.text_area.insert('end',str(mayores))


    def salir(self):
        breakpoint
        
        
        


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        
        # Crear el menú
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

