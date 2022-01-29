
import random


class Move:
    def __init__(self, name, pp, accuracy, power):
        self.name = name
        self.pp = pp
        self.accuracy = accuracy
        self.power = power

    def use_move(self):
        if (self.pp > 0):
            self.pp -= 1

    def is_available(self):
        if (self.pp > 0):
            return True
        else:
            return False


class Pokemon:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.moves = []
        self.fainted = False

    def __str__(self):
        return self.name

    def take_damage(self, damage):
        self.hp -= damage
        if (self.hp < 1):
            self.fainted = True

    # add move to moves if there is space (max 4)
    def add_move(self, move: Move):
        if len(self.moves) < 4:
            self.moves.append(move)

    # returns the damage to be inflicted
    def attack(self):
        # select random move from moves
        if len(self.moves) > 0:
            move = random.choice(self.moves)
            if move.is_available():
                # check accuracy to see if hit
                if move.accuracy <= random.randint(1,100):
                    move.use_move()
                    return move.name, move.power
        
        # return 0 power for miss, out of pp, or no moves
        return move.name, 0
       


class BattleSimulation:
    def __init__(self, poke1, poke2):
        self.poke1: Pokemon = poke1
        self.poke2: Pokemon = poke2
        self.move_log = []
        self.attacker: Pokemon = poke1
        self.defender: Pokemon = poke2


    def log_move(self, log_str):
        self.move_log.append(log_str)

    def switch_turn(self):
        if self.attacker == self.poke1:
            self.attacker = self.poke2
            self.defender = self.poke1
        else:
            self.attacker = self.poke1
            self.defender = self.poke2

    # take a turn, if on fainted return true
    def handle_turn(self):
        
        move_name, damage = self.attacker.attack()
        self.defender.take_damage(damage)

        log = self.attacker.name + " hit " + self.defender.name + " with " + move_name + " for " + str(damage) + "; " + self.poke1.name + " hp: " + str(self.poke1.hp) + ", " + self.poke2.name + " hp: " + str(self.poke2.hp)
        self.log_move(log)

        if self.defender.fainted:
            self.log_move(self.attacker.name + " is the winner!")
            return False

        self.switch_turn()
        return True

    # Run simulated battle, return winning pokemon
    def simulate(self):
        while(self.handle_turn()):
            continue

if __name__ == "__main__":
    p1 = Pokemon('Charmander')
    p2 = Pokemon('Squirtle')

    m1: Move = Move('Tackle', 25, 80, 15)
    m2: Move = Move('Water Gun', 25, 75, 25)
    m3: Move = Move('Ember', 25, 75, 25)
    m4: Move = Move('Pound', 25, 80, 35)

    p1.add_move(m1)
    p1.add_move(m3)
    p1.add_move(m4)

    p2.add_move(m1)
    p2.add_move(m2)
    p2.add_move(m4)

    battle = BattleSimulation(p1, p2)
    battle.simulate()

    print(len(battle.move_log))
    for log in battle.move_log:
        print(log)


