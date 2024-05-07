# 1.
class Node :
    def __init__(self, data:object, next = None) -> None:
        self.data = data
        self.next:Node = next
        
class LinkedList :
    def __init__(self) -> None:
        self.head:Node = None
        
    def push(self, data:object) -> None:
        """push the data to the front of the list

        Args:
            data (object): data that will push to the list
        """
        node = Node(data= data, next= self.head)
        self.head = node
        
    def append(self, data:object) -> None:
        """append the data to the ended of the list

        Args:
            data (object): data that will append to the list
        """
        if self.head is None :
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next :
            itr = itr.next
            
        node = Node(data=data)
        itr.next = node
        
    def insert(self, data:object, index:int) -> None:
        """insert the data to the specific index

        Args:
            data (object): data that will be insert to the list
            index (int): position to insert

        Raises:
            Exception: occured when index is out of range
        """
        if index < 0 or index > self.length() :
            raise Exception("invalid indexing...")
        
        if index == 0 :
            self.push(data= data)
        if index == self.length() :
            self.append(data= data)
            
        i = 0
        itr = self.head
        while itr :
            if i == index - 1 :
                node = Node(data= data, next= itr.next)
                itr.next = node
            
            itr = itr.next
            i += 1
            
    def remove(self, index:int) -> object:
        """removing the item in the list

        Args:
            index (int): opsition of item that will removed

        Raises:
            Exception: occured when index is out of range

        Returns:
            object: value of the deleted item
        """
        if index < 0 or index > self.length() :
            raise Exception("invalid indexing...")
        
        if index == 0 :
            data = self.head.data
            self.head = self.head.next
            return data
        
        i = 0
        itr = self.head
        while itr :
            if i == index - 1 :
                data = itr.data
                itr.next = itr.next.next
                return data
            
            itr = itr.next
            i += 1
            
    def insertList(self, dataList:list) -> None:
        """converted python list to linked list

        Args:
            dataList (list): python list of the item
        """
        self.head = None
        dataList.reverse()
        for i in dataList :
            self.push(i)
            
    def insertAfter(self, oldData:object, newData:object) -> None:
        """insert the newData after first oldData in the list

        Args:
            oldData (object): item that excist in the list
            newData (object): new item that want to insert
        """
        itr = self.head
        while itr :
            if itr.data == oldData :
                node = Node(data= newData, next=itr.next)
                itr.next = node
                return
                
            itr = itr.next
            
    def removeValue(self, data:object) -> None:
        """remove the first item that match with data

        Args:
            data (object): target data that want to delete
        """
        itr = self.head
        while itr :
            if itr.next.data == data :
                itr.next = itr.next.next
                return
            
            itr = itr.next
    
    def length(self) -> int:
        """get length of the linked list

        Returns:
            int: length of the list
        """
        length = 0
        itr = self.head
        while itr :
            length += 1
            itr = itr.next
            
        return length
        
    def print(self) -> None:
        """printing linked list data
        """
        if self.head is None :
            print("List is empty.")
            return
        
        itr = self.head
        while itr :
            print(itr.data, end=" -> ")
            itr = itr.next
            
        print()
        
if __name__ == "__main__" :
    print("1.")
    ll = LinkedList()
    ll.append(48)
    ll.append(120)
    
    ll.push(12)
    
    ll.insert(50, 2)
    
    ll.print()
    
    ll.insertList([50, 4, 6, 90])
    ll.insertAfter(6, 88)
    ll.print()
    ll.removeValue(6)
    ll.print()
    
# 2.

class DNode :
    def __init__(self, data:object, next=None, prev=None) -> None:
        self.data:object = data
        self.next:DNode = next
        self.prev:DNode = prev
        
class DoubleLinkedList :
    def __init__(self) -> None:
        self.head:DNode = None
    
    
    def print_forward(self) -> None:
        if self.head is None :
            print("List is empty...")
            return
        
        itr = self.head
        while itr :
            print(itr.data, end=" <-> ")
            itr = itr.next
            
        print()

    def print_backward(self) -> None:
        if self.head is None :
            print("List is empty...")
            return
        
        lastItr = self.head
        while lastItr.next :
            lastItr = lastItr.next
            
        while lastItr :
            print(lastItr.data, end=" <-> ")
            lastItr = lastItr.prev
            
        print()
    
    def length(self) -> int:
        count = 0
        itr = self.head
        while itr :
            count += 1
            itr = itr.next
            
        return count
    
    def push(self, data:object) -> None:
        node = DNode(data= data, next= self.head)
        if not (self.head is None) :
            self.head.prev = node
        self.head = node
        
    def append(self, data:object) -> None:
        if self.head is None :
            self.push(data= data)
            
        itr = self.head
        while itr.next :
            itr = itr.next
            
        itr.next = DNode(data= data, prev= itr)
        
    def insert(self, data:object, index: int) -> None:
        if index < 0 or index > self.length() :
            raise Exception("invalid indexing...")
        
        if index == 0 :
            self.push(data= data)
            return
        if index == self.length() :
            self.append(data= data)
            return
        
        count = 0
        itr = self.head
        while itr :
            if count == index - 1 :
                node = DNode(data= data, next= itr.next, prev= itr)
                itr.next = node
                node.next.prev = node
                
            itr = itr.next
            count += 1
            
    def removeAt(self, index:int) -> object :
        if index < 0 or index > self.length() :
            raise Exception("invalid indexing...")

        if index == 0 :
            self.head = self.head.next
            self.head.prev = None
            return
        
        count = 0
        itr = self.head
        while itr :
            if count == index :
                prevNode = itr.prev
                nextNode = itr.next
                data = itr.data
                
                prevNode.next = nextNode
                if index != self.length() :
                    nextNode.prev = prevNode
                return data
            
            count += 1
            itr = itr.next
            
if __name__ == "__main__" :
    print("2.")
    dll = DoubleLinkedList()
    dll.push(55)
    dll.append(333)
    dll.push(62)
    dll.insert(data= 95, index= 2)
    dll.append(5565)
    dll.print_forward()
    dll.removeAt(0)
    dll.print_forward()
    dll.print_backward()