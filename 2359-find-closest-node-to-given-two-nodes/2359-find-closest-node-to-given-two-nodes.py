class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1
        MAX_NODES = 10 ** 5 + 1
        visited1 = {node1}
        visited2 = {node2}
        closest_node = MAX_NODES

        while True:
            if node1 != -1:
                node1 = edges[node1]
            if node2 != -1:
                node2 = edges[node2]
            if node1 in visited1 and node2 in visited2: break

            visited1.add(node1)
            visited2.add(node2)

            if node1 in visited2:
                closest_node = node1
            if node2 in visited1 and node2 < closest_node:
                closest_node = node2
            if closest_node < MAX_NODES:
                return closest_node

        return -1
