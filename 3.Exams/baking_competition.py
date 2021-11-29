num_people = int(input())

total_baked = 0
m_cookies = 0
m_cakes = 0
m_pancakes = 0
baking = False
for i in range(num_people):
    name = input()
    cookies = 0
    cakes = 0
    pancakes = 0
    baking = False
    while not baking:
        type_pastry = input()

        if type_pastry == 'Stop baking!':
            baking = True
        if baking:
            print(f"{name} baked {cookies} cookies, {cakes} cakes and {pancakes} waffles.")
            break
        num_pastry = int(input())
        total_baked += num_pastry
        if type_pastry == 'cookies':
            cookies += num_pastry
            m_cookies += num_pastry * 1.50
        elif type_pastry == 'cakes':
            cakes += num_pastry
            m_cakes += num_pastry * 7.80
        elif type_pastry == 'waffles':
            pancakes += num_pastry
            m_pancakes += num_pastry * 2.30

total_money = m_cookies + m_cakes + m_pancakes
print(f"All bakery sold: {total_baked}")
print(f"Total sum for charity: {total_money:.2f} lv.")