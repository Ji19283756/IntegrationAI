class MathFunction:
    def __init__(self, function_str: str, function):
        self.function_str = function_str
        self.function = function

    def trap_reimann(self, a_start: float, b_end: float, increments: int, debug=False) -> float:
        total = 0
        x_delta = (b_end - a_start) / increments

        if debug:
            print("X_delta", x_delta)
            print([a_start + x * x_delta for x in range(increments + 1)])

        for current_index in [a_start + x * x_delta for x in range(increments + 1)]:
            if current_index == a_start or current_index == b_end:
                total += self.function(current_index)
            else:
                total += self.function(current_index) * 2

            if debug:
                print("current index", current_index)
                print("function", self.function(current_index))
                print("total", total)

        if debug:
            print("total", total)
            print("x delta * total", x_delta * total)
            print("final", x_delta * total / 2)

        return x_delta * total / 2

