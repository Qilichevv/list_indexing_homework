def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    return [list1[1]]*len(list1) == list1
print(main([1,1,1,1,1]))