# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy

def clone(self):
    return Pair(self.key,self.value) # return this object, the reason you can write pair here 
                                        # is because the function declares Pair, but if you where to use it 
                                        # separately there would be an error. But if you attach it to the class 
                                        # that you expect it to use. Pair is defined.

def copyState(state: List[Pair]) -> List[Pair]:
    copy_State = []
    for pair in state: 
        copy = pair.clone()
        copy_State.append(copy)
    return copy_State

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # The reason that you keep getting the same 
        # returning the same list with the exact same 
        # elements is simply because 
        # you're manipualting memory, you're not copying and manipulating data.

        Pair.clone = clone
        copied_Pairs=[]

        for pair in pairs:  # here you're copying one state
            copy = pair.clone()
            copied_Pairs.append(copy)

        pair_State = [] # Create an list 
        
      #  print(len(copied_Pairs))
      #  print(copied_Pairs)
      #  print(copied_Pairs[0].key)
      #  print(copied_Pairs[1].key)
      #  print(copied_Pairs[2].key)
      #
      # leavning this just so I don't forget 
      #     copyState = []
      #     for pair in copied_Pairs:  
      #         copy = pair.clone()
      #          copyState.append(copy)
        for i in range (len(copied_Pairs)):
            j = i - 1 
            copy_State = None
            '''
            [2 , 5 , 9]
                 j   i
              
            think about each new state, how do you copy each new state?

            you want to copy the previous state no, and then change it? 
            Where is the previous state? 

            the copied_Pair only ever has three pairs. 

            copy the copied_Pair and put it into the pair state

            insert the copy, with the previous state, inside the conditional? 

            Why? 

            Because inside the conditional is where you will have the "previous" state, 
            
            if you put it inside the outside of the while loop, you're going to copy and 
            append each state, according to the length of the list you're working with at 
            the moment.

            It is in pair_State 

            and you only want the previous entry of the previous state, not all 
            the previous states. 

            Okay there is defintely a better way of doing this.

            I think the current way you're writing the code is fine.

            It is not actually not that much code. 

            Okay so there is like prevState, currentState and finalState. 

            Test out how you can save these state in relation to each single iteration.


            '''
            while j >=0 and copied_Pairs[j+1].key < copied_Pairs[j].key:
                # You're manipulating the reference 
                # so how about, you make a copy, once you've identified that you need to sort 
                # create the copy either append it before or after. Once you've switched the 
                # keys.
                temp = copied_Pairs[j + 1].key
                tempStr = copied_Pairs[j + 1].value

                copied_Pairs[j + 1].value = copied_Pairs[j].value
                copied_Pairs[j].value = tempStr

                copied_Pairs[j + 1].key = copied_Pairs[j].key 
                copied_Pairs[j].key = temp


                j -=1 
            copy_State = copyState(copied_Pairs)
            pair_State.append(copy_State)
        #print(pair_State)
        return pair_State