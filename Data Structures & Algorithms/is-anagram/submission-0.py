class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # return sorted(s)==sorted(t)  O(mlogm + mlogm), O(n+m)

        if len(s)!=len(t):
            return False
        
        countedS={}
        countedT={}

        for i in range(len(s)):
            countedS[s[i]]=1+countedS.get(s[i],0)
            countedT[t[i]]=1+countedT.get(t[i],0)

        return countedS==countedT
