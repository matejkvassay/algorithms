#include <stdio.h>

void insert_sort(int array[], int size){
    int i, j, key;
    for (i=1; i<size; i++){
        key = array[i];
        j = i-1;
        while (j>=0 && array[j]>key){
            array[j+1] = array[j];
            j = j-1;
        }
        array[j+1] = key;
    }
}

void print_array(int array[], int size){
    int i;
    for (i=0; i < size; i++){
        if (i == size - 1){
            printf("%d\n", array[i]);
        }
        else{
            printf("%d, ", array[i]);
        }
    }
}

int main(){
    int array[] = {7,2,5,14,3,8,1,4};
    int size = sizeof(array) / sizeof(array[0]);
    printf("Input array:\n");
    print_array(array, size);
    insert_sort(array, size);
    printf("Sorted array:\n");
    print_array(array, size);
    return 0;
}