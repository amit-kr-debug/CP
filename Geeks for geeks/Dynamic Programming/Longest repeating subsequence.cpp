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