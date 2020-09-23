#include <bits/stdc++.h>
using namespace std;
string scs(string x, string y){
    int n = x.size();
    int m = y.size();
    int dp[n+1][m+1];
    string s;

    memset(dp,0,sizeof(dp));

    for(int i = 1; i<n+1; i++){
        for (int j =1; j<m+1; j++){
            if(x[i-1] ==y[j-1])
                dp[i][j] = 1+dp[i-1][j-1];
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }

    cout << dp[n][m] << endl;
    int i = n, j = m;
    while(i>0 && j>0){
        cout << i <<" "<< j << endl;
        if(x[i-1] == y[j-1]){
            s += x[i-1];
            i--;
            j--;
        }
        else{

            if(dp[i-1][j]>dp[i][j-1]){
                s += x[i-1];
                i--;
            }
            else{
                s += y[j-1];
                j--;
            }
        }
    }
    while(i>0){
        s += x[i-1];
        i--;
    }
    while(j>0){
        s += y[j-1];
        j--;
    }
    return string(s.rbegin(), s.rend());
}
int main() {
    int tCases;
    cin >> tCases;
    while(tCases--){
        string x, y;
        cin >> x;
        cin >> y;
        cout << scs(x,y) << endl;
    }
}
