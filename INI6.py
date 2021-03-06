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
        self.arr=map(int,self.i.rstrip().split())
        return self.arr

class OpenArgumentFile:

      def read_single_file_array(self):
          with open(sys.argv[1], 'r', encoding='utf-8') as rf:
              for i in rf:
                  obj=RowLineInput(i)
                  arr=obj.rwlin_array()
          return arr

def test(arr):
    dict={}
    for i in arr:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

if __name__ == '__main__':
    saf=OpenArgumentFile()
    arr=saf.read_single_file_array()
    dict=test(arr)
    [print(key, value) for key, value in dict.items()]
