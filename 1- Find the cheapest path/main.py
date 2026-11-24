def encode_rail_fence_cipher(string, n):
    if not string:
        return ""

    rails = [""] * n
    row = 0
    direction = 1

    for ch in string:
        rails[row] += ch

        if row == 0:
            direction = 1
        elif row == n - 1:
            direction = -1

        row += direction

    return "".join(rails)


def decode_rail_fence_cipher(string, n):
    if not string:
        return ""

    pattern = []
    row = 0
    direction = 1

    for _ in string:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == n - 1:
            direction = -1

        row += direction

    counts = [0] * n
    for r in pattern:
        counts[r] += 1

    rails = []
    index = 0
    for count in counts:
        rails.append(list(string[index:index + count]))
        index += count

    positions = [0] * n
    result = []

    for r in pattern:
        result.append(rails[r][positions[r]])
        positions[r] += 1

    return "".join(result)