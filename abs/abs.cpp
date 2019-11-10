#include <iostream>
#include <cstdlib>

int SafeReadInt() {
    int x;
    if (!(std::cin >> x)) {
        std::cerr << "Invalid input\n";
        exit(0);
    }

    return x;
}

int main() {
    int x = SafeReadInt();

    std::cout << std::abs(x) << std::endl;

    return 0;
}
