from rtamt.operation.abstract_operation import AbstractOperation
import math
import numpy as np

class AndOperation(AbstractOperation):
    def __int__(self):
        super().__init__()

    def update(self, out_sample, robustness_type):

        if robustness_type == "Traditional":

            out = list(map(min, zip(out_sample)))

        elif robustness_type == "AGM":
            out = []
            array = np.array(out_sample)
            for i in range(0, array.shape[1]):
                if any(array[:, i] < 0):
                    out.append(sum(array[:, i]) / array.shape[0])
                else:
                    result = math.pow(math.prod(1 + array[:, i]), 1 / array.shape[0]) - 1
                    out.append(result)

        return out