class Node():
    def __init__(self, root, left, right, name):
        self.root = root
        self.name = name
        self.left = left
        self.right = right

class PrefixCodeTree():
    def __init__(self):
        self.Node = Node(None, None, None, "")

    def insert(self, codeword, symbol):
        if len(codeword) == 1:
            if codeword[0] == 0:
                self.Node.left = Node(self.Node, None, None, symbol)
            elif codeword[0] == 1:
                self.Node.right = Node(self.Node, None, None, symbol)
            return self.Node
        else:
            if codeword[0] == 0:
                self.Node.left = self.insert(codeword[1:], symbol)
            elif codeword[0] == 1:
                self.Node.right = self.insert(codeword[1:], symbol)

    def decode(self, encodedData, datalen):
        return None
