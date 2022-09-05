def classify(number):
    sum = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    for i in range(1, number):
        if number % i == 0: 
            sum += i

    if(sum == number):
        return "perfect"
    elif(sum > number):
        return "abundant"
    else:
        return "deficient"
    
