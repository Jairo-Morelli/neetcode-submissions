class Solution:
    '''
        Okay so the first piece of code already encodes the string. 

        What it does, is it simply just takes the current character, converts it to ascii values 
        once it does that it then increases its ascii value by 2, making turning it into a different type of 
        ascii character. 

        What you have to do now is find a way to combine empty strings inside your encoded function and decoded function
    '''

    def encode(self, strs: List[str]) -> str:
        # depending on the amount of "empty strings inside the list return a string with the information of said empty strings"
        '''
        if not any(strs):

            empty_string = ""
            for s in range(len(strs)):
                empty_string +=' '.join("\x00")

            return empty_string 
        '''
        # Literally empty list
        if not strs: 
            return ""

        encoded = "" 
        single_encoded = ""

        for s in strs:  
            if not s: 
                encoded = ''.join(("\x00"))
                print(f"empty string found!{repr(encoded)}")
            else:
                # 1. This securely encodes the string while printing your debug info 
                encoded = ''.join(chr((ord(c) + 2 ) % 256) for c in s)
                print(f"string isn't empty{encoded}")

            #2 FIX: Add a space between this encoded word and the next one

            if single_encoded: 
                single_encoded += " " + encoded
            else: 
                single_encoded = encoded
                


        print(f"Final single string: {repr(single_encoded)}")
        print("Final string:"+ single_encoded)


        return single_encoded 



    def decode(self, s: str) -> List[str]:
        # literally empty string
        if not s:
            return []

        decoded_strs = s.split(" ")
        decoded_list = []

        for s in decoded_strs:
            if not s.find("\x00") == -1:
                decoded_list.append("")
            else: 
                decoded = ''.join(chr((ord(c)- 2) % 256) for c in s)
                decoded_list.append(decoded)

        print(decoded_list)


        
        return decoded_list
