class graph():
    def __init__(self,initial_dic={}):
        self.network=initial_dic
        self.colors=[]
        self.min_path=-1
        self.path=[]
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
    def StartColoring(self):
        '''use to reset or start coloring'''
        maximum_node=max(self.network)
        self.colors=[]
        for i in range(0,maximum_node+1):
            self.colors.append(0)

    def Color(self,node,color):
        '''note that the color must be a positive number'''
        self.colors[node]=color

    def GetColor(self,node):
        return self.colors[node]
    
    def FindPath(self,start,dest):
        '''finds a path betwean start and des and returns it as a list'''
        self.min_path=len(self.network)+1
        colors_temp=self.colors.copy()
        self.StartColoring()
        self.path=[]

        self._FindPath(start,dest,0,[])
        self.colors=colors_temp.copy()
        return self.path

    def _FindPath(self,curr,dest,depth,curr_path):
        '''use FindPath instead to find a path'''
        curr_path.append(curr)
        if(depth>=self.min_path):
            return 
            
        if(curr==dest):
            self.min=depth
            self.path=curr_path.copy()

        self.Color(curr,depth)
        for node in self.network[curr]:

            if(self.GetColor(node)>depth+1 or self.GetColor(node)==0):
                self.Color(node,depth+1)
                self._FindPath(node,dest,depth+1,curr_path)
                curr_path.pop()
        
            
               
  

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
    print(gr.network)
    print(gr.FindPath(1,5))
    print(gr.FindPath(1,6))
    

