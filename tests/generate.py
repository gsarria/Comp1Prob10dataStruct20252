#!/usr/bin/env python3
import os, random; random.seed(51)
def compress(arr):
    if not arr: return []
    res=[]; cur=arr[0]; cnt=1
    for x in arr[1:]:
        if x==cur: cnt+=1
        else: res.append((cur,cnt)); cur=x; cnt=1
    res.append((cur,cnt)); return res
def w(name, arr):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(str(len(arr))+"\\n"+" ".join(map(str,arr))+"\\n")
    pairs=compress(arr)
    flat=[str(len(pairs))+"\\n", " ".join(str(x) for t in pairs for x in t)+"\\n"]
    open(f"tests/output_{name}.txt","w").writelines(flat)
def main():
    w("min",[7])
    n=2*10**5; arr=[(i//3)%10 for i in range(n)]; w("max",arr)
    n=1000; import random
    arr=[random.randint(0,5) for _ in range(n)]; w("rnd",arr)
if __name__=="__main__": main()
