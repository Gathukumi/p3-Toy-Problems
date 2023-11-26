def exactly_two_positive(a, b, c):
    # Count the number of positive integers
    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    # Return True if exactly two of the three integers are positive
    return positive_count == 2