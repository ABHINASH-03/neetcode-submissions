class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # Number of cards must be divisible by groupSize
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card
        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1

        # Process cards in sorted order
        for card in sorted(count):
            if count[card] > 0:
                groups = count[card]

                # Try to build groups starting from this card
                for i in range(groupSize):
                    current = card + i

                    if count.get(current, 0) < groups:
                        return False

                    count[current] -= groups

        return True