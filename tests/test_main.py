# test_main.py

import os

import pandas as pd

from csvtex import create_complete_latex_document, create_latex_table, save_latex_table


def test_create_latex_table():
    # Create a sample DataFrame
    data = {
        "Name": ["John", "Alice", "Bob"],
        "Age": [25, 30, 35],
        "City": ["New York", "London", "Paris"],
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to a temporary CSV file
    temp_file = "temp.csv"
    df.to_csv(temp_file, index=False)

    # Test creating a LaTeX table
    table = create_latex_table(temp_file, caption="Sample Table", label="tab:sample")
    assert r"\begin{table*}" in table
    assert r"\label{tab:sample}" in table
    assert "John & 25 & New York" in table

    # Clean up the temporary file
    os.remove(temp_file)


def test_create_latex_table_without_header():
    # Create a sample DataFrame
    data = [["John", 25, "New York"], ["Alice", 30, "London"], ["Bob", 35, "Paris"]]
    df = pd.DataFrame(data)

    # Save the DataFrame to a temporary CSV file
    temp_file = "temp.csv"
    df.to_csv(temp_file, index=False, header=False)

    # Test creating a LaTeX table without header
    table = create_latex_table(temp_file, header=False)
    assert r"\begin{table*}" in table
    assert "John & 25 & New York" in table
    assert "Alice & 30 & London" in table
    assert "Bob & 35 & Paris" in table

    # Clean up the temporary file
    os.remove(temp_file)


def test_save_latex_table():
    # Create a sample LaTeX table
    table = r"\begin{table}\centering\begin{tabular}{lrc}Col1 & Col2 & Col3 \\\midrule Row1 & Row2 & Row3 \\\end{tabular}\end{table}"

    # Save the table to a temporary file
    temp_file = "temp.tex"
    save_latex_table(table, temp_file)

    # Check if the file was created and contains the table
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as file:
        content = file.read()
        assert table in content

    # Clean up the temporary file
    os.remove(temp_file)


def test_create_complete_latex_document():
    # Create sample tables
    table1 = r"\begin{table}\centering\begin{tabular}{lr}A & B \\\midrule 1 & 2 \\\end{tabular}\end{table}"
    table2 = r"\begin{table}\centering\begin{tabular}{lr}C & D \\\midrule 3 & 4 \\\end{tabular}\end{table}"

    # Create a complete LaTeX document
    temp_file = "temp.tex"
    create_complete_latex_document([table1, table2], temp_file)

    # Check if the file was created and contains the tables
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as file:
        content = file.read()
        assert r"\documentclass" in content
        assert table1 in content
        assert table2 in content
        assert r"\end{document}" in content

    # Clean up the temporary file
    os.remove(temp_file)
