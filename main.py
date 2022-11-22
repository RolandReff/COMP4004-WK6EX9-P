def countVotes(filename,candidate):
  wins = 0
  countVotesFile = open(filename)
  for eachLine in countVotesFile:
    LinesSplit = eachLine.split()
    if LinesSplit[1] == candidate: 
      wins += 1
  return wins

def pluralityWinner(filename,candidates):
  Winner = []
  candidateList = [] # The list that stores the order of the candidates
  candidateWinList = [] # The list that stores the wins, the wins shares the same index as in the  candidateList
  wins = 0 
  for i in range(len(candidates)): # For loop that adds the candidates and the wins at the same time so they share the index in  the lists     wins = countVotes(filename,candidates[i])
    candidateList.append(candidates[i])
    candidateWinList.append(wins)
  for l in range(len(candidateList)): # Loops through the wins list and checks what index is the largest, and then addes the same index from the can list
    if candidateWinList[l] == max(candidateWinList):
      Winner.append(candidateList[l])
      Winner.append(candidateWinList[l])                
  return Winner       

if __name__ == "__main__":
  candidates = ['Memphis','Nashville','Chattanooga','Knoxville']
  win = pluralityWinner('votes.txt',candidates)
  print("Plurality winner from votes.txt")
  print(win)
