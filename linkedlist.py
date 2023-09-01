
from word import Word
import random
class SortedList():
    def __init__(self):
        self.head = None
        self.current = None
        self.length = 0
    def __appendToHead(self, newNode): 
        oldHead = self.head
        self.head = newNode
        self.head.next = oldHead 
        self.length += 1
        
    def deleteAll(self):
        while self.head!=None:
            temp=self.head
            self.head=self.head.next
            temp=None
        print('All previous keywords and synonyms inputted have been deleted.')
    
    def inserting(self, keyword,syn):
        self.length += 1
        newnode=Word(keyword,syn) #make node
        # If list is currently empty
        if self.head is None:
            self.head = newnode # a form of append
            return
        # Check if it is going to be new head
        if newnode < self.head: # we use this to sort keyword alphabeticaly, the < sorts it alphabetically 
            self.__appendToHead(newnode)
            return
        # Check it is going to be inserted
        # between any pair of Nodes (left, right) sorting
        leftNode = self.head
        rightNode = self.head.next 
        while rightNode != None:
            if newnode < rightNode: # this checks the alphabetical order of the existing nodes to see where to put
                leftNode.next = newnode
                newnode.next = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.next
        # Once we reach here it must be added at the tail
        leftNode.next = newnode #rightnode is null

    def lengthOfList(self):
        total=0
        if self.head==None:
            return total
        else:
            cur=self.head
            while cur.next!=None:
                total+=1
                cur=cur.next
            total+=1
            return total 
        
    def printThesaurus(self,number='1'): #default number=1 is alphabetically sorted
        current_node=self.head
        output=''
    
        while True: # no next current node
            if number=='1':
                current_node.synonyms.sort()
            elif number=='2':
                current_node.synonyms.sort(key=lambda x:(len(x),x))
            elif number=='3':
                current_node.synonyms.sort(key=lambda x:(len(x))) #?
            elif number=='4':
                random.shuffle(current_node.synonyms)

            if current_node.next==None:
                synonym_string=', '.join(current_node.synonyms)
                output+=f"{current_node.keyword}: {synonym_string}\n" 
                break
            else:
                synonym_string=', '.join(current_node.synonyms)
                output+=f"{current_node.keyword}: {synonym_string}\n"
                current_node=current_node.next
        return output

    def open(self,key): #
        try:
            key.pop() # remove empty string at the back
            for i in range(0,len(key),2):
                arr=list(key[i+1].split(', ')) #synonym is key[i+1], split them into singular synonyms
                arr[0]=arr[0].replace(" ", "") #remove spacing in the first synonym
                self.inserting(key[i],arr)
        except IndexError and AttributeError:
            print('File format not supported')
            return

    def deleteNode(self, key):
            
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted, only for head
        if (temp is not None):
            if (temp.keyword == key):
                self.head = temp.next
                temp = None
                return True


        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.keyword == key:
                break
            prev = temp #node of data i want deleted
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return False

        # Unlink the node from linked list
        prev.next = temp.next #make prev node connect to next node of temp etc 2->3 becomes 2->4

        temp = None #removes node, etc 3
        return True
    def get(self,keyword):
        current=self.head
        while True:
            if current==keyword:
                return current.synonyms
            if current.next==None:
                return 0
            current=current.next
    def getkey(self):
        current=self.head
        keywords={}
        keywordlist=[]
        while True:
            if current.next==None:
                keywordlist.append(current.keyword)
                keywords[current.keyword]=current.synonyms
                return keywords,keywordlist
            else:
                keywordlist.append(current.keyword)
                keywords[current.keyword]=current.synonyms
                current=current.next
                