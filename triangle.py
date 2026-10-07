import math
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

EPS = 1e-9

while True:
    logging.info("Новая проверка")

    try:
        raw_a = input("a: ")
        raw_b = input("b: ")
        raw_c = input("c: ")

        a, b, c = float(raw_a), float(raw_b), float(raw_c)
        logging.info(f"Пользователь ввёл стороны: a={a}, b={b}, c={c}")
    except Exception as e:
        logging.error(f"Ошибка ввода: Некорректные символы. {str(e)}")
        print([(-2, -2)] * 3)
        continue

    if a <= 0 or b <= 0 or c <= 0:
        logging.warning("Результат: не треугольник (стороны должны быть больше 0)")
        print([(-1, -1)] * 3)
        continue

    if (a + b <= c + EPS) or (a + c <= b + EPS) or (b + c <= a + EPS):
        logging.warning("Результат: не треугольник (нарушено неравенство треугольника)")
        print([(-1, -1)] * 3)
        continue

    if a == b == c:
        type_str = "равносторонний"
    elif a == b or a == c or b == c:
        type_str = "равнобедренный"
    else:
        type_str = "разносторонний"

    logging.info(f"Результат: {type_str}")

    # Расчет координат
    cx = (a * a + b * b - c * c) / (2 * a)
    cy = math.sqrt(max(0.0, b * b - cx * cx))
    xs, ys = [0, a, cx], [0, 0, cy]

    w, h = max(xs) - min(xs), max(ys) - min(ys)
    s = 80 / max(w, h)
    ox, oy = (100 - w * s) / 2, (100 - h * s) / 2

    coords = [(int((x - min(xs)) * s + ox), int((y - min(ys)) * s + oy)) for x, y in zip(xs, ys)]
    logging.info(f"Рассчитанные координаты: {coords}")
    print(coords)
