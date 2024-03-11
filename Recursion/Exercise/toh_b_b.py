# number of disks n
def tower_of_hanoi(n, from_peg, auxilary_peg, to_peg):
    count = 0
    if n == 0:
        return

    else:
        tower_of_hanoi(n-1, from_peg, to_peg,auxilary_peg)
        print("Move disk", n, 'from rod', from_peg, 'to', to_peg)

        tower_of_hanoi(n-1, to_peg, auxilary_peg, from_peg)




tower_of_hanoi(7, 'A', 'B', 'C')


