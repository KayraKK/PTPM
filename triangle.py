import math

EPS = 1e-9

while True:
    print("\nНовая проверка")

    try:
        a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))
    except:
        print("")
        print([(-2, -2)] * 3)
        continue

    if a <= 0 or b <= 0 or c <= 0:
        print("не треугольник")
        print([(-1, -1)] * 3)
        continue

    if (a + b <= c + EPS) or (a + c <= b + EPS) or (b + c <= a + EPS):
        print("не треугольник")
        print([(-1, -1)] * 3)
        continue

    if a == b == c:
        print("равносторонний")
    elif a == b or a == c or b == c:
        print("равнобедренный")
    else:
        print("разносторонний")

    cx = (a * a + b * b - c * c) / (2 * a)
    cy = math.sqrt(max(0.0, b * b - cx * cx))
    xs, ys = [0, a, cx], [0, 0, cy]

    w, h = max(xs) - min(xs), max(ys) - min(ys)
    s = 80 / max(w, h)
    ox, oy = (100 - w * s) / 2, (100 - h * s) / 2

    print([(int((x - min(xs)) * s + ox), int((y - min(ys)) * s + oy)) for x, y in zip(xs, ys)])