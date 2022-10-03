class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_stack = []
        to_delete = []

        for idx in range(len(s)):
            if s[idx] == "(":
                open_stack.append(idx)
            elif s[idx] == ")":
                if len(open_stack) > 0:
                    open_stack.pop()
                else:
                    to_delete.append(idx)

        to_delete += open_stack
        to_delete = set(to_delete)

        fixed_word = []
        for idx in range(len(s)):
            if idx not in to_delete:
                fixed_word.append(s[idx])

        return "".join(fixed_word)
