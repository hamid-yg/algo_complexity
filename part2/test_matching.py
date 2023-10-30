import networkx as nx
import unittest
from algo_part2 import maximum_degree_heuristic_matching
from algo_part2 import minimum_degree_heuristic_matching
def is_matching(graph, matching):
    for node in matching:
        neighbors = set(graph.neighbors(node))
        neighbors_in_matching = neighbors & matching
        if len(neighbors_in_matching) > 1:
            return False
    return True

class TestMatching(unittest.TestCase):
    def test_maximum_degree_matching(self):
        G = nx.gnp_random_graph(120, 0.04)
        matching = maximum_degree_heuristic_matching(G)
        self.assertTrue(is_matching(G, matching))

    def test_minimum_degree_matching(self):
        G = nx.gnp_random_graph(120, 0.04)
        matching = minimum_degree_heuristic_matching(G)
        self.assertTrue(is_matching(G, matching))

if __name__ == '__main__':
    unittest.main()
