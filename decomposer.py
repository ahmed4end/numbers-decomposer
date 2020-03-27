from random import randint, shuffle

class decompose():
	def __init__(self, n, auto=True):
		#decomposer engine
		first_layer = self.decomposeS(n)
		res = []
		for i in first_layer:
			m = self.decomposeM(i)
			if m!= None:res.append("+".join(str(j)+"^2" for j in m))
			elif randint(1,10)%2==0:
				formated =  "-".join(str(j) for j in self.decomposeT(i))
				res.append(formated if len(formated)!=2 else formated[:-1])
			else:res.append(str(i))
		print("+".join(res))
	def decomposeM(self, n):
		#decompose by multiplying
	    def rec(n, i):
	        if n<0:return None
	        if n==0:return []
	        for j in range(i-1, 0, -1):
	            hold = rec(n-j**2, j)
	            if hold!=None:return [j] + hold
	    return rec(n, int(n**0.5))

	def decomposeS(self, n):
		#decompose by summing
	    rand = list(range(1, n))
	    shuffle(rand)
	    def rec(n):
	        if n<0:return None
	        if n==0:return []
	        for j in rand:
	            shuffle(rand)     
	            hold = rec(n-j)
	            if hold!=None:return [j] + hold
	    return rec(n)


	def decomposeT(self, n):
		#decompose by taking away
	    rand = list(range(1, n))
	    random_start = randint(n, n+int(n*0.5))
	    def rec(n2, r):
	        if n2<0:return None
	        if n2==n:return []
	        r = [i for i in r if (n2-i)>=n]
	        r = sorted(r)[::-1]
	        for j in r:
	            hold = rec(n2-j, r)
	            if hold!=None:return [j] + hold
	    return [random_start] + rec(random_start, rand)


if __name__ =="__main__":
	decompose(5)
