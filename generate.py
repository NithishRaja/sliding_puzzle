#
# File to generate graph
#
#

# Dependencies
import json, os, queue

# Function to swap positions
def swapPosition(position, index):
    # Get empty position
    empty = position.index("0")
    # initialise empty string
    temp = ""
    # Swap position
    if index > empty:
        temp = position[:empty] + position[index] + position[empty+1:index] + "0" + position[index+1:]
    else:
        temp = position[:index] + "0" + position[index+1:empty] + position[index] + position[empty+1:]
    # Return new position string
    return temp

# Function to get positions adjacent to empty positions
def getAdjPositions(position, size):
    # Initialise empty array for adjacent positions
    adjPos = []
    # Get empty position
    empty = position.index("0")
    # Calculate adjacent positions
    pos1 = size*(int(empty/size)) + int(empty%size)+1
    pos2 = size*(int(empty/size)) + int(empty%size)-1
    pos3 = size*(int(empty/size)+1) + int(empty%size)
    pos4 = size*(int(empty/size)-1) + int(empty%size)
    # Check if adjacent positions exists
    if pos1 < size*size and pos1 >= 0:
        adjPos.append(swapPosition(position, pos1))
    if pos2 < size*size and pos2 >= 0:
        adjPos.append(swapPosition(position, pos2))
    if pos3 < size*size and pos3 >= 0:
        adjPos.append(swapPosition(position, pos3))
    if pos4 < size*size and pos4 >= 0:
        adjPos.append(swapPosition(position, pos4))
    # Return adjacent positions
    return adjPos

# Read config file
file = open("config.json")
config = json.load(file)
file.close()

# Initialise size
size = config["grid_size"]
# Initialise position string
position = ""
for i in range(size*size-1):
    position = position+str(i+1)
# Add empty
position = position + "0"

# Initialise base path
basePath = "./size"+str(size)
# Check if directory for graph exists, else create directory
if not os.path.isdir(basePath):
    os.mkdir(basePath)

# Initialise queue
q = queue.Queue()
# Enqueue first element
q.put(position)

# Iterate till queue is empty
while(not q.empty()):
    # Get current position
    position = q.get()
    # Check if file exists
    if not os.path.isfile(os.path.join(basePath, position+".json")):
        # Call function to get adjacent positions
        adjPos = getAdjPositions(position, size)

        # Open file for current position
        file = open(os.path.join(basePath, position+".json"), "w")
        # Write data to file
        json.dump({
            "adjacent": adjPos,
            "visited": False
        }, file)
        # Close file
        file.close()

        # Push adjacent positions to queue
        for item in adjPos:
            q.put(item)
