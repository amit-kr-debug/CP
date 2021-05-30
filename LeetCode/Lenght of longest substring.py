class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_pos = {}
        start_index = -1
        max_len = 0
        curr_len = 0
        for i,letter in enumerate(s):
            if letter not in letter_pos:
                letter_pos[letter] = i
                curr_len += 1

            else:
                if letter_pos[letter] > start_index:
                    curr_len = i - letter_pos[letter]
                    start_index = letter_pos[letter]
                else:
                    curr_len += 1
                letter_pos[letter] = i

            print(letter, curr_len)
            max_len = max(max_len, curr_len)
        return max_len


a = Solution()
print(a.lengthOfLongestSubstring("abbaca"))