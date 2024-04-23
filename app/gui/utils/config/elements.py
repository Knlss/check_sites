import tkinter as tk

class ElementConfig:
    def __init__(self):



        self.elements = {}

        self.elements_button_info = {
            "process_button": {"father":"program_process", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12 bold", "text":"PROCESSAR", "cursor":"hand2", "command":lambda: print(0), "relwidth":1, "relheight":1, "state":tk.NORMAL},

            "archive_button": {"father":"archive_select", "width":0, "height":0, "anchor":"center", "relx":0.949, "rely":0.5, "bg":"lightgray", "activebg":"gray", "fg":"black", "activefg":"#1A1110", "font":"helvetica", "text":"▼", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.1, "relheight":1, "state":tk.NORMAL},
            
            "folder_button": {"father":"path_select", "width":0, "height":0, "anchor":"center", "relx":0.949, "rely":0.5, "bg":"lightgray", "activebg":"gray", "fg":"black", "activefg":"#1A1110", "font":"helvetica", "text":"▼", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.1, "relheight":1, "state":tk.NORMAL},
            
            "size_button": {"father":"fontsize_def", "width":0, "height":0, "anchor":"center", "relx":0.874, "rely":0.5, "bg":"lightgray", "activebg":"gray", "fg":"black", "activefg":"#1A1110", "font":"helvetica", "text":"▼", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.25, "relheight":1, "state":tk.NORMAL},
            
            "align_left_button": {"father":"alignment_le_def", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 15 bold", "text":"←", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "align_center_button": {"father":"alignment_ce_def", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 15 bold", "text":"•", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "align_right_button": {"father":"alignment_ri_def", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 15 bold", "text":"→", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "border_top_button": {"father":"border_up_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"─", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "border_bottom_button": {"father":"border_low_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"─", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "border_left_button": {"father":"border_le_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"│", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "border_right_button": {"father":"border_ri_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 12", "text":"│", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.8, "relheight":0.8, "state":tk.NORMAL},
            
            "color_ac_button": {"father":"color_ac_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "color_ti_button": {"father":"color_ti_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},

            "color_in_button": {"father":"color_in_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL},
            
            "color_bo_button": {"father":"color_bo_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#F9F0F0", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "font":"helvetica 10", "text":"☰", "cursor":"hand2", "command":lambda: print(0), "relwidth":0.9, "relheight":0.9, "state":tk.NORMAL}
        }

        self.elements_checkbutton_info = {
            "default_mode_checkbutton": {"father":"default_mode_select", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "activebg":"lightgray", "fg":"black", "activefg":"#1A1110", "selectcolor":"", "font":"helvetica 10 bold", "text":"Redefinir para Padrão", "cursor":"hand2", "variable":"entry_default", "command":lambda: print(0), "relwidth":1, "relheight":1, "state":tk.NORMAL}
        }
        
        self.elements_entry_info = {
            "archive_show_entry": {"father":"archive_select", "width":0, "anchor":"center", "relx":0.448, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"arrow", "relwidth":0.9, "textvariable":"entry_archive", "limit_lenght":None, "state":tk.DISABLED},
            
            "folder_show_entry": {"father":"path_select", "width":0, "anchor":"center", "relx":0.448, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"arrow", "relwidth":0.9, "textvariable":"entry_folder", "limit_lenght":None, "state":tk.DISABLED},
            
            "input_column_entry": {"father":"input_column_def", "width":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"hand2", "relwidth":1, "textvariable":"entry_input", "limit_lenght":1, "state":tk.NORMAL},
            
            "output_column_entry": {"father":"output_column_def", "width":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"hand2", "relwidth":1, "textvariable":"entry_output", "limit_lenght":1, "state":tk.NORMAL},
            
            "input_name_entry": {"father":"column_title_def", "width":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"hand2", "relwidth":1, "textvariable":"entry_name", "limit_lenght":10, "state":tk.NORMAL},
            
            "size_show_entry": {"father":"fontsize_def", "width":0, "anchor":"center", "relx":0.373, "rely":0.5, "bg":"white", "fg":"black", "font":"helvetica 10", "cursor":"arrow", "relwidth":0.75, "textvariable":"entry_size", "limit_lenght":None, "state":tk.DISABLED},
        }

        self.elements_label_info = {
            "program_label": {"father":"program_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 40 bold", "justify":"center", "text":"Website Checker", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "status_label": {"father":"program_status", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"teste", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "archive_label": {"father":"archive_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Arquivo Selecionado:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "folder_label": {"father":"path_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Caminho para Download:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "input_label": {"father":"input_column_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 8 bold", "justify":"center", "text":"Coluna de Entrada:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "output_label": {"father":"output_column_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 8 bold", "justify":"center", "text":"Coluna de Saída:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "cell_label": {"father":"cell_section_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 20 bold", "justify":"center", "text":"Células", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "size_label": {"father":"fontsize_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Tamanho da Fonte:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "align_label": {"father":"alignment_def_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Alinhamento:", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_label": {"father":"border_section_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 20 bold", "justify":"center", "text":"Bordas", "cursor":"arrow", "relwidth":1, "relheight":1},

            "border_up_label": {"father":"border_up_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Superior", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_low_label": {"father":"border_low_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Inferior", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_le_label": {"father":"border_le_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Esquerda", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "border_ri_label": {"father":"border_ri_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Direita", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_label": {"father":"color_section_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 20 bold", "justify":"center", "text":"Cores", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_ac_label": {"father":"color_ac_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Acessível", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_ti_label": {"father":"color_ti_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Excedido", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_in_label": {"father":"color_in_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Inacessível", "cursor":"arrow", "relwidth":1, "relheight":1},
            
            "color_bo_label": {"father":"color_bo_select_title", "width":0, "height":0, "anchor":"center", "relx":0.5, "rely":0.5, "bg":"#FFFDFB", "fg":"black", "font":"helvetica 10 bold", "justify":"center", "text":"Bordas", "cursor":"arrow", "relwidth":1, "relheight":1},
        }