"""
2. Processes stage transition
In an Operating System, a number of processes are to be executed (numbered 1 to P). The processes move through different
stages, called A, B, C, D and E, as per the diagram shown below.



Each process can move through the stages as shown in the given direction only i.e. from A to B (written as AB), B to C
(written as BC), C to B or D or E (written as CB, CD or CE), D to B (written as DB) and C to E (written as CE). All
processes start in stage A, and a number of execution steps are performed. The execution of the processes is denoted
in the format SD X , which means process
number X moved from stage S(source) to D(destination) . All execution steps need to be checked for their feasibility
before they can be executed e.g. the step CE 4 can be
executed only if process 4 is in stage C already. All such infeasible steps are ignored by the system.
Write a program to determine which process is in which stage, at the end of execution of all given steps.

Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings anywhere in the program, as
these contribute to the standard output and testcases will fail.



Constraints:
I) 1 <= the number of processes <= 1000
II) 1 <= the number of execution steps <= 1000
Input Format:
The first line of input contains the number of processes P and the number of execution
steps Q, separated by a single white space.
Next Q lines contain the execution steps, written as SD X , where SD and X are
separated by a single white space.
Output Format:
The 5 lines of output contain the 5 stages (A,B,C,D,E) and the processes which are present in that particular stage. The
processes are printed in ascending order separated by a single white space.



Sample Input1:
10 11
AB 2
AB 5
AB 8
AB 4
AB 9
BC 5
BC 8
BC 9
CB 5
CD 8
CE 9



Sample Output1:
A 1 3 6 7 10
B 2 4 5
C
D 8
E 9

Explanation1:
Initially processes 1 to 10 are in stage A. When the steps AB 2, AB 5, AB 8, AB 4 and AB 9 are executed, the processes 2,5,8,4 and 9 move from A to B.
Now 1,3,6,7,10 are present in stage A and 2,5,8,4,9 are present in stage B. Similarly other steps are executed. With BC 5, process 5 moves to stage C, and then later with CB 5, it comes back to
stage B. This way all the steps are executed and the final stages for each process are determined.



Sample Input2:
3 3
AB 1
CD 1
AB 3



Sample Output2:
A 2
B 1 3
C
D
E



Explanation2:
Initially processes 1,2 and 3 are in stage A. With AB 1, process 1 moves to stage B. Next step is CD 1, however since 1 is in stage B and not stage C, this step cannot be executed and 1 remains in stage B. With AB 3, process 3 moves to stage B. Hence finally, process 2 remains in stage A and processes 1 and 3 are in stage B.
"""

def processQuery(n,p,query):        # n is number of processes, p is number of queries and query is an array of all queries

    # WRITE YOUR CODE HERE

    pass

def main():
    S = input().split()
    n = int(S[0])
    p = int(S[1])
    query = []
    for i in range(p):
        P = input()
        query.append(P)
    processQuery(n,p,query)

main()