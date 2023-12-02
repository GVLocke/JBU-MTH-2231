# Given the number of elements in the intersection of three sets,
# the number of elements in each pairwise intersection of these sets,
# and the number of elements in each set, find the number of elements in their union.


def three_set_union(
    length_of_set1,
    length_of_set2,
    length_of_set3,
    set1_set2_intersection,
    set2_set3_intersection,
    set1_set3_intersection,
    all_set_intersection,
):
    return (
        length_of_set1
        + length_of_set2
        + length_of_set3
        - set1_set2_intersection
        - set2_set3_intersection
        - set1_set3_intersection
        + all_set_intersection
    )


length_of_set1 = int(input("Enter the length of the first set: "))
length_of_set2 = int(input("Enter the length of the second set: "))
length_of_set3 = int(input("Enter the length of the third set: "))
set1_set2_intersection = int(
    input("Enter the length of the intersection of the first and second sets: ")
)
set2_set3_intersection = int(
    input("Enter the length of the intersection of the second and third sets: ")
)
set1_set3_intersection = int(
    input("Enter the length of the intersection of the first and third sets: ")
)
all_set_intersection = int(
    input("Enter the length of the intersection of all three sets: ")
)
print(
    three_set_union(
        length_of_set1,
        length_of_set2,
        length_of_set3,
        set1_set2_intersection,
        set2_set3_intersection,
        set1_set3_intersection,
        all_set_intersection,
    )
)
