import pandas as pd

PREAMBLE = r"""\documentclass[11pt, a4paper]{article}
\usepackage{booktabs}
\begin{document}"""

HEADER = r"""\begin{{table}}[htb]
{indent}\centering{caption}{label}
{indent}\begin{{tabular}}{{@{{}}{align}@{{}}}}
{indent}{indent}\toprule"""

FOOTER = r"""{indent}{indent}\bottomrule
{indent}\end{{tabular}}
\end{{table}}"""

LABEL = "\n{indent}\\label{{{label}}}"
CAPTION = "\n{indent}\\caption{{{caption}}}"


def create_latex_table(
    file,
    sep=",",
    caption="",
    label="",
    align="c",
    units=None,
    escape=True,
    fragment=False,
    header=True,
    index=False,
):
    """
    Creates a LaTeX table from a CSV file.

    Args:
        file (str): Path to the CSV file.
        sep (str): Column separator. Default: ','.
        caption (str): Caption of the table. Default: ''.
        label (str): Label of the table, for referencing it. Default: ''.
        align (str): Alignment for the columns of the table. Default: 'c'.
        units (list): List of units for each column. Default: None.
        escape (bool): Whether to escape special LaTeX characters. Default: True.
        fragment (bool): Whether to output only the tabular environment. Default: False.
        header (bool): Whether the first row is a header. Default: True.
        index (bool): Whether to include the DataFrame index in the table. Default: False.

    Returns:
        str: LaTeX code for the table.
    """
    df = pd.read_csv(file, sep=sep, header=0 if header else None)

    if escape:
        df = df.map(
            lambda x: str(x).translate(
                str.maketrans(
                    {
                        "#": r"\#",
                        "$": r"\$",
                        "%": r"\%",
                        "&": r"\&",
                        "_": r"\_",
                        "{": r"\{",
                        "}": r"\}",
                    }
                )
            )
        )
    indent = "" if fragment else "    "

    column_format = format_alignment(align, len(df.columns))

    if header:
        header_row = " & ".join(df.columns) + r" \\"
    else:
        header_row = " & ".join([""] * len(df.columns)) + r" \\"

    rows = [" & ".join(map(str, row)) + r" \\" for _, row in df.iterrows()]

    if units:
        units_row = (
            " & ".join(f"[{u}]" if u not in ("-", "/", "0") else "" for u in units)
            + r" \\"
        )
        rows.insert(0, units_row)

    if header:
        rows.insert(0, header_row)
        rows.insert(1, indent + indent + r"\midrule")

    content = "\n".join(indent + indent + row for row in rows)

    if not fragment:
        table_header = HEADER.format(
            label=add_label(label, indent),
            caption=add_caption(caption, indent),
            align=column_format,
            indent=indent,
        )
        table_footer = FOOTER.format(indent=indent)
        return "\n".join((table_header, content, table_footer))
    else:
        return content
    

def format_alignment(align, length):
    """Formats the column alignment."""
    if any(ch not in "lcr" for ch in align):
        align = "c"

    if len(align) == 1:
        return length * align
    elif len(align) == length:
        return align
    else:
        return "{:c<{l}.{l}}".format(align, l=length)


def add_label(label, indent):
    """Creates a table label."""
    return LABEL.format(label=label, indent=indent) if label else ""


def add_caption(caption, indent):
    """Creates a table caption."""
    return CAPTION.format(caption=caption, indent=indent) if caption else ""


def save_latex_table(table, outfile, replace=False):
    """Saves the LaTeX table to a file."""
    mode = "w" if replace else "a"
    with open(outfile, mode) as out:
        out.write(table)
        out.write("\n\n")
    print(f"The table is {'written to' if replace else 'appended to'} {outfile}")


def create_complete_latex_document(tables, outfile, replace=False):
    """Creates a complete LaTeX document with the given tables."""
    content = [PREAMBLE] + tables + [r"\end{document}"]
    save_latex_table("\n\n".join(content), outfile, replace)
