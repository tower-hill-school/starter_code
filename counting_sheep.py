import os, sys, itertools

lines = [line.strip() for line in open(sys.argv[1])][1:]

cases = lines[:]

def process_case(last_number):
    'return the actual last number or the string INSOMNIA'
    print(last_number) # demo code

case_num = 0
for case in cases:
    case_num += 1
    answer = process_case(int(case))
    print(f'Case #{case_num}: {answer}')