import rtamt.enumerations.options
from rtamt.operation.abstract_operation import AbstractOperation
import math
import numpy as np
class AlwaysBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def update(self, samples, robustness_type):
        if robustness_type == rtamt.RobustnessMetrics.Standard:
            samples = np.array(samples)
            diff = self.end - self.begin
            out = [min(samples[j:j+diff+1]) for j in range(0, len(samples) - diff+1)]
            tmp = [-1 for i in range(0,len(samples)-len(out))]
            out += tmp
        elif robustness_type == rtamt.RobustnessMetrics.AGM:
            samples = np.array(samples)
            diff = self.end - self.begin
            out = []
            for j in range(0, len(samples) - diff):
                if any(samples[j:j + diff + 1] <= 0):
                    out_diff = sum(samples[j:j + diff + 1]) / (diff + 1)
                    out.append(out_diff)
                else:
                    out_diff = math.pow(math.prod(1 + samples[j:j + diff + 1]), 1 / (diff + 1)) - 1
                    out.append(out_diff)
            for j in range(len(samples) - diff, len(samples)):
                out_diff = (sum(samples[j:j + diff + 1]) + (-1 * (diff + j + 1 - len(samples)))) / (diff + 1)
                out.append(out_diff)
        return out
