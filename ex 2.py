class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        if denominator == 0:
            return f"На ноль делить нельзя"
        else:
            return divider / denominator


print(DivisionByNull.divide_by_null(55, 20))
print(DivisionByNull.divide_by_null(11, 0))
print(DivisionByNull.divide_by_null(45, 0))
