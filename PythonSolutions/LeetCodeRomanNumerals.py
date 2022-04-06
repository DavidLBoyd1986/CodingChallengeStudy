def roman_to_int(s: str) -> int:

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    position = len(s) - 1
    previous_value = ''
    while position > -1:
        current_value = s[position]
        if previous_value in ['V', 'X', 'L']:
            if current_value == 'I':
                total = total - values.get(current_value)
                position -= 1
                previous_value = current_value
                continue
        if previous_value in ['L', 'C']:
            if current_value == 'X':
                total = total - values.get(current_value)
                position -= 1
                previous_value = current_value
                continue
        if previous_value in ['D', 'M']:
            if current_value == 'C':
                total = total - values.get(current_value)
                position -= 1
                previous_value = current_value
                continue

        total = total + values.get(current_value)
        position -= 1
        previous_value = current_value

    return total



answer = roman_to_int("MCMXCIV")
print(answer)

