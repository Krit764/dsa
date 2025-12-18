#include <stdio.h>

int main() {
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    int key;
    int i, low, high, mid, a;

    printf("Array elements are 1 to 10\n");
    printf("Enter element to search: ");
    scanf("%d", &key);

    // Linear Search
    a = 0;
    for(i = 0; i < 10; i++) {
        if(arr[i] == key) {
            printf("Linear Search: Element found at index %d\n", i);
            a = 1;
            break;
        }
    }
    if(!a)
        printf("Linear Search: Element not found\n");

    // Binary Search
    low = 0;
    high = 9;
    a = 0;

    while(low <= high) {
        mid = (low + high) / 2;
        if(arr[mid] == key) {
            printf("Binary Search: Element found at index %d\n", mid);
            a = 1;
            break;
        }
        else if(arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    if(!a)
        printf("Binary Search: Element not found\n");

    return 0;
}
