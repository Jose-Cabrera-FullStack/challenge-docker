def find_matching_pair(arr, target_sum):
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target_sum:
            return (arr[i], arr[j])
        elif s < target_sum:
            i += 1
        else:
            j -= 1
    return None
