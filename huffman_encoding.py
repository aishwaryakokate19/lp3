import heapq

# Node structure for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparator for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman codes
def huffman_encoding(text):
    # Step 1: Frequency dictionary
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: Create priority queue (min-heap)
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    # Step 3: Build Huffman Tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    root = heap[0]

    # Step 4: Generate codes by traversing tree
    codes = {}
    def generate_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes


# Example usage
text = "huffmanencodingexample"
codes = huffman_encoding(text)

print("Character | Huffman Code")
print("--------------------------")
for char, code in codes.items():
    print(f"    {char}      |   {code}")
