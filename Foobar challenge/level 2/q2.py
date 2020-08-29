# 2nd level 2nd question the bunny prisoner
def solution(x, y):
    aux = x + y - 1
    return (aux * (aux-1)) // 2 + x