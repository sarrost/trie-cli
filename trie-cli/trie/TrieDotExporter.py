from anytree import Node
from anytree.exporter import DotExporter
import os

def export_trie(
    trie, img_filename='trie.png', graphviz_filename=None
):
    if not trie.empty():
        words = trie.list_words()
        for i in range(len(words)):
            words[i] = '*' + words[i]

        nodes = {}
        root = None
        count = 0
        for word in words:
            parent_node = None
            parent_node_label = ""
            for i, val in enumerate(word):
                if i not in nodes:
                    nodes[i] = {}
                key = parent_node_label + val
                count += 1
                if key not in nodes[i]:
                    nodes[i][key] = Node(
                        key, parent=parent_node, display_name=val
                    )

                if root is None:
                    root = nodes[i][key]

                parent_node = nodes[i][key]
                parent_node_label += val

        DotExporter(
            nodes[0]["*"],
            nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name)
        ).to_dotfile(
            'trie.graphviz.txt' if graphviz_filename is None
            else graphviz_filename
        )

        DotExporter(
            nodes[0]["*"],
            nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name)
        ).to_picture(img_filename)

        if graphviz_filename is None:
            os.remove('trie.graphviz.txt')
