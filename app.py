#
# File containing application logic
#
#

# Dependencies
import tkinter as tk
from functools import partial
import random

# Initialise application class
class Application(tk.Frame):
    # Define constructor
    def __init__(self, size, master=None):
        super().__init__(master)
        # Initialise variables
        self.master = master
        self.grid()
        self.size = size
        # Initialise variable to hold position of empty tile
        self.empty = [self.size-1,self.size-1]
        # Initialise array to hold position of each tile
        self.position = []
        for i in range(self.size*self.size-1):
            self.position.append( [int(i/self.size), int(i%self.size)] )
        # Call function to add widgets
        self.create_widgets()

    # Function to add widgets
    def create_widgets(self):
        # Initialise array for buttons
        self.button = []
        # Initialise buttons for tiles
        for i in range(self.size*self.size-1):
            # Initialise button
            self.button.append( tk.Button(self, text=str(i), relief="sunken") )
            self.button[i].grid(row = int(i/self.size), column = int(i%self.size), padx = 1, pady = 1)
            self.button[i]["command"] = partial(self.swapButton, i)

        # Initialise button to shuffle tiles
        self.shuffle = tk.Button(self, text="Shuffle", command=self.shuffle_tiles)
        # Initialise button to reset tiles
        self.reset = tk.Button(self, text="Reset", command=self.reset_tiles)
        # Set position for shuffle and reset buttons
        if self.size%2==0:
            self.shuffle.grid(column=0, row=self.size, columnspan=int(self.size/2))
            self.reset.grid(column=int(self.size/2), row=self.size, columnspan=int(self.size/2))
        else:
            self.shuffle.grid(column=0, row=self.size, columnspan=int(self.size/2))
            self.reset.grid(column=int(self.size/2)+1, row=self.size, columnspan=int(self.size/2))

    # Function to swap positions
    def swapPosition(self, pos):
        # Swap positions
        temp = self.position[pos]
        self.position[pos] = self.empty
        self.empty = temp

    # Function to move button
    def swapButton(self, pos):
        # Check if button is adjacent to empty tile
        if self.position[pos][0] == self.empty[0] and abs(self.position[pos][1]-self.empty[1]) < 2:
            # Call function to swap positions
            self.swapPosition(pos)
        elif self.position[pos][1] == self.empty[1] and abs(self.position[pos][0]-self.empty[0]) < 2:
            # Call function to swap positions
            self.swapPosition(pos)
        # Call function to refresh display
        self.refresh_display()

    # Function to shuffle tiles
    def shuffle_tiles(self):
        # Seed random number generator
        random.seed()
        for count in range(100):
            # Initialise array to hold positions adjacent to empty tile
            temp = []
            # Get list of positions adjacent to empty position
            for i in range(self.size*self.size-1):
                # Check if distance between current tile and empty tile is 1
                if abs(self.position[i][0] - self.empty[0]) + abs(self.position[i][1] - self.empty[1]) == 1:
                    # Append position to array
                    temp.append(i)
            # Select a random position from array
            randpos = temp[ random.randint(0, len(temp)-1) ]
            self.swapPosition(randpos)
        # Call function to update display
        self.refresh_display()

    # Function to reset tiles
    def reset_tiles(self):
        # Set tile positions to original value
        for i in range(self.size*self.size-1):
            self.position[i] = [int(i/self.size), int(i%self.size)]
        # Set empty tile to original position
        self.empty = [self.size-1,self.size-1]
        # Call function to update display
        self.refresh_display()

    # Function to refresh display
    def refresh_display(self):
        # Iterate over buttons
        for i in range(self.size*self.size-1):
            self.button[i].grid(row = self.position[i][0], column = self.position[i][1])
