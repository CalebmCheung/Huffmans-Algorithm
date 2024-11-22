
# Node class for Binary tree structure
class Node:

    character = ''
    freq = 0

    leftChild = None
    rightChild = None
    parent = None

    def __init__(self, character, freq) -> None:
        self.character = character
        self.freq = freq