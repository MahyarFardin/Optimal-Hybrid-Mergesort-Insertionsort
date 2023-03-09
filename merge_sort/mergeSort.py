'''In this program we want to sort
arrays using by merge sort.'''


def merg_sort(unsorted_Array):

    # if the length of array is 1 or 0 that array is sorted
    if len(unsorted_Array) == 1 or len(unsorted_Array) == 0:
        return unsorted_Array

    elif len(unsorted_Array) > 1:
        mid = len(unsorted_Array) // 2  # find the middile of array
        # the left side of array: from index = 0 to middile of array
        Left = unsorted_Array[:mid]
        # the right side of array: from middile + 1 to end of array
        Right = unsorted_Array[mid:]

        merg_sort(Left)
        merg_sort(Right)

        i = 0        # Initial index of left side
        j = 0        # Initial index of right side
        k = 0        # Initial index of merged subarray

        # data to temp arrays Left[] and Right[]
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                unsorted_Array[k] = Left[i]
                i += 1
            else:
                unsorted_Array[k] = Right[j]
                j += 1
            k += 1

        # checking if any element was Left
        while i < len(Left):
            unsorted_Array[k] = Left[i]
            i += 1
            k += 1

        # checking if any element was Right
        while j < len(Right):
            unsorted_Array[k] = Right[j]
            j += 1
            k += 1


# print the array
def print_array(array):
    for i in range(len(array)):
        print(array[i], end=' ')
    print()


# test above code
if __name__ == "__main__":
    array = [64, 32, 85, 2, 5, 14]
    print('given array is ', end='\n')
    print_array(array)
    merg_sort(array)
    print('sorted array is ', end='\n')
    print_array(array)
