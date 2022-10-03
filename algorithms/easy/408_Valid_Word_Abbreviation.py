class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) == 0:
            return False

        lp = 0
        word_lp = 0

        while lp < len(abbr) and word_lp < len(word):
            if abbr[lp].isdigit():
                num = ""
                if int(abbr[lp]) == 0:
                    return False

                while lp < len(abbr) and abbr[lp].isdigit():
                    num += abbr[lp]
                    lp += 1

                if word_lp + int(num) > len(word):
                    return False
                else:
                    word_lp += int(num)

            else:

                if word[word_lp] == abbr[lp]:
                    lp += 1
                    word_lp += 1
                else:
                    return False
        if lp == len(abbr) and word_lp == len(word):
            return True
        else:
            return False

#Not hard task, but you need to keep your attention