def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("Reading file content:")
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1


    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_file("sample.txt")

