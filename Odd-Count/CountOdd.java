/*
Given an array, find the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
 */

import java.util.HashMap;
import java.util.Map;

public class CountOdd {

	public int count(int[] arr)
	{
		Map<Integer, Integer> mp= new HashMap<>();
		for (int i : arr) {
			if (mp.containsKey(i))
				mp.put(i, mp.get(i)+1);
			else
				mp.put(i, 1);
		}
		
		for(Map.Entry<Integer, Integer> entry: mp.entrySet())
		{
			if (entry.getValue() % 2 != 0)
				return entry.getKey();
		}
		
		return 0;
	}

	public static void main(String[] args) {
		int[] arr= {1,1,1,1,1,2,2};
		System.out.println(new CountOdd().count(arr));
	}
	
}

