import os, sys, itertools

lines = [line.strip() for line in open(sys.argv[1])][1:]

def process_case(stacks_of_pancakes):
    'return the number of flips'
    print(stacks_of_pancakes) # demo code

# reverse the lines to make it quicker to pop them
lines.reverse()
case_num = 0
while lines:
    case_num += 1
    pancakes = map(int(lines.pop().split(' ')))
    # not really needed but here if you want it
    number_of_diners = int(lines.pop()) 
    print(number_of_diners) # demo code
    print(pancakes) # demo code
    answer = process_case(pancakes)
    print(f'Case #{case_num}: {answer}')