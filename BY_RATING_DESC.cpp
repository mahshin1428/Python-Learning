#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int ans=0;
        map<char,int>mp;
        for(int i=0;i<s.size();i++)
        {
            mp[s[i]]++;
            char z=s[i];
            while(s[i]==z)
            {
                i++;
            }
            i--;
            if(mp[z]>1)ans=1;
 
        }
        if(ans==1)cout<<"NO"<<endl;
        else cout<<"YES"<<endl;
    }
}
