'''
This problem is really cool! I am going to make a binary tree and fill it will all the numbers
then all I need to do is find the child with the maximum value and visit it!
using the visitor pattern baby!
'''


class Visitor:
    def getVal(self, node):
        pass

class AddVisitor(Visitor):
    nums = []
    def getVal(self, node):
        return self.nums.append(node.num)
    def getSum(self):
        return sum(self.nums)
    
class Node:
    def __init__(self, num, children: list=[]):
        self.num = num
        self.children = children
        self.sum_of_greatest = 0
    def accept(self, visitor: Visitor):
        visitor.getVal(self)
        # print(self.num)
        if self.children and (self.children[0].num > self.children[1].num):
            self.children[0].accept(visitor)
        if self.children and (self.children[0].num < self.children[1].num):
            self.children[1].accept(visitor)
            
    def __str__(self):
        return str(self.num)
    def __repr__(self):
        return str(self.num)


    
data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62,98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]
def build_tree(i, j):
    if i > len(data) - 2:
        return Node(data[i][j], [])
    return Node(data[i][j], [build_tree(i+1,j), build_tree(i+1,j+1)])
    

    


def max_path():
    root = Node(3, [
            Node(7, [
                Node(2, [
                    Node(8,[]),
                    Node(5,[])
                ]),
                Node(4, [
                    Node(5,[]),
                    Node(9,[])
                ])
            ]),
            Node(4, [
                Node(4,[
                    Node(5,[]),
                    Node(9,[])
                ]),
                Node(6, [
                    Node(9,[]),
                    Node(3,[])
                ])
            ])

        ]
    )
    
    v = AddVisitor()

    # root.accept(v)

    # print(v.getSum())

    auto_tree = build_tree(0,0)

    auto_tree.accept(v)
    print(v.nums)
    print(v.getSum())

max_path()
