def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
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
            a.append(list1[i])
        
        i += 1

    return  a

print(main([1,0,0,0,1]))