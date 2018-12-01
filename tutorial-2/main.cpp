#include <iostream>
#include "square.hpp"
using namespace std;

int main() {
    Square sq(4);
    cout << "Area: " << sq.area() << endl;
    return 0;
}