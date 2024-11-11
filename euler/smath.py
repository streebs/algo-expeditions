# I am using this as my own library for the things that I want to implement, 
# but also is resused alot throught out Project Euler.

import math
import sys

def isPrime(n: int) -> bool:
    '''
    Checks if number is prime
    ### Arguments
    **n**: positive integer
    ### Return
    returns True if n is prime
    '''
    # find the sqrt of n and round up
    if n == 2:
        return True
    if n == 1:
        return False
    
    x = math.floor(n**.5)
    for i in range(2, x+1):
        if n % i == 0:
            return False

    return True 


def factorization(n : int, prime=True) -> list:
    '''
    Factor an integer
    ### Arguments
    **n**: positive integer<br>
    **prime**(opt): get prime factorization | Default: True<br>
    **recur**(opt): use recursive algorithm | Default: True<br>

    ### Return
    list of factors
    '''
    if prime:
        # if n is prime return n
        if isPrime(n):
            return [n]
        # find 2 facors of n and recurse
        a = 0
        b = 0
        for i in range(2, n):
            if n % i == 0:
                a = i
                b = int(n / a)
                break
        return factorization(a) + factorization(b)
    
    if not prime:
        a = 0
        b = 0
        factors = set()
        for i in range(1, math.floor(n**.5)):
            if n % i == 0:
                a = i
                b = int(n / a)
                factors.add(a)
                factors.add(b)
        return list(factors)

def linear_regression(x_vec: list, y_vec: list, y):
    n = len(x_vec)
    sum_x = sum(x_vec)
    sum_y = sum(y_vec)
    sum_xy = sum([a*b for a,b in zip(x_vec, y_vec)])
    sum_x_2 = sum([x*x for x in x_vec])

    a = (sum_y * sum_x_2 - sum_x * sum_xy) / (n * sum_x_2 - sum_x**2)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_2 - sum_x**2)

    # y = a + bx
    # (y - a) / b = x

    return (y - a) / b


def collatz(n: int, seq=[]):
    seq += [n]
    if n == 1:
        return seq
    if n % 2 == 0:
        return collatz(int(n / 2), seq)
    else:
        return collatz(3*n + 1, seq)
    

class Graph:
    MAX_VERTICIES = 10
    matrix = [[] for i in range(0,MAX_VERTICIES)]
    numVerticies = 0
    labels = ["" for i in range(0,MAX_VERTICIES)]

    def __init__(self):
        for i in range(0, self.MAX_VERTICIES):
            for j in range(0, self.MAX_VERTICIES):
                self.matrix[i].append(sys.maxsize)

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
            if self.matrix[sourceIndex][i] != sys.maxsize:
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
            



