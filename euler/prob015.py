from smath import Graph
import time
import sys

# according to exponential interpolation the time it take for this function to process depending on n is:
# 2.06551*10^-7e^(1.48869x) <- pretty accurate too!

class Graph:
    MAX_VERTICIES = 0
    matrix = []
    numVerticies = 0
    labels = []
    recurs = 0

    def __init__(self, n: int):
        self.MAX_VERTICIES = n**2
        self.matrix = [[] for i in range(0,self.MAX_VERTICIES)]
        self.numVerticies = 0
        self. labels = ["" for i in range(0,self.MAX_VERTICIES)]
        for i in range(0, self.MAX_VERTICIES):
            for j in range(0, self.MAX_VERTICIES):
                self.matrix[i].append(0)

        self.numVerticies = 0

    def add_egde(self, source: str, target: str, weight: int):
        fromNode = self.get_index(source)
        toNode = self.get_index(target)

        self.matrix[fromNode][toNode] = weight

    def add_vertex(self, label: str):
        if self.numVerticies >= self.MAX_VERTICIES:
            return
        self.labels[self.numVerticies] = label
        self.numVerticies += 1

    def get_index(self, label: str):
        for i in range(0, self.MAX_VERTICIES):
            if label == self.labels[i]:
                return i
        return -1
    
    def is_edge(self, sourceIndex: int, targetIndex: int):
        if self.matrix[sourceIndex][targetIndex] != 0:
            return True
        return False
    
    def get_adjacent_verticies(self, sourceIndex: int):
        edges = []
        for i in range(0, self.MAX_VERTICIES):
            if self.matrix[sourceIndex][i] != 0:
                edges.append(self.labels[i])
        return edges
    
    def get_weight(self, sourceIndex: int, targetIndex: int):
        return self.matrix[sourceIndex][targetIndex]
    
    def breadth_first_search(self, startingVertex: str):
        
        visited = [-1 for i in range(self.MAX_VERTICIES)]

        cnt = self.breadth_first_search_helper(startingVertex, visited)

        print(f"starting BFS with vertex: {startingVertex}")

        for i in range(0, self.MAX_VERTICIES):
            if visited[i] == -1:
                break
            print(f"    visited {self.labels[visited[i]]}")
        print(f"number of courses: {cnt}")

    def breadth_first_search_helper(self, startingVertex: str, visited: list[int]):
        frontier = []
        visitedQ = []
        currentV = None

        frontier.insert(0, self.get_index(startingVertex))
        visitedQ.insert(0, self.get_index(startingVertex))
        visited[self.get_index(startingVertex)] = 0
        cnt = 0
        while (frontier != []):
            currentV = frontier.pop()
            
            for i in range(0, self.MAX_VERTICIES):
                if self.matrix[currentV][i] < sys.maxsize and visited[i] == -1:
                    frontier.insert(0, i)
                    visited[i] = i
                    visitedQ.insert(0, i)

        cnt += len(visited)

        for i in range(0, self.MAX_VERTICIES):
            visited[i] = -1

        for i in range(0, self.MAX_VERTICIES):
            if visitedQ == []:
                return cnt
            visited[i] = visitedQ.pop()

    def depth_first_search(self, startingVertex: str):
        
        visited = [-1 for i in range(self.MAX_VERTICIES)]
        # visited = []
        # visited = {i:'undiscovered' for i in range(self.MAX_VERTICIES)}
        h = self.depth_first_search_helper(startingVertex, visited)

        print(f"starting DFS with vertex: {startingVertex}")

        for i in range(self.MAX_VERTICIES):
            if visited[i] == -1:
                break
            print(f"    visited {self.labels[visited[i]]}")
        return h

    def depth_first_search_helper(self, startingVertex: str, visited: list[int]):
        stack = []
        stack.append(self.get_index(startingVertex))
        history = []
        cnt = 0
        while stack:
            currentV = stack.pop()
            # history.append(self.labels[currentV])
            if visited[currentV] == -1:
                cnt += 1
                visited[currentV] = currentV
                for edge in self.get_adjacent_verticies(currentV):
                    stack.append(self.get_index(edge))
                    # history.append(self.labels[self.get_index(edge)])
        return cnt
    
    def find_all_paths(self, startingVertex: str, nth):
        '''
        This function is specific to a square graph that has only right, and down paths. namely from project euler
        '''
        ## get all adjacent verticies from starting vertex
        ## add them to the stack
        discovered = []

        n = self.labels[-1]
        cnt = 0
        stack = []
        v = self.get_adjacent_verticies(self.get_index(startingVertex))
        stack.append(v[0])
        
        ## while the stack is not empty
        while stack:
            nextV = stack.pop()

            for v in self.get_adjacent_verticies(self.get_index(nextV)):
                stack.append(v)
            if nextV == n:
                cnt += 2

        return cnt

    def r(self, startingVertex: str, explored:list=[]):
        if startingVertex == self.labels[-1]:
            return 1
        if startingVertex in explored:
            return 0
        x = 0
        for v in self.get_adjacent_verticies(self.get_index(startingVertex)):
            if v not in explored:
                explored.append(v)
                x += self.r(v, explored)
            else:
                continue

    
    def find_all_paths_rec(self, startingVertex: str, previous:list = []):
        if startingVertex == self.labels[-1]:
            return 1
        # if startingVertex in previous:
        #     return 1
        
        x = 0
        for i in self.get_adjacent_verticies(self.get_index(startingVertex)):
            if i not in previous:
                previous.append(i)
            x += self.find_all_paths_rec(i)
        return x

    def print_graph(self):
        ## This isnt working currently :/
        print(f"Number of Verticies: {self.numVerticies}")
        
        header = ""
        for l in self.labels:
            header += ("    "+l)
        print(header)

        for i in range(0, self.numVerticies):
            print(self.labels[i], end=" ")
            for j in range(0, self.numVerticies):
                new_info = "    "
                if self.matrix[i][j] == sys.maxsize:
                    new_info += ""
                else:
                    new_info += f"{self.matrix[i][j]}"
                print(new_info, end="")
            print()

    def dfs_rec(self, startingVertex, visited):
        visited.append(startingVertex)
        print(startingVertex)

        for v in self.get_adjacent_verticies(self.get_index(startingVertex)):
            if v not in visited:
                self.recurs += 1
                self.dfs_rec(v, visited)

    def dfs(self, startingVertex):
        visited = []

        self.dfs_rec(startingVertex, visited)
            

