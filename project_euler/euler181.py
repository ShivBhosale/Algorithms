# Euler 181
# gonna be auite challenging but let's give it a try atleast

'''
Having three black objects B and one white object W they can be grouped in 7 ways like this:

(BBBW)	(B,BBW)	(B,B,BW)	(B,B,B,W)	(B,BB,W)	(BBB,W)	(BB,BW)
In how many ways can sixty black objects B and forty white objects W be thus grouped?

This is definitely a counting problem. I just don't know how to count yet. So I'm gonna 
start brute force first

# discovered a nice modification to the formula
'''


memo_unq = {}
def unq(n):
    if n in memo_unq: return memo_unq[n]
    if n<0:
        return 0
    if n == 0:
        return 1
    ans = 0
    for i in range(1, int(n/2)+1):
        non_key = n-i
        ans+=unq(int(non_key/i))
    memo_unq[n] = 1+ans
    return memo_unq[n]

# key formed by i and j
def key(i,j, Nb, Nw):
    if Nb <=0 or Nb<=0:return 0
    keyed_ways = unq(Nb-i)*unq(Nw-j)#+key(i,j,Nb-i,Nw-j)
    for r in range(i, Nb+1):
        for k in range(j, Nw+1):
            keyed_ways += key(i,j,Nb-r,Nw-k)
    # for k in range(1, min(nB, nW)+1):
    #     keyed_ways += unq(nB-i*k)*unq(nW-j*k)
    return keyed_ways


nB, nW = 3,2
nB, nW = 3, 3
nB, nW = 1, 8

total_ways = unq(nB)*unq(nW)
for i in range(1, nB+1):
    for j in range(1, nW+1):
        total_ways += key(i,j,nB,nW)

print(total_ways) 

# print(key(1,2,2,2))