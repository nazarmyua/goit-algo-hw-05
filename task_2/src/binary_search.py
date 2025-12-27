def search(arr, target):
    if not arr:
        return (0, None)

    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:

            return (iterations, mid_value)
        elif mid_value < target:
            left = mid + 1
        else:

            upper_bound = mid_value
            right = mid - 1

    if left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)
