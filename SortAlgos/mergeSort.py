def Merge(left_arr, rigth_arr):
    arr_resultado = []
    while len(left_arr) > 0 and len(rigth_arr) > 0:
        if left_arr[0] > rigth_arr[0]:
            arr_resultado.append(rigth_arr[0])
            rigth_arr.pop(0)
        else:
            arr_resultado.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0:
        arr_resultado.append(left_arr[0])
        left_arr.pop(0)

    while len(rigth_arr) > 0:
        arr_resultado.append(rigth_arr[0])
        rigth_arr.pop(0)
    
    return arr_resultado

def mergesort(arr):
    if len(arr) == 1:
        return arr
    
    middle = len(arr) // 2
    left_array = arr[:middle]
    rigth_array = arr[middle:]

    sorted_left = mergesort(left_array)
    sorted_rigth = mergesort(rigth_array)

    return Merge(sorted_left, sorted_rigth)

result = mergesort([0,9,8,7,6,5,4,3,2,1])
print(result)