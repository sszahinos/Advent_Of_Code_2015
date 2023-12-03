import sys

file = 'input.txt'

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        upCount = count_occurrences(line, '(')
        downCount = count_occurrences(line, ')')
        print('Floor: ', upCount - downCount)
    input()
        
def count_occurrences(line, symbol):
    total = 0
    for c in line:
        if (c == symbol):
            total += 1
    return total

if __name__ == "__main__":
    main()