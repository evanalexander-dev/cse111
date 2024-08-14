import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
from math import pi


def main():
    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main)
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    lbl_radius = Label(frm_main, text="Radius:")
    ent_radius = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=100)
    lbl_radius_units = Label(frm_main, text="cm")
    lbl_area = Label(frm_main, text="Area:")
    lbl_area_value = Label(frm_main, width=10)
    lbl_area_units = Label(frm_main, text="cm²")
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_area.grid(row=1, column=0, padx=(30, 3), pady=3)
    lbl_area_value.grid(row=1, column=1, padx=3, pady=3)
    lbl_area_units.grid(row=1, column=2, padx=3, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            radius = ent_radius.get()
            area = pi * int(radius) ** 2

            lbl_area_value.config(text=f"{area:.2f}")
        except ValueError:
            lbl_area_value.config(text="")

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_area_value.config(text="")
        ent_radius.focus()

    ent_radius.bind("<KeyRelease>", calculate)

    btn_clear.config(command=clear)

    ent_radius.focus()


if __name__ == "__main__":
    main()
