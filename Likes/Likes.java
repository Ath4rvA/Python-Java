

/*
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
 */
public class Likes {

	public String likes(String[] arr)
	{
		String result="";
		if (arr.length==0)
			return "no one likes this";
		else if (arr.length==1)
			result= String.format("%s likes this", arr[0]);
		else if (arr.length==2)
			result= String.format("%s and %s like this", arr[0], arr[1]);
		else if (arr.length==3)
			result= String.format("%s, %s and %s like this", arr[0], arr[1], arr[2]);
		else if (arr.length==4)
			result= String.format("%s, %s and %d others like this", arr[0], arr[1], arr.length-2);
		
		return result;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] names= {"Alex", "Jacob", "Mark", "Max"};
		System.out.println(new Likes().likes(names));
	}

}
