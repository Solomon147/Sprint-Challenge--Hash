def has_negatives(a):

    """
    YOUR CODE HERE
    """
    par = {}
    char = {}
    result = []
    for num in a:
        if num > 0:
            par[num] = -num
        if num < 0:
            char[num] = num * -1
    for key in par:
        if par[key] in char:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
