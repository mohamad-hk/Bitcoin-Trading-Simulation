def find_name_of_day(number_day):
    name_of_day = ""
    match number_day:
        case 0:
            name_of_day = "monday"
        case 1:
            name_of_day = "tuesday"
        case 2:
            name_of_day = "wednesday"
        case 3:
            name_of_day = "thursday"
        case 4:
            name_of_day = "friday"
        case 5:
            name_of_day = "saturday"
        case 6:
            name_of_day = "sunday"

    return name_of_day
