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

def MaxHeapChunk(arr, i):

    left_sibling_index = 2*i
    right_sibling_index = 2*i+1
    array_length = len(arr)
    parent_index = i

#    if right_sibling_index < array_length and arr[parent_index] < max(arr[left_sibling_index], arr[right_sibling_index]):
#        parent_index=arr.index(max(arr[left_sibling_index], arr[right_sibling_index]))
#    elif left_sibling_index < array_length and arr[parent_index] < arr[left_sibling_index]:
    if left_sibling_index < array_length and arr[parent_index] < arr[left_sibling_index]:
        parent_index=left_sibling_index
    if right_sibling_index < array_length and arr[parent_index] < arr[right_sibling_index]:
        parent_index=right_sibling_index
    if parent_index!=i:
        arr[i],arr[parent_index]=arr[parent_index],arr[i]
        MaxHeapChunk(arr,parent_index)

def BuildMaxHeap(n, arr):
    arr.insert(0, 'Inf')
    n=len(arr)
    for i in range(n//2, 0, -1):
        MaxHeapChunk(arr, i)
    return arr[1:]

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
    print(*BuildMaxHeap(n, arr))
    ###

if __name__ == '__main__':
    main()
