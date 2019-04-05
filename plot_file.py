import sys
import re

import matplotlib.pyplot as plt
import numpy as np


alg_map = {
    '1': 'Wave',
    '2': 'Random',
    '3': 'Simple next',
    '4': 'Smallest list',
    '5': 'Smallest heap',
    '6': 'Minimum branch',
}


def to_float(some_string):
    try:  # convert string into a number
        x = float(some_string)
        return x
    except ValueError as err_:
        print("Cannot convert {}".format(some_string))
        exit(err_)


def get_name(in_file):
    return in_file.split('__')[0]


def get_id(in_file):
    return in_file.split('__')[-1][0]  # [0] is name of test file, [-1] is '<id>.txt', [-1][0] is '<id>'


def filter(in_file):
    x_full = []  # vertices or rozmiar problemu
    y_full = []  # time of executing or zlozonosc czasowa
    count = 0
    
    with open(in_file, "r") as f:
        text = f.read()
        text = text.split('\n')
        for line in text:  # Search for a specific line
            if re.search("number of vertices", line):  
                item = line.split()[-1]  # it is the last item in line
                x = to_float(item)
                x_full.append(x)
            elif re.search("execution time", line):
                item = line.split()[-2]  # last item is 'sec', but we need a number
                y = to_float(item)
                y_full.append(y)
                count += 1

    if (len(x_full) != len(y_full)) or (len(x_full) != count):
        raise Exception(
                "Some log has no line with vertices or time with ececution"
            )
    else:
        measurement = {
            'x': x_full,
            'y': y_full,
            'id': get_id(in_file),
            'name': get_name(in_file),
        }
        return measurement


def sort_relative(data):
    """Sort dictionary of 2 relative lists named 'x' and 'y' using numpy.
    Param 'x' is key.
    """
    order = np.argsort(data['x'])
    data['x'] = np.array(data['x'])[order]
    data['y'] = np.array(data['y'])[order]


def save_plot(title, legend_list):
    plt.legend(legend_list, loc='upper left')
    plt.title("Complexity for {}".format(title))
    plt.xlabel("Size of a problem in vertices, {N}")
    plt.ylabel("Time to be executed, {sec}")
    out_file = title + ".pdf"
    plt.savefig(out_file)
    plt.close()


if __name__ == "__main__":  # in terminal:
                            # python3 plot_file.py <name>__alg*.txt
    results = []
    for file_name in sys.argv[1:]:
        try:
            measurement = filter(file_name)
            results.append(measurement)
            print("Successfully filtered {}".format(file_name))
        except Exception as err:
            print("Something went wrong")
            exit(err)

    separated_results = {}
    # Key is 'file name'. If 2 files or more with the same name, they would be held together.
    for measurement in results:
        key = measurement['name']
        if key in separated_results:
            separated_results[key].append(measurement)
        else:
            separated_results[key] = [measurement, ]

    for key in separated_results:
        # For each file name create separate .pdf file
        legend = []
        for measurement in separated_results[key]:
            sort_relative(measurement)
            plt.plot(
                measurement['x'],
                measurement['y'],
                linewidth=0.4,
            )
            alg_id = measurement['id']
            label = 'Alg ' + alg_map[alg_id]
            legend.append(label)
        save_plot(
            title=key,
            legend_list=legend,
        )
        print("Exported {}".format(key))
