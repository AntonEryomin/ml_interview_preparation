class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        chars = [smb for smb in palindrome]

        lp, rp = 0, len(chars)-1
        while lp < rp:
            if palindrome[lp] != 'a':
                chars[lp] = 'a'
                return "".join(chars)
            lp += 1
            rp -= 1

        chars[-1] = "b"
        return "".join(chars)
