import random  

# Hằng số  
MIN_PLAYERS = 2  
MAX_PLAYERS = 4  
MIN_DICE = 1  
MAX_DICE = 6  
WINNING_SCORE = 50  

def roll():  
    return random.randint(MIN_DICE, MAX_DICE)  

def player_turn(player_index, current_score):  
    while True:  
        s_roll = input("Bạn có muốn lăn xúc xắc (y) không?: ")  
        if s_roll.lower() != "y":  
            return current_score  

        val = roll()  
        if val == 1:  
            print("Bạn lăn phải 1! Bạn mất lượt.")  
            return 0  
        else:  
            current_score += val  
            print(f"Bạn lăn được: {val}")  
            print(f"Điểm hiện tại của bạn là: {current_score}")  

def main():  
    while True:  
        players_input = input("Nhập số người chơi (2-4): ")  
        if players_input.isdigit():  
            players = int(players_input)  
            if MIN_PLAYERS <= players <= MAX_PLAYERS:  
                break  
            else:  
                print("Số người chơi không hợp lệ. Vui lòng nhập 2-4 người chơi.")  
        else:  
            print("Đầu vào không hợp lệ. Vui lòng nhập một số trong khoảng 2 đến 4.")  

    players_scored = [0] * players  

    while max(players_scored) < WINNING_SCORE:  
        for i in range(players):  
            print(f"\nLượt của Người chơi {i + 1}")  
            print(f"Tổng điểm của bạn là: {players_scored[i]}\n")  
            current_score = player_turn(i, 0)  
            players_scored[i] += current_score  
            print(f"Tổng điểm của bạn là: {players_scored[i]}")  

    max_score = max(players_scored)  
    winning_player = players_scored.index(max_score) + 1  
    print(f"Người chơi {winning_player} thắng với số điểm {max_score}")  

if __name__ == "__main__":  
    main()