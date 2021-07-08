# SLIDING PUZZLE

## Running the code

* Grid configuration can be updated in `config.json` file

### UI

* Run `python index.py` to run the application

### Solution

* Run `python generate.py` to generate the graph for grid size in `config.json`
* Run `python shortestPath.py` to calculate the shortest path from solved state to every other state
* Run `python solve.py <position string>` to calculate the shortest path to solve from current position

## Editing code

* Application logic is present inside `app.py` file
* Logic to generate graph is present inside `generate.py` file
* `shortestPath.py` contains logic to perform DFS on graph
