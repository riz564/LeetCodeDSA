class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lss=''
        cnt=0
        for ch in s:
            if ch in lss:
                if len(lss) > cnt:
                    cnt = len(lss)
                lss=lss[lss.index(ch)+1:] 
            lss+=ch
            
        if len(lss) > cnt:
            cnt = len(lss)
        return cnt
