/**
Given a string of S as input. Your task is to write a program to remove or delete minimum number of characters from the
string so that the resultant string is palindrome.

Note: The order of characters in the string should be maintained.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows.
First line of each test case contains a string S.

Output:
For each test case, print the deletions required to make the string palindrome.

Constraints:
1<=T<=100
1<=length(S)<=10000

Example:
Input:
2
aebcbda
geeksforgeeks
Output:
2
8
**/

#include <bits/stdc++.h>
using namespace std;

int lcs(string x, string y){
    int i,j;
    int n = x.size();
    int m = y.size();
    int dp[n+1][m+1];
    for(i=0; i<n+1; i++){
        for(j=0; j<m+1; j++){
            if (i==0 || j==0)
                dp[i][j] = 0;
            else if(x.at(i-1) == y.at(j-1))
                dp[i][j] = 1+dp[i-1][j-1];
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[n][m];
}

int main() {
	// your code goes here
	int tCases;
	cin >> tCases;
	while(tCases--){
	    string str1;
	    cin >> str1;
	    string str2 = string(str1.rbegin(), str1.rend());
	    int size = str1.size();
	    cout << size - lcs(str1, str2)<<"\n";
	}
	return 0;
}