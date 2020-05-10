# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:46:23 2020

@author: cssc
"""

import time
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
    def get_children_data(self):
        children_data_list=[]
        for child in self.children:
            children_data_list.append(child.data)
        return childre# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:46:23 2020

@author: cssc
"""

import time
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
    def get_children_data(self):
        children_data_list=[]
        for child in self.children:
            children_data_list.append(child.data)
        return children_data_list

root = None
def load_input_data(path):
    f = open(path,'r')
    global root
    current_root = root
    for line in f:
        print("Processing line : {}".format(line))
        if line.startswith('#'):
            print('skipping line as it is a comment')
            continue
        parent_id = line.split('\t')[0]
        child_id = line.rstrip('\n').split('\t')[1]
        print("parent_id : {}".format(parent_id))
        print("child_id : {}".format(child_id))
        if int(parent_id) > int(child_id) :
            print("skipping line as it is already processed")
            continue
        if current_root == None:
            print("Processing first node")
            current_root = Node(parent_id)
            current_root.add_child(Node(child_id))
            root = current_root
        elif int(current_root.data) == int(parent_id):
            print("Parent already exists, appending child")
            current_root.add_child(Node(child_id))
        else:
            for child in current_root.children:
                if child.data == parent_id:
                    print("New Parent found, changing current_root")
                    current_root = child
            current_root.add_child(Node(child_id))
        print("Current_Root :{},current_root_children :{}".format(current_root.data,current_root.get_children_data()))
    
def getnode(data, root):
    for node in root.children:
        if node.data == data:
            return node
        else:
            getnode(data, node)

def findallcommonnodes(node1,node2):
    tree_dict = load_input_data('data1.txt')
    node1_ancestors = []
    getparent(tree_dict,node1_ancestors,node1)
    print(node1_ancestors)

def getparent(tree_dict,node1_ancestors,node_value):
    print("searching for {}".format(node_value))
    for (key,value) in tree_dict.items():
        #print("key : {}".format(key))
        #print("value : {}".format(value))
        if value == node_value:
            print("im in in")
            node1_ancestors.append(key)
            if key == 0:
                return key
            else:
                return getparent(key)n_data_list

root = None
def load_input_data(path):
    f = open(path,'r')
    current_root = root
    for line in f:
        print("Processing line : {}".format(line))
        if line.startswith('#'):
            print('skipping line as it is a comment')
            continue
        parent_id = line.split('\t')[0]
        id = line.rstrip('\n').split('\t')[1]
        if parent_id > id :
            print("skipping line as it is already processed")
            continue
        if current_root == None:
            print("Processing first node")
            current_root = Node(parent_id)
            current_root.add_child(Node(id))
        elif current_root.data == parent_id:
            print("Parent already exists, appending child")
            current_root.add_child(Node(id))
        else:
            for child in current_root.children:
                if child.data == parent_id:
                    print("New Parent found, changing current_root")
                    current_root = child
            current_root.add_child(Node(id))
        print("Current_Root :{},current_root_children :{}".format(current_root.data,current_root.get_children_data()))
        time.sleep(1)
    
def getnode(data, root):
    for node in root.children:
        if node.data == data:
            return node
        else:
            getnode(data, node)

def findallcommonnodes(node1,node2):
    tree_dict = load_input_data('data1.txt')
    node1_ancestors = []
    getparent(tree_dict,node1_ancestors,node1)
    print(node1_ancestors)

def getparent(tree_dict,node1_ancestors,node_value):
    print("searching for {}".format(node_value))
    for (key,value) in tree_dict.items():
        #print("key : {}".format(key))
        #print("value : {}".format(value))
        if value == node_value:
            print("im in in")
            node1_ancestors.append(key)
            if key == 0:
                return key
            else:
                return getparent(key)