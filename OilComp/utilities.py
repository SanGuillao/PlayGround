def getUserInputFromMenu(menu):
    try:
        user_input = int(input(menu))
        return user_input
    except ValueError:
        while True:
            try:
                user_input = int(input("Please enter an option from the"
                    " menu: "))
                return user_input
            except ValueError:
                pass
                
