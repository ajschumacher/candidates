### Extracting data from `nr_1550.pdf`


#### Step 1

Source: [https://www.dcboee.org/popup.asp?url=/pdf_files/nr_1550.pdf](https://www.dcboee.org/popup.asp?url=/pdf_files/nr_1550.pdf)

Process: Downloaded on Sunday 2014-08-17

Output: Local file [nr_1550.pdf](nr_1550.pdf)


#### Step 2

Source: Local file [nr_1550.pdf](nr_1550.pdf)

Process: `pdftotext -layout nr_1550.pdf` (`pdftotext` from `poppler` package)

Output: Local file [nr_1550.txt](nr_1550.txt)


#### Step 3

Source: Local file [nr_1550.txt](nr_1550.txt)

Process: [nr_1550.txt](nr_1550.txt) has internal commas but no internal
pipes. Manually edited the text file into a pipe-separated file.

Notes: Originally [nr_1550.pdf](nr_1550.pdf) was a four-page PDF, with
a running header:

```
District of Columbia Board of Elections
Direct Access and State Board of Education Candidates
in the November 4, 2014 General Election
```

and it had a date and time in a running footer:

```
8/7/2014 1:38 PM
```

Seven columns were native to the table structure in the PDF;
the "race" column was added to represent section headers in
order to put the complete contents in one CSV.

Entirely blank rows were dropped, except where this would
drop a whole race.

Output: Local file [nr_1550.psv](nr_1550.psv)


#### Step 4

Source: Local file [nr_1550.psv](nr_1550.psv)

Process: `cat nr_1550.psv | ./pipe2csv.py > nr_1550.csv` (local script [pipe2csv.py](pipe2csv.py))

Output: Local file [nr_1550.csv](nr_1550.csv)
