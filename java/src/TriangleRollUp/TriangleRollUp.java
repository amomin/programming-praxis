package TriangleRollUp;

import java.util.ArrayList;
//import java.util.Stack;
//import java.util.LinkedList;
import java.util.ArrayDeque;
import java.util.Iterator;

public class TriangleRollUp
{
	public static void main(String[] args)
	{
		ArrayList<Integer> inpt = new ArrayList<Integer>();
		for(int i = 0; i < args.length; i++)
		{
			inpt.add(Integer.parseInt(args[i]));
		}
		
		ArrayDeque<ArrayList<Integer>> answer = TriangleRollUp.TriangleFrom(inpt);		
		//for (Iterator<ArrayList<Integer>> itr = answer.iterator(); itr.hasNext();)
		//for (Iterator<ArrayList<Integer>> itr = answer.descendingIterator(); itr.hasNext();)
		for(ArrayList<Integer> row : answer)
		{
			//ArrayList<Integer> row = itr.next();
			System.out.println(row.toString());
		}
	}
	
	public static ArrayDeque<ArrayList<Integer>> TriangleFrom(ArrayList<Integer> els)
	{
		ArrayDeque<ArrayList<Integer>> result = new ArrayDeque<ArrayList<Integer>>();		
		ArrayList<Integer> next = els;
		if (next.size() < 1) return result;
		result.addFirst(next);
		next = NextRow(next);		
		while (next.size() > 0)
		{
			result.addFirst(next);
			next = NextRow(next);
		}		
		return result;
	}
	
	private static ArrayList<Integer> NextRow(ArrayList<Integer> row)
	{
		if (row.size() < 1) throw new java.util.InputMismatchException("Input row cannot be empty");		
		ArrayList<Integer> next = new ArrayList<Integer>();
		if (row.size() == 1) return next;
		int second = row.get(0);
		for (int i = 1; i < row.size(); i ++)
		{
			int first = second;
			second = row.get(i);
			next.add(first + second);
		}
		return next;
	}
}