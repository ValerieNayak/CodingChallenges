# Valerie Nayak
# 7/2/2020
# July LeetCode Challenge
# Day 2: Binary Tree Level Order Traversal II

class TreeNode:
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None

def levelOrderBottom(root):
    nodes_at_depths = []

    def traverse_helper(node, level):
        if node is not None:
            if len(nodes_at_depths) <= level:
                nodes_at_depths.append([])
            nodes_at_depths[level].append(node.val)
            traverse_helper(node.left, level + 1)
            traverse_helper(node.right, level + 1)
    
    traverse_helper(root, 0)
    return reversed(nodes_at_depths)