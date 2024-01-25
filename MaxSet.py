# Matthew Baker
# Bakerma2@oregonstate.edu
# CS325: Analysis of Algorithms
# HW4: Question 1 - Max Set


def main():
    pass


def max_independent_set(nums):
    """
    Determine the sequence consisting of non-consecutive elements in an array that produces the maximum sum.  Uses a
    dynamic programming approach that iterates through an input array and stores sub-problem solutions in a cache array.
    An array of all negative integers will return an empy array.

    Args:
        nums (arr): An array of integers.
    Returns:
        max_sum (arr): An array with the sequence of elements that produces the max sum.
    """

    # Initialize the cache array
    n = len(nums)
    cache = [0] * n
    cache[0] = nums[0]

    # Iterate through the input array and build the cache
    for i in range(1, n):
        # Ignore negatives
        if nums[i] > 0:
            cache[i] = max(cache[i - 1], cache[i - 2] + nums[i])
        else:
            cache[i] = nums[i]

    # Check for edge cases of all negatives or a sum of 0
    if cache[n - 1] < 0:
        return []
    elif cache[n - 1] == 0:
        return [0]

    # Build the maximum sum sequence from the cache array by working backwards, then reverse the output array to match
    # the original input order.
    else:
        max_sum = []
        i = n - 1
        while i >= 0:
            if cache[i] == cache[i - 1]:
                i -= 1
            else:
                max_sum.append(nums[i])
                i -= 2
        max_sum.reverse()
        return max_sum


if __name__ == '__main__':
    main()
