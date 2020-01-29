"""
给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空，
将此二叉树上下翻转并将它变成一棵树， 原来的右节点将转换成左叶节点。返回新的根。

例子:

输入: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

输出: 返回二叉树的根 [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  




解题思路：
翻转的形式一开始不是很清楚，但是discuss里面的高票答案给了一个很好的解释。看例子，树的左边最深的底层是4，
4是新的root。对于每个root node，将链接右孩子的指针去掉，将root node变为当前左孩子的left node
，root node成为左孩子的right node。

    1
   /  x
  2 -- 3
 /  x
4 -- 5
^
new root
"""

class Solution:
    def upsideDownBinaryTree(self, root):
        # 递归
        parent, parent_right = None, None
        while root:
            l = root.left
            root.left = parent_right
            parent_right = root.right
            root.right = parent
            parent = root
            root = l
        return parent