print(
    "This program determines the satisfiability of a proposition. \
      \nEnter a logical proposition with a maximum of 3 variables (p, q, r). \
      \nAllowed operators: AND (/\), NOT (~), and OR (\/)"
)
statement_string = input("Enter a proposition: ")

# generate a set of the unique characters
statement_string_unique_chars = set(statement_string)

# check if there are any invalid characters
valid_chars = set(["p", "q", "r", "/", "\\", "~"])
if not statement_string_unique_chars.issubset(valid_chars):
    print("Error: string proposition contains invalid characters.")
    exit(1)

# parse the operators
statement_string = statement_string.replace("/\\", " and ")
statement_string = statement_string.replace("\\/", " or ")
statement_string = statement_string.replace("~", " not ")

# check if there are any characters left other than p, q, r, and the operators
statement_string_unique_chars = set(statement_string)
valid_chars = set(["p", "q", "r", " ", "a", "n", "d", "o", "r"])
if not statement_string_unique_chars.issubset(valid_chars):
    print("Error: string proposition contains invalid characters.")
    exit(1)

# try all different combinations of p, q, and r truth values
A = [True, False]
satisfiable = False
if "p" in statement_string and "q" in statement_string and "r" in statement_string:
    for p in A:
        for q in A:
            for r in A:
                if eval(statement_string):
                    satisfiable = True
                    print(
                        "Statement is satisfiable when p is {}, q is {}, and r is {}.".format(
                            p, q, r
                        )
                    )
elif "p" in statement_string and "q" in statement_string:
    for p in A:
        for q in A:
            if eval(statement_string):
                satisfiable = True
                print("Statement is satisfiable when p is {} and q is {}.".format(p, q))
elif "p" in statement_string:
    for p in A:
        if eval(statement_string):
            satisfiable = True
            print("Statement is satisfiable when p is {}.".format(p))
if not satisfiable:
    print("Statement is not satisfiable.")
