class Node():
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

class PrefixCodeTree():
    def __init__(self):
        self.root = None

    def insert(self, codeword, symbol):
        if self.root is None:
            if codeword[0] == 0:
                self.root = Node(None)
                self.root.left = Node(symbol)
            elif codeword[0] == 1:
                self.root = Node(None)
                self.root.right = Node(symbol)
        else:
            if len(codeword) == 1:
                if codeword[0] == 0:
                    self.left = Node(symbol)
                elif codeword[0] == 1:
                    self.right = Node(symbol)
            else:
                self.insert(codeword[1:], symbol)
        
    def decode(self, encodedData, datalen):
        return None
