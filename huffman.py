#write a program to implement huffman encoding using greedy strategy
import time
import heapq           # Used to create a priority queue (min-heap)

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right       
        self.huff = ''            # 0 or 1 assigned later for tree traversal

    def __lt__(self, nxt):
        return self.freq < nxt.freq

# print Huffman codes by traversing the tree
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)   # Traverse left subtree
    if node.right:
        printNodes(node.right, newVal)    # Traverse right subtree
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")  # Leaf node: print symbol and code

# Step 1: Take input for symbols and their frequencies
n = int(input("Enter number of symbols: "))
chars = []
freq = []
for i in range(n):
    char = input(f"Enter symbol : ")
    chars.append(char)
    f = int(input(f"Enter frequency for {char}: "))
    freq.append(f)

# Step 2: Create a heap of initial nodes
nodes = []
for i in range(n):
    heapq.heappush(nodes, Node(freq[i], chars[i]))    # Push each node into heap

start_time = time.time()

# Step 3: Build Huffman tree by combining two lowest frequency nodes
#this part is greedy approach
while len(nodes) > 1:
    left = heapq.heappop(nodes)           # Smallest node
    right = heapq.heappop(nodes)          # Second smallest node
   
    left.huff = 0      # Assign 0 to left branch
    right.huff = 1      # Assign 1 to right branch
   
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right) # Merge nodes
    heapq.heappush(nodes, newNode)    # Push new node back into heap

# Step 4: Get the root node (final Huffman tree)
huffman_tree_root = nodes[0]

# Step 5: Print Huffman codes for all symbols
print("Huffman Codes:")
printNodes(huffman_tree_root)

# Step 6: Display execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution time: {execution_time:.6f} seconds")

# time complexity=O(n log n)
#space complexity=O(n)
# ex
# symbol    frequency  HUFFMAN CODE
#  A         5            00
#  B         9            01
#  C         12           10
#  D         13           11

#             (39)
#          /       \
#       (14)       (25)
#      /    \     /    \
#    (5)    (9)  (12)   (13)
#    A      B    C       D