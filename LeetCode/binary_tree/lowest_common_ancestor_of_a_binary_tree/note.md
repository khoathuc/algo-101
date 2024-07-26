# Naive
using DFS, store ancestor of each node and found the common ancestor

# using LCA
- let h(u) is height of node u
- let h(u) < h(v)
	- move u to u' that h(u') == h(v)
	- move u and u' to their next parents until their parents is the same.

=> found lowest common ancestor