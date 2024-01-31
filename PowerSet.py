# Matthew Baker
# Bakerma2@oregonstate.edu
# CS325: Analysis of Algorithms
# HW4: Question 2 - Power Set


def main():
    pass


def powerset(inputSet: list) -> list:
    """
    Generates the power set for a given input set. A power set is the set of all subsets that can be made using elements
    from the original set. For example the power set of the set [1, 2] would be [[], [1], [2], [1,2]]

    Args:
        inputSet (list): A set of integers.
    Returns:
        output_set (list): The powerset of the input set.
    """

    # Base case of empty set ends recursion.
    n = len(inputSet)
    if n == 0:
        return [[]]

    # Recursive cases, each layer of recursion generates subsets af a particular size n.
    output_set = []
    next_input_set = inputSet[0:n-1]
    subsets = powerset(next_input_set)

    # Build the subsets.
    for subset in subsets:
        if subset not in output_set:
            output_set.append(subset)
        if subset + [inputSet[n-1]] not in output_set:
            output_set.append(subset + [inputSet[n-1]])
    return output_set


if __name__ == '__main__':
    main()
