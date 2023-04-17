def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """

    return f'[{x1}, {x2}, {x3}]'
x1=int(input())
x2=int(input())
x3=int(input())

print(main(x1,x2,x3))