public class test {
    public static void main(String[] args) {

        int[] arr = new int[] {2, 4, 9, 8, 5, 7, 2, 3, 3};
        insertionSort(arr);

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i] + " ");
        }

    }

    public static void insertionSort(int[] arr) {
        int size = arr.length;
        for (int i = 1; i < size; i++) {
            int num = arr[i];

//            for (int j = i - 1; j >= 0; j--) {
//                if (arr[j] < num) {
//                    arr[j + 1] = num;
//                    break;
//                }
//                arr[j+1] = arr[j];
//            }

            int j = i - 1;
            while (j >= 0 && arr[j] > num) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = num;
        }
    }
}
