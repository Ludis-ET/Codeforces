testcase = int(input())
for _ in range(testcase):
    ballons, contest = 0, set()
    count = int(input())
    string = str(input())
    for a in string:
        ballons += 1 if a in contest else 2
        contest.add(a)
    print(ballons)