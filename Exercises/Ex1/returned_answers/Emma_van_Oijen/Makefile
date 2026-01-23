# Produces pdf file.
# Note that - suppresses errors such that the process continues.
# An error is expected at the end of first LaTeX call for instance since the Bibtex file hasn't been compiled yet.
all: Ex1-Assignment2.tex Ex1-Assignment2.bib
	-pdflatex Ex1-Assignment2.tex --no-print-output
	biber Ex1-Assignment2
	-mf diagram1.mf --no-print-output
	-mf diagram2.mf --no-print-output
	-pdflatex Ex1-Assignment2.tex --no-print-output

#Additional, not really needed to compile full pdf
Bibtex: Ex1-Assignment2.bib
	biber Ex1-Assignment2

#Additional, not really needed to compile full pdf
Latex: Ex1-Assignment2.tex
	-pdflatex Ex1-Assignment2.tex

# Remove all files except source files, Makefile and the final pdf.
FILETYPES = *.600pk *.mf *.tfm *.aux *.bbl *.bcf *.blg *.log *.run.xml *.2602gf *.mp *.t1

clean:
	rm -f $(FILETYPES)
