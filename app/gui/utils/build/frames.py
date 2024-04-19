import tkinter as tk

class CreateFrame:

    def create_place_frame(self, father, width, height, anchor, relx, rely, bg):
        self.frame = tk.Frame(father, width=width, height=height, bg=bg)
        self.frame.place(anchor=anchor, relx=relx, rely=rely)

    def create_grid_frame(self, father, width, bg, row, column):
        self.father.grid_rowconfigure(0, weight=1)
        self.father.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame = tk.Frame(father, width=width, bg=bg)
        self.frame.grid(row=row, column=column, sticky="nsew")

    def create_pack_frame(self, father, bg, side, fill, expand):
        self.frame = tk.Frame(father, bg=bg)
        self.frame.pack(side=side, fill=fill, expand=expand)