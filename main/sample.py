AXIS = range(4)

winners = []
def convert(x, y, z):
    return x + 4 * y + 16 * z

for x in AXIS:
    for y in AXIS:
        winners.append([convert(x, y, z) for z in AXIS])
for y in AXIS:
    for z in AXIS:
        winners.append([convert(x, y, z) for x in AXIS])
for z in AXIS:
    for x in AXIS:
        winners.append([convert(x, y, z) for y in AXIS])

for x in AXIS:
    winners.append([convert(x, y, y) for y in AXIS])
    winners.append([convert(x, y, 4-y) for y in AXIS])
for y in AXIS:
    winners.append([convert(z, y, z) for z in AXIS])
    winners.append([convert(4-z, y, z) for z in AXIS])
for z in AXIS:
    winners.append([convert(x, x, z) for x in AXIS])
    winners.append([convert(x, 4-x, z) for x in AXIS])

winners.append([convert(x, x, x) for x in AXIS])
winners.append([convert(x, x, 4-x) for x in AXIS])
winners.append([convert(x, 4-x, x) for x in AXIS])
winners.append([convert(x, 4-x, 4-x) for x in AXIS])

# for win in winners:
#     print(str(win))

# print(len(winners))

msg = ' '.join(map(str, AXIS))
print(msg)
msg = ' '.join(str(x) for x in range(4))
print(msg)
