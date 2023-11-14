from csv import reader, writer
from tqdm import tqdm


# given a series of values, will scale and normalize all values on a range of 0 to 1
def normalize(line_data):
    line_max = max(line_data)
    line_min = min(line_data)

    processed_line = list(map(lambda x: (x - line_min) / (line_max - line_min), line_data))

    return processed_line


def process(line_data: list) -> list:
    line_data = list(map(float, line_data))
    # scales all the trapezoidal sums, is until [:-1] in order to avoid the actual data
    normalized_trap_sum = normalize(line_data[:-1])

    # gives the percent change from the actual value to the last value,
    # not sure if this works
    percent_change = (line_data[-1] - line_data[-2]) / line_data[-2]

    return normalized_trap_sum + [percent_change]


def make_increase():
    pass


def is_increasing(line_data):
    return line_data[0] < line_data[-1]


with open("output.csv", "r", newline="") as file, open("processed_output.csv", "w+", newline="") as new_file:
    file_reader = reader(file)
    file_writer = writer(new_file)

    fields = ['function name', 'start', 'end', 'p_increment1', 'p_increment2', 'p_increment4',
               'p_increment8', 'p_increment16', 'p_increment32', 'p_increment 4', 'percent_change']

    # first, we'll try to make generalizations about data, but only if it is increasing
    processed_data = list(filter(lambda x: is_increasing(list(map(float, x[3:-1]))), list(file_reader)[1:]))

    file_writer.writerow(fields)

    for data in tqdm(processed_data, desc="Processing Data..."):
        file_writer.writerow(data[:3] + process(data[3:]))
