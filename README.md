# coin-swap-problem
Solver for the coin swapping problem

OVERVIEW
	This program aims at solving the mathematical Coin Permutation Problem.
	
	In the initial position, there are X coins 'a' and X coins 'b' in a row, without space.
	X=5:
		aaaaabbbbb
		
	The goal is to end up in a configuration where all coins alternate, without space, in X moves or less:
		ababababab
		
	The authorized moves are: taking 2 adjacent coins, and move them close to another coin, in line, without removing the spaces.
	For X=5, there are 2 solutions, one of them is:
		aaaaabbbbb
		a  aabbbbbAA
		aBBaabb  baa
		abba  bABbaa
		abbaBAbab  a
		  babababABa


HEURISTICS:
	- Heuristic 1:
		If we have to come back to a previous configuration, we have lost (we could save at least 2 moves)
	
	- Heuristic 2:
		Let's call S the number of alternations of a configuration, which is the number of times a letter is followed by a different letter, ignoring spaces.
		In the initial configuration, S=1.
		The goal is to get S=(2*X)-1.
		But each move can only increase S by 2 at most. So, if we have Y moves left, but S<(2*(X-Y))-1, we know we don't have enough moves to get to the final configuration.
		Heuristic 2 automatically includes all of heuristic 1's cases.
	
	- Heuristic 3:
		* let's look at the last move.
		We can easily prove that:
			1) it's a mixed group ('ab' or 'ba') that moves
				-> since it's intact in the final configuration, it has to alternate 'a' and 'b'
			2) it comes from a border
				-> otherwise it would leave a hole
			3) it moves to fill a hole
				Let's assume it doesn't.
					-> case 1: if there was a hole, the final solution would have that hole too (impossible)
					-> case 2: if there was no hole, the move would be from border to border
						- ABba : final position is not solution
						- ABab : already solution
			4) that hole is the last hole.
				-> otherwise there would be a hole in the final configuration.
		Summary:
			The last move moves a group 'ab' or 'ba' from a border to fill the last hole.

		This last move only gains up to 1 alternation.
		So now we can refine Heuristic 2.
		To be valid, a configuration with Y remaining moves:
			- is the final configuration
			- or S>=2*(X-Y)




>>> s = solveCoins(6)
>>> displaySol(s)
2 SOLUTIONS


Solution 1, 6 moves
aaaaaabbbbbb
a  aaabbbbbbaa
abbaaab  bbbaa
abb  abaabbbaa
abbababa  bbaa
abbabababab  a
babababababa

Solution 2, 6 moves
aaaaaabbbbbb
bbaaaaaabbb  b
bbaaa  abbbaab
bbaaabbab  aab
bbaa  bababaab
b  ababababaab
babababababa





>>> s = solveCoins(7)
>>> displaySol(s)
18 SOLUTIONS


Solution 1, 7 moves
aaaaaaabbbbbbb
a  aaaabbbbbbbaa
abbaaaabbb  bbaa
abba  abbbaabbaa
abbabaabb  abbaa
abbaba  bababbaa
abbababababab  a
bababababababa

Solution 2, 7 moves
aaaaaaabbbbbbb
a  aaaabbbbbbbaa
abbaaaabbb  bbaa
abba  abbbaabbaa
abbabaabbbaab  a
abbaba  bbaababa
abbababab  ababa
bababababababa

Solution 3, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaabbaabbb  bbaa
abbaabbbaabbaa
abbaabb  abbaaba
abba  bababbaaba
abbabababab  aba
bababababababa

Solution 4, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaabbaabbb  bbaa
abbaabbbaabbaa
abbaabbbaab  aba
abba  bbaabababa
abbabab  abababa
bababababababa

Solution 5, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaabbaabbb  bbaa
aaabbaabbb  b  aba
abbaabbbaab  aba
abba  bbaabababa
abbabab  abababa
bababababababa

Solution 6, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaabbaabbb  bbaa
aaabbaabbb  b  aba
aaabba  bb  bababa
abba  bbaabababa
abbabab  abababa
bababababababa

Solution 7, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaa  aabbbbbb  aba
aaa  a  bbbbbababa
aaabba  bb  bababa
abba  bbaabababa
abbabab  abababa
bababababababa

Solution 8, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaa  aabbbbbb  aba
aaabbaabbb  b  aba
abbaabbbaab  aba
abba  bbaabababa
abbabab  abababa
bababababababa

Solution 9, 7 moves
aaaaaaabbbbbbb
aaa  aabbbbbbbaa
aaa  aabbbbbb  aba
aaabbaabbb  b  aba
aaabba  bb  bababa
abba  bbaabababa
abbabab  abababa
bababababababa

Solution 10, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bab  aaaaaabb  bbb
bab  a  aaabbaabbb
bababa  aa  baabbb
babababbaa  baab
bababab  ababaab
bababababababa

Solution 11, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bab  aaaaaabb  bbb
bab  a  aaabbaabbb
bab  abbaaabbaab
babababbaa  baab
bababab  ababaab
bababababababa

Solution 12, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bab  aaaaaabb  bbb
bababaaaaa  b  bbb
bababa  aa  baabbb
babababbaa  baab
bababab  ababaab
bababababababa

