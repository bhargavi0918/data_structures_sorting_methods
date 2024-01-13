def selection_sort(arr):
    length = len(arr)

    for i in range(0,length):
        min_index= i
        for j in range(i+1,length):
            if arr[j] < arr[min_index]:
                min_index= j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

def main():
    arr =list(map(int,input("Enter the array elements:").split()))
    print(selection_sort(arr))

main()