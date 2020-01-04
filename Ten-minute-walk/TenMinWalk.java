
public class TenMinWalk {
	
	public boolean walk(char[] arr)
	{
		if (arr.length != 10)
			return false;
			
		int counter=0;
		for (char c : arr) {
			if(c=='n')
				counter+=1;
			else if(c=='s')
				counter-=1;
			else if(c=='w')
				counter+=2;
			else if (c=='e')
				counter+=-2;
		}
		if(counter==0)
			return true;
				
		
		return false;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[] test= {'n','s','n','s','w','e','w','e','s','n'};
		System.out.println(new TenMinWalk().walk(test));
	}

}
