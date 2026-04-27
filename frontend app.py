import customtkinter as ctk

import customtkinter as ctk
from tkinter import ttk
from models import *

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Empresarial")
        self.geometry("1000x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.sidebar = ctk.CTkFrame(self, width=180)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        opciones = [
            ("Recetas", self.mostrar_recetas),
            ("Clientes", self.mostrar_clientes),
            ("Eventos", self.mostrar_eventos),
            ("Pedidos", self.mostrar_pedidos),
            ("Calendario", self.mostrar_calendario),
            ("Historial", self.mostrar_historial),
        ]

        for texto, comando in opciones:
            ctk.CTkButton(self.sidebar, text=texto, command=comando)\
                .pack(fill="x", padx=10, pady=5)


        self.main = ctk.CTkFrame(self)
        self.main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        #=========================
        self.header = ctk.CTkFrame(self.main, height=60)
        self.header.grid(row=0, column=0, sticky="ew")

        self.titulo = ctk.CTkLabel(self.header, text="Página actual", font=("Arial", 18))
        self.titulo.pack(side="left", padx=10)

        ctk.CTkLabel(self.header, text="LOGO", fg_color="#f97316", width=120)\
            .pack(side="right", padx=10)

        
        self.contenido = ctk.CTkFrame(self.main)
        self.contenido.grid(row=1, column=0, sticky="nsew")

        self.mostrar_recetas()

    
    def cambiar_vista(self, titulo):
        self.titulo.configure(text=titulo)

        for widget in self.contenido.winfo_children():
            widget.destroy()


    def mostrar_recetas(self):
        self.cambiar_vista("Recetas")

        search = ctk.CTkEntry(self.contenido, placeholder_text="Buscar receta...")
        search.pack(fill="x", padx=10, pady=5)

        tree = ttk.Treeview(self.contenido, columns=("Nombre",), show="headings")
        tree.heading("Nombre", text="Nombre de receta")
        tree.pack(fill="both", expand=True, padx=10)

        try:
            recetas = obtenerRecetas()
            for r in recetas:
                tree.insert("", "end", values=(r[1],))

        except Exception as e:
            ctk.CTkLabel(
                self.contenido,
                text="No hay base de datos o tabla 'recetas'",
                text_color="red"
            ).pack(pady=10)

        btn_frame = ctk.CTkFrame(self.contenido)
        btn_frame.pack(pady=10)

        ctk.CTkButton(btn_frame, text="Añadir").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Cambiar").pack(side="left", padx=5)


    def mostrar_clientes(self):
        self.cambiar_vista("Clientes")

        tree = ttk.Treeview(self.contenido, columns=("Nombre","Teléfono"), show="headings")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Teléfono", text="Teléfono")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        try:
            clientes = obtenerClientes()
            for c in clientes:
                tree.insert("", "end", values=(c[1], c[2]))

        except:
            ctk.CTkLabel(
                self.contenido,
                text="No hay tabla de clientes",
                text_color="red"
            ).pack()

    # ===========================
    def mostrar_eventos(self):
        self.cambiar_vista("Eventos")
        ctk.CTkLabel(self.contenido, text="Eventos").pack()

    def mostrar_pedidos(self):
        self.cambiar_vista("Pedidos")
        ctk.CTkLabel(self.contenido, text="Pedidos").pack()

    def mostrar_calendario(self):
        self.cambiar_vista("Calendario")

        grid = ctk.CTkFrame(self.contenido)
        grid.pack(pady=20)

        for i in range(6):
            for j in range(7):
                ctk.CTkLabel(grid, text="", width=40, height=40, fg_color="#e5e7eb")\
                    .grid(row=i, column=j, padx=2, pady=2)

    def mostrar_historial(self):
        self.cambiar_vista("Historial")
        ctk.CTkLabel(self.contenido, text="Historial").pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()

