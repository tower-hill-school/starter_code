import os, sys, itertools

lines = [line.strip() for line in open(sys.argv[1])][1:]

cases = lines[:]

def process_case(phrase):
    'translate case and return it'
    print(phrase) # demo code


case_num = 0
for case in cases:
    case_num += 1
    answer = process_case(case)
    print(f'Case #{case_num}: {answer}')