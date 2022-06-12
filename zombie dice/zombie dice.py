import zombiedice, random

class Random:
    #randomly decides if it will continue or stop
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll() # first roll

        count = random.randint(0,1)
        while diceRollResults is not None and count == 0:
            diceRollResults = zombiedice.roll() # roll again
            count = random.randint(0,1)

class Brains2:
    #stops rolling after it has rolled two brains
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):

        brains = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else: 
                break

class Shotguns2:
    #stops rolling after it has rolled two shotguns
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):

        shotguns = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else: 
                break

class Max4:
    #initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):

        rolls = random.randint(1, 4)
        shotguns = 0

        while rolls > 0:
            diceRollResults = zombiedice.roll()
            shotguns += diceRollResults['shotgun']

            if(shotguns > 1):
                break
            rolls -= 1
        
        

class MoreSGThanBrains:
    #stops rolling after it has rolled more shotguns than brains
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):

        shotguns = 0
        brains = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns > brains:
                break
            diceRollResults = zombiedice.roll()




zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random (example)'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading (example)'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns (example)', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun(example)', minShotguns=1),
    # Add any other zombie players here.
    Random(name='random bot'),
    Brains2(name= '2 brains bot'),
    Shotguns2(name= '2 shotguns bot'),
    Max4(name= 'max 4 bot'),
    MoreSGThanBrains(name= 'shotgun > brains bot')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
