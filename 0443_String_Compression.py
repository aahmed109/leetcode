class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i=0
        while i<len(chars):
            c = chars[i]
            cnt = 0
            while i<len(chars) and chars[i] == c:
                i+=1
                cnt+=1

            s+=c
            print(i, cnt)
            if cnt > 1:
                s+=str(cnt)

            print(s)

        t = list(s)
        for j in range(len(t)):
            chars[j] = t[j]
        return len(t)
