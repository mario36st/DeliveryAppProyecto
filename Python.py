import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#Función guardar datos
def registrar_datos():
    nombre_guardado = txt_nombre.get()
    direccion_guardada = txt_direccion.get()
    pedido_guardado = menu_pedido.get()
    print(f"Pedido registrado: {nombre_guardado} pidió {pedido_guardado} para llevar a {direccion_guardada}")
    #Acá validamos si no ingreso algo diciendole al usuario que vuelva a ingresar los datos.
    if not nombre_guardado or not direccion_guardada:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    #Guardamos en un archivo los pedidos
    with open("pedidos.txt", "a") as archivo:
        archivo.write(f"{nombre_guardado} | {direccion_guardada} | {pedido_guardado}\n") #Escribe en el documento de texto nombre, dirección y pedido guardado separados por barras (el \n garantiza salto de linea asi estan uno abajo de otro)
    messagebox.showinfo("Éxito", "¡Pedido guardado en el archivo correctamente!") #Muestra visual de pedido guardado

    txt_nombre.delete(0, tk.END)
    txt_direccion.delete(0, tk.END)

#Abajo creamos la ventana
ventana = tk.Tk()
ventana.title("Sistema de delivery")
ventana.geometry("400x500")
#Abajo ponemos los cuadros de texto
lbl_nombre = tk.Label(ventana, text="Nombre del Cliente:", font=("Arial", 10, "bold"))
lbl_nombre.pack(pady=5) # pady agrega un pequeño espacio arriba y abajo

# Creamos la caja donde el usuario va a escribir
txt_nombre = tk.Entry(ventana, font=("Arial", 11))
txt_nombre.pack(pady=5)

# --- CAMPO: DIRECCIÓN ---
lbl_direccion = tk.Label(ventana, text="Dirección de Entrega:", font=("Arial", 10, "bold"))
lbl_direccion.pack(pady=5)

txt_direccion = tk.Entry(ventana, font=("Arial", 11))
txt_direccion.pack(pady=5)

#Agregamos un menu de barra.
lbl_pedido = tk.Label(ventana, text="Seleccione el Pedido:", font=("Arial", 10, "bold"))
lbl_pedido.pack(pady=5)

# Creamos el menú desplegable
menu_pedido = ttk.Combobox(ventana, state="readonly", font=("Arial", 10))
# Le cargamos las opciones (una tupla de strings)
menu_pedido['values'] = ("Pizza", "Lomito", "Hamburguesa", "Empanadas")
menu_pedido.pack(pady=5)
menu_pedido.current(0) # Esto hace que la primera opción ("Pizza") aparezca seleccionada por defecto
#aqui creamos un boton para guardar las elecciones.
btn_registrar = tk.Button(ventana, text="Registrar Pedido", bg="green", fg="white", font=("Arial", 11, "bold"), command=registrar_datos)
btn_registrar.pack(pady=20)
ventana.mainloop()

