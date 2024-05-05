while True:
    histogram = list(map(int, input().split()))
    histogram.pop(0)

    if not histogram:
        break

    stack = []
    ans = 0
    for idx, height in enumerate(histogram):
        while stack and histogram[stack[-1]] > height:  # 더 작은 직사각형을 만났을 때
            h = histogram[stack.pop()]  # 높이
            w = idx
            if stack:
                w = (idx - 1) - stack[-1]  # right index - left index
            ans = max(ans, w * h)
        stack.append(idx)

    while stack:  # 으른쪽 끝에 도달
        h = histogram[stack.pop()]
        w = len(histogram)
        if stack:
            w = (len(histogram) - 1) - stack[-1]  # 마지막 index - left index
        ans = max(ans, w * h)

    print(ans)
