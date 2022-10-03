class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(smbs):
            lp, rp = 0, len(smbs) - 1
            while lp < rp:
                if smbs[lp] != smbs[rp]:
                    return False
                else:
                    lp += 1
                    rp -= 1

            return True

        lp, rp = 0, len(s) - 1
        while lp < rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1

            else:
                if is_palindrome(s[lp + 1: rp + 1]) or is_palindrome(s[lp: rp]):
                    return True
                else:
                    return False
        return True
