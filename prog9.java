import java.io.*;
import java.util.*;
import java.lang.*;

class bank
{
    void interest(int pi,float ra,int ti)
    {
        double ci=pi*(Math.pow(1+(ra/100),ti));
        double amtrec=ci+pi;
        System.out.println("compound interest is"+ci+"amount received "+amtrec);
    }
}
class prog9
{
    public static void main(String v[])
    {
        int p=5000;
        float rate=6.5f;
        int t=5;

        bank obj=new bank();

        obj.interest(p,rate,t);


    }
}