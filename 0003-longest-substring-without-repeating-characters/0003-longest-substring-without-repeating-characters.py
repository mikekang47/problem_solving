class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        result = 0
        i = 0
        j = 0
        j1 = len(s)
        dic = defaultdict(int)
        while j < j1:
            if dic.get(s[j]) is None:
                dic[s[j]] += 1
                if j == j1 - 1:
                    break
                j += 1
            else:
                if len(dic) > result:
                    result = len(dic)
                while dic[s[j]]:
                    dic[s[i]] -= 1
                    if dic[s[i]] == 0:
                        del dic[s[i]]
                    i += 1
                dic[s[j]] += 1
                j += 1
    
        if len(dic) > result:
            result = len(dic)
        return result
