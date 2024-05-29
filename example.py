import os

import pandas as pd

from csvtex import create_latex_table

if __name__ == "__main__":
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
    table = create_latex_table(temp_file, caption="Sample_Table", label="tab:sample")
    print(table)
    assert r"\begin{table*}" in table
    assert r"\label{tab:sample}" in table
    assert "John & 25 & New York" in table

    # Clean up the temporary file
    os.remove(temp_file)
