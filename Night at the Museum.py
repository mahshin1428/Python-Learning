def min_rotations(e):
    current = 'a'
    rotations = 0

    for char in e:
        clockwise = abs(ord(char) - ord(current))
        counterclockwise = 26 - clockwise
        rotations += min(clockwise, counterclockwise)
        current = char

    return rotations


exhibit = input().strip()
print(min_rotations(exhibit))
