#include<iostream>
using namespace std;

class complex{
    int a;
    int b;
    public:
        void setData(int, int);
        void setDataBySum(complex , complex);
        void print();
};

void complex :: setData(int a1, int a2){
    a = a1;
    b = a2;
}

void complex :: setDataBySum(complex o1, complex o2){
    a = o1.a + o2.a;
    b = o1.b + o2.b;
}

void complex :: print(){
    cout << a << " + " << b << "i" << endl;
}

int main(){
    complex o1, o2, o3;
    o1.setData(1,2);
    o2.setData(2,3);
    o3.setDataBySum(o1, o2);
    o1.print();
    o2.print();
    o3.print();
}