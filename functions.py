class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        char = s[len(s) - 1]
        while(char != ' '):
            count += 1
            if (count == len(s)):
                break
            char = s[len(s) - count - 1]
        return count
