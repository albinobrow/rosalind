#!/usr/bin/env python
# coding: utf-8


import datetime, re, sys
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
          with open(sys.argv[1], 'r', encoding='utf-8') as fhr:
              arr=[]
              for i in fhr:
                  obj=RowLineInput(i)
                  arr.append(obj.rwlin_string())
          return arr

class OpenAchivementFile:      
      def name_output_file(self):
          dt_now = datetime.datetime.now()
          return re.sub(r"\.txt$", ".result."+dt_now.strftime('%Y-%m-%d--%H-%M-%S')+".txt", sys.argv[1])

def test(arr):
    ###
    count=0
    text,pattern=arr
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            count+=1
    return count
    ###

if __name__ == '__main__':
    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
        fhw.write(str(test(arr))+'\n')
