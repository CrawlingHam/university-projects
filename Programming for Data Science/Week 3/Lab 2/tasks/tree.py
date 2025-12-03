from __future__ import annotations

class Node:
    def __init__(self, value: int) -> None:
        self.children: list[Node] = []
        self.parent: Node = None
        self.value = value

    def set_parent(self, parent: Node) -> None:
        self.parent = parent

    def get_parent(self) -> Node:
        return self.parent

    def add_child(self, child: Node) -> None:
        child.set_parent(self)
        self.children.append(child)

    def get_children(self) -> list[Node]:
        return self.children


def create_the_tree() -> Node:
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.add_child(n3)
    n1.add_child(n4)

    n2.add_child(n5)
    n2.add_child(n6)

    n0.add_child(n1)
    n0.add_child(n2)

    return n0
