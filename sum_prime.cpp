#include <iostream>
using namespace std;

int main() {
int max;
cout<< ".........Enter the maximun number........"<< endl;
cin>> max;
int sum = 0;
bool prime = true;
for (int j=1 ; j<max; j++){
    for (int i=2; i<j; i++) {
        if (j%i == 0){
            prime = false;
        }
    }
    if (prime){
        sum += j;
    }else {
        prime = true;
        continue;
    }
}
cout<<sum;
return 0;
}
