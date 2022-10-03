"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        way_p = [p]
        way_q = [q]

        while p.parent is not None:
            way_p.append(p.parent)
            p = p.parent

        while q.parent is not None:
            way_q.append(q.parent)
            q = q.parent

        # reversed to lists
        way_p = reversed(way_p)
        way_q = reversed(way_q)

        common_node = None
        for idx in range(min(len(way_q), len(way_p))):
            if way_q[idx] == way_q[idx]:
                common_node = way_q[idx]
            else:
                return common_node

        return common_node


"""
Elegante way!

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, q1 = p, q

        while p1 != q1:
            p1 = p1.parent if p1.parent else q
            q1 = q1.parent if q1.parent else p
            
        return p1
"""