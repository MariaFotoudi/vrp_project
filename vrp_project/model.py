import math
import random

class model:

    def __init__(self):
        self.all_nodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        warehouse = Node(0, 250, 250, 0, 0)
        self.all_nodes.append(warehouse)
        birthday = 806
        random.seed(birthday)
        for i in range(100):
            idd = i + 1
            x = random.randint(0, 500)
            y = random.randint(0, 500)
            demand = random.randint(100, 300)
            unloading_time = 10
            customer = Node(idd, x, y, demand, unloading_time)
            self.all_nodes.append(customer)
            self.customers.append(customer)

        rows = len(self.all_nodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0,len(self.all_nodes)):
            for j in range(0,len(self.all_nodes)):
                a = self.all_nodes[i]
                b = self.all_nodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist

class Node:
    pass
    def __init__(self, idd, xx, yy, demand, unloading_time,):

        self.ID = idd
        self.x = xx
        self.y = yy
        self.demand = demand
        self.unloading_time = unloading_time
        self.isRouted = False

class Route:
    def __init__(self,dp,capacity):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        self.cost = 0
        self.time = 0
        self.load = 0
        self.capacity = 1700








