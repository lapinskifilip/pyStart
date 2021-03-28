from math import floor

liquid = float(input('Ilość płynu dostarczonego w L: '))
bottle_filled = 0.33 - (0.33 * 0.12)

bottles = liquid / bottle_filled
filled = floor(bottles)

left = round(((bottles - filled) * bottle_filled), 2)

print(f'Napełniono {filled} butelek. Pracownikowi pozostało: {left} ml płynu')
