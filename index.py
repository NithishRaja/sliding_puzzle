#
# Index file
#
#

# Dependencies
import tkinter as tk
import json
# Local Dependencies
from app import Application

# Read in config file
file = open("config.json")
config = json.load(file)

# Initialise a frame
root = tk.Tk()
# Pass frame to application
app = Application(config["grid_size"], master=root)
# Start application
app.mainloop()
