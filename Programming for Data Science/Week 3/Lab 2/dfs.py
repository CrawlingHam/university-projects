from tree import Node, create_the_tree

def traverse(node: Node, visited_nodes: list[int]) -> None:
    visited_nodes.append(node.value)
    for child in node.get_children():
        traverse(node=child, visited_nodes=visited_nodes)

def depth_first_search(root: Node) -> list[int]:
    visited_nodes: list[int] = []
    traverse(node=root, visited_nodes=visited_nodes)
    return visited_nodes

if __name__ == "__main__":
    test_count = 10

    for i in range(test_count):
        root = create_the_tree()
        result = depth_first_search(root)
        print(f"Test {i + 1}: DFS traversal order: {result}")
