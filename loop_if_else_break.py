def contains_magic_number(list1, magic_number):
    for i in list1:
        if i == magic_number:
            print("This list contains the magic number")
            # if not add break , will run more meaningless loop
            break
        else:
            print("This list does NOT contain the magic number")


if __name__ == "__main__":
    # ref https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_else_in_a_loop.html
    # ref https://docs.quantifiedcode.com/python-anti-patterns/correctness/else_clause_on_loop_without_a_break_statement.html
    contains_magic_number(range(10), 5)
