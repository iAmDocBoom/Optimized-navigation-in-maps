import sys

src_path = {}
src_dist= {}

class Graph(object):
    node_reference= dict
    edge_attr_reference= dict
    adjlist_reference= dict

# Code to create a Constructor for Graph()
    def __init__(self, data=None, **ptr):
        nd = self.node_reference
        self.node = nd()
        self.adjacent = nd()
        self.graph = {}

# Code to add a node
    def addnode(self, n, dictionary=None, **ptr):
        if dictionary is None:
            dictionary = ptr
        else:
            try:
                dictionary.update(ptr)
            except Exception:
				print 'Sorry! There is an error in adding node'
        if n in self.node:
            self.node[n].update(dictionary)
        else:
            self.adjacent[n] = self.adjlist_reference()
            self.node[n] = dictionary

# Code to add an edge
    def addedge(self, m, n, d1=None, **ptr):
        if d1 is None:
            d1 = ptr
        else:
            try:
                d1.update(ptr)
            except AttributeError:
                print 'Sorry! There is an error in adding edge'

        if m not in self.node:
            self.adjacent[m] = self.adjlist_reference()
            self.node[m] = {}
        if n not in self.node:
            self.adjacent[n] = self.adjlist_reference()
            self.node[n] = {}

        Data_dict = self.adjacent[m].get(n, self.edge_attr_reference())
        Data_dict.update(d1)
        self.adjacent[m][n] = Data_dict
        self.adjacent[n][m] = Data_dict

# Code to get nodes
    def getnodes(self, data=False):
        if data:
            return iter(self.node.items())
        return iter(self.node)

# Code to get an edge
    def getedge(self, u, v, dft=None):
        try:
            return self.adjacent[u][v]
        except KeyError:
            return dft

# Code to fetch neighbors
    def getneighbors(self, n):
        try:
            return list(self.adjacent[n])
        except KeyError:
            print 'Sorry! There is an error in getting neighbors'

def main(argv):
    # read argurments
    filename=argv[1]
    src=argv[2]
    dst=argv[3]

    # initiate Graph
    graph=Graph()
    # open and read file
    file_dat=open(filename)
    for data in file_dat:
        if data.strip()=="END OF INPUT":
            break
        line_data=data.split()
        cost=int(line_data[2])

        #Code to create a graph and to add nodes and edges to it
        graph.addnode(line_data[0])
        graph.addnode(line_data[1])
        graph.addedge(line_data[0],line_data[1],dist=cost)

    # Code to initiate Source Destination with distance 0 else infinity
    for node in graph.getnodes():
        if node == src:
            src_dist[node] = 0
            src_path[node] = [node]
        else:
            src_dist[node] = float('inf')
            src_path[node] = []

    nodelist = []
    nodelist.append((0,src))
    nodelist = sorted(nodelist, key=lambda col: col[0])

    # Code to search for neighbors having shortest edge cost
    while len(nodelist):
        next_node= nodelist.pop(0)
        neighbors_list = graph.getneighbors(next_node[1])
        for n in neighbors_list:
            edge_n=graph.getedge(next_node[1],n)['dist']
            d = next_node[0] + edge_n
            if d < src_dist[n]:
                p = src_path[next_node[1]] + [n]
                src_dist[n] = d
                src_path[n] = p
                nodelist.append((d,n))
                nodelist = sorted(nodelist, key=lambda col: col[0])

    # Code to fetch the shortest path
    if src_dist[dst] < float('inf'):
        path_list = src_path[dst]
        print 'distance: ' + str(src_dist[dst]) + ' km'
        print 'route:'
        for i in range(1,len(path_list)):
            p=path_list[i-1]
            q=path_list[i]
            edge_p_q=graph.getedge(path_list[i-1],path_list[i])['dist']
            print '%s to %s, %s km' %(p,q,edge_p_q)
    else:
        print 'distance: infinity'
        print 'route:'
        print 'none'

if __name__ == '__main__':
    main(sys.argv)
