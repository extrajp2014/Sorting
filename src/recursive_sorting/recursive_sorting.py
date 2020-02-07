# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    idx_arrA = 0
    idx_arrB = 0
    for i in range(elements):
        if len(arrA) == idx_arrA:
            for j in range(idx_arrB, len(arrB)):
                merged_arr[i + j - idx_arrB] = arrB[j]
            return merged_arr
        elif len(arrB) == idx_arrB:
            for j in range(idx_arrA, len(arrA)):
                merged_arr[i + j - idx_arrA] = arrA[j]
            return merged_arr
        elif arrA[idx_arrA] < arrB[idx_arrB]:
            merged_arr[i] = arrA[idx_arrA]
            idx_arrA += 1
        else:
            merged_arr[i] = arrB[idx_arrB]
            idx_arrB += 1

    return (merged_arr)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr)<2:
        return arr
    else:
        mid_idx_arr = len(arr) // 2
        arr_left = merge_sort(arr[:mid_idx_arr])
        arr_right = merge_sort(arr[mid_idx_arr:])
    return merge(merge_sort(arr_left), merge_sort(arr_right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
