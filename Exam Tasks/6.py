# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Test Cases:
# 'Pig latin is cool' -> 'igPay atinlay siay oolcay'
# 'This is my string' -> 'hisTay siay ymay tringsay'
# "Ultima necat" -> 'ltimaUay ecatnay'
# "Lux in tenebris lucet" -> 'uxLay niay enebristay ucetlay'
# "Cucullus non facit monachum" -> 'ucullusCay onnay acitfay onachummay'

def Pig_latin(txt):
    txt = txt.split()
    listn = []
    for i in txt:
        string = ""
        if i.isalpha():
            string  = string + i[1:] + i[0] + "ay"
        else:
            string = string + i
        listn.append(string)
    return " ".join(listn)

print(Pig_latin('Pig latin is cool'))
