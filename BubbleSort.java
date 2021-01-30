public class BubbleSort
{
    public static void main(String args[])
    {
        int a[] = {5,46,65,33,22,45,65,77,89,32,14};
        bubbleSort(a);
        printArray(a);

    }

    private static void printArray(int[] a)
    {
        for(int num: a)
        {
            System.out.print(num + " ");
        }
    }

    private static void bubbleSort(int[] a)
    {
        boolean swapped;
        for(int i=0; i<a.length-1; i++)
        {
            swapped = false;
            for(int j=0; j<a.length-i-1; j++)
            {
                if(a[j]>a[j+1])
                {
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                    swapped = true;
                }
            }
            if(!swapped)
                break;
        }
    }
}