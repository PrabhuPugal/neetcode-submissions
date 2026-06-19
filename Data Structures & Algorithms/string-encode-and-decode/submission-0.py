class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for i in strs:
            temp = str(len(i)) + "#" + i
            encoded.append(temp)
        encoded_string=''.join(encoded)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1            
            length_of_string=int(s[i:j])
            start=j+1
            word=s[start:start+length_of_string]

            decoded.append(word)
            i=start+length_of_string
        return decoded
                
                
