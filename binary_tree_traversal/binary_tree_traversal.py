from __future__ import annotations

"""
     F
   /   \
  B     G
 / \     \
A  D      I
  / \    /
 C   E  H

preorder  : root -> left -> right   F, B, A, D, C, E, G, I, H.
inorder   : left -> root -> right   A, B, C, D, E, F, G, H, I. (對binary search tree做inorder traversal就是依序拿取)
postorder : left -> right -> root   A, C, E, D, B, H, I, G, F.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionRecursion:
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root: TreeNode, res: List[int]):
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def inorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: TreeNode, res: List[int]):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def postorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, root: TreeNode, res: List[int]):
        if not root:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

    # euqal
    def postorder_traversal_2(self, root: TreeNode) -> List[int]:
        def postorder(root, res):
            if not root:
                return
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.val)
            return res

        return postorder(root, [])


class SolutionIteratively:

    # root -> left -> right
    # In stack
    # right -> left -> root (LIFO)
    def preorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            res.append(node.val)
        return res

    # left -> root -> right
    # In stack:
    # push right -> root -> left (LIFO)
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node)
                stack.append(node.left)
            else:
                if stack:
                    node = stack.pop()
                    res.append(node.val)
        return res

    # left -> right -> root
    def postorder_traversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]


root = TreeNode("F")
root.left = TreeNode("B")
root.right = TreeNode("G")
root.left.left = TreeNode("A")
root.left.right = TreeNode("D")
root.left.right.left = TreeNode("C")
root.left.right.right = TreeNode("E")
root.right.right = TreeNode("I")
root.right.right.left = TreeNode("H")

print("preorder:", SolutionRecursion().preorder_traversal(root))

print("inorder:", SolutionRecursion().inorder_traversal(root))

print("postorder:", SolutionRecursion().postorder_traversal(root))

# print(
#     'postorder:', SolutionRecursion().postorder_traversal_2(root)
# )

print("preorder:", SolutionIteratively().preorder_traversal(root))

print("inorder:", SolutionIteratively().inorder_traversal(root))

print("postorder:", SolutionIteratively().postorder_traversal(root))
