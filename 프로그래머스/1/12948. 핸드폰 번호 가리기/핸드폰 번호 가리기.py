def solution(phone_number):
    # hidden = phone_number[:-4]
    # phone_number = phone_number.replace(hidden, '*' * len(hidden))
    # return phone_number
    mask = '*' * (len(phone_number) - 4)
    back = phone_number[-4:]
    return mask + back