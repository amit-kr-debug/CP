def toh(n, source, aux, des):
    if n == 1:
        string = f"Move {n} form {source} to {des}"
        print(string)
        return
    toh(n-1, source, des, aux)
    string = f"Move {n} form {source} to {des}"
    print(string)
    toh(n-1, aux, source, des)


toh(10, "A", "B", "C")