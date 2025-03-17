// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int r,c;
    cin>>r>>c;
    vector<vector<int>> m(r,vector<int>(c));
    vector<int> rowval(r,0);
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
        cin>>m[i][j];
    }
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<m[i][j]<<" ";
    }cout<<"\n";
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
        if(m[i][j]==1){
            rowval[i]++;
        }
    }
    }
    int maxval=0;
    for(int i=0;i<r;i++){
        if(rowval[i]>maxval){
            maxval=rowval[i];
        }
    }
    cout<<maxval;

    return 0;
}
