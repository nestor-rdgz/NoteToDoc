# NoteToDoc Python Script
This Python script generates a .docx and .txt file containing all the bibliography and the notes taken in [Zotero](https://www.zotero.org/) *(previously exported in a .csv file)*, to ease the process of writing papers (e.g. surveys and reviews) and thesis. 

1. Before using the Python script, make sure you have the necessary packages already installed in your system by running:
    
    `python -m pip install -r requirements.txt`

2. After that, to properly run the script, export you bibliography elements from Zotero to a .CSV file

3. Finally, just place the `notetodoc.py` file in the same folder as you CSV file, and execute it using the command line:
    
    `python notetodoc.py [name of your csv].csv `

    or specifiying the name of the output file

    `python notetodoc.py [name of your csv].csv [name for the output file].docx`

And that's all! A .docx file will appear afterwards:
* `[name you specified].docx` or, if you did not specify a name for the output, `notes.docx`


*Although the file is .docx, you can open it with LibreOffice Writer*
