from rtamt.operation.abstract_operation import AbstractOperation
import math
class EventuallyBoundedOperation(AbstractOperation):
    def __init__(self, begin, end, robustness_type):
        self.begin = begin
        self.end = end
        self.robustness_type = robustness_type

    def update(self, samples, robustness_type):
        if self.robustness_type == "Traditional":
            diff = self.end - self.begin
            out = [max(samples[j:j + diff + 1]) for j in range(0, len(samples) - diff + 1)]
            tmp = [float("inf") for i in range(0, len(samples) - len(out))]
            out += tmp
        elif self.robustness_type == "AGM":
            diff = self.end - self.begin
            out = []
            for j in range(0, len(samples) - diff + 1):
                if any(samples[j:j + diff + 1] > 0):
                    out_diff = sum(samples[j:j + diff + 1]) / (diff + 1)
                    out.append(out_diff)
                else:
                    out_diff = - math.pow(math.prod(1 + samples[j:j + diff + 1]), 1 / (diff + 1)) + 1
                    out.append(out_diff)
            for j in range(len(samples) - diff + 1, len(samples) + 1):
                out_diff = - math.pow(math.prod(1 + samples[j:j + diff + 1]) * (-2)**(diff - len(samples) - j)), 1 / (diff + 1) + 1
                out.append(out_diff)
        return out