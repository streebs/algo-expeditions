from smath import Graph
import time

# g = Graph()

# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")
# g.add_vertex("E")
# g.add_vertex("F")
# g.add_vertex("G")
# g.add_vertex("H")
# g.add_vertex("I")


# g.add_egde("A", "B", 1)
# g.add_egde("A", "D", 1)
# g.add_egde("B", "C", 1)
# g.add_egde("B", "E", 1)
# g.add_egde("C", "F", 1)
# g.add_egde("D", "E", 1)
# g.add_egde("D", "G", 1)
# g.add_egde("E", "F", 1)
# g.add_egde("E", "H", 1)
# g.add_egde("F", "I", 1)
# g.add_egde("G", "H", 1)
# g.add_egde("H", "I", 1)


# print(g.find_all_paths("A"))

# g1 = Graph(2)

# g1.add_vertex("A")
# g1.add_vertex("B")
# g1.add_vertex("C")
# g1.add_vertex("D")

# g1.add_egde("A", "B", 1)
# g1.add_egde("A", "C", 1)
# g1.add_egde("B", "D", 1)
# g1.add_egde("C", "D", 1)

# print(g1.find_all_paths("A"))
# print("----------------------------------------")
# print()

def lattice_paths(n: int, rec=False):
    # build the graph
    g = Graph(n)

    # generate verticies for an n x n matrix
    for i in range(1, n**2+1):
        g.add_vertex(str(i))

    # add edges on each vertex going down and right
    for i in range(1, n**2+1):
        if i > n**2 - n and i != n**2: # bottom row
            g.add_egde(str(i), str(i+1), 1)
        elif i % n == 0 and i != n**2: # last column
            g.add_egde(str(i), str(i+n), 1)
        elif n**2 == i:
            ...
        else:
            g.add_egde(str(i), str(i+1), 1)
            g.add_egde(str(i), str(i+n), 1)
    #g.print_graph()
    
    return g.find_all_paths_rec("1") if rec else g.find_all_paths("1")


print("iterative Tests-------------------------------")
node_test = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# node_test = [16]
for i in node_test:
    t1 = time.time()
    c1 = lattice_paths(i)
    t2 = time.time()

    print(f"{i} x {i} has {c1} paths and took {t2-t1}")

print("Recursive Tests-------------------------------")
node_test = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# node_test = [16]
for i in node_test:
    t1 = time.time()
    c1 = lattice_paths(i, True)
    t2 = time.time()

    print(f"{i} x {i} has {c1} paths and took {t2-t1}")

# according to exponential interpolation the time it take for this function to process depending on n is:
# 2.06551*10^-7e^(1.48869x) <- pretty accurate too!



