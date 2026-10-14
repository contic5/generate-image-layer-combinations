import tkinter as tk
from tkinter import ttk  # Import themed widgets
from tkinter import filedialog
from generate_image_layer_combinations import generate_image_layer_combinations
from pathlib import Path

class Image_Combinations_GUI(tk.Tk):
    def __init__(self):
        super().__init__(className="Generate Image Layer Combinations")  # Initialize the base tk.Tk class
        self.geometry("500x400")
        self.label = ttk.Label(self, text="Generate Image Layer Combinations",wraplength=300,font=("Arial",24),justify="center")
        self.label.pack()

        self.label = ttk.Label(self, text='Upload a folder with subfolders named "images" and "backgrounds". The program will generate combinations of backgrounds and images.',wraplength=300,font=("Arial",12),justify="center")
        self.label.pack()

        self.named_output=tk.BooleanVar(value=True)
        self.named_output_button=ttk.Checkbutton(self,text="Write named output.",variable=self.named_output)
        self.named_output_button.pack()

        self.results_label=ttk.Label(self,text="Ready to generate images",font=("Arial",18),wraplength=300,justify="center")
        self.results_label.pack()

        self.current_file_label=ttk.Label(self,text="")
        self.current_file_label.pack()

        self.button = ttk.Button(self, text="Select Folder", width=25, command=self.select_folder)
        self.button.pack()
    
    def select_folder(self):
        #self.withdraw()  # Hides the main small root window
        folder_location = filedialog.askdirectory(title="Select Folder")
        
        if folder_location:
            print("Selected folder:", folder_location)
            generate_image_background_combinations(Path(folder_location),self.named_output.get())
        else:
            print("No folder selected.") 

if __name__ == "__main__":
    root=Image_Combinations_GUI()
    root.mainloop()