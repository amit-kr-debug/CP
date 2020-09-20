/**
Given a String, find the longest palindromic subsequence

Input:
The first line of input contains an integer T, denoting no of test cases. The only line of each test case consists of a
string S(only lowercase)

Output:
Print the Maximum length possible for palindromic subsequence.

Constraints:
1<=T<=100
1<=|Length of String|<=1000


Examples:
Input:
2
bbabcbcab
abbaab
Output:
7
4
**/

#include <bits/stdc++.h>
using namespace std;

class Solution{


	public:
	int lcs(string str1, string str2)
	{
	    int n = str1.size();
	    int m = str2.size();
	   // cout << n, m;
	    int dp[n+1][m+1];
	    for(int i =0; i <m+1; i++){
	        dp[0][i] = 0;
	    }
	    for(int i =1; i <n+1; i++){
	        dp[i][0] = 0;
	    }

	    for(int i = 1; i <n+1; i++){
	        for(int j = 1; j <m+1; j++){
	            if (str1.at(i-1) == str2.at(j-1)){
	                dp[i][j] = 1+dp[i-1][j-1];
	            }
	            else{
	                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
	                }
	        }
	    }
	    return dp[n][m];

	}
};

int main()
{


   	int t;
    cin >> t;
    while (t--)
    {
        string s1;
        cin >> s1;
        string s2 = string(s1.rbegin(), s1.rend());
	    Solution ob;
	    cout << ob.lcs(s1, s2) << "\n";

    }
    return 0;
}
