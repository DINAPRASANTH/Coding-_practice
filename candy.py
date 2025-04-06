class Solution(object):
    def distributeCandies(self, candyType):
        eatable=len(candyType)/2
        typesofcandy=len(set(candyType))

        if eatable>typesofcandy:
            return typesofcandy
        else:
            return eatable
