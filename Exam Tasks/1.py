# Determine if a walk (given as an array of directions) takes exactly 10 minutes 
# and returns you to the starting point.

# Args:
# walk (list of str): List of one-letter direction strings ('n', 's', 'e', 'w').
# Each direction takes 1 minute (so list with length of 10 elements takes 10 minutes)

# Returns:
# bool: True if the walk is exactly 10 minutes and returns to start, False otherwise.

# Test Cases:
# ['w','e','w','e','w','e','w','e','w','e','w','e'] -> False
# ['n','s','n','s','n','s','n','s','n','s'] -> True
# ['n','n','n','s','n','s','n','s','n','s'] -> False
# ['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] -> False
# # ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] -> True

def walking(walk):
    # x = 0
    # y = 0
    # if len(walk) != 10:
    #     return False
    # for i in walk:
        
    return len(walk) == 10 and (walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w"))
        
        # if i == "n":
        #     y = y +1
        # if i == "s":
        #     y = y -1
        # if i == "e":
        #     x = x + 1
        # if i == "w":
        #     x = x - 1

print(walking(['n','s','n','s','n','s','n','s','n','s']))