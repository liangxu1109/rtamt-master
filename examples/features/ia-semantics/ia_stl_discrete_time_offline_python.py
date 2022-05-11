import sys
import rtamt


def monitor():
    # data

    dataSet = {
        'time': [0, 1, 2, 3, 4, 5],
        'x': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
        'y': [0.2, 0.0, 0.6, 0.7, 0.9, 0.6],
        'z': [0.3, 0.2, 0.5, 0.3, 0.8, 0.7],
        'a': [0.2, 0.4, 0.6, 0.8, 0.9, 1.0],
        'b': [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
    }

    # # AGM ROBUSTNESS
    spec = rtamt.STLSpecification(language=rtamt.Language.PYTHON, semantics=rtamt.Semantics.STANDARD, robustness_type = rtamt.RobustnessMetrics.Standard.__str__())
    spec.name = 'IA-STL discrete-time online Python monitor with STANDARD semantics'
    spec.declare_var('x', 'float')
    spec.declare_var('y', 'float')
    spec.declare_var('z', 'float')
    spec.declare_var('a','float')
    spec.declare_var('b', 'float')
    spec.set_var_io_type('x', 'input')
    spec.set_var_io_type('y', 'output')
    spec.set_var_io_type('z', 'output')
    spec.set_var_io_type('a', 'output')
    spec.set_var_io_type('b', 'output')
    spec.spec = '(x>=0.25 and y>=0.35 and z>=0.45) or (eventually[0:2](a > 0.55) and (b > 0.65))'
    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(dataSet)
    print(rtamt.RobustnessMetrics.AGM.__str__()+' robustness: ' + str(rob))

    # # Traditional ROBUSTNESS
    spec = rtamt.STLSpecification(language=rtamt.Language.PYTHON, semantics=rtamt.Semantics.STANDARD,
                                  robustness_type=rtamt.RobustnessMetrics.Standard.__str__())
    spec.name = 'IA-STL discrete-time online Python monitor with STANDARD semantics'
    spec.declare_var('x', 'float')
    spec.declare_var('y', 'float')
    spec.declare_var('z', 'float')
    spec.set_var_io_type('x', 'input')
    spec.set_var_io_type('y', 'output')
    spec.set_var_io_type('z', 'output')
    spec.spec = 'x>=0.25 and y>=0.35 and z>=0.45'
    try:
        spec.parse()
    except rtamt.STLParseException as err:
        print('STL Parse Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(dataSet)
    print(rtamt.RobustnessMetrics.Standard.__str__() + ' robustness: ' + str(rob))



if __name__ == '__main__':
    # Process arguments

    monitor()
