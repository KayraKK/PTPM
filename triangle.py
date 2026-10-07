import math

try:
    a, b, c = float(input()), float(input()), float(input())
except:
    print("")
    print([(-2, -2)] * 3)
    exit()

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("не треугольник")
    print([(-1, -1)] * 3)
else:
    if a == b == c:
        print("равносторонний")
    elif a == b or a == c or b == c:
        print("равнобедренный")
    else:
        print("разносторонний")

    cx = (a * a + b * b - c * c) / (2 * a)
    cy = math.sqrt(b * b - cx * cx)
    xs, ys = [0, a, cx], [0, 0, cy]

    w, h = max(xs) - min(xs), max(ys) - min(ys)
    s = 80 / max(w, h)
    ox, oy = (100 - w * s) / 2, (100 - h * s) / 2

    print([(int((x - min(xs)) * s + ox), int((y - min(ys)) * s + oy)) for x, y in zip(xs, ys)])