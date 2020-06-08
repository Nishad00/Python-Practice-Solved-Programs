class Node:

    def __init__(self,data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self,next):
        self.__next = next

class LinkedList:

    def __init__(self):
        self.__head = None 
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self,data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def display(self):
        temp  = self.__head
        count = 0
        while temp is not None:
            print("\nNode ",temp.get_data()," is present at Position ",count)
            count += 1
            temp = temp.get_next()

    def find_node(self,data):
        if self.__head is not None:
            count = 0
            flag = False
            temp = self.__head
            while temp is not None:
                if(temp.get_data() == data):
                    print("\nNode ",temp.get_data()," is found at Position ",count)    
                    flag = True     
                    return count
                else:
                    count += 1
                    temp = temp.get_next()

            if(flag == False):
                print("\nNode ",data," is Not found at any Positions ")
                return -1

        else:
            print("\n List is Empty")
            return -1
    
    def insert(self,data,before):
        new_node = Node(data)
        temp = self.__head
        prev = None
        while temp is not None:
            if(temp.get_data() == before):
                pos = self.find_node(temp.get_data())
                print(pos)
                if pos == 0:
                    new_node.set_next(self.__head)
                    self.__head = new_node
                    break
                else:
                    new_node.set_next(temp)
                    prev.set_next(new_node)
                    break
            else:
                prev = temp
                temp = temp.get_next()

    def delete(self,data):
        temp = self.__head
        prev = None
        if(temp.get_data() == data):
            self.__head = temp.get_next()
            temp.set_next(None)
            return None
        while temp is not None:
            if(temp.get_data() == data):
                if temp.get_next() is not None:
                    prev.set_next(temp.get_next())
                    temp.set_next(None)
                    break
                else:
                    prev.set_next(None)
                    break
            else:
                prev = temp
                temp = temp.get_next()
        



l = LinkedList()
l.add("Nishad")
l.add("Kunal")
l.add("Pavan")
l.add("Pratik")
l.add("Sarvesh")
l.add("Kedar")
l.add("Gaurav")
l.display()
# l.insert("NP","Sarvesh")
# l.find_node("Nishad")
# l.delete("Nishad")
# l.display()
        


