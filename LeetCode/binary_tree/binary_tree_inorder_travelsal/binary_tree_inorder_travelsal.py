"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/binary-tree-inorder-traversal/

"""Import required"""
"""Define global variables"""

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global var_1
        global var_2

        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            var_1 = [int(num_str) for num_str in nums_data.split()]

            var_2 = f.readline()
class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res


def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve()

app()