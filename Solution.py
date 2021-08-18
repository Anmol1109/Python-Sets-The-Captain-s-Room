# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = map(int,input().split(' '))
arr = sorted(arr)
for i in range(1, len(arr)):
    if i != len(arr) - 1:
        if arr[i] != arr[i - 1] and arr[i] != arr[i+1]:
            print(arr[i])
            break
    else:
        print(arr[i])
