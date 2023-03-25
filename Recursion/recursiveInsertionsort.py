
def insertionsort(seq):
    issort(seq,len(seq))
    return seq

def issort(seq,k):
    if k > 1:
        issort(seq,k-1)
        insert(seq,k-1)

def insert(seq, k):
    pos = k
    while pos > 0 and seq[pos] < seq[pos - 1]:
        seq[pos] , seq[pos-1] = seq[pos-1], seq[pos]
        pos = pos- 1

seq = [7,8,5,2,4,6,3]
n = 7
print(insertionsort(seq))