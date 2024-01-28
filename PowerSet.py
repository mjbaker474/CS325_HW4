# Matthew Baker
# Bakerma2@oregonstate.edu
# CS325: Analysis of Algorithms
# HW4: Question 2 - Power Set


def main():
    pass


def powerset(inputSet):
    output_set = []
    n = len(inputSet)
    if n == 0:
        return [[]]


    next_input_set = inputSet[0:n-1]

    subsets = powerset(next_input_set)
    for subset in subsets:
        if subset not in output_set:
            output_set.append(subset)
        if subset + [inputSet[n-1]] not in output_set:
            output_set.append(subset + [inputSet[n-1]])
    return output_set


if __name__ == '__main__':
    main()
