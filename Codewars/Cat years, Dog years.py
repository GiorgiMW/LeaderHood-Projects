def human_years_cat_years_dog_years(human_years):
    dog = 0
    cat = 0
    count = 1
    for i in range(human_years):
        if count == 1:
            dog = dog + 15
            cat = cat + 15
            count =  count + 1
        elif count == 2:
            cat = cat + 9
            dog = dog + 9
            count = count + 1
        else:
            cat = cat + 4
            dog = dog + 5
            count = count + 1
    return [human_years,cat,dog]
            