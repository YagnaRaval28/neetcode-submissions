class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_seen=set()
        t_seen=set()
        for i in s:
            if i not in s_seen:
                s_seen.add(i)
        for j in t:
            if j not in t_seen:
                t_seen.add(j)
        for k in s_seen:
            if k not in t_seen:
                return False        
        return True