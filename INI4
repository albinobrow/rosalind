#!/usr/bin/env python
# coding: utf-8

import sys
if sys.version_info[0]<3: input=raw_input

class StandardInput:

    def stdin_string(self):
        self.s=input().rstrip()
        return self.s

    def stdin_integer(self):
        self.n=int(input().rstrip())
        return self.n

    def stdin_array(self):
        self.arr=input().rstrip().split()
        return self.arr

    def stdin_integer_array(self):
        self.arr=map(int,input().rstrip().split())
        return self.arr

def test(arr):
    a,b=arr
    if a%2==0:
        a+=1
    return sum(range(a, b+1, 2))

if __name__ == '__main__':
    obj=StandardInput()
    arr=obj.stdin_integer_array()
    print(test(arr))
