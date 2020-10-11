# Vocabcli

Vocabcli is a simple CLI tool to create lists of vocab and help you learn them.

## Installation

Clone this repo and run the `install.sh` script. You need to have Python installed.

## Usage

For now, the only fonction implemented is the "challenge", which consist in a test: prompted with the words of the list one after another, you must provide the translation. If you fail, you'll be prompted with the correction. To take a challenge, run:

~~~ shell
vocabcli challenge <name-of-your-list>
~~~

For example, to take a challenge on the "test" list:

~~~ shell
vocabcli challenge test
~~~

To add your list of words, just add a .json file with the name of your list in the "wordlists" folder.

## TODO

- add list creation function to create lists from CLI
- add csv import
- add score at the end of a challenge
- keep record of highscores
- add other learning modes