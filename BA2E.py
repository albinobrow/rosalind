#!/usr/bin/env python
# coding: utf-8


import datetime, re, string, sys, itertools, numpy as np, operator
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

class OpenArgumentFile:
      def read_single_file(self):
          with open(sys.argv[1], 'r', encoding='utf-8') as fhr:
              arr=RowLineInput(fhr.readlines()).rwlin_array()
          return arr

class OpenAchivementFile:      
      def name_output_file(self):
          dt_now = datetime.datetime.now()
          return re.sub(r"\.txt$", ".result."+dt_now.strftime('%Y-%m-%d--%H-%M-%S')+".txt", sys.argv[1])


def PrettyPrintArray(arr):
    arr=list(map(str, arr))
    return ' '.join(arr)


def HammingDistance(s,t):
    n=len(s)
    count=0
    for i in range(n):
        if s[i]!=t[i]:
            count+=1
    return count


def GeneratePatterns( k ):
    arr = []
    base=['A', 'C', 'G', 'T']
    for i in itertools.product(base, repeat=k):
        pattern=''.join(i)
        arr.append( pattern )
    return arr


def MOTIFENUMERATION(Dna, k, d):
    patterns = []
    arr = GeneratePatterns( k )
    
    for p in arr:
        count = 0
        for i in Dna:
            for j in range( len( i ) - k + 1 ):
                if HammingDistance( i[j:j+k], p  ) <= d:
                    count += 1
                    break

        if count == len( Dna ):
            patterns.append( p )
    patterns = sorted( set( patterns ))
    if len( patterns ) == 0:
        patterns.append( 'nan' )
    return patterns


def BestMotifs( Dna, k ):
    arr =[[0]*4]*k
    arr=np.array(arr)
    for i in Dna:
        for j in range(k):
            if i[j] == 'A':
                arr[j][0]+=1
            if i[j] == 'C':
                arr[j][1]+=1
            if i[j] == 'G':
                arr[j][2]+=1
            if i[j] == 'T':
                arr[j][3]+=1
    return np.array(arr).T/len(Dna)


def MakeMotifProfile( Dna, k ):
    arr =[[0]*4]*k
    arr=np.array(arr)
    for i in Dna:
        for j in range(k):
            if i[j] == 'A':
                arr[j][0]+=1
            if i[j] == 'C':
                arr[j][1]+=1
            if i[j] == 'G':
                arr[j][2]+=1
            if i[j] == 'T':
                arr[j][3]+=1
    return (np.array(arr).T + 1 )/(len(Dna) + 4 )


def profileMostProbable(string, k, profile):
    mx = {'A':0, 'C':1, 'G':2, 'T':3,}
    maxstring = (-1, '')
    for i in range(len(string) - k + 1):
        prob = 1
        subseq = string[i:i+k]
        for pos,base in enumerate(subseq):
            prob *= profile[mx[base]][pos]
            if prob < maxstring[0]:
                break
        if prob > maxstring[0]:
            maxstring = (prob, subseq)
    return maxstring[1]


def ScoreProfileMatrix( profile , k):
    score=0
    arr=np.array( profile )
    for i in arr.T:
        score+=1-max(i)
    return score/k


def GREEDYMOTIFSEARCH(Dna, k, t):
    bestmotifs = []    
    for i in range(t):
        bestmotifs.append(Dna[i][0:k])
    for i in range(len(Dna[0]) - k + 1):
        motifs=[]
        motif1=Dna[0][i:i+k]
        motifs.append( motif1 )
        for j in range(1,t):   
            profile=MakeMotifProfile(motifs, k)
            motifj=profileMostProbable(Dna[j], k, profile)
            motifs.append(motifj)
        if ScoreProfileMatrix( MakeMotifProfile( motifs, k ), k) < ScoreProfileMatrix( MakeMotifProfile( bestmotifs, k ), k):
            bestmotifs = motifs
    return bestmotifs


def test(arr):
    ###
    
    k,t=list(map(int,  arr[0].split() ))
    Dna =  arr[1:] 
#    Dna = arr[1].split()

    return GREEDYMOTIFSEARCH(Dna, k, t)

    ###


if __name__ == '__main__':

    arr=OpenArgumentFile().read_single_file()
    output_file=OpenAchivementFile().name_output_file()
    with open( output_file, 'w', encoding='utf-8') as fhw:
#        fhw.write(str( PrettyPrintArray(test(arr)) )+'\n')
        for a in test(arr):
            fhw.write( a +'\n')
