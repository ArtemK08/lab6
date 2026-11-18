
def area(length, width):
    
    if length < 0 or width < 0:
        raise ValueError("Довжина та ширина не можуть бути від'ємними.")
    return length * width


def perimeter(length, width):
    
    if length < 0 or width < 0:
        raise ValueError("Довжина та ширина не можуть бути від'ємними.")
    return 2 * (length + width)
