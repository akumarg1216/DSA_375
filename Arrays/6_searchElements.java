public class searchElements {
    static int search(int[] arr, int l, int h, int key){
        if(l>h){
            return -1;
        }

        int mid = (l+h)/2;
        if(arr[mid] == key){
            return mid;
        }
        if(arr[1]<=arr[mid]){
            if (key>arr[1] && key<=arr[mid]){
                return search(arr, 1, mid-1, key);
            }
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i] + " ");
        }
        System.out.println("============================================");
        return search(arr, mid+1, h, key);
    }
    
    public static void main(String[] args) {
        int arr[] = {4,5, 6, 7, 8, 9, 1, 2, 3};
        int key = 90;
        int i = search(arr, 0, arr.length-1, key);
        if(i!=-1)
            System.out.println("Index: "+i);
        else
            System.out.println("Key not found");
    }
}