def lattice_paths(n: int):
    # build the graph
    g = Graph(n)
    cant_go_right = 0
    cant_go_down = 0
    two_options = 0
    last = 0
    # generate verticies for an n x n matrix
    for i in range(1, n**2+1):
        g.add_vertex(str(i))

    # add edges on each vertex going down and right
    for i in range(1, n**2+1):
        if i > n**2 - n and i != n**2: # bottom row
            g.add_egde(str(i), str(i+1), 1)
            cant_go_down += 1
        elif i % n == 0 and i != n**2: # last column
            g.add_egde(str(i), str(i+n), 1)
            cant_go_right += 1
        elif n**2 == i:
            last += 1
        else:
            two_options += 1
            g.add_egde(str(i), str(i+1), 1)
            g.add_egde(str(i), str(i+n), 1)
    
    return g.find_all_paths("1", n)

print("iterative Tests-------------------------------")
node_test = [2,3,4,5,6,7,8,9,10,11]
# node_test = [16]
for i in node_test:
    t1 = time.time()
    c1 = lattice_paths(i)
    t2 = time.time()

    print(f"{i} x {i} has {c1} paths and took {t2-t1} seconds")

# This was tricky, but I found it!
# I started out with a depth first search algorithm, but that was taking too long (20 days to find all paths in a 20 x2 0!)
# Then I found a way to reduce the number of paths search by half. However this was not sufficient. As half of many days is still days.
# I ultimately found a solution by deriving a pattern from the results from a 2 x 2 matrix to an 11 x 11 matrix
# the solution is 40! / (20!*20!)
# I did not discover this but, this pattern can be found by looking at the middle column on Pascal's Triangle
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1
#1 6 15 20 15 6 1
# a 1 x 1 has 2
# a 2 x 2 has 6
# a 3 x 3 has 20 and so on!







