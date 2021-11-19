// Program For PDA Which Accpets Strings Of (a^n)(b^2n)\n
// By - Mayank Singh

#include<bits/stdc++.h>
using namespace std;

int top;
char s[10];
class Stack
{
    public:
    void push(int x)
    {
        s[top++]=x;
    }
    void pop(int x)
    {
        s[top--]=x;
    }
};

int main()
{
    int i,n;
    char a[10];
    cout<<"\t\tProgram For PDA Which Accpets Strings Of (a^n)(b^2n)\n";
    cout<<"\t\tEnter String : ";
    cin>>a;
    n=strlen(a);
    Stack st;
    top=-1;
    for(i=0;i<n;i++) 
    {
        if(a[i]=='a' || a[i]=='b')
        {
            if(a[i]=='a')
            {
                st.push(a[i]);
                st.push(a[i]);
            }
            else
            {
                st.pop(a[i]);
            }    
        }
        else
            break;    
        }    
    }
    if(top==-1)
    {
        cout<<"\nString Accepted.\n";
    }
    else
    {
        cout<<"\nString Rejected.\n";
    }    
    return 0;
}
