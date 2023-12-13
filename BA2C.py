#!/usr/bin/env python
# coding: utf-8


import datetime, re, string, sys, itertools, numpy as np, operator
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


def HammingDistance(s,t):
    n=len(s)
    count=0
    for i in range(n):
        if s[i]!=t[i]:
            count+=1
    return count


def GeneratePatterns( k ):
    arr = []
    base=['A', 'C', 'G', 'T']
    for i in itertools.product(base, repeat=k):
        pattern=''.join(i)
        arr.append( pattern )
    return arr

    
def MostProbableKmer(MatrixProfile, k):
    a=np.array(MatrixProfile).T   
    data={}
    arr = GeneratePatterns( k )
    for x in arr:
        p=0
        for i in range(k):
            if x[i:i+1]=='A':
                p+=a[i][0]
            elif x[i:i+1]=='C':
                p+=a[i][1]
            elif x[i:i+1]=='G':
                p+=a[i][2]
            elif x[i:i+1]=='T':
                p+=a[i][3]
        data[x]=p
    return sorted(data.items(), key=operator.itemgetter(1), reverse=True)


def FindMotif(s, sorted_data):
    for i in sorted_data:
        if i[0] in s:
            return i[0]


def MakeFloatMatrix( arr ):
    brr=[]
    for i in arr:
        brr.append(list(map(float, i.split())))
    return brr


def test(arr):
    ###

    s=arr[0]
    k=int( arr[1] )
    MatrixProfile =  MakeFloatMatrix( arr[2:] )
    return  FindMotif(s, MostProbableKmer(MatrixProfile, k))

    ###


if __name__ == '__main__':

    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
        fhw.write(str(  ( test(arr) )+'\n'))
