#include <iostream>
using namespace std;

int main(){
    int n=9;
    int aria = 0;
    int max=0;
    int arr[]={1, 7, 6, 2, 5, 4, 3, 8, 7};

    for (int i=0; i<n-1; i++){
        int k = 0;
        for (int j=0; j<n-1; j++){
            if(arr[i]<=arr[j]){
                aria = arr[i] * k;
                k++;
            }else if(arr[j]<arr[i]){
                aria = arr[j] * k;
                k++;
            }
            if (max<aria){
                max=aria;
            }
        }
        cout <<"Aria[" << i <<"]: " << aria <<endl;
    }

    cout << max << endl;
    return 0;
}