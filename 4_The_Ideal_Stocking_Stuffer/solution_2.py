import sys
import hashlib

file = 'input.txt'

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        answer = get_answer(line)
    print('answer: ', answer)
    input()
        
def get_answer(line):
    found = False
    count = 0
    answer = ""
    while (not found):
        code = line+answer
        result = hashlib.md5(code.encode('utf-8')).hexdigest()
        if (check_zeroes(result)):
            return answer
        count += 1
        answer = str(count)
        if (count % 100000 == 0):
            print("count ", count)
    return answer

def check_zeroes(code):
    if (code[:6] == "000000"):
        return True
    return False

if __name__ == "__main__":
    main()