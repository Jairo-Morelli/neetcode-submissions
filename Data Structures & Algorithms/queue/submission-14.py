'''
 The time complexity is O(1)
 The space complexity is O(n)
 
 Why is the time complexity O(1)

 Because you are literally manually delinking, linking and moving the nodes 
 one by one. No loops. 

 Space complexity is O(n) because the deque grows with the size of elements put into it.
'''
class DNodeList:
    def __init__(self, val_: int):
        self.nextNode = None
        self.prevNode = None 
        self.val = val_

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None 

    def isEmpty(self) -> bool:
        return self.head == None and self.tail == None
      

    def append(self, value: int) -> None:
        newNode = DNodeList(value)
        if not self.tail:
            self.head = self.tail = newNode
            self.head.nextNode = self.tail  # make it circular
            self.tail.prevNode = self.head   # make it circular
        else:
            newNode.prevNode = self.tail 
            self.tail.nextNode = newNode 
            self.head.prevNode = newNode
            newNode.nextNode = self.head
            self.tail = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = DNodeList(value)
        if not self.head:
            self.head = self.tail = newNode
            self.head.nextNode = self.head   # make it circular
            self.tail.prevNode = self.head   # make it circular
        else:
            newNode.nextNode = self.head 
            self.head.prevNode = newNode
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.head = newNode
        


    def pop(self) -> int:
        if self.isEmpty():
            return -1

        curr = self.tail
        val = curr.val
        print("head node",self.head)
        print("head prevNode",self.head.prevNode)
        print("tail node", self.tail)
        print("tail nextNode",self.tail.nextNode)
        print("tail prevNode",self.tail.prevNode)

        if self.head == self.tail:
            self.head= self.tail = None
            print(val)
            return val
      
        #move the tail node backwards
        self.tail = self.tail.prevNode
        #delink the previous node
        curr = None

        # Relink the nodes
        self.head.prevNode = self.tail
        self.tail.nextNode = self.head
        return val
        
    # You're not relinking after you move the node forward or backwards
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.head 
        val = curr.val
       # print("head node",self.head)
       # print("head prevNode",self.head.prevNode)
       # print("tail node", self.tail)
       # print("tail nextNode",self.tail.nextNode)
       # print("tail prevNode",self.tail.prevNode)
        # Simply just check if the head == tail to see if they are at the same location in memory
        if self.head == self.tail:
            self.head= self.tail = None
            return val
        # move the head node forward 
        # Okay so there is an issue with this code, and the issue is that the nextNode and prevNode
        # member variables will always link back to each other. Which is how it is actually designed. 
        self.head = self.head.nextNode
     
        # Relink the nodes
        self.head.prevNode = self.tail
        self.tail.nextNode = self.head
        #delink the previous node
        curr = None
  
        return val
     
  
