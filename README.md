# metadata.poems

Script to pull metadata from descriptions of digital items via the DigitalNZ API and turn them into short poems.

## Usage

1. Update `credentials.py` with your DigitalNZ API key: http://digitalnz.org/api_keys
2. Run `poet.py` to print a poem to the console.

## Notes
I'm still mucking about with this & the code needs a tidy.
- `Poet.seed()` grabs a random item description from the DigitalNZ API. Tweak the search call to alter the types of starting text.
- `Poet.compose()` builds the poem, looping over each word & inserting various indents and newlines according to randomised starting conditions. 
- `Poet.edit()` trims the poem to 140 characters or less and, if there is at least one full sentence, removes partial ending sentences.

This isn't properly hooked it up to Twitter in an automated way yet. I leave that as an exercise for the reader.
