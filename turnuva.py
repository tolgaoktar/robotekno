import random

# Fizz-Tsubasa-Yasaho oyunu için gereken değişkenler
options = ['fizz', 'tsubasa', 'yasaho']
player_score = 0
computer_score = 0

# Kazanan kombinasyonları için dictionary
winning_combinations = {
    'fizz': 'tsubasa',
    'tsubasa': 'yasaho',
    'yasaho': 'fizz'
}

# Oyuncunun hamle yapması
def player_turn():
    while True:
        player_choice = input("Enter your choice (fizz/tsubasa/yasaho): ").lower()
        if player_choice in options:
            return player_choice
        else:
            print("Invalid choice, please try again.")

# Bilgisayarın hamle yapması
def computer_turn():
    return random.choice(options)

# Hamleleri karşılaştırma ve kazananı belirleme
def compare_moves(player_choice, computer_choice):
    global player_score
    global computer_score
    
    if winning_combinations[player_choice] == computer_choice:
        print("Player wins!")
        player_score += 1
    elif winning_combinations[computer_choice] == player_choice:
        print("Computer wins!")
        computer_score += 1
    else:
        print("Tie!")

# Oyunu başlatma
def play_game():
    global player_score
    global computer_score
    
    # Oyun 5 turdan oluşacak
    for i in range(5):
        print("Round", i+1)
        player_choice = player_turn()
        computer_choice = computer_turn()
        print("Player chose", player_choice)
        print("Computer chose", computer_choice)
        compare_moves(player_choice, computer_choice)
    
    # Oyun sonu puan durumu
    print("Final score:")
    print("Player:", player_score)
    print("Computer:", computer_score)

# Oyunu başlat
play_game()
