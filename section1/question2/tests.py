from solution import solution

test_cases = {
'''3 3 A
A 1
B 2
C 3
A->B
B->C
A->C''': 'A->B->C 6',
'''3 3 A
A 2
B 8
C 5
A->B
A->C
C->B''': 'A->C->B 15',
'''4 4 A
A 1
B 2
C 3
D 8
A->B
B->C
A->D
B->D''': 'A->B->D 11',
'''1 0 A
A 0''': 'A 0',
'''6 7 A
A 1
B -1
C -2
D 5
E 9
F 7
A->B
A->C
B->D
C->D
D->E
D->F
A->D''': 'A->D->E 15'
}

for case, ans in test_cases.items():
    result = solution(case)
    assert result == ans, print(result, ans)
