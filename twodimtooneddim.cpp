// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int r,c;
    cin>>r>>c;
    vector<vector<int>> twodim(r,vector<int>(c));
    int p;
    p=r*c;
    vector<int> onedim(p);
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
           cin>>twodim[i][j];
        }
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
           cout<<twodim[i][j]<<" ";
        }
        cout<<"\n";
    }
    
    int k=0;
        for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
          
           onedim[k]=twodim[i][j];
           k+=1;
        }
    }

    for(int k=0;k<p;k++){
        cout<<onedim[k]<<" ";
    }
    

    return 0;
}
