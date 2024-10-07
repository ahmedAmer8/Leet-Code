class Solution:
    def minLength(self, s: str) -> int:
        st = []
        i = 0
        while i < len(s):
            if not st:
                st.append(s[i])
                i += 1
                continue
            if s[i] == 'B' and st[-1] == 'A':
                st.pop()
            elif s[i] == 'D' and st[-1] == 'C':
                st.pop()
            else:
                st.append(s[i])
            i += 1
        return len(st)
