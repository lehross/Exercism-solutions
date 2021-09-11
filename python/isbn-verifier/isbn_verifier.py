def is_valid(isbn):
    isbn = isbn.replace("X", "10").replace("-", "")
    
    if not isbn.isdigit() or len(isbn) < 10:
        return False
    
    return (sum([int(isbn[i]) * (10 - i) for i in range(9)]) + int(isbn[9:])) % 11 == 0
