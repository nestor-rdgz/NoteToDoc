# NoteToDoc Python Script
This Python script generates a .docx and .txt file containing all the bibliography and the notes taken in Zotero *(previously exported in a .csv file)*, to ease the process of writing papers suchas a surveys or reviews. 

1. Before using the Python script, make sure you have the necessary packages already installed in your device by running:
    
    `python -m pip install -r requirements.txt`

2. After that, to properly run the script, export you bibliography elements from Zotero to a .CSV file and name it: `exported.csv`

3. Finally, just place the `notetodoc.py` script in the same folder as you CSV file, and execute it using the command line:
    
    `python notetodoc.py`

And that's all! Two files will appear afterwards:
* `notes.docx`
* `notes.txt`
