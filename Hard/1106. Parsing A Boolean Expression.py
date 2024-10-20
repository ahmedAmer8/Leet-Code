class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(op, t, f):
            if op == '|':
                return t
            elif op == '&':
                return not f
            else:
                if t: return False
                return True

        stack = []
        for ch in expression:
            if ch == ',':
                continue
            if ch == ')':
                t = f = False
                while stack[-1] not in ['|', '&', '!']:
                    val = stack.pop()
                    if val == 't':
                        t = True
                    if val == 'f':
                        f = True
                e = evaluate(stack.pop(), t, f)
                if e: stack.append('t')
                else: stack.append('f')
            else:
                stack.append(ch)
        return True if stack[0] == 't' else False
                    
            
