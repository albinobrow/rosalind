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

      def read_single_file(self):
          with open(sys.argv[1], 'r', encoding='utf-8') as rf:
              arr=[]
              for i in rf:
                  obj=RowLineInput(i)
                  arr.append(obj.rwlin_string())
          return arr

def test(arr):
    arr_processed=[]
    for num, string in enumerate(arr):
        if num%2==1:
            arr_processed.append(string)
    return arr_processed
    
if __name__ == '__main__':
    saf=OpenArgumentFile()
    arr=saf.read_single_file()
    [print(i) for i in test(arr)]
