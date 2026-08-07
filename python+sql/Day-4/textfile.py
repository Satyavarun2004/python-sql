import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"\nExecution Time: {end - start:.6f} seconds")

        return result

    return wrapper


def read_file(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line


@execution_time
def analyze_file(file_name):
    try:
        lines = [line.strip() for line in read_file(file_name)]

        words = [word for line in lines for word in line.split()]

        print("File Analysis")
        print("Line Count :", len(lines))
        print("Word Count :", len(words))

    except FileNotFoundError:
        print("Error: File not found.")


file_name = input("Enter file name: ")
analyze_file(file_name)