def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def createParentheses(parentheses, numOpen, numClosed):
        if numClosed > numOpen or numClosed > n or numOpen > n:
            return

        if numClosed == numOpen == n:
            ans.append(parentheses)
            return            

        createParentheses(parentheses + '(', numOpen + 1, numClosed)            
        createParentheses(parentheses + ')', numOpen, numClosed + 1)

    createParentheses('', 0, 0)
    return ans
