# 📊 csvtex - Convert CSV Files to LaTeX Tables 📄

[![GitHub repo](https://img.shields.io/badge/GitHub-scottsuk0306/csvtex-blue?logo=github)](https://github.com/scottsuk0306/csvtex)
[![PyPI package](https://img.shields.io/pypi/v/csvtex?logo=pypi)](https://pypi.org/project/csvtex/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python versions](https://img.shields.io/pypi/pyversions/csvtex)](https://pypi.org/project/csvtex/)

`csvtex` is a Python package that allows you to effortlessly convert CSV files into beautifully formatted LaTeX tables. 🎨💅

## 🚀 Installation

You can install `csvtex` using pip:

```bash
pip install csvtex
```

## 🎓 Usage

Here's a quick example of how to use `csvtex`:

```python
from csvtex import create_latex_table, save_latex_table

# Create a LaTeX table from a CSV file
table = create_latex_table('data.csv', caption='My Table', label='tab:mytable')

# Save the LaTeX table to a file
save_latex_table(table, 'table.tex')
```

For more detailed usage and examples, please refer to the [documentation](https://github.com/scottsuk0306/csvtex/wiki).

## ✨ Features

- 📥 Convert CSV files to LaTeX tables with ease
- 🎨 Customize table captions, labels, and column alignments
- 🔧 Specify units for each column
- 🚫 Automatically escape special LaTeX characters
- 📜 Generate complete LaTeX documents with multiple tables
- 🌐 Support for different CSV separators (comma, semicolon, tab)
- 🐍 Compatible with Python 3.6+

## 🤝 Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request on the [GitHub repository](https://github.com/scottsuk0306/csvtex).

## 📄 License

`csvtex` is released under the [MIT License](https://opensource.org/licenses/MIT).

## 🙏 Acknowledgements

- This project was inspired by the need for a simple and efficient way to convert CSV data into LaTeX tables.
- Thanks to the open-source community for their valuable contributions and support.

---

🌟 Give `csvtex` a try and unleash the power of beautiful LaTeX tables! 🌟