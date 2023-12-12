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


def MOTIFENUMERATION(Dna, k, d):
    patterns = []
    arr = GeneratePatterns( k )
    
    for p in arr:
        count = 0
        for i in Dna:
            for j in range( len( i ) - k + 1 ):
                if HammingDistance( i[j:j+k], p  ) <= d:
                    count += 1
                    break
        if count == len( Dna ):
            patterns.append( p )
    patterns = sorted( set( patterns ))
    if len( patterns ) == 0:
        patterns.append( 'nan' )
    return patterns
    


def test(arr):
    ###
    
    k,d=list(map(int,  arr[0].split() ))
    Dna =  arr[1:] 
#    Dna = arr[1].split()

    return MOTIFENUMERATION(Dna, k, d)

    ###


if __name__ == '__main__':

    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
        fhw.write(str( PrettyPrintArray(test(arr)) )+'\n')
#        for a in test(arr):
#            fhw.write( a +'\n')
