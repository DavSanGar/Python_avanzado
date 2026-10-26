import functools


@functools.lru_cache(maxsize=None)
def kadane_with_subarray(arr):
    max_sum = current_sum = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    max_subarray = arr[start:end+1]
    return max_sum, max_subarray

arr = tuple([2,-3,5,7,-1,4,-2,1])
resultado, subarray = kadane_with_subarray(arr)
print("La suma maxima del subarray contiguo es de: ", resultado)
print("El subarray contiguo con la suma maxima es: ", subarray)