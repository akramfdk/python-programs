import tkinter as tk
import pyjokes as pj

def generate_joke():
    label.config(text = pj.get_joke())


root = tk.Tk()
root.title("Be Funny!!")
root.geometry("500x300")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

# add a label to the window
label = tk.Label(
    root, 
    text="Hello Everyone!!!", 
    anchor="w",
    wraplength=450,
    justify="left",
    font=("lucida calligraphy", 12)
)

# label.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")
label.grid(row=0, column=0, padx=20, pady=30)

button = tk.Button(
    root, 
    text="Generate Joke", 
    width=20, 
    height=2, 
    command= generate_joke,
    font=("Verdana", 12, "bold")
    )

button.grid(row=1,column=0, padx=20, pady=20)

root.mainloop()