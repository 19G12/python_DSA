
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None
        return

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    def isEmpty(self):
        return self.head == None
    
    def enqueue(self, elem):
        node = Node(elem)
        if self.isEmpty():
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return
        
    def dequeue(self):
        if(self.head == None):
            print("QUEUE UNDERFLOW")
            return None
        data = self.head.value
        self.head = self.head.next
        if(self.head == None):
            self.tail = None
            return
        self.head.prev = None
        return data
    
    def first(self):
        if not (self.head == None):
            return self.head.value
        print("QUEUE IS EMPTY")
        return None
    
    def size(self):
        count = 0
        head = self.head
        while(head != None):
            count += 1
            head = head.next 
        return count
        
    
    def printQueue(self):
        head = self.head
        while(head != None):
            print(head.value, end="->")
            head = head.next
        print("None")
        return

queue = Queue()

print(" -- Performing queue operations on D.LinkedList -- ")

# Insert 4 at the end. So queue becomes 4->None  
queue.enqueue(4)
  
# Insert 5 at the end. So queue becomes 4->5None  
queue.enqueue(5)
  
# Insert 6 at the end. So queue becomes 4->5->6->None  
queue.enqueue(6)
  
# Insert 7 at the end. So queue becomes 4->5->6->7->None  
queue.enqueue(7)  

queue.printQueue()

queue.dequeue()
queue.printQueue() #5 6 7 

queue.dequeue()
queue.printQueue() #6 7 

queue.dequeue()
queue.printQueue() #7 

queue.dequeue()
queue.printQueue() #None 

queue.dequeue()
queue.printQueue() #None & message