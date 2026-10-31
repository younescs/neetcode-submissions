class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)
        have, required = 0, len(need)
        res = [-1, -1]
        min_window = float('inf')
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    have += 1
            
            while have == required:
                length = r - l + 1
                if length < min_window:
                    min_window = length
                    res = [l, r]
                
                c_left = s[l]
                if c_left in need:
                    window[c_left] -= 1
                    if window[c_left] < need[c_left]:
                        have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if min_window != float('inf') else ""