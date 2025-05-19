class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setchar= set()
        left=0
        maxsum=0
        for right in range(len(s)):
            while s[right] in setchar:
                setchar.remove(s[left])
                left+=1
            setchar.add(s[right])
            maxsum=max(maxsum, right-left+1)
        return maxsum