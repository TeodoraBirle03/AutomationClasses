lunile_anului = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31,
}
def calendar(luna):
    for luna in lunile_anului:
        return lunile_anului.get(luna)

print(calendar('November'))
print(calendar('February'))
print(calendar('June'))

