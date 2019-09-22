#!/usr/bin/python
"""Simple cli for trie data structure implementation.

    This is a basic application with basic functionality. It allows
    for the creation of a trie data structure which can be exported
    to an image file and graphviz dot formatted file representing
    the vertices and egdes of the data structure.

    Default behaviour is to use one file to read/write the words
    represented by the trie, but this can be changed in the options.

    For details execute the following on the command line:

        $ ./trie.py -h

    or

        $ python trie.py -h

    if the former fails.
"""
import cli.app
from trie.Trie import Trie
from trie.TrieDotExporter import export_trie


@cli.app.CommandLineApp
def ls(app):
    params = vars(ls.params)
    filename = params['file']
    img_output = params['output']
    graphviz_output = params['graphviz_output']
    input_list = params['input']
    input_file = params['input_file']
    add = params['add']
    add_filename = params['add_file']
    remove = params['remove']
    remove_filename = params['remove_file']
    search = params['search']

    specified_new = params['new']
    specified_list = params['list']

    specified_input_list = True if input_list is not None else False
    specified_input_file = True if input_file is not None else False
    specified_add = True if add is not None else False
    specified_add_filename = True if add_filename is not None else False
    specified_remove = True if remove is not None else False
    specified_remove_filename = True if remove_filename is not None else False
    specified_search = True if search is not None else False

    if img_output is None:
        img_output = 'trie.png'
    if filename is None:
        filename = 'trie.txt'

    # load trie
    t = Trie()
    if not specified_new:
        t.load(filename)
    if specified_input_file:
        t.load(input_file)
    elif specified_input_list:
        t = Trie(input_list.split())

    # add/insert
    if specified_add_filename:
        with open(add_filename) as file:
            words = file.read().split()
            t.add_many(words)
    if specified_add:
        t.add_many(add.split())

    # remove
    if specified_remove_filename:
        with open(remove_filename) as file:
            words = file.read().split()
            t.remove_many(words)
    if specified_remove:
        t.remove_many(remove.split())

    # print
    if specified_list:
        words = t.list_words()
        out = ''
        for word in words:
            out += word + ' '
        print(out)
    if specified_search:
        out = ''
        if t.contains(search):
            out = 'Successfully found \'' + search + '\' in trie!\nPrefixes: '
            prefixes = t.prefixes_of(search)
            if prefixes != []:
                out += words[0]
                words = words[1:]
                for word in prefixes:
                    out += ', ' + word
        else:
            out = f'\'{search}\' was not found in the trie.'
        print(out)

    # save
    t.save(filename)
    export_trie(t, img_filename=img_output, graphviz_filename=graphviz_output)


ls.add_param(
    "-f", "--file", action="store",
    help="read/write the trie (word(s)) to FILE (default is `trie.txt`)."
)
ls.add_param(
    "-n", "--new", action="store_true",
    help="start with new empty trie."
)
ls.add_param(
    "-o", "--output", action="store",
    help="image output filename (default is `trie.png`)."
)
ls.add_param(
    "-g", "--graphviz-output", action="store",
    help="generate dot graphviz output file called GRAPHVIZ_OUTPUT."
)
ls.add_param(
    "-i", "--input", action="store",
    help="build trie from word(s)."
)
ls.add_param(
    "-I", "--input-file", action="store",
    help="build trie from word(s) in INPUT_FILE."
)
ls.add_param(
    "-a", "--add", action="store",
    help="add word(s) to trie."
)
ls.add_param(
    "-A", "--add-file", action="store",
    help="add word(s) in ADD_FILE to trie."
)
ls.add_param(
    "-r", "--remove", action="store",
    help="remove word(s) from trie."
)
ls.add_param(
    "-R", "--remove-file", action="store",
    help="remove word(s) in REMOVE_FILE from trie."
)
ls.add_param(
    "-l", "--list", action="store_true",
    help="list word(s) in loaded trie " +
         "(after all operations have been performed)."
)
ls.add_param(
    "-s", "--search", action="store",
    help="search trie for SEARCH and list all " +
         "prefixes to SEARCH if found (i.e. FILE)."
)


if __name__ == "__main__":
    ls.run()
