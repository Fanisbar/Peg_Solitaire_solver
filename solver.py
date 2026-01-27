def make_starting_state(size):
    state = list()
    for i in range(1, 3*size-1):
        row = list()
        for j in range(1, 3*size-1):
            # corners
            if (i<=size-1 or i>2*size-1) and (j<=size-1 or j>2*size-1):
                row.append(" ")
            # center
            elif (i==size+size//2) and (j==size+size//2):
                row.append("0")
            # everything else
            else:
                row.append("+")
        state.append(row)

    return state

def visualize_state(state):
    for row in state:
        for item in row:
            print(item+" ", end='')
        print('')

# test
visualize_state(make_starting_state(3))
