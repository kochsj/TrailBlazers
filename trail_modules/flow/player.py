class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.clothed = True

def character_creation():
    """
    Function to create the characters in the party
    creates instances of the Character class
    A leader and 4 members.
    Returns a list of the members for use by the game.
    """
    wagon_party = []
    response = input('What is your leader\'s first name? ')
    leader = Character(response)
    wagon_party.append(leader)
    print(f'1. {response}')

    response = input('What is the first name of your next member? ')
    member_a = Character(response)
    wagon_party.append(member_a)
    print(f'2. {response}')

    response = input('What is the first name of your next member? ')
    member_b = Character(response)
    wagon_party.append(member_b)
    print(f'3. {response}')

    response = input('What is the first name of your next member? ')
    member_c = Character(response)
    wagon_party.append(member_c)
    print(f'4. {response}')

    response = input('What is the first name of your next member? ')
    member_d = Character(response)
    wagon_party.append(member_d)
    print(f'5. {response}')

    return wagon_party
