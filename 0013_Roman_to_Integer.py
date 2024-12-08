class Solution:
	def romanToInt(self, s: str) -> int:
		mapping={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		ind=list(s)
		sk=0
		for i in range(1,len(ind)):
			if mapping[ind[i-1]]<mapping[ind[i]]:
				sk-=mapping[ind[i-1]]
				i+=1
			else:
				sk+=mapping[ind[i-1]]
		return sk+mapping[ind[-1]]
