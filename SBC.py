#!/usr/bin/env python3
# Rhythmkumar Patel
# rhyhtmkumar18083@iiitd.ac.in
# 2018083


import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"


class Graph(object):
    name = "Rhythmkumar Patel"
    email = "rhythmkumar18083@iiitd.ac.in"
    roll_num = "2018083"

    def __init__(self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices

        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))

        self.edges = ordered_edges
        self.path = []
        self.validate()

        graph = {}
        for i in range(len(self.vertices) + 1):
            graph[i] = []

        for i in self.edges:
            x, y = i
            l1 = graph[x]
            l2 = graph[y]
            l1.append(y)
            l2.append(x)
            graph[x] = l1
            graph[y] = l2

        # print (graph)
        self.graph = graph

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (
                not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception(
                "Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set(
                [node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(
                vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set(
                [edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(
                edges, duplicate_edges))

    def min_dist(self, start_node, end_node, vertices):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''

        # Using BFS, this gives a list which will store the distances from start node as given in vertices
        # for e.g. if vertices is [1,2,3,4,5,6], start node = 2, & edges is [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]
        # then dist = [-1, 1, 0, 1, 2, 1, 3]
        # 1 is at 1 min dist from 2
        # 2 is at 0 min dist from 2 (same node)
        # 3 is at 1 min dist from 2
        # 4 is at 2 min dist from 2
        # 5 is at 1 min dist from 2
        # 6 is at 3 min dist from 2
        # -1 at start is for making the index value equal to the node

        # initializes a list with -1
        dist = [-1 for i in range(len(self.vertices) + 1)]

        queue = []

        dist[start_node] = 0  # distance from start node to start node is 0

        queue.append(start_node)  # appends start node in queue

        while len(queue) != 0:  # runs till all nodes are iterated
            nxt = queue[0]

            for i in self.graph[nxt]:  # gives adjacent nodes of i
                if dist[i] == -1:
                    # increments 1 with current node dist in each iteration
                    dist[i] = dist[nxt] + 1
                    queue.append(i)  # adds that in queue, as per BFS
                # print (dist)
            queue.remove(nxt)  # after parsing, removes from queue, as per BFS

        # print (dist)
        return (dist[end_node])

    def all_shortest_paths(self, start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """

        self.path = []
        self.all_paths(start_node, end_node, self.min_dist(
            start_node, end_node, vertices), curPath=[start_node])
        return self.path

    def all_paths(self, node, destination, dist, curPath):
        """
        Finds all paths from node to destination with length = dist

        Args:
            node: Node to find path from
            destination: Node to reach
            dist: Allowed distance of path
            path: path already traversed

        Returns:
            List of path, where each path is list ending on destination

            Returns None if there no paths
        """
        # finds all paths from a node where length == dist
        # path is list of all shortest current paths
        # current path is a list of one such shortest path

        # BASE CASE
        if dist == 0 and node == destination:  # if successful, then current path becomes an element in path
            self.path.append(curPath)
            return

        if dist == 0:  # if unsuccessful, returns nothing
            return

        l = self.graph[node]  # gives neighbouring nodes
        # print ("Node:",node)
        # print ("current Path:",curPath)
        # print ("l: ", l)
        for i in l:  # iterates each neighbouring node
            if i not in curPath:  # checks if the node is not visited so loops & returning to same element are avoided
                # print("Next vertices is: ", i)
                self.all_paths(i, destination, dist - 1, curPath + [i])
                # Recursion implementation where distance reduces by 1 & the
                # node gets appended in current path

    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """

        nodePairs = []
        shortestPath = []
        noShortestPath = []
        noShortestPathPass = []
        ratio = []

        for i in range(1, len(vertices)):
            if i != node:
                for j in range(i + 1, len(vertices) + 1):
                    if j != node:
                        # adds node pairs where that node is not included
                        nodePairs.append((i, j))

        # print (nodePairs)
        for k in nodePairs:

            # calls the above shortest path functions
            shortestPath.append(self.all_shortest_paths(k[0], k[1]))

        # print (shortestPath)

        for l in shortestPath:
            noShortestPath.append(len(l))  # no. of shortest paths in a list
            count = 0

            for m in l:  # no. of shortest pass in a list that pass through the node
                if node in m:
                    count += 1

            noShortestPathPass.append(count)

        # print (noShortestPathPass)

        for n in range(len(shortestPath)):
            # list of no. of shortest path of each node that passes / no. of
            # shortest path of each node
            ratio.append(noShortestPathPass[n] / noShortestPath[n])

        betCen = sum(ratio)  # betweenness centrality
        N = len(vertices)

        # standard betweenness centrality
        stdBetCen = (betCen / (((N - 1) * (N - 2)) / 2))

        return (stdBetCen)

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.


        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        l = []
        fin = []  # final list consisting of vertices having maximum betweenness centrality

        for i in vertices:
            # list of betweenness centralities of vertices
            l.append(self.betweenness_centrality(i))

        print("List of betweenness centralities:")
        print(l)
        maxSBC = max(l)
        print("Maximum betweenness centrality: ", maxSBC)

        for j in range(len(l)):
            if l[j] == maxSBC:  # since l and vertices have same length, we get the index of vertices where the index of l has max betCen
                fin.append(vertices[j])

        return fin

    def __str__(self):
        return graph1.top_k_betweenness_centrality()


if __name__ == "__main__":

    # vertices = [1, 2, 3, 4, 5, 6]
    # edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (3, 6), (4, 5), (4, 6)]

    # vertices = [1, 2, 3, 4]
    # edges    = [(1, 2), (2, 4), (4, 3), (3, 1), (3, 2), (4, 1)]

    # vertices = [1, 2, 3, 4, 5, 6, 7, 8]
    # edges    = [(1, 2), (1, 3), (3, 4), (4, 5), (5, 7), (7, 8), (8, 5), (8, 6), (6, 4), (2, 6), (6, 5), (2, 3), (3, 5), (6, 7)]

    # vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # edges = [(10, 2), (7, 2), (2, 1), (1, 6), (1, 3), (3, 11), (3, 15),
    #          (3, 5), (5, 12), (3, 4), (4, 8), (14, 8), (9, 8), (8, 13)]

    # vertices = [1, 2, 3, 4, 5, 6]
    # edges    = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]

    # vertices = [1, 2, 3, 4, 5, 6, 7]
    # edges    = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7)]

    vertices = []
    edges = []

    verticesTemp = input("Enter Vertices seprated with commas: ").split(",")
    for x in verticesTemp:
        vertices.append(int(x))

    edge = input("Enter Edge tuples seprated with commas: ")
    edge = "".join(edge.split())

    for x in edge.split("),("):
        x = x.replace(')', '').replace('(', '')
        temp = x.split(',')
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        edges.append(tuple(temp))

    graph1 = Graph(vertices, edges)

    # graph1.all_paths(2,6,3, curPath=[2])
    # print (graph1.all_shortest_paths(2,4))
    # print (graph1.top_k_betweenness_centrality())
    indexes = graph1.__str__()
    print("Indexes of vertices where top betweenness centrality is found:")
    print(indexes)
