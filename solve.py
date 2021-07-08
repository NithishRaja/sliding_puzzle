#
# File to find solution for given position
#
#

# Dependencies
import json, os

# Function to solve given position
def solve(position]):
    # Initialise array to hold all intermediate states
    pathArray = []
    # Read config file
    file = open("config.json")
    config = json.load(file)
    file.close()
    # Initialise size
    size = config["grid_size"]
    # Initialise base path
    basePath = "./size"+str(size)

    # Read file
    file = open(os.path.join(basePath, position+".json"))
    data = json.load(file)
    file.close()

    # Iterate till solved state is reached
    while(not data["parent"] == None):
        position = data["parent"]
        # Read file
        file = open(os.path.join(basePath, position+".json"))
        data = json.load(file)
        file.close()
        pathArray.append(position)

    # Return path
    return pathArray

if __name__ == "__main__":
    # Call function to solve
    path = solve(sys.argv[1])
    print(sys.argv[1])
    for step in path:
        print(step)
