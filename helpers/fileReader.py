def read_input_as_lines(path):
    with open(path) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def read_input_as_string(path):
    with open(path) as f:
        string = f.read()
    return string