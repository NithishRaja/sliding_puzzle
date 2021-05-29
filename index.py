#
# Index file
#
#

# Dependencies
import tkinter as tk

# Local Dependencies
from app import Application

# Initialise a frame
root = tk.Tk()
# Pass frame to application
app = Application(master=root)
# Start application
app.mainloop()
