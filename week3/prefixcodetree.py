class Node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class PrefixCodeTree():
    def __init__(self):
        self.root = Node("")

    def insert(self, codeword, symbol):
        tmp = self.root
        # Inserting nodes into the trees. 0 is a left node, 1 is right
        for i in range(0, len(codeword)):
            if i == len(codeword) - 1:
                if codeword[i] == 0:
                    tmp.left = Node(symbol)
                elif codeword[i] == 1:
                    tmp.right = Node(symbol)
            else:
                if codeword[i] == 0:
                    if tmp.left is None:
                        tmp.left = Node("")
                    tmp = tmp.left
                elif codeword[i] == 1:
                    if tmp.right is None:
                        tmp.right = Node("")
                    tmp = tmp.right

    def decode(self, encodedData, datalen):
        # Convert byte to bitstring
        bitstring = "".join(f"{byte:0>8b}" for byte in encodedData)[:datalen]
        message = ""
        tmp = self.root
        # Traverse down the tree according to bits
        for bit in bitstring:
            if int(bit) == 0:
                tmp = tmp.left
            elif int(bit) == 1:
                tmp = tmp.right

            if tmp.name != "":
                message += tmp.name
                tmp = self.root
        return message
