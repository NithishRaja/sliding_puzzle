#
# Test file
#
#

# Dependencies
import json, os, queue

# Function to perform relax operation on given vertex
def relax(currentVertex, basePath):
    # Initialise array to hold updated vertices
    updated = []
    # Read data from file
    file = open(os.path.join(basePath, currentVertex+".json"))
    data = json.load(file)
    file.close()

    # Iterate over adjacent vertices
    for vertex in data["adjacent"]:
        # Initialise flag
        flag = False
        # Read data from file
        file = open(os.path.join(basePath, vertex+".json"))
        vertexData = json.load(file)
        file.close()

        # Check and update distance
        if vertexData["distance"] == None:
            flag = True
        elif vertexData["distance"] > data["distance"] + 1:
            flag = True

        if flag:
            # Update vertex
            vertexData["distance"] = data["distance"] + 1
            vertexData["parent"] = currentVertex
            updated.append(vertex)
            # Write updated data to file
            file = open(os.path.join(basePath, vertex+".json"), "w")
            json.dump(vertexData, file)
            file.close()

    # Return list of adjacent vertices
    return updated

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

# Initialise queue
q = queue.Queue()

# Initialise base path
basePath = "./size"+str(size)
# Check if directory for graph exists, else create directory
if os.path.isdir(basePath):
    # Read data from solved position file
    file = open(os.path.join(basePath, position+".json"))
    data = json.load(file)
    file.close()
    # Update data to make position starting position
    data["distance"] = 0
    # Write data to file
    file = open(os.path.join(basePath, position+".json"), "w")
    json.dump(data, file)
    file.close()

    # Enqueue first element
    q.put(position)

# Iterate till queue is empty
while(not q.empty()):
    # Get current position
    pos = q.get()
    # Call relax function for given vertex
    adjPos = relax(pos, basePath)
    # Enqueue adjacent vertices
    for item in adjPos:
        q.put(item)
