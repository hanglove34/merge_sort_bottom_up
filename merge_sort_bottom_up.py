import random
import time

def sort_list(a, pos, size, array_length):
    mid = pos + size
    d = 0
    i = 0
    result = []

    while d + i < size * 2:
        if pos + size >= array_length or mid + i >= array_length:
            if pos + d < array_length:
                result.append(a[pos + d])
                d += 1
            else:
                break
        elif d == size:
            result.append(a[mid + i])
            i +=1
        elif i == size:
            result.append(a[pos + d])
            d += 1
        elif a[pos + d] <= a[mid + i]:
            result.append(a[pos + d])
            d += 1
        else:
            result.append(a[mid + i])
            i += 1
    return (result)


def sort_Data(a, pos, size, array_length):
    sortList = sort_list(a, pos, size, array_length)
    for i in range(0, len(sortList)):
        if pos + i < array_length:
            a[pos + i] = sortList[i]

def merge(a):
    array_length = len(a)

    impair = array_length % 2
    m = 1
    while int(m / 2) <= array_length:
        for d in range(0, array_length + impair, 2*m):
            sort_Data(a, d, m, array_length)
        m = 2*m



# Iterative implementation of merge sort
if __name__ == '__main__':
 
    A = []
    for i in range(0, 1000000):
        A.append(i)
    random.shuffle(A)

    startTime = time.time()


    # A = [9,5,4,8,3,2,1,7,6,10]
 
    # print("Original array:", A)
    merge(A)
    print(time.time() - startTime)
    # print("Modified array:", A)
