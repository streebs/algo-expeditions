from smath import Graph


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

def lattice_paths(n: int):
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
    
    return g.find_all_paths("1")


print(lattice_paths(20))



