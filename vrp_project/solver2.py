from model import *

class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []

class CustomerInsertion(object):
    def __init__(self):
        self.customer = None
        self.route = None
        self.cost = 10 ** 9


class CustomerInsertionAllPositions(object):
    def __init__(self):
        self.customer = None
        self.route = None
        self.insertionPosition = None
        self.cost = 10 ** 9




class Solver2:
    def __init__(self, m):
        self.allNodes = m.all_nodes
        self.customers = m.customers
        self.depot = m.all_nodes[0]
        self.distanceMatrix = m.matrix
        self.capacity = m.capacity
        self.sol = None
        #self.bestSolution = None deite an xriazontai
        #self.searchTrajectory = [] deite an xreiazontai

    def solve(self):
        self.SetRoutedFlagToFalseForAllCustomers()
        print("Nearest Neighborhood Solution :")
        self.ApplyNearestNeighborMethod()
        self.ReportSolution(self.sol)
        print()
        # self.MinimumInsertions() deite an xreiazete

        return self.sol

    def SetRoutedFlagToFalseForAllCustomers(self):
            for i in range(0, len(self.customers)):
                self.customers[i].isRouted = False

    def ApplyNearestNeighborMethod(self):
        modelIsFeasible = True
        self.sol = Solution()
        insertions = 0
        

        while insertions < len(self.customers):
            bestInsertion = CustomerInsertion()
            lastOpenRoute: Route = self.GetLastOpenRoute()

            if lastOpenRoute is not None:
                self.IdentifyBestInsertion(bestInsertion, lastOpenRoute)

            if bestInsertion.customer is not None:
                self.ApplyCustomerInsertion(bestInsertion)
                insertions += 1
            else:
                # If there is an empty available route
                if lastOpenRoute is not None and len(lastOpenRoute.sequenceOfNodes) == 2:
                    break
                else:
                    rt = Route(self.depot, self.capacity)
                    self.sol.routes.append(rt)

    def GetLastOpenRoute(self):
        if len(self.sol.routes) == 0:
            return None
        else:
            return self.sol.routes[-1]

    def IdentifyBestInsertion(self, bestInsertion, rt):
        for i in range(0, len(self.customers)):
            candidateCust: Node = self.customers[i]
            if candidateCust.isRouted is False:
                var = rt.sequenceOfNodes[-1]
                if rt.load + candidateCust.demand <= rt.capacity :
                    lastNodePresentInTheRoute = rt.sequenceOfNodes[-1]
                    trialCost = self.distanceMatrix[lastNodePresentInTheRoute.ID][candidateCust.ID]
                    if trialCost < bestInsertion.cost:
                        bestInsertion.customer = candidateCust
                        bestInsertion.route = rt
                        bestInsertion.cost = trialCost

    def ReportSolution(self, sol):
        for i in range(0, len(sol.routes)):
            rt = sol.routes[i]
            print("Route", i + 1, "Cost:", round(rt.cost, 2), end=' --- ')
            for j in range(0, len(rt.sequenceOfNodes)):
                print(rt.sequenceOfNodes[j].ID, end=' ')
            print()
        print("Total Objective Function Cost:", round(self.sol.cost, 2))


    def ApplyCustomerInsertion(self, insertion):
        insCustomer = insertion.customer
        rt = insertion.route


        #insIndex = len(rt.sequenceOfNodes) - 1
        rt.sequenceOfNodes.append(insCustomer)

        beforeInserted = rt.sequenceOfNodes[-2]

        costAdded = self.distanceMatrix[beforeInserted.ID][insCustomer.ID] + self.distanceMatrix[insCustomer.ID][
            self.depot.ID]
        costRemoved = self.distanceMatrix[beforeInserted.ID][self.depot.ID]


        rt.cost += costAdded - costRemoved
        self.sol.cost += costAdded - costRemoved

        rt.load += insCustomer.demand

        insCustomer.isRouted = True

    def CalculateTotalCost(self, sol):
        c = 0
        for i in range(0, len(sol.routes)):
            rt = sol.routes[i]
            for j in range(0, len(rt.sequenceOfNodes) - 1):
                a = rt.sequenceOfNodes[j]
                b = rt.sequenceOfNodes[j + 1]
                c += self.distanceMatrix[a.ID][b.ID]
        return c


