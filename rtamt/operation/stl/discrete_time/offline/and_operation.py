from rtamt.operation.abstract_operation import AbstractOperation
import math

class AndOperation(AbstractOperation):
    def __int__(self):
        super().__init__()

    def update(self, left, right, robustness_type):

        if robustness_type == "Traditional":

            out = list(map(min, zip(left, right)))

        elif robustness_type == "AGM":
            out = []
            for i in range(0, len(left)):
                if left[i] < 0 or right[i] < 0:
                    out.append((left[i] + right[i]) / 2)
                else:
                    result = math.sqrt((left[i] + 1) * (right[i] + 1)) - 1
                    out.append(result)

        return out