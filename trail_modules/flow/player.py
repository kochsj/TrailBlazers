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
    print('Every wagon train needs a leader...')
    print('1. Banker')
    print('2. Carpenter')
    print('3. Farmer')
    response = ''
    while response != '1' and response != '2' and response != '3':
        response = input('What occupation does your leader have?')
    if response == '1':
        money = 1600
    if response == '2':
        money = 800
    if response == '3':
        money = 400

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

    return (wagon_party, money)
