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

def InsertSort(n, arr):
    count=0
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                count+=1
    return count

def ExtractionStep(ing):
    ###
    n,text=ing
    n=int(n)
    arr=RowLineInput(text).rwlin_integer_array()
    return [n, arr]
    ###

def main():
    ###
    ing=OpenArgumentFile().read_single_file()
    n,arr=ExtractionStep(ing)
    print(InsertSort(n, arr))
    ###

if __name__ == '__main__':
    main()
