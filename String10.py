def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    c=x*y

    return f"({x}+{y})*2={2*c}"
x=int(input())
y=int(input())
print(main(x,y))