# Betweenness Centrality

This projects main purpose is to understand what betweenness centrality actually means. Betweenness Centrality is a metric that measures the importance of each node in a graph/network by giving it a numerical value. The nodes with the highest values of Betweenness Centrality will be the most important nodes in the graph. 

In this project, we will consider an undirected, unweighted, connected graphs with no loops. DFS & BFS algorithms have been used to calculate the shortest distance between two vertices.

Betweenness Centrality of node V = Summation(Number of shortest Path from Node s to t that pass from vertex V / total number of shortest path from Node s to t)

# To Run the file
Clone the repository and extract the folder. To run the file, you need to have python3 installed. You can follow instructions given in this website (https://realpython.com/installing-python/) to install python3. Also, you need to make sure that the following modules are already installed in your system.
1. itertools
2. re

Once you have installed python3 and the modules, you can run the file by opening the folder location in your terminal/Command Line and typing in the following command:
```
python3 SBC.py
```

# Input 
The first line must contain all the vertices (integers) of the graph seperated with a comma. 
The second line must contain the edges i.e. 2-integered tuples seprated by a comma.

### Sample Input #1
```
Enter Vertices seprated with commas: 1, 2, 3, 4, 5, 6
Enter Edge tuples seprated with commas: (1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (3, 6), (4, 5), (4, 6)
```
### Output
```
List of betweenness centralities:
[0.0, 0.2, 0.2, 0.2, 0.2, 0.0]
Maximum betweenness centrality:  0.2
Indexes of vertices where top betweenness centrality is found:
[2, 3, 4, 5]
```

### Sample Input #2
```
Enter Vertices seprated with commas: 1,2,3,4,5,6,7
Enter Edge tuples seprated with commas: (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7)
```
### Output
```
List of betweenness centralities:
[0.03333333333333333, 0.03333333333333333, 0.03333333333333333, 0.03333333333333333, 0.03333333333333333, 0.03333333333333333, 0.4]
Maximum betweenness centrality:  0.4
Indexes of vertices where top betweenness centrality is found:
[7]
```