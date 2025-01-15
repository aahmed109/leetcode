class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for i in range(len(words)):
            l = list(set(list(words[i])))
            ins = 1
            for c in l:
                if words[i].count(c) > chars.count(c):
                    ins = 0
                    break
            if ins == 1: res += len(words[i])
        return res
