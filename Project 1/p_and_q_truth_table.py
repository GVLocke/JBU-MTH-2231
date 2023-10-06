num_columns = 7
column_width = 11
header = "|{}|{}|{}|{}|{}|{}|{}|".format(
    # print the header row, centered in each column
    str("p").center(column_width),
    str("q").center(column_width),
    str("p and q").center(column_width),
    str("p or q").center(column_width),
    str("p xor q").center(column_width),
    str("p -> q").center(column_width),
    str("p <-> q").center(column_width),
)
line = "+{}+".format(
    "+".join(["{}".format("-" * (column_width)) for i in range(num_columns)])
)
A = [True, False]

print(line)
print(header)
print(line)
for p in A:
    for q in A:
        values = [p, q, p and q, p or q, p ^ q, q if p else not p, p == q]
        row = "|{}|".format(
            "|".join(["{}".format(str(value).center(column_width)) for value in values])
        )
        print(row)
        print(line)
