import java.util.*;
public class NthTermSumOfDigits {

    public static void main(String[] args) {
		Scanner in =new Scanner(System.in);
		int n = in.nextInt();
		in.close();
		int a[]=new int[n+6];
		a[0]=1;a[1]=1;a[2]=2;a[3]=4;a[4]=8;a[5]=16;
		int sum=0;
		for(int i=0;i<5;i++)
		{
		    sum+=a[i];
		}
		for(int i=6;i<n;i++)
		{
		    while(a[i-1]>0)
		    {
		        sum+=a[i-1]%10;
		        a[i-1]/=10;
		    }
		    a[i]=sum;
		}
		System.out.print(a[n-1]);

	}
}
