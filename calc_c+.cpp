#include <iostream>
#include <cmath>
#include <conio.h>

using namespace std;

void showMenu()
{
    cout << "********************************************" << endl;
    cout << "***          Scientific Calculator        ***" << endl;
    cout << "***                                      ***" << endl;
    cout << "***            [1] Addition               ***" << endl;
    cout << "***            [2] Subtraction            ***" << endl;
    cout << "***            [3] Multiplication         ***" << endl;
    cout << "***            [4] Division               ***" << endl;
    cout << "***            [5] Exponential            ***" << endl;
    cout << "***            [6] Logarithm Base 10      ***" << endl;
    cout << "***            [7] Natural Logarithm      ***" << endl;
    cout << "***            [8] Square Root            ***" << endl;
    cout << "***            [9] Exit                   ***" << endl;
    cout << "********************************************" << endl;
    cout << "Enter your choice (1-9): ";
}

int main()
{
    int choice;
    float num1, num2;

    while (1)
    {
        showMenu();
        cin >> choice;

        if (choice == 9)
            break;

        cout << "Enter first number: ";
        cin >> num1;

        if (choice != 8 && choice != 7)
        {
            cout << "Enter second number: ";
            cin >> num2;
        }

        switch (choice)
        {
        case 1:
            cout << num1 << " + " << num2 << " = " << num1 + num2 << endl;
            break;
        case 2:
            cout << num1 << " - " << num2 << " = " << num1 - num2 << endl;
            break;
        case 3:
            cout << num1 << " * " << num2 << " = " << num1 * num2 << endl;
            break;
        case 4:
            if (num2 == 0)
            {
                cout << "Error: Division by zero" << endl;
            }
            else
            {
                cout << num1 << " / " << num2 << " = " << num1 / num2 << endl;
            }
            break;
        case 5:
            cout << num1 << "^" << num2 << " = " << pow(num1, num2) << endl;
            break;
        case 6:
            cout << "log(" << num1 << ") = " << log10(num1) << endl;
            break;
        case 7:
            cout << "ln(" << num1 << ") = " << log(num1) << endl;
            break;
        case 8:
            cout << "sqrt(" << num1 << ") = " << sqrt(num1) << endl;
            break;
        default:
            cout << "Invalid choice" << endl;
        }

        cout << "Press any key to continue..." << endl;
        getch();
    }

    return 0;
}
