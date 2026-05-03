import java.io.*;
import java.util.*;
import java.lang.*;

class season
{
    int disc;
    void calcost(int sv)
    {
        if(sv<1000)
        {
            disc=10;
        }
        else if(sv>=1000 && sv<=1500)
        {
            disc=12;
        }
        else
        {
            disc=15;
        }

        double tot=sv-(sv*disc)/100;
        System.out.println("total value to pay:"+tot);
    }
}
class prog8
{
    public static void main(String v[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the purchase price of product:");
        int price=sc.nextInt();

        season obj=new season();
        obj.calcost(price);
    }
}