from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import ImageTk, Image


class MainView:

    def __init__(self, root_window, terreno):
        self.main_container = Frame(root_window)
        self.main_container.grid(row=0, column=0)
        self.btn_container = Frame(root_window)
        self.btn_container.grid(row=0, column=1)
        self.iniciar_btn = Button(self.btn_container, text="Iniciar algoritmo")
        self.iniciar_btn.grid(row=0, column=0)
        self.checkbox_value = BooleanVar(root_window)
        self.FastGeneration = Checkbutton(self.btn_container,text= "Obtener primero en objetivo",variable=self.checkbox_value,)
        self.FastGeneration.grid(row=1,column=0)

        # Algorithm information
        self.algorithm_info_container = Frame(root_window)
        self.algorithm_info_container.grid(row=1, column=0, sticky="W")
        # Fitness label
        self.generation_fitness_label = Label(self.algorithm_info_container, text="Fitness: ", anchor=W, justify=LEFT)
        self.generation_fitness_label.grid(row=0, column=0)
        # Generations label
        self.generation_number_label = Label(self.algorithm_info_container, text="Generaciones: ", anchor=W, justify=LEFT)
        self.generation_number_label.grid(row=1, column=0)
        # Generation input group
        self.generation_input_group = Frame(self.algorithm_info_container)
        self.generation_input_group.grid(row=0, column=1)
        # Label para entrada de generacion
        self.generation_input_label = Label(self.generation_input_group, text="Generacion: ")
        self.generation_input_label.grid(row=0, column=0)
        self.generation_input_field = Entry(self.generation_input_group)
        self.generation_input_field.grid(row=0, column=1)
        # Search generation btn
        self.search_generation_btn = Button(self.generation_input_group, text="Buscar generacion")
        self.search_generation_btn.grid(row=0, column=2)
        #Robot input group
        self.robot_input_group = Frame(self.algorithm_info_container)
        self.robot_input_group.grid(row=1, column=1)
        #Label para entrada de robot
        self.robot_input_label= Label(self.robot_input_group , text="Buscar robots")
        self.robot_input_label.grid(row=0,column=0)
        self.robot_input_combo= Combobox(self.robot_input_group,state="readonly")
        self.robot_input_combo.grid(row=0,column=1)
        self.robot_input_combo["values"] = [i for i in range(1,11)]
        #Search robot btn
        self.search_robot_btn= Button(self.robot_input_group,state=DISABLED,text="Buscar robot")
        self.search_robot_btn.grid(row=0,column=2)

        self.terrenoStored = terreno
        # Cargar imagenes
        self.terreno_normal = ImageTk.PhotoImage(Image.open("assets/normal.png"))
        self.terreno_moderado = ImageTk.PhotoImage(Image.open("assets/moderado.png"))
        self.terreno_dificil = ImageTk.PhotoImage(Image.open("assets/dificil.png"))
        self.terreno_bloqueado = ImageTk.PhotoImage(Image.open("assets/bloqueado.png"))
        self.robot = ImageTk.PhotoImage(Image.open("assets/robot.png"))
        # Display del terreno
        self.terrain_grid = [[0 for j in range(20)] for i in range(20)]
        self.terrain_img_grid = [[0 for j in range(20)] for i in range(20)]
        for fila_terreno in range(20):
            for bloque in range(20):
                if terreno[fila_terreno][bloque] == 1:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_normal, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                elif terreno[fila_terreno][bloque] == 2:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_moderado, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                elif terreno[fila_terreno][bloque] == 3:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_dificil, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                else:
                    bloque_canvas = Canvas(self.main_container, width=20, height=20, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_bloqueado, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas

    def show_error_message(self, message):
        messagebox.showerror("ERROR", message)

    def updateImg(self,cordenadas):
        self.terrain_grid[cordenadas[0]][cordenadas[1]].itemconfig(self.terrain_img_grid[cordenadas[0]][cordenadas[1]],image=self.robot)

    def reiniciar(self):
        for fila_terreno in range(20):
            for bloque in range(20):
                if self.terrenoStored[fila_terreno][bloque] == 1:
                    self.terrain_grid[fila_terreno][bloque].itemconfig(self.terrain_img_grid[fila_terreno][bloque], image=self.terreno_normal)
                elif self.terrenoStored[fila_terreno][bloque] == 2:
                    self.terrain_grid[fila_terreno][bloque].itemconfig(self.terrain_img_grid[fila_terreno][bloque], image=self.terreno_moderado)
                elif self.terrenoStored[fila_terreno][bloque] == 3:
                    self.terrain_grid[fila_terreno][bloque].itemconfig(self.terrain_img_grid[fila_terreno][bloque], image=self.terreno_dificil)
                else:
                    self.terrain_grid[fila_terreno][bloque].itemconfig(self.terrain_img_grid[fila_terreno][bloque], image=self.terreno_bloqueado)

