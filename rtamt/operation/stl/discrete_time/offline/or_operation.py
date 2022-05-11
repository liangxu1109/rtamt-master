from rtamt.operation.abstract_operation import AbstractOperation
import numpy as np
import math
class OrOperation(AbstractOperation):
    def __init__(self):
        pass

    def update(self, out_sample, robustness_type):

        if robustness_type == "Traditional":
            array = np.array(out_sample)
            array = np.delete(array, -1, axis=0)
            out = []
            for i in range(0, array.shape[1]):
                out.append(max(array[:, i]))

        elif robustness_type == "AGM":
            out = []
            array = np.array(out_sample)
            array = np.delete(array, -1, axis=0)
            for i in range(0, array.shape[1]):
                if any(array[:, i] > 0):
                    out.append(sum(array[:, i]) / array.shape[0])
                else:
                    result = - math.pow(math.prod(1 - array[:, i]), 1 / array.shape[0]) + 1
                    out.append(result)

        return out
