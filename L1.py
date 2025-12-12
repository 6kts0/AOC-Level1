import pandas as pd

CSV_READ = pd.read_csv('nums.csv', header=None, dtype=str)
ROTATIONS = pd.DataFrame(CSV_READ)

LOOP_CAP = 100
DIAL_START = 50
L_ROTATION = "L"
R_ROTATION = "R"

ZERO_COUNT = 0

LR_CALC = 0
I_LET = ''
I_INT = 0

def first_val_p1():
    global LR_CALC
    global ZERO_COUNT
    for idx, i in ROTATIONS.iterrows():
        I_LET = i[0][0:1]       
        I_INT = int(i[0][1:4])
        if L_ROTATION in I_LET:  
            I_INT = -I_INT 
            I_INT = (I_INT + DIAL_START) % LOOP_CAP
            LR_CALC = I_INT
            print("              --- START VALUE = 50 ---")
            print('=' * 41)
            print(f"After rotation: dial at {I_INT} | Zero count: {ZERO_COUNT}")
            print('=' * 41)
            LR_CALC = I_INT

def num_sect_p1():
    global LR_CALC
    global ZERO_COUNT
    print(LR_CALC)
    for idx, i in ROTATIONS.iloc[1:].iterrows():
        I_LET = i[0][0:1] 
        I_INT = int(i[0][1:4]) 
        if L_ROTATION in I_LET:
            I_INT = -I_INT
            I_INT = (I_INT + LR_CALC) % LOOP_CAP
            if I_INT == 0:
                ZERO_COUNT += 1
            print(f"After rotation: dial at {I_INT} | Zero count: {ZERO_COUNT}")
            print('=' * 41)
            LR_CALC = I_INT
        elif R_ROTATION in I_LET:
            I_INT = (I_INT + LR_CALC) % 100
            if I_INT == 0:
                ZERO_COUNT += 1
            print(f"After rotation: dial at {I_INT} | ZERO count: {ZERO_COUNT}")
            print('=' * 41)
            LR_CALC = I_INT

    
def num_sect_p2():
    global ZERO_COUNT
    ZERO_COUNT = 0
    x = 50
    
    # Simple rotation clarification and convert datatype
    rotations = (ROTATIONS[0]
        .str.replace('R', '')
        .str.replace('L', '-')
        .astype(int))
    
    for rotation in rotations:
        # Count full loops
        ZERO_COUNT += abs(rotation) // 100
        # Get partial rotation (keep the sign)
        rem = rotation % 100
        
        old_x = x # Pre rotated position

        new_x = (x + rem) % 100 # Rotated and wrapped position
        
        # Check if rotation passed through 0
        # Wraps right rotation if new position is less the the old position
        # Wraps left rotation if the new position is greater than the old
        if (rotation > 0 and new_x < old_x) or (rotation < 0 and new_x > old_x):
            ZERO_COUNT += 1
        
        # Updated position
        x = new_x

    print(f'Touched 0: {ZERO_COUNT}')




def main():
    #first_val_p1()     
    #num_sect_p1()
    num_sect_p2()

if __name__ == "__main__":
    main()