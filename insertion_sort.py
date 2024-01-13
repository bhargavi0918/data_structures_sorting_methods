def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        for i in range(1,n):
            j=i-1
            key=arr[i]
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                arr[j+1] = key
        return arr
def main():
    arr=list(map(int,input("Enter array elements:").split( )))
    insertion_sort(arr)
    print(arr)

main()