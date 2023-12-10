def letter_count_of_number(n):
    # 1 to 19
    one_to_nineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4,
                       3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # 20, 30, 40, 50, 60, 70, 80, 90
    twenty_to_ninety = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    # 100, 200, 300, 400, 500, 600, 700, 800, 900
    hundred_to_nine_hundred = [0, 10, 10, 12, 11, 11, 10, 12, 12, 11]
    # 1000
    one_thousand = 11
    
    if n < 20:
        return one_to_nineteen[n]
    elif n < 100:
        return twenty_to_ninety[n // 10] + one_to_nineteen[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return hundred_to_nine_hundred[n // 100]
        else:
            return hundred_to_nine_hundred[n // 100] + 3 + letter_count_of_number(n % 100)
    else:
        return one_thousand
    
def number_letter_counts(n):
    count = 0
    for i in range(1, n + 1):
        count += letter_count_of_number(i)
    return count

if __name__ == '__main__':
    print(number_letter_counts(1000))