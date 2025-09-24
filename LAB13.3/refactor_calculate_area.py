from math import pi
from typing import Callable, Dict


def area_rectangle(width: float, height: float) -> float:

    if width < 0 or height < 0:
        raise ValueError("Rectangle dimensions must be non-negative")
    return width * height


def area_square(side_length: float) -> float:

    if side_length < 0:
        raise ValueError("Square side length must be non-negative")
    return side_length * side_length


def area_circle(radius: float) -> float:

    if radius < 0:
        raise ValueError("Circle radius must be non-negative")
    return pi * radius * radius


def _require_height(y: float | None) -> float:

    if y is None:
        raise ValueError("Rectangle area requires both width (x) and height (y)")
    return y


_AREA_FUNCTIONS: Dict[str, Callable[[float, float | None], float]] = {
    "rectangle": lambda x, y: area_rectangle(x, _require_height(y)),
    "square": lambda x, _y: area_square(x),
    "circle": lambda x, _y: area_circle(x),
}


def calculate_area(shape: str, x: float, y: float | None = None) -> float:

    shape_key: str = shape.lower()
    try:
        handler = _AREA_FUNCTIONS[shape_key]
    except KeyError as error:
        raise ValueError(
            f"Unsupported shape: {shape}. Supported: {', '.join(_AREA_FUNCTIONS)}"
        ) from error
    return handler(x, y)


if __name__ == "__main__":
    print("rectangle 3x4:", calculate_area("rectangle", 3, 4))
    print("square 5:", calculate_area("square", 5))
    print("circle r=2:", calculate_area("circle", 2))


