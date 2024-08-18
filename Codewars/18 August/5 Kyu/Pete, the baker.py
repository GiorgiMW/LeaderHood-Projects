def cakes(recipe, available):
    total = float("inf")
    for i,x in recipe.items():
        if i in available.keys():
            if available[i] // recipe[i] < total:
                total = available[i] // recipe[i]
        else:
            return 0
    return total