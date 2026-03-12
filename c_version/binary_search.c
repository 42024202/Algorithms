#include <stdio.h>

int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8};

void binary_search(int *arr, int target, int size)
{
    int low, high, mid, guess;
    high = size - 1;
    low = 0;

    while (low <= high)
    {
        mid = (low + high) / 2;
        guess = arr[mid];
        if (guess == target)
        {
            printf("Your number is %d", guess);
            break;
        }
        else if (guess > target)
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
}

int main()
{
    binary_search(numbers, 2, 8);
}

