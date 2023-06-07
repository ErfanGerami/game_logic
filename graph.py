class graph():
    def __init__(self,initial_dic={}):
        self.network=initial_dic
        self.marks=[]
        if(len(initial_dic)!=0):
            self.maximum_node=max(initial_dic)
        else:
            self.maximum_node=-1
        self.nodes=[0 for i in range(self.maximum_node+1)]

    def AddNode(self,node):
        '''note that nodes must be positive'''

        self.network[node]=set({})
        if(node>self.maximum_node):
            for i in range(self.maximum_node,node+1):
                self.nodes.append(0)
            self.nodes[node]=1
            self.maximum_node=node
        else:
            self.nodes[node]=1
            self.maximum_node=node

    def AddEdge(self,node1,node2):
        self.network[node1].add(node2)
        self.network[node2].add(node1)
        
    def DeleteNode(self,node):
        for i in self.network[node]:
            self.network[i].remove(node)
        self.network.pop(node)
        if(self.maximum_node==node):
            cnt=node-1
            while(self.nodes[cnt]!=1):
                cnt-=1
            self.maximum_node=cnt
            self.nodes=self.nodes[0:cnt+1]
        else:  
            self.nodes[node]=0

    def DeleteEdge(self,node1,node2):
        self.network[node1].remove(node2)
        self.network[node2].remove(node1)
    #-------------------------------------
    def IsThere(self,node):
        '''return True if the node is in the graph and False if it is not'''
        return self.nodes[node]
    def GetConnections(self,node):
        '''returns a set that contains the nodes that the given node is connected to'''
        return self.network[node]
    
    #---------------------------------------------
    def StartMarking(self):
        '''use to reset or start Marking'''
        
        self.marks=[ 0 for i in range(self.maximum_node+1)]

    def Mark(self,node,color):
        self.marks[node]=color

    def GetMark(self,node):
        return self.marks[node]
    
    def FindPath(self,start,dest):
        '''finds a path betwean start and des and returns it as a list'''
        path=self._FindPath(start,dest)
        return path

    def _FindPath(self, start, dest):
        paths = [[start]]
       
        visited=[ 0 for i in range(self.maximum_node+1)]

        while paths:
            path = paths.pop(0)
            node = path[-1]

            if node == dest:
                return path

            for neighbor in self.GetConnections(node):
                if not visited[neighbor]:
                    visited[neighbor]=1;
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
    print(gr.maximum_node)
    gr.StartMarking()
    print(gr.GetMark(6))
    gr.Mark(6,1)
    print(gr.GetMark(6))
    gr.DeleteNode(7)
    gr.AddEdge(1,2)
    gr.AddEdge(2,3)
    gr.AddEdge(2,5)
    gr.AddEdge(3,6)
    gr.AddEdge(4,5)
    gr.AddEdge(1,6)
    print(gr.maximum_node)
    gr.DeleteEdge(1,6)
    print(gr.FindPath(1,5))
    print(gr.FindPath(1,6))
    

