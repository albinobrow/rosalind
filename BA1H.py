#!/usr/bin/env python
# coding: utf-8


import datetime, re, string, sys
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


def HammingDistanceProblem( p, q ):
    count=0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
        else:
            pass
    return count

def ApproximatePatternMatchingProblem( pattern, seq, d ):
    k = len( pattern )
    arr = []
    for i in range( len( seq ) - k + 1 ):
        if HammingDistanceProblem( seq[i:i+k], pattern ) <= d:
            arr.append( i )
    return arr


def PrettyPrintArray(arr):
    arr=list(map(str, arr))
    return ' '.join(arr)


def test(arr):
    ###

    pattern=arr[0]
    seq=arr[1]
    d=int(arr[2])
    num=ApproximatePatternMatchingProblem( pattern, seq, d )
    return num

    ###


if __name__ == '__main__':

    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
        fhw.write(str(PrettyPrintArray(test(arr)))+'\n')
