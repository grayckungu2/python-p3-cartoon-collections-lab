def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    for string in strings:
        if string in cheeses:
            return string
    return None