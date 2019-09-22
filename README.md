# trie-cli
A simple cli application for the implementation of a 
[trie data structure](https://en.wikipedia.org/wiki/Trie) in python.

## Requirements
* [Python 3](https://www.python.org/)
* [pip](https://pypi.org/project/pip/)
* [graphviz](https://www.graphviz.org/)
* An image viewer (optional)

## Installation
`git clone` or download this repo. In the main directory execute the following
command:
```bash
    $ ./install.py
```
All required python packages and backend utilities should be installed should 
be installed now.

## Usage
Switch to the `trie-cli/` directory and execute the following:
```bash
    $ ./trie.py -h
```
This will bring up a help menu explaining all available options.

### Examples

Creates an empty trie and inserts the words 'I', 'never', ..., 'short' into the
trie. Also creates a visual of the trie and saves it to `trie.png`.
```bash
    $ ./trie.py -i 'I never knew recess would be so short'
```

Reads words from plaintext file `trie.txt` and inserts all words found into
trie. Attempt to add word 'love' to the trie and remove word 'recess' from trie. Finally saves all words in trie
back to `trie.txt` and print all words to terminal.
```bash
    $ ./trie.py -a love -r hatred -l
```

## Troubleshooting
If you're having issues running any of the commands above ensure that the python
and shell files have sufficient permissions to execute. If all else fails simply
do:
```bash
    $ pip install -r requirements.txt
```
And
```bash
    $ python trie.py -h
```
to execute the files.






