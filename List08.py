def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = []
    i = 0
    while i < len(list1):
        if int(list1[i]) == 1:
            a.append(True)

        else:
            a.append(list1[False])
        
        i += 1

    return a

    return