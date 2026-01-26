def visualize_state(state):
    i=0
    for char in state:
        if char=="2":
            print("  ", end='')
        elif char=="1":
            print("+ ", end='')
        elif char=="0":
            print("0 ", end='')
        i+=1
        if i==7:
            print("")
            i=0
starting_state = "2211122221112211111111110111111111122111222211122"
visualize_state(starting_state)
