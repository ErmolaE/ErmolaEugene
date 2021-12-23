import monopoly_classes as mc
from random import randint

player1=mc.player("player1", 1, 1500, 0, 0, 1500)

player2=mc.player("player2", 2, 1500, 0, 0, 1500)

player3=mc.player("player3", 3, 1500, 0, 0, 1500)

player4=mc.player("player4", 4, 1500, 0, 0, 1500)

cell0=mc.cell("GO", 0)  

cell1=mc.estate("mediterranean avenue", 1, 0, 60, [2, 4, 10, 30, 90, 160, 250], 0, 0, 50, 0)

cell2=mc.community_chest("community chest", 2)

cell3=mc.estate("baltic avenue", 3, 0, 60, [4, 8, 20, 60, 180, 320, 450], 0, 0, 50, 0)

cell4=mc.cell("Income tax", 4)

cell5=mc.railway_station("reading railroad", 5, 0, 200, [25, 50, 100, 200], 0, 0)

cell6=mc.estate("oriental avenue", 6, 0, 100, [6, 12, 30, 90, 270, 400, 550], 0, 0, 50, 0)

cell7=mc.chance("chance", 7)

cell8=mc.estate("vermont avenue", 8, 0, 100, [6, 12, 30, 90, 270, 400, 550], 0, 0, 50, 0)

cell9=mc.estate("vermont avenue", 9, 0, 120, [8, 16, 40, 100, 300, 450, 600], 0, 0, 50, 0)

cell10=mc.cell("In jail", 10)

cell11=mc.estate("st.charles place", 11, 0, 140, [10, 20, 50, 150, 450, 625, 750], 0, 0, 100, 0)

cell12=mc.utility_company("electric company", 12, 0, 150, [4, 10], 0, 0)

cell13=mc.estate("states avenu", 13, 0, 140, [10, 20, 50, 150, 450, 625, 750], 0, 0, 100, 0)

cell14=mc.estate("virginia avenue", 14, 0, 160, [12, 24, 60, 180, 500, 700, 900], 0, 0, 100, 0)

cell15=mc.railway_station("pennsylvania railroad", 15, 0, 200, [25, 50, 100, 200], 0, 0)

cell16=mc.estate("st.james place", 16, 0, 180, [14, 28, 70, 200, 550, 750, 950], 0, 0, 100, 0)

cell17=mc.community_chest("community chest", 17)

cell18=mc.estate("tennesse avenue", 18, 0, 180, [14, 28, 70, 200, 550, 750, 950], 0, 0, 100, 0)

cell19=mc.estate("new york avenue", 19, 0, 200, [16, 32, 80, 220, 600, 800, 1000], 0, 0, 100, 0)

cell20=mc.cell("free parking", 20)

cell21=mc.estate("kentucky avenue", 21, 0, 220, [18, 36, 90, 250, 700, 875, 1050], 0, 0, 150, 0)

cell22=mc.chance("chance", 22)

cell23=mc.estate("indiana avenue", 23, 0, 220, [18, 36, 90, 250, 700, 875, 1050], 0, 0, 150, 0)

cell24=mc.estate("illinois avenue", 24, 0, 240, [20, 40, 100, 300, 750, 925, 1100], 0, 0, 150, 0)

cell25=mc.railway_station("b&o railroad", 25, 0, 200, [25, 50, 100, 200], 0, 0)

cell26=mc.estate("atlantic avenue", 26, 0, 260, [22, 44, 110, 330, 800, 975, 1150], 0, 0, 150, 0)

cell27=mc.estate("ventnor avenue", 27, 0, 260, [22, 44, 110, 330, 800, 975, 1150], 0, 0, 150, 0)

cell28=mc.utility_company("water works", 28, 0, 150, [4, 10], 0, 0)

cell29=mc.estate("marvin gardens", 29, 0, 280, [24, 48, 120, 360, 850, 1025, 1200], 0, 0, 150, 0)

cell30=mc.cell("Go to jail", 30)

cell31=mc.estate("pacific avenue", 31, 0, 300, [26, 52, 130, 390, 900, 1100, 1275], 0, 0, 200, 0)

cell32=mc.estate("north carolina avenue", 32, 0, 300, [26, 52, 130, 390, 900, 1100, 1275], 0, 0, 200, 0)

