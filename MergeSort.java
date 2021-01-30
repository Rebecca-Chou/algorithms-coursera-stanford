public class MergeSort 
{
    public static void main(String args[])
    {
        int a[] = {10,54,63,6,420};

        int n = mergeSort(a, 0, a.length-1);
        printArray(a);
        System.out.print("\n"+n);
    }

    private static int mergeSort(int[] a, int l, int r)
    {
        if(l<r)
        {
            int m = (l+r)/2;
            int x = mergeSort(a, l, m);
            int y = mergeSort(a, m+1, r);
            int z = merge(a,l,m,r);
            return x + y + z;
        }
        return 0;
    }

    private static int merge(int a[], int l, int m, int r)
    {
        int n1 = m-l+1;
        int n2 = r-m;
        int inversion = 0;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for(int i=0;i<n1;i++)
            L[i] = a[l+i];
        for(int j=0;j<n2;j++)
            R[j] = a[m+1+j];
        
        int i=0,j=0;
        int k=l;
        while(i<n1 && j<n2)
        {
            if(L[i]<=R[j])
            {
                a[k] = L[i];
                i++;
                k++;
            }
            else
            {
                a[k] = R[j];
                j++;
                k++;
                inversion += n1-i;
            }
        }
        while(i<n1)
        {
            a[k] = L[i];
            i++;
            k++;
        }
        while(j<n2)
        {
            a[k] = R[j];
            j++;
            k++;
        }
        return inversion;
    }

    private static void printArray(int[] a)
    {
        for(int num: a)
            System.out.print(num + " ");
    }
}