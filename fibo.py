#!/usr/bin/python3
import sys

def fib(n):
    
    x,y=1,1
    
    for i in range(n):
        print(x)
        x,y=y,x+y
        
if __name__== '__main__':
    n=int(sys.argv[-1])
    fib(n)
