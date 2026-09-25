# List Arabic footnotes per page with anchor context, from the AR-full transcription.
# usage: python3 arfn.py START_LINE END_LINE [k1,k2,...]
import re,sys
A='/home/condoriano/hobby/islamic-books-hun/fiqh-us-seerah/FiqhusSeerah-Muhammad-al-Ghazali-AR-full.md'
L=open(A,encoding='utf-8').read().split('\n')
def fns(s,e):
    out=[];page=None;k=0;pages={}
    for i in range(s-1,e-1):
        m=re.match(r'^\[صفحة (\d+)\]',L[i])
        if m: page=m.group(1); continue
        pages.setdefault(page,[]).append(i)
    for pg,idxs in pages.items():
        body=[i for i in idxs if not L[i].startswith('>')]
        notes=[i for i in idxs if re.match(r'^> \(([٠-٩0-9]+|\*)\)',L[i])]
        for n in notes:
            mk=re.match(r'^> (\(([٠-٩0-9]+|\*)\))',L[n]).group(1); ctx=''
            for b in body:
                j=L[b].find(mk)
                if j>=0: ctx=L[b][max(0,j-70):j+len(mk)]; break
            k+=1; out.append((k,pg,n+1,mk,L[n][:100],ctx))
    return out
if __name__=='__main__':
    s,e=int(sys.argv[1]),int(sys.argv[2])
    want=set(int(x) for x in sys.argv[3].split(',')) if len(sys.argv)>3 else None
    for r in fns(s,e):
        if want is None or r[0] in want: print(r[0],'p'+str(r[1]),r[2],r[3],'|',r[5])
