import sys
path_to_module = "./src/"
sys.path.append(path_to_module)

from main import *

trie = Trie()

def test_base_Trie():
    assert trie.i == 0