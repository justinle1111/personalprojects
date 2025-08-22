from typing import List, Iterable, Optional, Tuple

# ----- Tile kind indexing (0..33) -----
# 0..8:    balls 1-9      (b1..D9)
# 9..17:   sticks 1-9    (s1..B9)
# 18..26:  characters (C1..C9)
# 27..30:  winds: E,S,W,N (WE, WS, WW, WN)
# 31..33:  dragons: red, green, white (DR, DG, DW)
# 34..42 : flower/seasons 1-9 (F1..S4)s

#Output of CNN Example: [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 34, 35]

SUIT_OFFSETS = {'B': 0, 'S': 9, 'C': 18}

WINDS = {'WE': 27, 'WS': 28, 'WW': 29, 'WN': 30}
DRAGONS = {'DR': 31, 'DG': 32, 'DW': 33}

BONUS_CODES = ['F1', 'F2', 'F3', 'F4', 'S1', 'S2', 'S3', 'S4'] 
BONUS_KIND_START = 34

if __name__ == "__main__":
    ex_cnn_output = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 34, 35]
    sorted_hand = sorted(ex_cnn_output)
    
    print("Hello World")