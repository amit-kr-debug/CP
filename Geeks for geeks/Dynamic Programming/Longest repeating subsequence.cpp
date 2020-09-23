/**
Given a string str, find length of the longest repeating subseequence such that the two subsequence don’t have same
string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in
the original string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first
line of each test case contains an integer N denoting the length of string str.
The second line of each test case contains the string str consisting only of lower case english alphabets.
Output:
Print the length of the longest repeating subsequence for each test case in a new line.


Constraints:
1<= T <=100
1<= N <=1000

Example:
Input:
2
3
abc
5
axxxy

Output:
0
2
**/
#include<bits/stdc++.h>
using namespace std;

int main(){
    int tCases;
    cin >> tCases;
    while(tCases--){
        string x,y;
        int n,m;
        cin >> n;
        cin >> x;
        y = x;
        m = n;
        int dp[n+1][m+1];
        memset(dp, 0, sizeof(dp));
        for(int i=1; i<n+1; i++){
            for(int j=1; j<m+1; j++){
                if(i!=j && x[i-1] == y[j-1])
                        dp[i][j] = 1+dp[i-1][j-1];

                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }

        cout << dp[n][m] <<endl;
    }
return 0;
}


/**
#include<bits/stdc++.h>
using namespace std;

int main(){
    int tCases;
    cin >> tCases;
    while(tCases--){
        string x;
        int n;
        cin >> n;
        cin >> x;
        int dp[n+1][n+1];
        memset(dp, 0, sizeof(dp));
        for(int i=1; i<n+1; i++){
            for(int j=1; j<n+1; j++){
                if(i!=j && x[i-1] == x[j-1])
                        dp[i][j] = 1+dp[i-1][j-1];

                else
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }

        cout << dp[n][n] <<endl;
    }
return 0;
**/
