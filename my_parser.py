def parse(feet_inches):
    feet_inches_list = feet_inches.split(" ")
    feet = float(feet_inches_list[0])
    inches = float(feet_inches_list[1])
    return feet, inches


def convert(feet, inches):
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters