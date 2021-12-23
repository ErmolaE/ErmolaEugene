import monopoly_logic as ml

def get_player_name(player_count):
    name_players=[]
    for i in range(player_count):
        t=i+1
        name_player=input(f"Please input player {t} name: \n")
        name_players.append(name_player)
    return name_players

def not_money(id_player):
    while True:
        ml.show_estate_money()
        answer=input("You don't have enough money, please sell hotel(input 1) or mortgage estate(input 1):\n")
        if answer=="1":
            cell_id=input("Please input id estate:\n")
            #TODO validation
            ml.sell_hotel(id_player, cell_id)
            break
        elif answer=="2":
            cell_id=input("Please input id estate:\n")
            ml.mortgage_estate(id_player, cell_id)
            break
        else:
            print("Incorrect input!")

def buy_free_estate(id_player, cell_id, value):
    while True:
        answer=input("Buy(input 1) or auction(input 1)?\n")
        if answer=="1":
            ml.buy_estate(id_player, cell_id, value)
            break
        elif answer=="2":
            print("Host an auction!")
            id_player=int(input("Input id player:\n"))
            value=int(input("Input value:\n"))
            #TODO validation
            ml.buy_estate(id_player, cell_id, value)
            break
        else:
            print("Incorrect input!")            

def other_actions(id_player):
    while True:
        answer=input("Do you want to build hotel (input 1), sell hotel (input 2), mortgage estate (input 3), buy out estate (input 4), trade (input 5), end turn (input 6)?\n")
        if answer=="1":
           estate_id=input("Input id estate:\n")
           #TODO validation
           ml.build_hotel(id_player, estate_id)
        elif answer=="2":
           estate_id=input("Input id estate:\n")
           #TODO validation
           ml.sell_hotel(id_player, estate_id)  
        elif answer=="3":
           estate_id=input("Input id estate:\n")
           #TODO validation
           ml.mortgage_estate(id_player, estate_id) 
        elif answer=="4":
           estate_id=input("Input id estate:\n")
           #TODO validation
           ml.byout_estate(id_player, estate_id)
        elif answer=="5":
           print("In development...")
        elif answer=="6":
           break
        else:
           print("Incorrect input!") 

def pre_game():
    while True:
        player_count=input("Please input number of players 2 or 3 or 4:\n")
        if player_count in ["2", "3", "4"]:
            player_count=int(player_count)
            break
        else:
            print("Incorrect input")
    id_players=[x+1 for x in range(player_count)] 
    name_players=get_player_name(player_count) 
    ml.create_players(player_count, name_players)
    return id_players

def game(id_players):
    while True:
        if len(id_players)==1:
            winner_id=id_players[0]
            winner_name=ml.find_name_player(winner_id)
            print(f"Congratulations to the player {winner_name} on the victory! End game.")
            break
        for id_player in id_players:
            player_name=ml.find_name_player(id_player)
            print(f"{player_name}s turn")
            ml.show_estate_money(id_player)
            dice1, dice2= ml.roll_dice()
            print(f"You rolled the dice. Dropped {dice1} and {dice2}")
            message=ml.action(id_player, dice1, dice2)
            if message in ml.l:
                not_money(id_player)
            if message == "free estate":
                print(message)
                cell_id, value=ml.find_curr_cell(id_player)
                buy_free_estate(id_player, cell_id, value)
            if message == "This is your estate":
                print(message)
            if message == "You are bankrupt":
                print(message)
                id_players.remove(id_player)
                continue              
            if message == "In development...":
                print(message)
            other_actions(id_player)

if __name__ == "__main__":
    id_players=pre_game()
    game(id_players)
    
            