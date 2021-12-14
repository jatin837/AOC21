def find(polymer):
    for i, ch in enumerate(polymer):
        try:
            d = ch + polymer[i+1] 
            if d in rule.keys():
                new_polymer = polymer[:i+1] + d + polymer[i+1:]
                print(new_polymer)
                find(new_polymer)
        except:
            pass

