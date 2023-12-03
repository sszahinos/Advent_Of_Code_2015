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

    lwArea = (2 * int(dim[0]) * int(dim[1]))
    whArea = (2 * int(dim[1]) * int(dim[2]))
    hlArea = (2 * int(dim[2]) * int(dim[0]))

    totalArea = lwArea + whArea + hlArea
    minArea = min(int(lwArea/2), int(whArea/2), int(hlArea/2))
    totalArea += minArea

    return totalArea

def get_dimensions(line):
    return line.split('x')

if __name__ == "__main__":
    main()