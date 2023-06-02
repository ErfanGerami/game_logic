class graph():
    def __init__(self,initial_dic={}):
        self.network=initial_dic
        self.colors={}
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
        if node in self.network:
            return True
        return False
    def GetConnections(self,node):
        '''returns a set that contains the nodes that the given node is connected to'''
        return self.network[node]
    def Color(self,node,positive_color):
        '''note that the color must be a positive number'''
        self.colors[node]=positive_color

    def IsColored(self,node):
        return (node in self.colors)
    def GetColor(self,node):
        return self.colors[node]
    
    def FindPath(self,start,dest):
        '''finds a path betwean start and des and returns it as a list'''
        path=self._FindPath(start,dest)
        size=len(path);
        for i in range(size//2):
            temp=path[i]
            path[i]=path[size-1-i]
            path[size-1-i]=temp
        return path

    def _FindPath(self,curr,dest):
        '''use FindPath instead to find a path'''
        if(curr==dest):
                return [dest]
        self.Color(curr,1)
        for node in self.network[curr]:
            if(not self.IsColored(node)):
                founded_path=self._FindPath(node,dest)
                if(len(founded_path)!=0):
                    founded_path.append(curr)
                    return founded_path
        return []
            
               
    
######################test
#gr=graph();
#gr.AddNode(1);
#gr.AddNode(2);
#gr.AddNode(3);
#gr.AddNode(4);
#gr.AddNode(5);
#gr.AddNode(6);
#gr.AddEdge(1,2);
#gr.AddEdge(2,3);
#gr.AddEdge(2,5);
#gr.AddEdge(3,6);
#gr.AddEdge(4,5);
#print(gr.FindPath(1,5));
###########################

