import io

from nbformat import reader
import matplotlib.pyplot as plt


def execute_notebook(nbfile, silent=True):
    """
    execute a notebook file
    Args:
        nbfile: the filename
        silent: should output be hidden.

    Returns: Nothing

    """
    with io.open(nbfile) as f:
        nb = reader.read(f)

    ip = get_ipython()

    for cell in nb.cells:
        if cell.cell_type != 'code':
            continue
        ip.run_cell(cell.source, silent=silent)


def cross_product(lists):
    """
    Returns a generator over all tuples in the cross product of the lists in `lists`.
    Args:
        lists: a list of lists
    Returns:
        generator that generates all tuples in the cross product.
    """
    if len(lists) == 0:
        yield ()
    else:
        for prev_tuple in cross_product(lists[1:]):
            for head in lists[0]:
                yield (head,) + prev_tuple


def plot_bar_graph(values, labels):
    """
    Plots a bar graph.
    Args:
        values: bar values.
        labels: bar labels

    Returns: None

    """
    plt.xticks(range(0, len(values)), labels)
    plt.bar(range(0, len(values)), values, align='center')


    # LATEX_MACROS = """
    # $$
    # \newcommand{\prob}{p}
    # \newcommand{\vocab}{V}
    # \newcommand{\params}{\boldsymbol{\theta}}
    # \newcommand{\param}{\theta}
    # \DeclareMathOperator{\perplexity}{PP}
    # \DeclareMathOperator{\argmax}{argmax}
    # \newcommand{\train}{\mathcal{D}}
    # \newcommand{\counts}[2]{\#_{#1}(#2) }
    # $$
    # """
    #
    #
    # def load_latex_macros():
    #     ip = get_ipython()
    #     ip.run_cell(LATEX_MACROS, silent=True)
