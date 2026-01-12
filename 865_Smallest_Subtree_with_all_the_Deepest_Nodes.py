'''
865. Smallest Subtree with all the Deepest Nodes

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depthMap : dict = {}
        # create a dict of candidates recursively
        def allNodes(node : TreeNode, parents : list[TreeNode] = [], depth : int = 0) -> None:
            if (node.left != None):
                allNodes(node.left, parents+[node], depth+1)
            if (node.right != None):
                allNodes(node.right, parents+[node], depth+1)
            if (node.left == None and node.right == None):
                # store path to node and depth
                depthMap[node.val] = (parents+[node], depth)
        allNodes(root)
        deepest : list[int] = []
        highestDepth : int = -1
        # find deepest nodes
        for node in depthMap.keys():
            # reset deepest if new highest found
            if (depthMap[node][1] > highestDepth):
                deepest = []
                highestDepth = depthMap[node][1]
                deepest.append(node)
            elif (depthMap[node][1] == highestDepth):
                deepest.append(node)
        counter: int = -1
        # go up the tree until all are the same
        while(True):
            val: int = depthMap[deepest[0]][0][counter]
            equal : bool = True
            for node in deepest:
                if (depthMap[node][0][counter] != val):
                    equal = False
                    break
            if (equal):
                return depthMap[deepest[0]][0][counter]
            counter -= 1