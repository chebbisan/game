from random import randrange
import configparser

def HighScore(score):
    leaderboard = open('score.txt', 'w')
    leaderboard.write(str(score))
    leaderboard.close()

file = open('score.txt', 'r')
bestscore = int(file.read())
score = 0
error = 0
print('WELLCUM, choose one from 1 to 3')
while error == 0:
    
    rand = randrange(1, 4)
    ans = int(input())
    if rand == ans:
        score += 1
    else:
        error += 1
        if score > bestscore:
            print('YOU WIN, your score is', score, '\n' 'better than previous highscore, it was', bestscore)
        else:
            print('YOU LOSE, your score is', score, '\n' 'Highscore is', bestscore)
 
if score > bestscore:
    HighScore(score)