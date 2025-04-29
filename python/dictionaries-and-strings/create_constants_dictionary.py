def parse_constants_file(filename):
    constants = {}
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines[2:]:
        line = line.strip()
        if not line:
            continue
        try:
            name, value_str, dimension = line.rsplit(None, 2)  # Properly split
            value = float(value_str)
            constants[name.lower()] = value
        except ValueError:
            continue

    return constants


if __name__ == '__main__':
    import os
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'constants.txt')
    constants_dict = parse_constants_file(file_path)

    for name, value in constants_dict.items():
        print(f"{name}: {value}")