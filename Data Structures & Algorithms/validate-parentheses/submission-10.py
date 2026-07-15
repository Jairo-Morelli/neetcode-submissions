class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] # O(n)
        dictionary = {"}": "{", "]":"[", ")":"("} # O(1)

        for i in s: # O(n)

            # if closing, use if statement and hashmap                
            if i in dictionary:
                if not stack: # if for whatever reason we find a closing bracket, but we don't have anything in the stack, we can exit out already
                    return False
                print(stack)
                if stack[len(stack)-1] != dictionary[i]: 
                    return False
                stack.pop(len(stack)-1)

            # if opening append 
            if i == "{":
                stack.append(i)
            elif i == "[":
                stack.append(i)
            elif i == "(":
                stack.append(i)
            print(stack) # if it prints like this [] that means its empty

        if not stack: 
            return True
        else:
            return False
  

    '''
    s = "([{}])"


    iter0: 
        stack = [ ( ]
                  0
    iter1:
        stack = [ [ ( ]
                  0  1 

    iter2:
        stack = [ { [ ( ]
                  0 1 2

    iter3:
        if } in dictionary (true):
            if { != { (true):
                return False
            stack.pop(0)

        stack = [ [ ( ]  
                  0 1 

    iter4: 
        if ] in dictionary (true):
            if [ != [ (true):
                return False 
            stack.pop(0)

        stack = [ ( ]
                  0 
    '''           
