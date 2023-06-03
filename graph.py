class graph():
    def __init__(self,initial_dic={}):
        self.network=initial_dic
        self.marks=[]
        self.min_path=-1
    def AddNode(self,node):
        self.network[node]=set({})

    def AddEdge(self,node1,node2):
        self.network[node1].add(node2)
        self.network[node2].add(node1)
        
    def DeleteNode(self,node):
        for i in self.network[node]:
            self.network[i].remove(node)
        self.network.pop(node)

    def DeleteEdge(self,node1,node2):
        self.network[node1].remove(node2)
        self.network[node2].remove(node1)
    #-------------------------------------
    def IsThere(self,node):
        '''return True if the node is in the graph and False if it is not'''
        return (node in self.network)
    def GetConnections(self,node):
        '''returns a set that contains the nodes that the given node is connected to'''
        return self.network[node]
    
    #---------------------------------------------
    def StartMarking(self):
        '''use to reset or start Marking'''
        maximum_node=max(self.network)
        self.marks=[]
        for i in range(0,maximum_node+1):
            self.marks.append(0)

    def Mark(self,node,color):
        self.marks[node]=color

    def GetMark(self,node):
        return self.marks[node]
    
    def FindPath(self,start,dest):
        '''finds a path betwean start and des and returns it as a list'''
        marks_temp=self.marks.copy()
        self.StartMarking()

        path=self._FindPath(start,dest)
        self.marks=marks_temp.copy()
        return  path

    def _FindPath(self, start, dest):
        paths = [[start]]
       

        while paths:
            path = paths.pop(0)
            node = path[-1]

            if node == dest:
                return path

            for neighbor in self.GetConnections(node):
                if not self.GetMark(neighbor):
                    self.Mark(neighbor,1)
                    path_temp = path + [neighbor]
                    paths.append(path_temp)

        return []
        
            
               
  

if __name__=="__main__":
    gr=graph()
    gr.AddNode(1)
    
    gr.AddNode(2)
    gr.AddNode(3)
    gr.AddNode(4)
    gr.AddNode(5)
    gr.AddNode(6)
    gr.AddNode(7)
    gr.DeleteNode(7)

    gr.AddEdge(1,2)
    gr.AddEdge(2,3)
    gr.AddEdge(2,5)
    gr.AddEdge(3,6)
    gr.AddEdge(4,5)
    gr.AddEdge(1,6)
    gr.DeleteEdge(1,6)
    print(gr.FindPath(1,5))
    print(gr.FindPath(1,6))
    

