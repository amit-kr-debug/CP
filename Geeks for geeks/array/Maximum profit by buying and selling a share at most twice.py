"""
In a daily share trading, a buyer buys shares in the morning and sells it on the same day. If the trader is allowed to
make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete
(Sell->buy->sell->buy). Given stock prices throughout the day, find out the maximum profit that a share trader could
have made.

Input:   price[] = {10, 22, 5, 75, 65, 80}
Output:  87
Trader earns 87 as sum of 12 and 75
Buy at price 10, sell at 22, buy at 5 and sell at 80

Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
Output:  100
Trader earns 100 as sum of 28 and 72
Buy at price 2, sell at 30, buy at 8 and sell at 80

Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
Output:  72
Buy at price 8 and sell at 80.

Input:   price[] = {90, 80, 70, 60, 50}
Output:  0
Not possible to earn.
"""
import sys

price = list(map(int, input().split()))
fb, sb = -sys.maxsize, -sys.maxsize
fs, ss = 0, 0
for i in range(len(price)):
    fb = max(fb, -price[i])
    fs = max(fs, fb+price[i])
    sb = max(sb, fs-price[i])
    ss = max(ss, sb+price[i])
print(ss)