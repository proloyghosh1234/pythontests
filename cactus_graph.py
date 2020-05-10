class Node(object):
    def __init__(self, data):
        self.data = data
        self.connected_nodes = []
    def add_connection(self, obj):
        if obj not in self.connected_nodes:
            self.connected_nodes.append(obj)
    def get_connected_nodes_data(self):
        connected_nodes_data_list=[]
        for Node in self.connected_nodes:
            connected_nodes_data_list.append(Node.data)
        return connected_nodes_data_list

all_nodes = []
def create_graph(path):
    f = open(path,'r')
    global all_nodes
    for line in f:
        print("Processing line : {}".format(line))
        if line.startswith('#'):
            print('skipping line as it is a comment')
            continue
        node1 = int(line.split('\t')[0])
        node2 = int(line.rstrip('\n').split('\t')[1])
        Node1 = None
        Node2 = None
        found_node1 = 0
        found_node2 = 0
        for N in all_nodes:
            if N.data == node1:
                Node1 = N
                found_node1 +=1
            if N.data == node2:
                Node2 = N
                found_node2 +=1
            if found_node1 + found_node2 == 2:
                break
        if not found_node1:
            Node1 = Node(node1)
            all_nodes.append(Node1)
        if not found_node2:
            Node2 = Node(node2)
            all_nodes.append(Node2)
        Node1.add_connection(Node2)
        Node2.add_connection(Node1)
    print("Print All added nodes")
    for N in all_nodes:
        print("Node : {}, Connected Nodes : {}".format(N.data,N.get_connected_nodes_data()))

def printall(all_nodes):
    for Node in all_nodes:
        print("Node : {}, Connected Nodes : {}".format(Node.data,Node.get_connected_nodes_data()))

def myf(node1, node2):
    Node1 = None
    Node2 = None
    for N in all_nodes:
        if N.data == node1:
            Node1 = N
        if N.data == node2:
            Node2 = N
        if Node1 != None and Node!= None:
            break
    Node1_all_related_nodes = getConnectedNodes_Recursive(Node1,Node2,all_nodes)
    Current_Node = Node1
    return Node1_all_related_nodes
#%%
def getConnectedNodes_Recursive(Node1,Node2,all_connected_nodes):
    Node1_connected_nodes=Node1.connected_nodes
    if Node2 in Node1.connected_nodes:
        Node1_connected_nodes.remove(Node2)
    if len(Node1.connected_nodes) == 1:
        if Node1.connected_nodes[0] in all_connected_nodes:
            return all_connected_nodes
        else:
            return all_connected_nodes+Node1_connected_nodes
    for Node in Node1_connected_nodes:
        all_connected_nodes+getConnectedNodes_Recursive(Node,Node2,all_connected_nodes)

    
