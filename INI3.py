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

def test(s, arr):
    a,b,c,d=arr
    return ' '.join([s[a:b+1],s[c:d+1]])

if __name__ == '__main__':
    obj=StandardInput()
    s=obj.stdin_string()
    arr=obj.stdin_integer_array()
    print(test(s, arr))
