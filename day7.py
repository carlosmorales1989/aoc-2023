from functools import cmp_to_key

part2 = True

def get_card_score(card):
    if part2:
        card_score = {'T':10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    else:
        card_score = {'T':10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if card in card_score:
        return card_score[card]
    else:
        return int(card)

def compare(hand1, hand2):
    if hand1.type != hand2.type:
        return hand2.type - hand1.type
    else:
        for i in range(5):
            score1 = get_card_score(hand1.hand[i])
            score2 = get_card_score(hand2.hand[i])
            if score1 != score2:
                return score1-score2
    print(f"err!{hand1}|{hand2}")
    return 0

class HandType:
    FIVE_KIND = 1
    FOUR_KIND = 2
    FULL_HOUSE = 3
    THREE_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

class Hand:

    def __init__(self, line) -> None:
        hand, bid = line.strip().split()
        self.hand = hand
        self.bid = int(bid)

        reps = {}
        for card in self.hand:
            if card not in reps:
                reps[card] = 0
            reps[card]+=1
        
        rep_counts = {i:[] for i in range(6)}
        for card in reps:
            print(f"{reps[card]}:{rep_counts}")
            rep_counts[reps[card]].append(card)

        if part2:
            self.set_type_part2(rep_counts, reps)
        else:
            self.set_type_part1(rep_counts)

    def set_type_part1(self, rep_counts):

        if len(rep_counts[5]) == 1:
            self.type = HandType.FIVE_KIND
        elif len(rep_counts[4]) == 1:
            self.type = HandType.FOUR_KIND
        elif len(rep_counts[3]) == 1 and len(rep_counts[2]) == 1:
            self.type = HandType.FULL_HOUSE
        elif len(rep_counts[3]) == 1:
            self.type = HandType.THREE_KIND
        elif len(rep_counts[2]) == 2:
            self.type = HandType.TWO_PAIR        
        elif len(rep_counts[2]) == 1:
            self.type = HandType.ONE_PAIR
        else:
            self.type = HandType.HIGH_CARD
        
    def set_type_part2(self, rep_counts, reps):
        j_count = reps.get('J',0)
        if j_count == 5:
            max_reps = 0
        else:
            max_reps = max([reps[card] for card in reps if card != 'J'])
        
        if max_reps + j_count == 5:
            self.type = HandType.FIVE_KIND
        elif max_reps + j_count == 4:
            self.type = HandType.FOUR_KIND
        elif (len(rep_counts[3]) == 1 and len(rep_counts[2]) == 1) or (len(rep_counts[2]) == 2 and j_count == 1):
            self.type = HandType.FULL_HOUSE
        elif max_reps + j_count == 3:
            self.type = HandType.THREE_KIND
        elif (len(rep_counts[2]) == 2) or (len(rep_counts[2]) == 1 and j_count == 1):
            self.type = HandType.TWO_PAIR        
        elif len(rep_counts[2]) == 1 or j_count == 1:
            self.type = HandType.ONE_PAIR
        else:
            self.type = HandType.HIGH_CARD
    
    def __str__(self) -> str:
        return f"Hand {self.hand}. Type:{self.type}"

    def __repr__(self) -> str:
        return str(self)

with open('data/day7') as day7:
    hands = []
    for line in day7:
        hand = Hand(line)        
        hands.append(hand)
        print(hand)
    sorted_hands =sorted(hands, key=cmp_to_key(compare))
    print(hands)
    print(sorted_hands)
    result = sum([sorted_hands[i].bid * (i+1) for i in range(len(sorted_hands))])
    print(result)
