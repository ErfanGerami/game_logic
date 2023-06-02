class graph():
    def __init__(self,initial_dic={}):
        self.network=initial_dic
    def AddNode(self,node):
        self.network[node]=set({})

    def AddEdge(self,node1,node2):
        self.network[node1].add(node2)
        self.network[node2].add(node1)
        
    def DeleteNode(self,node):
        for i in self.network[node]:
            self.network[i].remove[node]
        self.network.pop(node)

    def DeleteEdge(self,node1,node2):
        self.network[node1].remove(node2)
        self.network[node2].remove(node1)
    #-------------------------------------
    def IsThere(self,node):
        '''return True if the node is in the graph and False if it is not'''
        if node in self.network:
            return True
        return False
    def GetConnections(self,node):
        '''returns a set that contains the nodes that the given node is connected to'''
        return self.network[node]
                
  


############################test
# gr=graph()
# gr.AddNode(1)
# gr.AddNode(2)
# gr.AddNode(3)
# gr.AddEdge(2,3);
# gr.AddEdge(1,2);
# print(gr.network);
# print(gr.IsThere(1))
# print(gr.GetConnections(1))
###############################