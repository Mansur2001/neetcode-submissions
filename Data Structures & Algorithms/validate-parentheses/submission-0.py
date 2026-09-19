class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:

            if char in pairs:
                # It's a closing bracket

                if not stack:
                    return False

                top = stack.pop()

                if top != pairs[char]:
                    return False

            else:
                # It's an opening bracket
                stack.append(char)

        return not stack
