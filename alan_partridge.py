def part(arr):
    alan_terms = ['Partridge', 'PearTree', 'Chat', 'Dan', 'Toblerone', 'Lynn', 'AlphaPapa', 'Nomad']
    count = 0
    result = "Lynn, I've pierced my foot on a spike!!"
    for word in arr:
        if word in alan_terms:
            count += 1
    for word in arr:
        if word in alan_terms:
            result = "Mine's a Pint" + count * '!'
    return result
