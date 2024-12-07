from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = datetime.now()
    for item in filenames:
        read_info(item)
    print(datetime.now() - start_time, '(линейный)')

    # Многопроцессный
    start_time = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time, '(многопроцессный)')

