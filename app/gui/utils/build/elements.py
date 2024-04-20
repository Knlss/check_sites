import tkinter as tk

class CreateElement:

    def create_button(self, father, width, height, anchor, relx, rely, bg, activebg, fg, activefg, font, text, cursor, command, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                frame = tk.Button(father, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
                frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                return frame
            else:
                if relheight != None:
                    frame = tk.Button(father, width=width, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Button(father, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Button(father, width=width, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, font=font, text=text, cursor=cursor, command=command)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_checkbutton(self, father, width, height, anchor, relx, rely, bg, activebg, fg, activefg, selectcolor, font, text, cursor, variable, command, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                    frame = tk.Checkbutton(father, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                    return frame
            else:
                if relheight != None:
                    frame = tk.Checkbutton(father, width=width, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Checkbutton(father, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Checkbutton(father, width=width, height=height, bg=bg, activebackground=activebg, fg=fg, activeforeground=activefg, selectcolor=selectcolor, font=font, text=text, cursor=cursor, variable=variable, command=command)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_entry(self, father, width, anchor, relx, rely, bg, fg, font, cursor, relwidth=None):
        if relwidth != None:
            frame = tk.Entry(father, bg=bg, fg=fg, font=font, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
            return frame
        else:
            frame = tk.Entry(father, width=width, bg=bg, fg=fg, font=font, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame

    def create_label(self, father, width, height, anchor, relx, rely, bg, fg, font, justify, cursor, relwidth=None, relheight=None):
        if relheight or relwidth != None:
            if relheight and relwidth != None:
                frame = tk.Label(father, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
                frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                return frame
            else:
                if relheight != None:
                    frame = tk.Label(father, width=width, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relheight=relheight)
                    return frame
                elif relwidth != None:
                    frame = tk.Label(father, height=height, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
                    frame.place(anchor=anchor, relx=relx, rely=rely, relwidth=relwidth)
                    return frame
        else:
            frame = tk.Label(father, width=width, height=height, bg=bg, fg=fg, font=font, justify=justify, cursor=cursor)
            frame.place(anchor=anchor, relx=relx, rely=rely)
            return frame