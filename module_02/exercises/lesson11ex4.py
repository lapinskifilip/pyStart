text = "12 kilogramow jablek, 10 kilogramow gruszek, 20 kilogramow sliwek"

apples = text.split(', ')[0]
pears = text.split(', ')[1]
plums = text.split(', ')[2]

math = int(apples[0:2]) + int(pears[0:2]) + int(plums[0:2])

print(f'Owoce warzą razem {math} {text[3:13]}')
