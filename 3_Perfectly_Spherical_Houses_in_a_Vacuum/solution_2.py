import sys

file = 'input.txt'
visitedHouses = {(0,0)}
santaCurrentPosition = [0,0]
botCurrentPosition = [0,0]

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
    for index, movement in enumerate(line):
        if (index % 2 == 0):
            npcPosition = santaCurrentPosition
        else:
            npcPosition = botCurrentPosition

        if (movement == '^'):
            move_up(npcPosition)
        elif (movement == 'v'):
            move_down(npcPosition)
        elif (movement == '>'):
            move_right(npcPosition)
        else:
            move_left(npcPosition)
        
        visitedHouses.add(tuple(npcPosition))

def move_up(npcPosition):
    npcPosition[1] += 1

def move_down(npcPosition):
    npcPosition[1] -= 1

def move_right(npcPosition):
    npcPosition[0] += 1

def move_left(npcPosition):
    npcPosition[0] -= 1

if __name__ == "__main__":
    main()