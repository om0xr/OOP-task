class VotingSystem:
    def __init__(self):
        self.__candidates = {}

    def add_candidate(self, name):
        self.__candidates[name] = 0

    def remove_candidate(self, name):
        if name in self.__candidates:
            del self.__candidates[name]

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1

    def display_winner(self):
        if self.__candidates: # هنا بيتاكد ان في مرشحين وان القاموس مش فاضي
            winner = max(self.__candidates, key=self.__candidates.get)
            return f"The winner is: {winner} with {self.__candidates[winner]} votes"
        return "No candidates available"

voting = VotingSystem()
voting.add_candidate("Omar")
voting.add_candidate("ahmed")
voting.vote_to_candidate("Omar")
voting.vote_to_candidate("Omar")
voting.vote_to_candidate("ahmed")
print(voting.display_winner())
