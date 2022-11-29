
def make_coffee(size, sugar_dose=2):
    if sugar_dose > 5:
        return 'Слишком много сахара!'
    else:
        return f'Ваш кофе объемом {size} мл с {sugar_dose} кусочками сахара готов!'

text = make_coffee(300)

print(text)
