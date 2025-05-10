import tkinter as tk
from tkinter import messagebox
import math

# Full periodic table data with row and col added
ELEMENTS = [
    {"symbol": "H", "name": "Hydrogen", "atomic_number": 1, "category": "Nonmetal", "electrons": [1], "row": 0, "col": 0},
    {"symbol": "He", "name": "Helium", "atomic_number": 2, "category": "Noble Gas", "electrons": [2], "row": 0, "col": 17},
    {"symbol": "Li", "name": "Lithium", "atomic_number": 3, "category": "Alkali Metal", "electrons": [2, 1], "row": 1, "col": 0},
    {"symbol": "Be", "name": "Beryllium", "atomic_number": 4, "category": "Alkaline Earth Metal", "electrons": [2, 2], "row": 1, "col": 1},
    {"symbol": "B", "name": "Boron", "atomic_number": 5, "category": "Metalloid", "electrons": [2, 3], "row": 1, "col": 12},
    {"symbol": "C", "name": "Carbon", "atomic_number": 6, "category": "Nonmetal", "electrons": [2, 4], "row": 1, "col": 13},
    {"symbol": "N", "name": "Nitrogen", "atomic_number": 7, "category": "Nonmetal", "electrons": [2, 5], "row": 1, "col": 14},
    {"symbol": "O", "name": "Oxygen", "atomic_number": 8, "category": "Nonmetal", "electrons": [2, 6], "row": 1, "col": 15},
    {"symbol": "F", "name": "Fluorine", "atomic_number": 9, "category": "Nonmetal", "electrons": [2, 7], "row": 1, "col": 16},
    {"symbol": "Ne", "name": "Neon", "atomic_number": 10, "category": "Noble Gas", "electrons": [2, 8], "row": 1, "col": 17},
    {"symbol": "Na", "name": "Sodium", "atomic_number": 11, "category": "Alkali Metal", "electrons": [2, 8, 1], "row": 2, "col": 0},
    {"symbol": "Mg", "name": "Magnesium", "atomic_number": 12, "category": "Alkaline Earth Metal", "electrons": [2, 8, 2], "row": 2, "col": 1},
    {"symbol": "Al", "name": "Aluminum", "atomic_number": 13, "category": "Post-Transition Metal", "electrons": [2, 8, 3], "row": 2, "col": 12},
    {"symbol": "Si", "name": "Silicon", "atomic_number": 14, "category": "Metalloid", "electrons": [2, 8, 4], "row": 2, "col": 13},
    {"symbol": "P", "name": "Phosphorus", "atomic_number": 15, "category": "Nonmetal", "electrons": [2, 8, 5], "row": 2, "col": 14},
    {"symbol": "S", "name": "Sulfur", "atomic_number": 16, "category": "Nonmetal", "electrons": [2, 8, 6], "row": 2, "col": 15},
    {"symbol": "Cl", "name": "Chlorine", "atomic_number": 17, "category": "Nonmetal", "electrons": [2, 8, 7], "row": 2, "col": 16},
    {"symbol": "Ar", "name": "Argon", "atomic_number": 18, "category": "Noble Gas", "electrons": [2, 8, 8], "row": 2, "col": 17},
    {"symbol": "K", "name": "Potassium", "atomic_number": 19, "category": "Alkali Metal", "electrons": [2, 8, 8, 1], "row": 3, "col": 0},
    {"symbol": "Ca", "name": "Calcium", "atomic_number": 20, "category": "Alkaline Earth Metal", "electrons": [2, 8, 8, 2], "row": 3, "col": 1},
    {"symbol": "Sc", "name": "Scandium", "atomic_number": 21, "category": "Transition Metal", "electrons": [2, 8, 9, 2], "row": 3, "col": 2},
    {"symbol": "Ti", "name": "Titanium", "atomic_number": 22, "category": "Transition Metal", "electrons": [2, 8, 10, 2], "row": 3, "col": 3},
    {"symbol": "V", "name": "Vanadium", "atomic_number": 23, "category": "Transition Metal", "electrons": [2, 8, 11, 2], "row": 3, "col": 4},
    {"symbol": "Cr", "name": "Chromium", "atomic_number": 24, "category": "Transition Metal", "electrons": [2, 8, 13, 1], "row": 3, "col": 5},
    {"symbol": "Mn", "name": "Manganese", "atomic_number": 25, "category": "Transition Metal", "electrons": [2, 8, 13, 2], "row": 3, "col": 6},
    {"symbol": "Fe", "name": "Iron", "atomic_number": 26, "category": "Transition Metal", "electrons": [2, 8, 14, 2], "row": 3, "col": 7},
    {"symbol": "Co", "name": "Cobalt", "atomic_number": 27, "category": "Transition Metal", "electrons": [2, 8, 15, 2], "row": 3, "col": 8},
    {"symbol": "Ni", "name": "Nickel", "atomic_number": 28, "category": "Transition Metal", "electrons": [2, 8, 16, 2], "row": 3, "col": 9},
    {"symbol": "Cu", "name": "Copper", "atomic_number": 29, "category": "Transition Metal", "electrons": [2, 8, 18, 1], "row": 3, "col": 10},
    {"symbol": "Zn", "name": "Zinc", "atomic_number": 30, "category": "Transition Metal", "electrons": [2, 8, 18, 2], "row": 3, "col": 11},
    {"symbol": "Ga", "name": "Gallium", "atomic_number": 31, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 3], "row": 3, "col": 12},
    {"symbol": "Ge", "name": "Germanium", "atomic_number": 32, "category": "Metalloid", "electrons": [2, 8, 18, 4], "row": 3, "col": 13},
    {"symbol": "As", "name": "Arsenic", "atomic_number": 33, "category": "Metalloid", "electrons": [2, 8, 18, 5], "row": 3, "col": 14},
    {"symbol": "Se", "name": "Selenium", "atomic_number": 34, "category": "Nonmetal", "electrons": [2, 8, 18, 6], "row": 3, "col": 15},
    {"symbol": "Br", "name": "Bromine", "atomic_number": 35, "category": "Nonmetal", "electrons": [2, 8, 18, 7], "row": 3, "col": 16},
    {"symbol": "Kr", "name": "Krypton", "atomic_number": 36, "category": "Noble Gas", "electrons": [2, 8, 18, 8], "row": 3, "col": 17},
    {"symbol": "Rb", "name": "Rubidium", "atomic_number": 37, "category": "Alkali Metal", "electrons": [2, 8, 18, 8, 1], "row": 4, "col": 0},
    {"symbol": "Sr", "name": "Strontium", "atomic_number": 38, "category": "Alkaline Earth Metal", "electrons": [2, 8, 18, 8, 2], "row": 4, "col": 1},
     {"symbol": "Y", "name": "Yttrium", "atomic_number": 39, "category": "Transition Metal", "electrons": [2, 8, 18, 9, 2], "row": 4, "col": 2},
     {"symbol": "Zr", "name": "Zirconium", "atomic_number": 40, "category": "Transition Metal", "electrons": [2, 8, 18, 10, 2], "row": 4, "col": 3},
     {"symbol": "Nb", "name": "Niobium", "atomic_number": 41, "category": "Transition Metal", "electrons": [2, 8, 18, 12, 1], "row": 4, "col": 4},
     {"symbol": "Mo", "name": "Molybdenum", "atomic_number": 42, "category": "Transition Metal", "electrons": [2, 8, 18, 13, 1], "row": 4, "col": 5},
     {"symbol": "Tc", "name": "Technetium", "atomic_number": 43, "category": "Transition Metal", "electrons": [2, 8, 18, 13, 2], "row": 4, "col": 6},
     {"symbol": "Ru", "name": "Ruthenium", "atomic_number": 44, "category": "Transition Metal", "electrons": [2, 8, 18, 15, 1], "row": 4, "col": 7},
     {"symbol": "Rh", "name": "Rhodium", "atomic_number": 45, "category": "Transition Metal", "electrons": [2, 8, 18, 16, 1], "row": 4, "col": 8},
     {"symbol": "Pd", "name": "Palladium", "atomic_number": 46, "category": "Transition Metal", "electrons": [2, 8, 18, 18], "row": 4, "col": 9},
     {"symbol": "Ag", "name": "Silver", "atomic_number": 47, "category": "Transition Metal", "electrons": [2, 8, 18, 18, 1], "row": 4, "col": 10},
     {"symbol": "Cd", "name": "Cadmium", "atomic_number": 48, "category": "Transition Metal", "electrons": [2, 8, 18, 18, 2], "row": 4, "col": 11},
     {"symbol": "In", "name": "Indium", "atomic_number": 49, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 18, 3], "row": 4, "col": 12},
     {"symbol": "Sn", "name": "Tin", "atomic_number": 50, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 18, 4], "row": 4, "col": 13},
     {"symbol": "Sb", "name": "Antimony", "atomic_number": 51, "category": "Metalloid", "electrons": [2, 8, 18, 18, 5], "row": 4, "col": 14},
     {"symbol": "Te", "name": "Tellurium", "atomic_number": 52, "category": "Metalloid", "electrons": [2, 8, 18, 18, 6], "row": 4, "col": 15},
     {"symbol": "I", "name": "Iodine", "atomic_number": 53, "category": "Nonmetal", "electrons": [2, 8, 18, 18, 7], "row": 4, "col": 16},
     {"symbol": "Xe", "name": "Xenon", "atomic_number": 54, "category": "Noble Gas", "electrons": [2, 8, 18, 18, 8], "row": 4, "col": 17},
     {"symbol": "Cs", "name": "Cesium", "atomic_number": 55, "category": "Alkali Metal", "electrons": [2, 8, 18, 18, 8, 1], "row": 5, "col": 0},
     {"symbol": "Ba", "name": "Barium", "atomic_number": 56, "category": "Alkaline Earth Metal", "electrons": [2, 8, 18, 18, 8, 2], "row": 5, "col": 1},
     {"symbol": "La", "name": "Lanthanum", "atomic_number": 57, "category": "Lanthanide", "electrons": [2, 8, 18, 18, 9, 2], "row": 10, "col": 1},
     {"symbol": "Ce", "name": "Cerium", "atomic_number": 58, "category": "Lanthanide", "electrons": [2, 8, 18, 19, 9, 2], "row": 10, "col": 2},
     {"symbol": "Pr", "name": "Praseodymium", "atomic_number": 59, "category": "Lanthanide", "electrons": [2, 8, 18, 21, 8, 2], "row": 10, "col": 3},
     {"symbol": "Nd", "name": "Neodymium", "atomic_number": 60, "category": "Lanthanide", "electrons": [2, 8, 18, 22, 8, 2], "row": 10, "col": 4},
     {"symbol": "Pm", "name": "Promethium", "atomic_number": 61, "category": "Lanthanide", "electrons": [2, 8, 18, 23, 8, 2], "row": 10, "col": 5},
     {"symbol": "Sm", "name": "Samarium", "atomic_number": 62, "category": "Lanthanide", "electrons": [2, 8, 18, 24, 8, 2], "row": 10, "col": 6},
     {"symbol": "Eu", "name": "Europium", "atomic_number": 63, "category": "Lanthanide", "electrons": [2, 8, 18, 25, 8, 2], "row": 10, "col": 7},
     {"symbol": "Gd", "name": "Gadolinium", "atomic_number": 64, "category": "Lanthanide", "electrons": [2, 8, 18, 25, 9, 2], "row": 10, "col": 8},
     {"symbol": "Tb", "name": "Terbium", "atomic_number": 65, "category": "Lanthanide", "electrons": [2, 8, 18, 27, 8, 2], "row": 10, "col": 9},
     {"symbol": "Dy", "name": "Dysprosium", "atomic_number": 66, "category": "Lanthanide", "electrons": [2, 8, 18, 28, 8, 2], "row": 10, "col": 10},
     {"symbol": "Ho", "name": "Holmium", "atomic_number": 67, "category": "Lanthanide", "electrons": [2, 8, 18, 29, 8, 2], "row": 10, "col": 11},
     {"symbol": "Er", "name": "Erbium", "atomic_number": 68, "category": "Lanthanide", "electrons": [2, 8, 18, 30, 8, 2], "row": 10, "col": 12},
     {"symbol": "Tm", "name": "Thulium", "atomic_number": 69, "category": "Lanthanide", "electrons": [2, 8, 18, 31, 8, 2], "row": 10, "col": 13},
     {"symbol": "Yb", "name": "Ytterbium", "atomic_number": 70, "category": "Lanthanide", "electrons": [2, 8, 18, 32, 8, 2], "row": 10, "col": 14},
     {"symbol": "Lu", "name": "Lutetium", "atomic_number": 71, "category": "Lanthanide", "electrons": [2, 8, 18, 32, 9, 2], "row": 10, "col": 15},
     {"symbol": "Hf", "name": "Hafnium", "atomic_number": 72, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 10, 2], "row": 5, "col": 3},
     {"symbol": "Ta", "name": "Tantalum", "atomic_number": 73, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 11, 2], "row": 5, "col": 4},
     {"symbol": "W", "name": "Tungsten", "atomic_number": 74, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 12, 2], "row": 5, "col": 5},
     {"symbol": "Re", "name": "Rhenium", "atomic_number": 75, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 13, 2], "row": 5, "col": 6},
     {"symbol": "Os", "name": "Osmium", "atomic_number": 76, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 14, 2], "row": 5, "col": 7},
     {"symbol": "Ir", "name": "Iridium", "atomic_number": 77, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 15, 2], "row": 5, "col": 8},
     {"symbol": "Pt", "name": "Platinum", "atomic_number": 78, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 17, 1], "row": 5, "col": 9},
     {"symbol": "Au", "name": "Gold", "atomic_number": 79, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 18, 1], "row": 5, "col": 10},
     {"symbol": "Hg", "name": "Mercury", "atomic_number": 80, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 18, 2], "row": 5, "col": 11},
     {"symbol": "Tl", "name": "Thallium", "atomic_number": 81, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 18, 3], "row": 5, "col": 12},
     {"symbol": "Pb", "name": "Lead", "atomic_number": 82, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 18, 4], "row": 5, "col": 13},
     {"symbol": "Bi", "name": "Bismuth", "atomic_number": 83, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 18, 5], "row": 5, "col": 14},
     {"symbol": "Po", "name": "Polonium", "atomic_number": 84, "category": "Metalloid", "electrons": [2, 8, 18, 32, 18, 6], "row": 5, "col": 15},
     {"symbol": "At", "name": "Astatine", "atomic_number": 85, "category": "Metalloid", "electrons": [2, 8, 18, 32, 18, 7], "row": 5, "col": 16},
     {"symbol": "Rn", "name": "Radon", "atomic_number": 86, "category": "Noble Gas", "electrons": [2, 8, 18, 32, 18, 8], "row": 5, "col": 17},
     {"symbol": "Fr", "name": "Francium", "atomic_number": 87, "category": "Alkali Metal", "electrons": [2, 8, 18, 32, 18, 8, 1], "row": 6, "col": 0},
     {"symbol": "Ra", "name": "Radium", "atomic_number": 88, "category": "Alkaline Earth Metal", "electrons": [2, 8, 18, 32, 18, 8, 2], "row": 6, "col": 1},
     {"symbol": "Ac", "name": "Actinium", "atomic_number": 89, "category": "Actinide", "electrons": [2, 8, 18, 32, 18, 9, 2], "row": 11, "col": 1},
     {"symbol": "Th", "name": "Thorium", "atomic_number": 90, "category": "Actinide", "electrons": [2, 8, 18, 32, 18, 10, 2], "row": 11, "col": 2},
     {"symbol": "Pa", "name": "Protactinium", "atomic_number": 91, "category": "Actinide", "electrons": [2, 8, 18, 32, 20, 9, 2], "row": 11, "col": 3},
     {"symbol": "U", "name": "Uranium", "atomic_number": 92, "category": "Actinide", "electrons": [2, 8, 18, 32, 21, 9, 2], "row": 11, "col": 4},
     {"symbol": "Np", "name": "Neptunium", "atomic_number": 93, "category": "Actinide", "electrons": [2, 8, 18, 32, 22, 9, 2], "row": 11, "col": 5},
     {"symbol": "Pu", "name": "Plutonium", "atomic_number": 94, "category": "Actinide", "electrons": [2, 8, 18, 32, 24, 8, 2], "row": 11, "col": 6},
     {"symbol": "Am", "name": "Americium", "atomic_number": 95, "category": "Actinide", "electrons": [2, 8, 18, 32, 25, 8, 2], "row": 11, "col": 7},
     {"symbol": "Cm", "name": "Curium", "atomic_number": 96, "category": "Actinide", "electrons": [2, 8, 18, 32, 25, 9, 2], "row": 11, "col": 8},
     {"symbol": "Bk", "name": "Berkelium", "atomic_number": 97, "category": "Actinide", "electrons": [2, 8, 18, 32, 27, 8, 2], "row": 11, "col": 9},
     {"symbol": "Cf", "name": "Californium", "atomic_number": 98, "category": "Actinide", "electrons": [2, 8, 18, 32, 28, 8, 2], "row": 11, "col": 10},
     {"symbol": "Es", "name": "Einsteinium", "atomic_number": 99, "category": "Actinide", "electrons": [2, 8, 18, 32, 29, 8, 2], "row": 11, "col": 11},
     {"symbol": "Fm", "name": "Fermium", "atomic_number": 100, "category": "Actinide", "electrons": [2, 8, 18, 32, 30, 8, 2], "row": 11, "col": 12},
    {"symbol": "Md", "name": "Mendelevium", "atomic_number": 101, "category": "Actinide", "electrons": [2, 8, 18, 32, 31, 2], "row": 11, "col": 13},
    {"symbol": "No", "name": "Nobelium", "atomic_number": 102, "category": "Actinide", "electrons": [2, 8, 18, 32, 32, 2], "row": 11, "col": 14},
    {"symbol": "Lr", "name": "Lawrencium", "atomic_number": 103, "category": "Actinide", "electrons": [2, 8, 18, 32, 32, 3], "row": 11, "col": 15},
    {"symbol": "Rf", "name": "Rutherfordium", "atomic_number": 104, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 10, 2], "row": 6, "col": 3},
    {"symbol": "Db", "name": "Dubnium", "atomic_number": 105, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 11, 2], "row": 6, "col": 4},
    {"symbol": "Sg", "name": "Seaborgium", "atomic_number": 106, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 12, 2], "row": 6, "col": 5},
    {"symbol": "Bh", "name": "Bohrium", "atomic_number": 107, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 13, 2], "row": 6, "col": 6},
    {"symbol": "Hs", "name": "Hassium", "atomic_number": 108, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 14, 2], "row": 6, "col": 7},
    {"symbol": "Mt", "name": "Meitnerium", "atomic_number": 109, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 15, 2], "row": 6, "col": 8},
    {"symbol": "Ds", "name": "Darmstadtium", "atomic_number": 110, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 16, 2], "row": 6, "col": 9},
    {"symbol": "Rg", "name": "Roentgenium", "atomic_number": 111, "category": "Transition Metal", "electrons": [2, 8, 18, 32, 32, 17, 2], "row": 6, "col": 10},
    {"symbol": "Cn", "name": "Copernicium", "atomic_number": 112, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 32, 18, 2], "row": 6, "col": 11},
    {"symbol": "Nh", "name": "Nihonium", "atomic_number": 113, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 32, 18, 3], "row": 6, "col": 12},
    {"symbol": "Fl", "name": "Flerovium", "atomic_number": 114, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 32, 18, 4], "row": 6, "col": 13},
    {"symbol": "Mc", "name": "Moscovium", "atomic_number": 115, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 32, 18, 5], "row": 6, "col": 14},
    {"symbol": "Lv", "name": "Livermorium", "atomic_number": 116, "category": "Post-Transition Metal", "electrons": [2, 8, 18, 32, 32, 18, 6], "row": 6, "col": 15},
    {"symbol": "Ts", "name": "Tennessine", "atomic_number": 117, "category": "Metalloid", "electrons": [2, 8, 18, 32, 32, 18, 7], "row": 6, "col": 16},
    {"symbol": "Og", "name": "Oganesson", "atomic_number": 118, "category": "Noble Gas", "electrons": [2, 8, 18, 32, 32, 18, 8], "row": 6, "col": 17}
]
CATEGORY_COLORS = {
    "Nonmetal": "#63BFF0",  # Light Blue
    "Noble Gas": "#FFD700",  # Gold
    "Alkali Metal": "#FF4500",  # Orange
    "Alkaline Earth Metal": "#32CD32",  # Lime Green
    "Metalloid": "#9370DB",  # Purple
    "Post-Transition Metal": "#87CEEB",  # Sky Blue
    "Transition Metal": "#FF6347",  # Tomato
    "Lanthanide": "#FFB6C1",  # Light Pink
    "Actinide": "#D2691E",  # Chocolate
}

