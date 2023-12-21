def get_odds(a,b):
    return [odd_value for odd_value in range(int(a), int(b)) if odd_value % 2 != 0]

print(get_odds(2.3, 14.5))