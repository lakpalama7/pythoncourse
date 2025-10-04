
country="USA"

match country:
    case "United State" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Nepal":
        print("NPL")
    case _:
        print("Unkown country")


OUTPUT:
US
