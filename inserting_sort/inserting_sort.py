

def inserting_sort(unsorted_array):
    for index in range(1, len(unsorted_array)):

        current_value = unsorted_array[index]
        position = index

        while position > 0 and unsorted_array[position - 1] > current_value:
            unsorted_array[position] = unsorted_array[position - 1]
            position = position - 1

        unsorted_array[position] = current_value


if __name__ == '__main__':

    array = [2, 6, 85, 45, 12, 3]
    inserting_sort(array)
    print(array)
