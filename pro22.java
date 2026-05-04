import java.io.*;
import java.util.*;
import java.lang.*;

class Rangeexception extends Exception
{
	Rangeexception(String str)
	{
	super(str);
	}
}

class pro2
{
	public static void main(String args[])
	{
		try
		{
			int m1,m2,m3;
			m1=Integer.parseInt(args[0]);
			m2=Integer.parseInt(args[1]);
			m3=Integer.parseInt(args[2]);
			
			if((m1>0 && m1<=100)&&(m2>0 && m2<=100)&&(m3>0 && m3<=100))
			{
				if(m1>=40 && m2>=40 && m3>=40)
				{
					System.out.println("percentage is "+(((m1+m2+m3)*100)/300));
				}
				else
				{
					System.out.println("fail");
				}
				
			}
			else
				{
				throw new Rangeexception("it is invaild");
				}
		}
		catch(Rangeexception r)
		{
		System.out.println(r);
		}
		catch(Exception e)
		{
		System.out.println(e);
		}
	
	}
}