Solution 13, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bbaa  aaabbaabbb
bab  a  aaabbaabbb
bababa  aa  baabbb
babababbaa  baab
bababab  ababaab
bababababababa

Solution 14, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bbaa  aaabbaabbb
bab  a  aaabbaabbb
bab  abbaaabbaab
babababbaa  baab
bababab  ababaab
bababababababa

Solution 15, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bbaa  aaabbaabbb
bbaabbaaabbaab
bab  abbaaabbaab
babababbaa  baab
bababab  ababaab
bababababababa

Solution 16, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabb  bbb
bbaa  aaabbaabbb
bbaabbaaabbaab
babbaab  aabbaab
babbaababa  baab
bab  ababababaab
bababababababa

Solution 17, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabbbb  b
bbaa  aaabbbbaab
bbaabbaaab  baab
b  abbaaabbabaab
bababbaa  babaab
babab  abababaab
bababababababa

Solution 18, 7 moves
aaaaaaabbbbbbb
bbaaaaaaabbbb  b
bbaa  aaabbbbaab
bbaabbaaab  baab
bbaab  aabbabaab
bbaababa  babaab
b  abababababaab
bababababababa





>>> s = solveCoins2(10, 4)
>>> displaySol(s)
4 SOLUTIONS


Solution 1, 10 moves
aaaaaaaaaabbbbbbbbbb
a  aaaaaaabbbbbbbbbbaa
abbaaaaaaab  bbbbbbbaa
abba  aaaabaabbbbbbbaa
abbabbaaaabaabb  bbbaa
abbabba  abaabbaabbbaa
abbabbaababa  baabbbaa
abbab  ababababaabbbaa
abbababababababa  bbaa
abbabababababababab  a
babababababababababa

Solution 2, 10 moves
aaaaaaaaaabbbbbbbbbb
a  aaaaaaabbbbbbbbbbaa
abbaaaaaaab  bbbbbbbaa
abba  aaaabaabbbbbbbaa
abbabbaaaabaabb  bbbaa
abbabba  abaabbaabbbaa
abbabbaababa  baabbbaa
abbabbaababababaabb  a
abbabbaababababa  baba
abbab  abababababababa
babababababababababa

Solution 3, 10 moves
aaaaaaaaaabbbbbbbbbb
a  aaaaaaabbbbbbbbbbaa
abbaaaaaaab  bbbbbbbaa
abba  aaaabaabbbbbbbaa
abbabbaaaabaabb  bbbaa
abbabba  abaabbaabbbaa
abbabbaababaabba  bbaa
abbab  ababaabbababbaa
abbababababa  bababbaa
abbabababababababab  a
babababababababababa

Solution 4, 10 moves
aaaaaaaaaabbbbbbbbbb
a  aaaaaaabbbbbbbbbbaa
abbaaaaaaab  bbbbbbbaa
abba  aaaabaabbbbbbbaa
abbabbaaaabaabb  bbbaa
abbabba  abaabbaabbbaa
abbabbaababaabba  bbaa
abbabbaababaabbabab  a
abbabbaababa  babababa
abbab  abababababababa
babababababababababa






>>> s = solveCoins2(11, 1)
>>> displaySol(s)
1 SOLUTIONS


Solution 1, 11 moves
aaaaaaaaaaabbbbbbbbbbb
a  aaaaaaaabbbbbbbbbbbaa
abbaaaaaaaabb  bbbbbbbaa
abba  aaaaabbaabbbbbbbaa
abbabbaaaaabbaabbb  bbaa
abbabbaa  abbaabbbaabbaa
abbab  abaabbaabbbaabbaa
abbabababa  baabbbaabbaa
abbabababababaabb  abbaa
abbabababababa  bababbaa
abbababababababababab  a
bababababababababababa





>>> s = solveCoins2(12, 1)
>>> displaySol(s)
1 SOLUTIONS


Solution 1, 12 moves
aaaaaaaaaaaabbbbbbbbbbbb
a  aaaaaaaaabbbbbbbbbbbbaa
abbaaaaaaaaab  bbbbbbbbbaa
abba  aaaaaabaabbbbbbbbbaa
abbabbaaaaaabaabb  bbbbbaa
abbabbaa  aabaabbaabbbbbaa
abbabbaabbaabaabbaab  bbaa
abbab  abbaabaabbaabbabbaa
abbabababbaaba  baabbabbaa
abbababab  abababaabbabbaa
abbabababababababa  babbaa
abbabababababababababab  a
babababababababababababa






>>> s = solveCoins(13, 1)
>>> displaySol(s)
1 SOLUTIONS


Solution 1, 13 moves
aaaaaaaaaaaaabbbbbbbbbbbbb
a  aaaaaaaaaabbbbbbbbbbbbbaa
abbaaaaaaaaaabb  bbbbbbbbbaa
abba  aaaaaaabbaabbbbbbbbbaa
abbabbaaaaaaabbaabb  bbbbbaa
abbabbaa  aaabbaabbaabbbbbaa
abbabbaabbaaabbaabbaabb  baa
abbabbaabbaa  baabbaabbabbaa
abbab  abbaababaabbaabbabbaa
abbabababbaababa  baabbabbaa
abbababab  ababababaabbabbaa
abbababababababababa  babbaa
abbababababababababababab  a
bababababababababababababa

