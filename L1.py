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
    global DIAL_START
    global ZERO_COUNT
    ZERO_COUNT = 0
    x = 50
    for idx, i in ROTATIONS.iloc[1:].iterrows():
        ZERO_COUNT += abs(i) // 100
        foo = 1 if i > 0 else -1
        rem = foo * (i % 100)
        x += rem
        if x >= 100 or (x <= 0 and x != rem):
            ZERO_COUNT += 1
        x %= 100
print(f'{ZERO_COUNT}')



def main():
    num_sect_p2()
    #first_val_p1()     
    #num_sect_p1()

if __name__ == "__main__":
    main()