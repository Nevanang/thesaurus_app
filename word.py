
from node import Node
class Word(Node):
    def __init__(self,keyword,synonyms):
        self.keyword=keyword
        self.synonyms=synonyms
        super().__init__()
    def __lt__(self, otherNode): #without this, linkedlist will compare object which wil not work, can specify newnode instead of newnode.keyword
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Word' and 'NoneType'")
        if self.keyword == otherNode.keyword:
            return self.keyword < otherNode.keyword #alphabetically
        return self.keyword < otherNode.keyword
    def __str__(self): # for err checking
        s = f'({self.keyword},{self.synonyms})'
        return s
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.keyword == otherNode and self.keyword == otherNode 