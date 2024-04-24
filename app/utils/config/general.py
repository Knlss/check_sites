from openpyxl.styles import Alignment

class GeneralConfig:
    def __init__(self):
        
        styles = {
            "cell_styles": {
            "font_size_e": 11,
            "cell_e1_text": "RESULTADOS",
            "alignment_cell": Alignment(horizontal='center', vertical='center')
            },

            "border_styles": {
            "cell_border_left": None,
            "cell_border_right": None,
            "cell_border_top": None,
            "cell_border_bottom": None,
            "end_border_edges_top": None,
            "end_border_edges_bottom": None,
            "title_border_left": None,
            "title_border_right": None,
            "title_border_top": None,
            "title_border_bottom": None
            },
            
            "color_styles": {
            "font_color_acessible": "000000",
            "font_color_inacessible": "000000",
            "font_color_timeout": "000000",
            "border_color": "000000"
            },
        }

        cmd_config = {
            "files": {
                'filename': None,
                'future_filename': None,
                'directory': None
            },

            "columns": {
            "input_column_value": None,
            "output_column_value": None,
            },

            "generals": {
            "status_label": None,
            "first_cell_size": 13
            }
        }