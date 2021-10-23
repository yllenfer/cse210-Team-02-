from game.console import Console

class Parachute:
    
    def __init__(self):
        self.console = Console()
        self.parachute = ["  __ ", " /___\ ", " \   / ", "  \ /  ", "   0  ", "  /|\   ", "  / \  ",  "", "^^^^^^^"]            

    def draw_parachute(self):
        """
        Draws the parachute in the form of a for loop iterating through a list.
        """
        for piece in self.parachute:
            self.console.write(piece)

    def cut_parachute_piece(self):
        """
        Will cut the parachute piece by getting rid of the first item in the list
        """
        self.parachute.pop(0)

    def has_parachute(self):
        """
        Will determine if there is no more parachute by seeing how many items are in the list
        """
        return len(self.parachute) == 4

    def parachute_gone(self):
        """
        When there is no more parachute, the guy's head will turn from a 0 into an X
        """
        self.parachute[0].replace('0', 'X')
