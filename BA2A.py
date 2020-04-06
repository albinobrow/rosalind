#!/usr/bin/env python
# coding: utf-8

import re, sys
if sys.version_info[0]<3: input=raw_input

def HammingDistance(s,t):
    n=len(s)
    count=0
    for i in range(n):
        if s[i]!=t[i]:
            count+=1
    return count

def Neighbors(t, d):
    import itertools
    n=len(t)
    base=['A', 'C', 'G', 'T']
    for i in sorted(itertools.product(base, repeat=n)):
        i=''.join(i)
        if HammingDistance(i,t) <= d:
            print(i)
    return ''

def PatternToNumber(s):
    d={'A':0, 'C':1, 'G':2, 'T':3}
    n=len(s)
    c=0
    for i in range(n):
        c+=d[s[i:i+1]]*4**(n-i-1)
    return c

def MotifEnumeration(l, k, d):
    import itertools
    n=len(l)
    data={}
    base=['A', 'C', 'G', 'T']
    for x in sorted(itertools.product(base, repeat=k)):
        x=''.join(x)
        data[x]=0
        c=0
        a=[] 
        for y in range(n):
            for z in range(len(l[y])-k+1):
                if HammingDistance(l[y][z:z+k],x) <= d:
                     a.append(y)
                     c+=1
        a=sorted(set(a))
        if a==list(range(n)):
            data[x]+=c

    data=sorted(data.items(), key=lambda x:x[1], reverse=True)
    m=data[0][1]
    b=[]
    for i in data:
        if i[1]!=0:
            b.append(i[0])
    return ' '.join(b)

if __name__ == '__main__':
    fl_in=sys.argv[1]
    fl_out=re.sub('.txt$', '_result.txt', fl_in, 1)
    with open( fl_in, 'r' ) as flr:
        k,d=map(int, str(flr.readline().rstrip()).split())
        l=list(map(lambda x: x.rstrip(), flr.readlines()))
    with open( fl_out, 'w' ) as flw:
        flw.write(MotifEnumeration(l, k, d)+'\n')
