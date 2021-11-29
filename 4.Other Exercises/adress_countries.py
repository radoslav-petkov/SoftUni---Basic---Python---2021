import xlrd
import tkinter

loc = ('C:\Personal\Programming\Addresses.xlsx')

wb = xlrd.open_workbook(loc)

sheet_addresses = wb.sheet_by_index(0)
sheet_cards = wb.sheet_by_index(1)
country = input('Enter Country:')
coriant_card = input('Enter Coriant SFP LX,SX or RJ:')
end_print = True


for i in range(0,92):
    if country == sheet_addresses.cell_value(i, 1):
        while end_print:
            i += 1
            if sheet_addresses.cell_value(i, 1) == "":
                print('-------------------------------------------')
                print(f'City:{sheet_addresses.cell_value(i, 3)} Address:{sheet_addresses.cell_value(i, 4)}')
                print('-------------------------------------------')
            else:
                end_print = False
        break
    elif i == 91:
        print('Wrong Country!!!')

for row in range(0,6):
    if coriant_card == sheet_cards.cell_value(row, 0):
        print(f'Part number: {sheet_cards.cell_value(row, 1)} Description: {sheet_cards.cell_value(row, 2)}')