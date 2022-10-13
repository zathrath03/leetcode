from gc import get_referrers

class Solution:
    def deleteNode(self, node):
        referrers = get_referrers(node)
        if referrers:
            parent = referrers[0]
            if parent.get('next'):
                parent['next'] = node.next
                del node
        else:
            node.val, node.next = node.next.val, node.next.next