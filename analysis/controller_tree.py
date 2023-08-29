from typing import List, Dict, Any
import json
import matplotlib.pyplot as plt
import networkx as nx
from treelib import Tree

class ControllerTreeNode:
    """ControllerTreeNode class
    A ControllerTreeNode stores the controller of an agent"""
    
    def __init__(
        self,
        agent="",
        mode="",
        child=[]
    ):
    	self.agent = agent
    	self.mode:str = mode
    	self.child = []

class ControllerTree:
    def __init__(self, root):
        self.root:ControllerTreeNode = root
        self.nodes:List[ControllerTreeNode] = self.get_all_nodes(root)

    def get_all_nodes(self, root: ControllerTreeNode) -> List[ControllerTreeNode]:
        # Perform BFS/DFS to store all the tree node in a list
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node)
            queue += node.child
        return res

    def visualize(self):
        G = nx.Graph()
        count = 0
        for node in self.nodes:
            G.add_node(node.mode)
            for child in node.child:
                G.add_node(child.mode)
                G.add_edge(node.mode, child.mode)
        nx.draw_planar(G,with_labels="True")
        plt.show()
