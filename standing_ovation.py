import os, sys, itertools

lines = [line.strip() for line in open(sys.argv[1])][1:]

cases = lines[:]

def process_case(this_case):
    'Find the answer and return it'
    parts = this_case.split(' ')
    max_shyness = int(parts[0]) 
    persons = map(int, list(parts[1]))
    for shyness, person in enumerate(persons):
        print(shyness) # this is demo code
        print(person) # this is demo code


case_num = 0
for case in cases:
    case_num += 1
    answer = process_case(case)
    print(f'Case #{case_num}: {answer}')