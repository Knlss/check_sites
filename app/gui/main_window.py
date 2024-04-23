from gui.utils.build import elements as el_bld
from gui.utils.build import frames as fr_bld
from gui.utils.config import elements as el_cfg
from gui.utils.config import frames as fr_cfg
import tkinter as tk

def main():

    frame_config = fr_cfg.FrameConfig()
    element_config = el_cfg.ElementConfig()

    root = tk.Tk()
    root.geometry("1250x650")
    root.resizable(False, False)
    frame_config.frames["root"] = root

    for item_type, item_info in [
            (frame_config.frames_pack_info, fr_bld.CreateFrame().create_pack_frame),
            (frame_config.frames_grid_info, fr_bld.CreateFrame().create_grid_frame),
            (frame_config.frames_place_info, fr_bld.CreateFrame().create_place_frame),
            (element_config.elements_button_info, el_bld.CreateElement().create_button),
            (element_config.elements_entry_info, el_bld.CreateElement().create_input),
            (element_config.elements_checkbutton_info, el_bld.CreateElement().create_checkbutton),
            (element_config.elements_label_info, el_bld.CreateElement().create_label)
        ]:
        for item_name, info in item_type.items():
            instance = item_info            
            father_key = info.pop("father")
            father = frame_config.frames[father_key]
            frame = instance(father, **info)
            if item_type is frame_config.frames_pack_info or item_type is frame_config.frames_grid_info or item_type is frame_config.frames_place_info:
                frame_config.frames[item_name] = frame
            else:
                element_config.elements[item_name] = frame


    frame_config.frames["root"].mainloop()