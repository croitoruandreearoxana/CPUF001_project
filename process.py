import os

def read_input(file_path):
    if not os.path.exists(file_path):
        print("Input file not found.")
        exit(1)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Validate and convert to integers
    data = []
    for line in lines:
        line = line.strip()
        if line.isdigit():
            data.append(int(line))
        else:
            print(f"Invalid data found: {line}. Skipping.")
    if len(data) < 3:
        print("Not enough valid data in the file.")
        exit(1)
    return data

def write_output(file_path, result_dict):
    with open(file_path, 'w') as file:
        for key, value in result_dict.items():
            file.write(f"{key}: {value}\n")
