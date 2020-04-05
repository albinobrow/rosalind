#!/usr/bin/env python
# coding: utf-8

import re, sys
if sys.version_info[0]<3: input=raw_input

def BA1F(text):
    m,n=0,len(text)
    arr,res=[0]*(n+1),[]
    for i in range(n):
        if text[i]=='G':
            arr[i+1]=arr[i]+1
        elif text[i]=='C':
            arr[i+1]=arr[i]-1
        else:
            arr[i+1]=arr[i]
        if arr[i+1] < m:
            m=arr[i+1]
            res=[str(i+1)]
        elif arr[i+1] == m:
            res.append(str(i+1))
    return ' '.join(res)

if __name__ == '__main__':
    fl_in=sys.argv[1]
    fl_out=re.sub('.txt', '_result.txt', fl_in, 1)
    with open( fl_in, 'r' ) as flr:
        text=flr.readline().rstrip()
    with open( fl_out, 'w' ) as flw:
        flw.write(BA1F(text)+'\n')
