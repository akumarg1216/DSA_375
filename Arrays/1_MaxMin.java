

/**
 * MaxMin
 */
public class MaxMin {

    static class Pair{
        int min, max;
    }

    static Pair getMinMax(int arr[], int n){
        Pair minmax = new Pair();
        int i;

        if(n==1){
            minmax.max = arr[0];
            minmax.min = arr[0];
            return minmax;
        }

        if(arr[0]>arr[1]){
            minmax.max = arr[0];
            minmax.min = arr[1];
        } else {
            minmax.max = arr[1];
            minmax.min = arr[0];
        }

        for (i = 2; i < arr.length; i++) {
            if (arr[i]>minmax.max){
                minmax.max = arr[i];
            }
            else if(arr[i] < minmax.min){
                minmax.min = arr[i];
            }
        }

        return minmax;
    }

    public static void main(String[] args) {
        int arr[] = {1000,3000,99,80000,12,6};
        int arr_size = arr.length;
        Pair minmax = getMinMax(arr,arr_size);
        System.out.printf("Maximum: %d",minmax.max);
        System.out.printf("\nMinimum: %d",minmax.min);
    }
}