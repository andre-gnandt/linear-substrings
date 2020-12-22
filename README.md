# linear-substrings
A linear algorithm that finds the lexicographically last substring for any sub-length of any given String

Given any string S the algorithm will determine the lexicographically last substring of S in O(n) time, where n = length of S.




Additional features:

-given any length L such that 0 <= L <= n the algorithm will determine the lexicographically last substring of length L of S in O(n) time.

-The algorithm can determine the lexicgraphically last substring of S for all lengths <= n in O(n) time. This is performed by determining the starting and
ending indices of S for the lexicographically last substring for each length less than or equal to n, it determines this for all such lengths (all together) in O(n) time
in total (for all such lengths, O(n) time ). However, it is theoretically O(n^2) time to print all of these substrings out.



Interaction:
-Upon running the algorithm, you will be prompted to enter any string S. The algorithm then determines the lexicographically last substring of S as well 
as simultaneously determining the starting indices of each last substring for all lengths less than or equal to S, all of these operations are performed in 
O(n) time.

-You will then be prompted to repeatedly enter any length L, 0 <= L <= n to find the lexicographically last substring of length L, this is an O(1) operation since
the indices were determined before, however it is O(n) to print the string out.

-You can enter "all" to find the all last substrings of lengths less or equal to n, this is an O(n) operation, however it is O(n^2) to print them all out.

