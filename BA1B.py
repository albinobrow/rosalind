#!/usr/bin/env python
# coding: utf-8

import sys
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
        self.arr=self.i.rstrip().split()
        return self.arr

    def rwlin_integer_array(self):
        self.arr=list(map(int,self.i.rstrip().split()))
        return self.arr

class OpenArgumentFile:

      def read_single_file(self):
          with open(sys.argv[1], 'r', encoding='utf-8') as f:
              arr=[]
              for i in f:
                  obj=RowLineInput(i)
                  arr.append(obj.rwlin_string())
          return arr

def dict(arr):
    dict={}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

def MostFrequentKeys(dict):
    arr=sorted([kv[0] for kv in dict.items() if kv[1] == max(dict.values())])
    return arr

def PrettyPrintArray(arr):
    return ' '.join(arr)

def test(arr):
    ###
    text,n=arr
    n=int(n)
    arr_processed=[]
    for i in range(len(text)-n+1):
        arr_processed.append(text[i:i+n])
    d=dict(arr_processed)
    arr=MostFrequentKeys(d)
    ans=PrettyPrintArray(arr)
    return ans
    ###

if __name__ == '__main__':
    saf=OpenArgumentFile()
    arr=saf.read_single_file()
    print(test(arr))
