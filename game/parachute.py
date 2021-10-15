from game.console import Console

class Parachute:
    
    def __init__(self):
        self.console = Console()
        self.parachute = ["  __ ", " /___\ ", " \   / ", "  \ /  ", "   0  ", "  /|\   ", "  / \  ",  "", "^^^^^^^"]            

    def draw_parachute(self):
        for piece in self.parachute:
            self.console.write(piece)

    def cut_parachute_piece(self):
        self.parachute.pop(0)

    def has_parachute(self):
        return len(self.parachute) == 4

    def parachute_gone(self):
        self.parachute[0].replace('0', 'X')
