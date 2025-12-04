from data_models.models import TreeSearchResult
from tree import Node, create_the_tree
from bfs import breadth_first_search
from dfs import depth_first_search

class TreeSearch:
    def __init__(self, root: Node) -> None:
        self.root = root

    def run(self) -> TreeSearchResult:
        bfs_visited_nodes = self.breadth_first_search()
        dfs_visited_nodes = self.depth_first_search()

        return TreeSearchResult(
            bfs_visited_nodes=bfs_visited_nodes,
            dfs_visited_nodes=dfs_visited_nodes,
        )

    def breadth_first_search(self) -> list[int]:
        return breadth_first_search(root=self.root)

    def depth_first_search(self) -> list[int]:
        return depth_first_search(root=self.root)

if __name__ == "__main__":
    root = create_the_tree()
    tree_search = TreeSearch(root)
    result = tree_search.run()
    
    print(f"BFS traversal order: {result.bfs_visited_nodes}")
    print(f"DFS traversal order: {result.dfs_visited_nodes}")

# When should we use BFS instead of DFS, and when is DFS more appropriate?
# Answer: BFS is best for shallow trees or when finding the shortest path. 
# DFS is better for deep trees or when deep exploration is more important.
