import sys

file = 'input.txt'

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        position = get_position(line)
        print('Position: ', position)
    input()
        
def get_position(line):
    total = 0
    for index, c in enumerate(line):
        if (c == '('):
            total += 1
        elif (c == ')'):
            total += -1
        if (total == -1):
            return index + 1
    return -1

if __name__ == "__main__":
    main()