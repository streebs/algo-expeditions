from smath import Graph


g = Graph()

# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")
# g.add_vertex("E")
# g.add_vertex("F")


# g.add_egde("A", "B", 2)
# g.add_egde("A", "F", 9)
# g.add_egde("B", "F", 6)

# g.add_egde("B", "D", 1)

# g.add_egde("B", "C", 8)
# g.add_egde("C", "D", 1)
# g.add_egde("E", "C", 7)
# g.add_egde("E", "D", 3)
# g.add_egde("F", "E", 9)

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_vertex("H")
g.add_vertex("I")


g.add_egde("A", "B", 1)
g.add_egde("A", "D", 1)
g.add_egde("B", "C", 1)
g.add_egde("B", "E", 1)
g.add_egde("C", "F", 1)
g.add_egde("D", "E", 1)
g.add_egde("D", "G", 1)
g.add_egde("E", "F", 1)
g.add_egde("E", "H", 1)
g.add_egde("F", "I", 1)
g.add_egde("G", "H", 1)
g.add_egde("H", "I", 1)


g.depth_first_search("A")

# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")

# g.add_egde("A", "B", 1)
# g.add_egde("A", "C", 1)
# g.add_egde("B", "D", 1)
# g.add_egde("C", "D", 1)

# g.depth_first_search("A")


