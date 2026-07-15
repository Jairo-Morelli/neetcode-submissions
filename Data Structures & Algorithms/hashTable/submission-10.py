class Pair: 
    def __init__(self, key: int, val: int):
        self.key = key 
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0 
        self.capacity= capacity
        self.hash_map=[]
        for i in range(capacity):
            self.hash_map.append(None)

    def create_hash(self, key: int)-> int:
        string = str(key)
        hash_val=0 
        for c in string:
            hash_val += ord(c)
        return int(hash_val % self.capacity)

    def insert(self, key: int, value: int) -> None:
        index = self.create_hash(key)
        pair = Pair(key,value)

        self.hash_map[index]= pair
        self.size+=1

        if self.size >= int(self.capacity/2):
            self.resize()
           
    

    def get(self, key: int) -> int:
        # Will return the value associated with the key
        # hash function in here
        # the issue is here
        index = self.create_hash(key)
        pair = self.hash_map[index]

        if pair:
            return pair.val
        return -1

    def remove(self, key: int) -> bool:
        #   Either search without using the get method, then remove from array or
        #   use get to , get then remove the search method
        index = self.create_hash(key)
        if self.hash_map[index]:
            self.hash_map[index]=None
            self.size -=1 
            return True
        return False 
      

    def getSize(self) -> int:
        # Return the amount of KEYS within the self.map array 
        return self.size

    def getCapacity(self) -> int:
        # Return the SIZE of the self.map array
        return self.capacity

    def resize(self) -> None:
        # Double the capacity of the hash table, when the capacity reaches is either 
        # equal or more than 0.5
        # when you resize, you also have to rehash everything
        self.capacity = int( self.capacity / 0.5 )
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.hash_map
        self.hash_map = newMap
        self.size = 0 

        for pair in oldMap:
            if pair:        # if pair exist 
                self.insert(pair.key,pair.val)
        return None
            

