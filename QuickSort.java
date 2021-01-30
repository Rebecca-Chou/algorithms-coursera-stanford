import java.util.Random;

public class QuickSort 
{
    public static void main(String args[])
    {
        int a[] = {10,54,63,6,420,11,41};

        quickSort(a,0,a.length);
        printArray(a);
    }

    private static void quickSort(int[] a, int left, int right)
    {
        int l = left;
        int r = right - 1;
        int size = right -left;

        if(size > 1)
        {
            Random rand = new Random();
            int p = a[rand.nextInt(size)+l];

            while(l<r)
            {
                while(a[l]<p && l<r)
                    l++;
                while(a[r]>p && l<r)
                    r--;
                if(l<r)
                {
                    int temp = a[l];
                    a[l] = a[r];
                    a[r] = temp;
                    l++;
                }
            }
            quickSort(a,left,l);
            quickSort(a,r,right);
        }
    }

    private static void printArray(int[] a)
    {
        for(int num: a)
            System.out.print(num + " ");
    }
}