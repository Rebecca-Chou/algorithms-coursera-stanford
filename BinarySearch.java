public class BinarySearch 
{
    public static void main(String args[])
    {
        int a[] = {3,4,23,42,77,100};
        int x = 42;

        int result = binarySearch(a,0,a.length-1,x);
        if(result!=-1)
            System.out.print(x + " is in position " + result);
        else
            System.out.print(x + " is not found.");
    }

    private static int binarySearch(int a[], int l, int r, int x)
    {
        int mid = (l+r)/2;
        if(a[mid]==x)
            return mid;
        else if(a[mid]>x)
            return binarySearch(a,l,mid-1,x);
        else if(a[mid]<x)
            return binarySearch(a,mid+1,r,x);
        else
            return -1;
    }
}