public class Chapter2List{
    public static void main(String args[])
    {
        int[] test = {1,2,3,4,5};
        display(test);

        shift(test, 7);
        display(test);
    }

    //打印
    public static void display(int[] arr)
    {
        for(int x: arr)
            System.out.print(x + " ");
        System.out.println();
    }

    //顺序表右移k位
    public static void shift(int[] arr, int k)
    {
        int l = arr.length, p = 1, cur, next;

        //找到最大公约数p (如k为数组长度的因数则会陷入死循环)
        for(int i=2; i<k; i++)
        {
            if(k%i==0 && l%i==0)
                p=k;
        }

        for(int i=0; i<p; i++)
        {
            cur = i;
            next = (i+l-k%l);
            int temp = arr[i];
            while(next!=i)
            {
                arr[cur] = arr[next];
                cur = next;
                next = (cur+l-k%l)%l;
            }
            arr[cur] = temp;
        }
    }
}