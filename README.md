# leetSpeak

Leetspeak is a python script used to generate wordlist of leetspeak of a word. 

## What is Leetspeak or Leet?

Leet (or "1337"), also known as eleet or leetspeak, is a system of modified spellings used primarily on the Internet. It often uses character replacements in ways that play on the similarity of their glyphs via reflection or other resemblance

Source: https://en.wikipedia.org/wiki/Leet


## Setup
---

Clone the repository.

`git clone https://github.com/pkdiv/leetSpeak.git`

## Usage
---

`python generate.py -w <phrase>`

### Optional Arguments

|Argument|Purpose|
|----|-----|
|-o / --outputFile| Specify the output filename|
|-l / --level| Specify the level of leetspeak. Level 0 - Simple single character ascii substitutions. Level 1 - Ascii, Multicharacter and also include chacters from utf-8 character set. |
