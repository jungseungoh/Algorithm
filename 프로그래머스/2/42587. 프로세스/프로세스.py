# 숫자가 클수록 우선순위가 높음
from collections import deque
def solution(priorities, location):
    q = deque([(i,p) for i,p in enumerate(priorities)])
    cnt=0
    
    while q:
        cur = q.popleft()
        if any(cur[1] < x[1] for x in q): # 우선순위가 더 높은 프로세스가 있으면 다시 넣는다.
            q.append(cur)
        else:
            cnt+=1
            if cur[0]==location:
                return cnt