# NoteToDoc Python Script
![GitHub](https://img.shields.io/github/license/nestor-rdgz/NoteTOdOC?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/nestor-rdgz/NoteToDoc?color=blue&label=Last%20commit)
![GitHub Repo stars](https://img.shields.io/github/stars/nestor-rdgz/NoteToDoc?color=yellow&label=Stars)
![GitHub forks](https://img.shields.io/github/forks/nestor-rdgz/NoteToDoc?style=social)

This Python script generates a .docx file containing the bibliography and the notes taken in [Zotero](https://www.zotero.org/) *(previously exported in a .csv file)*, to ease the process of writing papers (e.g. surveys and reviews) and thesis. 

## How to use the script?
1. Before using the Python script, make sure you have the necessary packages already installed in your system by running:
    
    `python -m pip install -r requirements.txt`

2. After that, to properly run the script, export you bibliography elements from Zotero to a .CSV file

3. Clone this repository and just place your .csv file in the same folder. Execute the script using the command line:
    
    `python notetodoc.py [name of your csv].csv `

    or specifiying the name of the output file

    `python notetodoc.py [name of your csv].csv [name for the output file].docx`

And that's all! A .docx file will appear afterwards:
* `[name you specified].docx` or, if you did not specify a name for the output, `notes.docx`

*Although the file is .docx, you can open it with LibreOffice Writer*

## Example
`python notetodoc.py power_electronics.csv ACDC_notes.docx`

