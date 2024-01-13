def bubble_sort(arr):      # time complexity:O(n^2),space_complexity = O(1)
    n=len(arr)
    swapped = False
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                swapped=True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped:
            return arr

def main():
    arr = list(map(int,input("Enter array elements:").split( )))
    bubble_sort(arr)
    print("Sorted array is:")
    for num in range(len(arr)):
        print(arr[num],end=" ")

main()