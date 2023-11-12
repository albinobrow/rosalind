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


def MostFrequentKeys(text, k):
    dict = {}
    for i in range(len(text)-k+1):
        if text[i:i+k] not in dict:
            dict[ text[i:i+k] ] = 1
        else:
            dict[ text[i:i+k] ] += 1
    arr=sorted([kv[0] for kv in dict.items() if kv[1] == max(dict.values())])
    return arr


def ClumpFindingProblem(seq, k, L, t):
    arr=[]
    for j in range(len(seq) - L + 1):
        text = seq[j:j+L]
        dict = {}
        for i in range(len(text)-k+1):
            if text[i:i+k] not in dict:
                dict[ text[i:i+k] ] = 1
            else:
                dict[ text[i:i+k] ] += 1
        arr+=sorted([kv[0] for kv in dict.items() if kv[1] >= t ])
    arr=sorted(set(arr))
    return arr


def PrettyPrintArray(arr):
    return ' '.join(arr)


def test(arr):
    ###

    seq=arr[0]
    k,L,t=list(map(int, arr[1].split()))
    
    brr=ClumpFindingProblem(seq, k, L, t)
    return brr

    ###


if __name__ == '__main__':
    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
        fhw.write(str(PrettyPrintArray(test(arr)))+'\n')
