import random
import credentials
from pydnz import Dnz

dnz = Dnz(credentials.dnz_key)

class Poet:
    def __init__(self):
        pass

    def seed(self):
        searching = True

        # select a random source
        source = random.choice([
            'TAPUHI',
            'Te Papa Collections Online',
            'tv3.co.nz',
        ])
        # query API until something interesting turns up
        while searching:
            results = dnz.search(
                '',
                page=random.randint(1,100000),
                per_page=1,
                _and={'display_collection':[source]},
                fields=['description'],
            )
            # check whether results have records
            if not results.records:
                continue
            seed = results.records[0]['description']
            print seed
            if len(seed) > 21:
                searching = False

        seed = self.nurture(seed)
        
        return seed

    def nurture(self, seed):
        if random.choice([1,2]) >= 1:
            seed = seed.lower()
        seed = seed.replace("&apos;", "'")
        seed = seed.replace("&quot;", "'")
        seed = seed.strip()

        return seed.encode('utf-8')

    def indent(self, max_dent=6):
        return ' ' * random.choice(range(max_dent))

    def chance(self, chance=0.5):
        if random.random() > chance:
            return True
        return False

    def compose(self):
        """ Write poem from metadata seed. """
        seed = self.seed()
        draft = [self.indent()]
        parts = seed.split(' ')

        odds = random.randint(40,75) / 100.
        print odds

        for part in parts:
            part = part.strip()
            draft.append(part)

            if part.endswith((',', '.')):
                draft.extend(['\n', self.indent()])
            elif self.chance(odds):
                draft.extend(['\n', self.indent()])
            else:
                draft.append(' ')
            if self.chance(0.92):
                draft.append('\n')

        poem = self.edit(draft)
        return poem.encode('utf-8')

    def breaker(self, s):
        if not '.' in s:
            return s
        parts = s.split('.')
        s = '.'.join(parts[:-1])

        return s + '.'

    def edit(self, draft):
        """ Tidy poem & get under 140 chars """
        elements = []
        for element in draft:
            elements.append(element)
            if len(''.join(elements)) > 140:
                elements.pop(-1)
                break

        poem = self.breaker(''.join(elements))

        return poem.rstrip()

    def assess(self, poem):
        """ Check if poem's worth publishing. """
        if not '\n' in poem:
            return False
        return True


def main():
    poet = Poet()
    happy = False
    while not happy:
        poem = poet.compose()
        happy = poet.assess(poem)
    print '\n{}\n'.format(poem)

if __name__ == '__main__':
    main()