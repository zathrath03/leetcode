class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1
        MAX_NODES = 10 ** 5 + 1
        n1 = {node1}
        n2 = {node2}
        ans = MAX_NODES

        while True:
            if node1 != -1:
                node1 = edges[node1]
            if node2 != -1:
                node2 = edges[node2]
            if node1 in n1 and node2 in n2: break

            n1.add(node1)
            n2.add(node2)

            if node1 in n2:
                ans = node1
            if node2 in n1 and node2 < ans:
                ans = node2
            if ans < MAX_NODES:
                return ans

        return -1
