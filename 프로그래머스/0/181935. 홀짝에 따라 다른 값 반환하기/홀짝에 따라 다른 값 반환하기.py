def solution(n):
    answer = 0
    if n%2 == 1:
        answer = ((1+n)/2)**2
    else:
        while n > 0:
            answer += n**2
            n -= 2
    return answer