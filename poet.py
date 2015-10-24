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
            #'TAPUHI',
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
        seed= seed.encode('utf-8')
        if random.choice([0,1]):
            seed = seed.lower()
        seed = seed.replace("&apos;", "'")
        seed = seed.replace("&quot;", "'")

        return seed.strip()

    def chance(self, chance=0.5):
        if random.random() > chance:
            return True
        return False

    def compose(self):
        """ Write poem from metadata seed. """
        seed = self.seed()
        draft = []
        parts = seed.split(' ')

        self.odds = random.randint(42,76) / 100.
        self.indent_lvl = 0
        style = random.choice(['abstract', 'cascade'])
        print self.odds, style

        for part in parts:
            part = part.strip()
            draft.append(part)
            if style == 'abstract':
                draft.append(self.abstract_format(part))
            elif style == 'cascade':
                draft.append(self.cascade_format(part))

        poem = self.edit(draft)
        return poem.encode('utf-8')

    def dent(self, max_dent=6):
        return ' ' * random.choice(range(max_dent))

    def abstract_format(self, part):
        element = ''
        if part.endswith((',', '.')) or self.chance(self.odds):
            element = '{}{}'.format('\n', self.dent())
        if self.chance(0.92):
            if element:
                element = element + '\n'
            else:
                element = '\n\n'
            self.indent_lvl = random.choice([0, 1])
        if not element:
            element = ' '
        return element

    def cascade_format(self, part):
        element = ''
        if part.endswith((',', '.')) or self.chance(self.odds):
            self.indent_lvl += 1
            element = '{}{}'.format('\n', ' ' * self.indent_lvl)
        if self.chance(0.88):
            if element:
                element = element + '\n'
            else:
                element = '\n\n'
            self.indent_lvl = random.choice([0, 1])
        if not element:
            element = ' '
        return element

    def breaker(self, s):
        """ Remove hanging sentences """
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