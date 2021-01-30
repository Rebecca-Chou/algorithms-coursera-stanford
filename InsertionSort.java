public class InsertionSort 
{
    public static void main(String args[])
    {
        int a[] = {5,2,42,6,1,3,2};
        insertionSort(a);
        printArray(a);
    }    

    private static void insertionSort(int[] a)
    {
        int j;
        for(int i=1;i<a.length;i++)
        {
            j=i;
            while(j>0 && a[j-1]>a[j])
            {
                int temp = a[j];
                a[j] = a[j-1];
                a[j-1] = temp;
                j--;
            }
        }
    }

    private static void printArray(int[] a)
    {
        for(int num: a)
            System.out.print(num + " ");
    }
}