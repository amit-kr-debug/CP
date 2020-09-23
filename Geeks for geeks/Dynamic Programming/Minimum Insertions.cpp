/**
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is S.

Output:

Print the minimum number of characters.

Constraints:

1 ≤ T ≤ 50
1 ≤ S ≤ 40

Example:

Input:
3
abcd
aba
geeks

Output:
3
0
3
**/

#include<bits/stdc++.h>
using namespace std;
int main(){
    int tCases;
    cin >> tCases;
    while(tCases--){
        string x;
        cin >> x;
        string y = string(x.rbegin(), x.rend());
        int n = x.size();
        int m = n;
        int dp[n+1][m+1];
        memset(dp, 0, sizeof(dp));
        for(int i = 1; i <n+1; i++){
            for(int j = 1; j<m+1; j++){
                if(x[i-1] == y[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        cout << n - dp[n][m]<<"\n";
    }
    return 0;
}
