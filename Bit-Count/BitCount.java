
public class BitCount {

	public int count(int n)
	{
		String res="";
		int[] remainder= new int[1000];
		int cnt=0;
		while (n!= 0)
		{
			remainder[cnt]= n%2;
			n= n/2;
			cnt+=1;
		}
		int ones=0;
		for (int i : remainder) {
			res= res.concat(Integer.toString(i));
		}
		for (int i = 0; i < res.length(); i++) {
			if(res.charAt(i)=='1')
			{
				ones+=1;
			}
		}
		return ones;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//BitCount bc= new BitCount();
		int answer= new BitCount().count(213151231);
		System.out.println("Answer: "+answer);
	}

}
