value = 11

match value:
    case 10|11:
        print("ok")
    case 15:
        print("warning")
    case _:
        print("unknown code")