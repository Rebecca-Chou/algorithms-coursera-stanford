public class SelectionSort 
{
    public static void main(String args[])
    {
        int a[] = {64,25,12,22,11};
        selectionSort(a);
        printArray(a);
    }

    private static void selectionSort(int[] a)
    {
        for(int i=0;i<a.length-1;i++)
        {
            int min_idx = i;
            for(int j=i+1;j<a.length;j++)
            {
                if(a[j]<a[min_idx])
                    min_idx = j;
            }
            int temp = a[i];
            a[i] = a[min_idx];
            a[min_idx] = temp;
        }
    }

    private static void printArray(int[] a)
    {
        for(int num: a)
            System.out.print(num + " ");
    }
}