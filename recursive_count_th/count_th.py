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


    


    
def count_th(word,count):
    try:
        x = word.index('th')
        if x:
            
            y = word[0: x:] + word[x + 2::]
            count +=1
            count_th(y,count)
    except:
        print(word,count)
        
  
     
    


count_th('dksjthkdjkksthaafddthalfkddkjsthaddfath',0)
