class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return chr(257)
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        for s in strs:
            res.append(s)
        return ''.join(res)            

    def decode(self, s: str) -> List[str]:
        if s == chr(257):
            return []
        
        header_end = s.find('#')
        sizes_str = s[:header_end].split(',')
        content = s[header_end + 1:]
        
        res = []
        pointer = 0
        for sz in sizes_str:
            if sz:
                length = int(sz)
                res.append(content[pointer : pointer + length])
                pointer += length
        return res