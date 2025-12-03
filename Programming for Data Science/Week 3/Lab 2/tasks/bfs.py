from tree import Node, create_the_tree
from collections import deque

def breadth_first_search(root: Node) -> list[int]:
    queue: deque[Node] = deque([root])
    visited_nodes: list[int] = []

    while queue:
        node = queue.popleft()
        visited_nodes.append(node.value)

        for child in node.get_children():
            queue.append(child)

    return visited_nodes

if __name__ == "__main__":
    test_count = 10

    for i in range(test_count):
        root = create_the_tree()
        result = breadth_first_search(root)
        print(f"Test {i + 1}: BFS traversal order: {result}")