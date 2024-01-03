def find_coordinates(given, index, x, y, size):                                 # 주어진 사분면 문자열을 바탕으로 실제 x, y 좌표를 찾는다.
    if size == 1:
        return x, y
    else:
        offset = size // 2
        if given[index] == '1':
            return find_coordinates(given, index + 1, x + offset, y, offset)
        elif given[index] == '2':
            return find_coordinates(given, index + 1, x, y, offset)
        elif given[index] == '3':
            return find_coordinates(given, index + 1, x, y + offset, offset)
        elif given[index] == '4':
            return find_coordinates(given, index + 1, x + offset, y + offset, offset)


def calculate_quadrant(x, y, tx, ty, size):                                   # 실제 x, y 좌표를 바탕으로 사분면 문자열을 구한다.
    if size == 1:                                                             # tx, ty 좌표는 구하려는 좌표
        return ''                                                             # x, y 는 현재 좌표

    offset = size // 2
    if tx >= x + offset and ty < y + offset:
        return '1' + calculate_quadrant(x + offset, y, tx, ty, offset)
    elif tx < x + offset and ty < y + offset:
        return '2' + calculate_quadrant(x, y, tx, ty, offset)
    elif tx < x + offset and ty >= y + offset:
        return '3' + calculate_quadrant(x, y + offset, tx, ty, offset)
    else:
        return '4' + calculate_quadrant(x + offset, y + offset, tx, ty, offset)


_, given = input().split()
dx, dy = map(int, input().split())
dy = -dy                                # dy 양수값이 위로 올라가는 것이기 때문에 부호를 뒤집어줘야 한다.
size = 2 ** len(given)                  # 한 변의 길이는 (size) 주어진 사분면 문자열의 길이로 구할 수 있다.
tx, ty = find_coordinates(given, 0, 0, 0, size)         # 주어진 사분면의 실제 x, y 좌표를 구한다.
tx += dx
ty += dy                                                            # 이동하려는 x, y 좌표를 구한다.

if 0 <= tx < size and 0 <= ty < size:
    print(calculate_quadrant(0, 0, tx, ty, size))             # 이동하려는 x, y 좌표의 사분면 문자열을 구한다.
else:
    print(-1)
