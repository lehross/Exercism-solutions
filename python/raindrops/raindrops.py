def convert(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    result = []

    for fact in factors:
        if number % fact == 0:
            result.append(factors[fact])

    if result:
        return(''.join(result))
    else:
        return(str(number))
