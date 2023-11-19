#!/usr/bin/env python
# coding: utf-8


import datetime, re, string, sys, itertools
if sys.version_info[0]<3: input=raw_input

class RowLineInput:

    def __init__(self, i):
        self.i=i

    def rwlin_string(self):
        self.s=self.i.rstrip()
        return self.s

    def rwlin_integer(self):
        self.n=int(self.i.rstrip())
        return self.n

    def rwlin_array(self):
        self.arr=list(map( lambda x: x.rstrip(), self.i))
        return self.arr

    def rwlin_integer_array(self):
        self.arr=list(map(int,self.i.rstrip().split()))
        return self.arr

class OpenArgumentFile:

      def read_single_file(self):
          with open(sys.argv[1], 'r', encoding='utf-8') as fhr:
              arr=RowLineInput(fhr.readlines()).rwlin_array()
          return arr

class OpenAchivementFile:
      
      def name_output_file(self):
          dt_now = datetime.datetime.now()
          return re.sub(r"\.txt$", ".result."+dt_now.strftime('%Y-%m-%d--%H-%M-%S')+".txt", sys.argv[1])


def PrettyPrintArray(arr):
    arr=list(map(str, arr))
    return ' '.join(arr)

def PatternCount(s,t):
    n=len(s)
    m=len(t)
    count=0
    for i in range(n-m+1):
        if s[i:i+m]==t:
            count+=1
    return count

def GenerateFrequencyArray(s, k):
    base=['A', 'C', 'G', 'T']
    l=[]
    for i in sorted(itertools.product(base, repeat=k)):
        i=''.join(i)
        l.append(PatternCount(s,i))
    return l

def ImplementPatternToNumber(s):
    d={'A':0, 'C':1, 'G':2, 'T':3}
    n=len(s)
    c=0
    for i in range(n):
        c+=d[s[i:i+1]]*4**(n-i-1)
    return c


def ImplementNumberToPattern( n, k ):
    p=''
    for i in range(k-1,-1,-1):
        if 3*4**i <= n:
            p+='T'
            n-=3*4**i
        elif 2*4**i <= n:
            p+='G'
            n-=2*4**i
        elif 1*4**i <= n:
            p+='C'
            n-=1*4**i
        else:
            p+='A'
            n-=0*4**i
    return p


def test(arr):
    ###
    
    n=int( arr[0] )
    k=int( arr[1] )
    
    
    return ImplementNumberToPattern( n, k )
    ###


if __name__ == '__main__':

    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
        fhw.write(str( (test(arr)) )+'\n')
