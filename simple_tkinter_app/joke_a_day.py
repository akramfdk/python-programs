# ensure pyjokes and tkinter are installed

import tkinter as tk
import pyjokes as pj

# gets a new joke and updates the label text
def generate_joke():
    label.config(text = pj.get_joke())

 # create main window and set its title and size
root = tk.Tk()
root.title("Be Funny!!")
root.geometry("500x300")


# configures the grid layout
# column 0 and row 0 expand to take the space if window resizes
# row 1 doesn't stretch so button remains centered
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

# add a label to the window
label = tk.Label(
    root, 
    text="Hello Everyone!!!", 
    anchor="w",  # aligns text left inside the label
    wraplength=450,  # wraps text if longer than 450px
    justify="left",
    font=("lucida calligraphy", 12)
)

# label.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")
# placed in grid at row 0, col 0 with padding
label.grid(row=0, column=0, padx=20, pady=30)

# adds a button
button = tk.Button(
    root, 
    text="Generate Joke", 
    width=20,   # 20 characters wide
    height=2,   # 2 characters tall
    command= generate_joke,  # when clicked calls generate_joke() function
    font=("Verdana", 12, "bold")
    )

# placed in grid at row 1, column 0
button.grid(row=1,column=0, padx=20, pady=20)

# keeps window open until user closes it
# handles button clicks and UI updates
root.mainloop()