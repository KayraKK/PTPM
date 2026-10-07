import math


def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "не треугольник", [(-1, -1)] * 3

    if a == b == c:
        t = "равносторонний"
    elif a == b or a == c or b == c:
        t = "равнобедренный"
    else:
        t = "разносторонний"

    cx = (a * a + b * b - c * c) / (2 * a)
    cy = math.sqrt(b * b - cx * cx)
    xs, ys = [0, a, cx], [0, 0, cy]

    w, h = max(xs) - min(xs), max(ys) - min(ys)
    s = 80 / max(w, h)
    ox, oy = (100 - w * s) / 2, (100 - h * s) / 2

    coords = [
        (int((x - min(xs)) * s + ox), int((y - min(ys)) * s + oy))
        for x, y in zip(xs, ys)
    ]
    return t, coords


def parse_and_solve(a_str, b_str, c_str):
    try:
        return triangle(float(a_str), float(b_str), float(c_str))
    except ValueError:
        return "", [(-2, -2)] * 3