from smath import Graph
import time



# def lattice_paths(n: int, rec=False):
#     # build the graph
#     g = Graph(n)

#     # generate verticies for an n x n matrix
#     for i in range(1, n**2+1):
#         g.add_vertex(str(i))

#     # add edges on each vertex going down and right
#     for i in range(1, n**2+1):
#         if i > n**2 - n and i != n**2: # bottom row
#             g.add_egde(str(i), str(i+1), 1)
#         elif i % n == 0 and i != n**2: # last column
#             g.add_egde(str(i), str(i+n), 1)
#         elif n**2 == i:
#             ...
#         else:
#             g.add_egde(str(i), str(i+1), 1)
#             g.add_egde(str(i), str(i+n), 1)
#     #g.print_graph()
    
#     return g.find_all_paths_rec("1") if rec else g.find_all_paths("1")


# print("iterative Tests-------------------------------")
# node_test = [2,3,4,5,6,7,8,9,10,11]
# # node_test = [16]
# for i in node_test:
#     t1 = time.time()
#     c1 = lattice_paths(i)
#     t2 = time.time()

#     print(f"{i} x {i} has {c1} paths and took {t2-t1}")

def buildMatrix(size: int):
        # build the graph
        g = Graph(size)

        # generate verticies for an n x n matrix
        for i in range(1, size**2+1):
            g.add_vertex(str(i))

        # add edges on each vertex going down and right
        for i in range(1, size**2+1):
            if i > size**2 - size and i != size**2: # bottom row
                g.add_egde(str(i), str(i+1), 1)
            elif i % size == 0 and i != size**2: # last column
                g.add_egde(str(i), str(i+size), 1)
            elif size**2 == i:
                ...
            else:
                g.add_egde(str(i), str(i+1), 1)
                g.add_egde(str(i), str(i+size), 1)
        return g.matrix





