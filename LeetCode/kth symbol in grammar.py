class Solution:
    def kthGrammar(self, N: int, K: int):
        if N == 1:
            return 0
        mid = 2 ** (N - 2)
        if K <= mid:
            return self.kthGrammar(N - 1, K)
        else:
            a = self.kthGrammar(N - 1, K - mid)
            if a == 0:
                return 1
            else:
                return 0
