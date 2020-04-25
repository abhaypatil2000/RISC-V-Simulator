
btb={}
#btb['0x4']={1,'T','0xa'}
#Each row is of the form - valid bit, Current state, taken address
def add_instruction(pc,takenAdd,initialState): 
    if pc in btb:
        return
    else:
        btb[pc]=[1,initialState,takenAdd]
        #print (btb)
        return
def update_state(pc,new_state):
    if pc not in btb:
        return 
    else:
        btb[pc][1]=new_state        
        return 
"""add_instruction('0xa','0x4','T') 
add_instruction('0x5','0x4','T') 
add_instruction('0x6','0x4','T') 
print (btb)
update_state('0xa','NT')
print(btb)""" 
  