cell33=mc.community_chest("community chest", 33)

cell34=mc.estate("pennsylvania avenue", 34, 0, 320, [28, 56, 150, 450, 1000, 1200, 1400], 0, 0, 200, 0)

cell35=mc.railway_station("short line", 35, 0, 200, [25, 50, 100, 200], 0, 0)

cell36=mc.chance("chance", 36)

cell37=mc.estate("park place", 37, 0, 350, [35, 70, 175, 500, 1100, 1300, 1500], 0, 0, 200, 0)

cell38=mc.cell("Luxury tax", 38)

cell39=mc.estate("boardwalk", 39, 0, 400, [50, 100, 200, 600, 1400, 1700, 2000], 0, 0, 200, 0)

l=[cell0, cell1, cell2, cell3, cell4,  cell5, cell6, cell7,  cell8, cell9, cell10, cell11, cell12, cell13, cell14,  cell15, cell16, cell17,  cell18, cell19,cell20, cell21, cell22, cell23, cell24,  cell25, cell26, cell27,  cell28, cell29, cell30, cell31, cell32, cell33, cell34,  cell35, cell36, cell37,  cell38, cell39]
players=[]

def create_players(count_players, name_players):
    global players
    if count_players==2:
        players.extend([player1, player2])
    if count_players==3:
        players.extend([player1, player2, player3])
    if count_players==4:
        players.extend([player1, player2, player3, player4])
    for i in range(len(players)):
        players[i].set_name(name_players[i])

def find_name_player(player_id):
    player=find_player(player_id)
    player_name=player.name
    return player_name

def find_cell(pos):
    for cell in l:
        if cell.id == pos:
            return cell

def find_player(id_player):
    for player in [player1, player2, player3, player4]:
        if player.id==id_player:
            return player

def roll_dice():
    dice1=randint(1, 6)
    dice2=randint(1, 6)
    return dice1, dice2

def paid_rent(player, cell):
    rent=cell.calc_rent()
    own_player=find_player(cell.own)
    print(f"You have to pay {own_player.name} {rent}")
    if rent <= player.money:
        player.decrease_money(rent) 
        own_player.increase_money(rent)
        return print(f"{player.name} paid {own_player.name} {rent}")
    elif rent > player.capital:
        player.set_bankrupt=1
        own_player.increase_money(player.capital)
        #TODO продажа всех отелей и залог всей недвижимости player и добавление заложенной недвижимоcти в own_player
        return "You are bankrupt"
    else:
        return cell

def action(id_player, dice1, dice2):
    player=find_player(id_player)
    pos=player.roll(dice1, dice2)
    cell=find_cell(pos)
    print(f"This is {cell.name}")            
    if type(cell) in (mc.estate, mc.railway_station, mc.utility_company):    
        if cell.own==0:
            return "free estate"
        elif cell.own==player.id:
            return "This is your estate"
        else:
            return paid_rent(player, cell)
    if type(cell) in (mc.chance, mc.community_chest, mc.cell):
        return "In development..."

def find_curr_cell(id_player):
    player=find_player(id_player)
    cell=find_cell(player.position)
    value=cell.price
    return player.position, value

def buy_estate(id_player, cell_id, value):
    player=find_player(id_player)
    cell=find_cell(cell_id)
    player.buy_estate(cell, value)
    cell.set_own(player.id)
    return print(f"You bought {cell.name}")

def show_estate_money(id_player):
    player=find_player(id_player)
    money=f"You have {player.money}."
    if len(player.estates)==0:
        estates="You don't have estates."
    else:
        estates=', '.join(map(lambda x: x.name+str(x.id), player.estates))
    return print(money+estates)

def mortgage_estate(id_player, cell_id):
    player=find_player(id_player)
    cell=find_cell(cell_id)
    player.in_mortgaged(cell)

def byout_estate(id_player, cell_id):
    player=find_player(id_player)
    cell=find_cell(cell_id)
    player.out_mortgaged(cell)

def sell_hotel(id_player, cell_id):
    player=find_player(id_player)
    cell=find_cell(cell_id)
    print("In development")

def build_hotel(id_player, estate_id):
    player=find_player(id_player)
    estate=find_cell(estate_id)
    player.build_hotel(estate)