def show_element_details(element):
    """Show detailed info about the element."""
    details = (
        f"Name: {element['name']}\n"
        f"Symbol: {element['symbol']}\n"
        f"Atomic Number: {element['atomic_number']}\n"
        f"Category: {element.get('category', 'Unknown')}\n"
        f"Electrons: {element['electrons']}"
    )
    messagebox.showinfo("Element Details", details)

def draw_electron_configuration(canvas, element):
    """Draw the electron configuration for an element."""
    canvas.delete("all")  # Clear previous drawings
    nucleus_x, nucleus_y = 225, 225  # Center coordinates for nucleus
    canvas.create_oval(
        nucleus_x - 20, nucleus_y - 20, nucleus_x + 20, nucleus_y + 20, fill="gray", outline=""
    )
    canvas.create_text(
        nucleus_x, nucleus_y, text=element["symbol"], fill="white", font=("Arial", 16, "bold")
    )

    # Draw electron shells
    radius_step = 30  # Distance between shells
    radius = radius_step
    for shell_index, electrons in enumerate(element["electrons"]):
        canvas.create_oval(
            nucleus_x - radius,
            nucleus_y - radius,
            nucleus_x + radius,
            nucleus_y + radius,
            outline="white",
        )
        # Place electrons on the shell
        angle_step = 360 / electrons if electrons else 0
        for e in range(electrons):
            angle = math.radians(e * angle_step)
            electron_x = nucleus_x + radius * math.cos(angle)
            electron_y = nucleus_y + radius * math.sin(angle)
            canvas.create_oval(
                electron_x - 5, electron_y - 5, electron_x + 5, electron_y + 5, fill="yellow", outline=""
            )
        radius += radius_step

# Main application
root = tk.Tk()
root.title("Interactive Periodic Table")
root.geometry("1920x1080")
root.configure(bg="#333333")

# Create a canvas for electron configuration
config_canvas = tk.Canvas(root, width=450, height=450, bg="#444444")
config_canvas.pack(side="right", padx=20, pady=20)

# Create the periodic table grid
grid_frame = tk.Frame(root, bg="#333333")
grid_frame.pack(side="left", padx=20, pady=20)

for element in ELEMENTS:
    row = element["row"]
    col = element["col"]
    color = CATEGORY_COLORS.get(element.get("category", "Unknown"), "#FFFFFF")  # Default to white if category not found
    button = tk.Button(
        grid_frame,
        text=element["symbol"],
        bg=color,
        fg="black",
        font=("Arial", 12, "bold"),
        width=4,
        height=2,
        command=lambda e=element: (show_element_details(e), draw_electron_configuration(config_canvas, e)),
    )
    button.grid(row=row, column=col, padx=2, pady=2)

root.mainloop()
