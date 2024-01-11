phone = "123-1233"

def validate_phone(value):
    numbers = list(map(str,value.split("-")))
    if len(numbers) != 3:
        raise ValueError("Phone Number is uncorrect")
    elif len(numbers[0]) != 3 or  len(numbers[1]) != 3 or  len(numbers[2]) != 4:
        raise ValueError("Phone Number is uncorrect")
    else:
        return value
