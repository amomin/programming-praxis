# Gas Station problem #

From [praxis on July 17th](http://programmingpraxis.com/2015/07/17/the-gas-station-problem/)


> Today’s exercise is a classic problem in computer science courses:
> 
> There is a truck driving clockwise on a circular route; the truck has a gas tank with infinite capacity, initially empty. Along the route are gas stations with varying amounts of gas available: you are given a list of gas stations with the amounts of gas they have available and the amounts of gas required to drive to the next gas station. You must find a gas station that, for a trip starting from that gas station, will be able to return to that gas station.
> 
> For instance, consider a route with eight gas stations having 15, 8, 2, 6, 18, 9, 21, and 30 gallons of gas; from each of those gas stations to the next requires 8, 6, 30, 9, 15, 21, 2, and 18 gallons of gas. Obviously, you can’t start your trip at the third gas station, with 2 gallons of gas, because getting to the next gas station requires 30 gallons of gas and you would run out of gas reaching it.
> 
> Your task is to write a program that determines a suitable starting point for the truck; your algorithm should be linear in the number of gas stations and require constant space. When you are finished, you are welcome to read or run a suggested solution, or to post your own solution or discuss the exercise in the comments below
