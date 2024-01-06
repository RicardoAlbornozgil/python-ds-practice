def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
     # Create a dictionary to store counts of each element
    counts = {}

    # Count occurrences of each element
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
