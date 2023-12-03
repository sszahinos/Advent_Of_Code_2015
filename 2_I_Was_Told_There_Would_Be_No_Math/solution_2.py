import sys

file = 'input.txt'

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        total += get_total_area(line)
    print('Total: ', total)
    input()
        
def get_total_area(line):
    #l w h
    dim = get_dimensions(line.strip())
    dim = [int(num) for num in dim]

    bow = dim[0] * dim[1] * dim[2]
    print("Before: ", dim)
    dim.remove(max(dim))
    print("After: ", dim)
    print("--")
    ribbon = 0
    for d in dim:
        ribbon += int(d) * 2
    return bow + ribbon

def get_dimensions(line):
    return line.split('x')

if __name__ == "__main__":
    main()