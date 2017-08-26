def football():
    players = str(input())
    players = [int(player) for player in players]
    for i in range(0, len(players)-6):
        seven_players = sum(players[i:i+7])
        if seven_players == 0 or seven_players == 7:
            print("YES")
            return
    print("NO")
                 
                           
       
    

if __name__ == '__main__':
    football()
    