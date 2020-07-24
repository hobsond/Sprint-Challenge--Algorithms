'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# we want to find out how many times th inside of word
# we want to check if th is in side of the word if so
# we take away that index also that index + 1
# count for everytime that happens 
# then if th is not in there we return the count


    

def count_th(word):
    length = len(word)
    if length < 2:
        return 0
    if word[0:2] == 'th':
        return count_th(word[2:]) + 1
    else:
        return count_th(word[1:])
  
     
    


print(count_th('dksjthkdjkksthaafddthalfkddkjsthaddfath'))
