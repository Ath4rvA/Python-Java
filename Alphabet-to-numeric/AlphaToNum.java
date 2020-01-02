
public class AlphaToNum {

	public String alphaToNum(String s)
	{
		s= s.toLowerCase();
		String result="";
		char[] alphas= s.toCharArray();
		for (char c : alphas) {
			int temp= (int)c;
			if(temp >=97 && temp<=122)
			{
				temp= temp-96;
				result=result.concat(Integer.toString(temp));
				result=result.concat(" ");
			}
		}
		return result;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new AlphaToNum().alphaToNum("The sunset sets at twelve o' clock."));
	}

}
