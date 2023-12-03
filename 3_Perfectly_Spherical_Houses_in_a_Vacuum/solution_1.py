import sys

file = 'input.txt'
visitedHouses = {(0,0)}
currentPosition = [0,0]

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        move_santa(line)
    print('Total: ', len(visitedHouses))
    input()
        
def move_santa(line):
    for movement in line:
        if (movement == '^'):
            move_up()
        elif (movement == 'v'):
            move_down()
        elif (movement == '>'):
            move_right()
        else:
            move_left()
        print("Current pos: ", tuple(currentPosition))
        visitedHouses.add(tuple(currentPosition))

def move_up():
    currentPosition[1] += 1

def move_down():
    currentPosition[1] -= 1

def move_right():
    currentPosition[0] += 1

def move_left():
    currentPosition[0] -= 1

if __name__ == "__main__":
    main()