class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        prev = 0
        for idx in range(len(path)):
            if path[idx] == '/':
                sub = path[prev:idx]
                if sub == "..":
                    if stack:
                        stack.pop()
                elif sub in (".", ""):
                    pass
                else:
                    stack.append(sub)
                prev = idx + 1

        if prev < len(path):
            sub = path[prev:]
            if sub == "..":
                if stack:
                    stack.pop()
            elif sub in (".", ""):
                pass
            else:
                stack.append(sub)

        return "/" + "/".join(stack)
