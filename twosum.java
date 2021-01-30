import java.io.*;
import java.util.Scanner;
import java.util.HashSet;
import java.io.File;

public class twosum{
    public static void main(String args[]){
        //read file and store values to array and hashmap
        try{
            int num = 1000000;
            File file = new File("algo1-programming_prob-2sum.txt");
            Scanner k = new Scanner(file);
            HashSet<Long> map = new HashSet<>();
            long a[] = new long[num];
            int i = 0;
            while(k.hasNext()){
                long temp = k.nextLong();
                map.add(temp);
                a[i++] = temp;
            }
            k.close();
            //calculate
            
            int num_target = 0;
            for(int t = -10000; t<=10000; t++){
                for (int j = 0; j < num; j++){
                    long y = t - a[j];
                    if (map.contains(y) && y!=a[j]){
                        num_target++;
                        break;
                    } 
                }
            }
            System.out.println(num_target);
        }catch(FileNotFoundException e){
            System.out.print("Error");
        }

        
    }
}
