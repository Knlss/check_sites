import tkinter as tk

class CreateFrame:

    def create_place_frame(self, father, width, height, anchor, relx, rely, bg):
        frame = tk.Frame(father, width=width, height=height, bg=bg)
        frame.place(anchor=anchor, relx=relx, rely=rely)
        return frame

    def create_grid_frame(self, father, width, bg, row, column):
        father.grid_rowconfigure(0, weight=1)
        father.grid_columnconfigure((0, 1, 2), weight=1)
        frame = tk.Frame(father, width=width, bg=bg)
        frame.grid(row=row, column=column, sticky="nsew")
        return frame

    def create_pack_frame(self, father, bg, side, fill, expand):
        frame = tk.Frame(father, bg=bg)
        frame.pack(side=side, fill=fill, expand=expand)
        return frame