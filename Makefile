
all: 
	make pdf
	make pdf
	make pdf
	make index
	make pdf

release:
	make clean
	make all
	make accents

cover:
	python frontespizio.py

cleancover:
	rm -f cc_complementi/frontespizio.tex

index:
	makeindex analisi_dati.idx

pdf:	
	make cover
	pdflatex analisi_dati.tex

clean:
	rm -f *.aux *.idx *.toc *.ind *.ilg *.log *.bbl *.blg
	rm -f *.dvi *.ps *.pdf *~
	rm -f */*.aux */*.idx */*.toc */*.log */*.bbl */*.blg */*~
	rm -rf */*/*~
	rm -f *.mtc* *.maf
	rm -f *.brf *.out
	rm -f *.pyc
	make cleanmacro
	make cleancover

macro:
	cd pp_statistica/macro/; make all
	cd pp_distribuzioni/macro/; make all
	cd pp_errori_II/macro/; make all
	cd pp_fit/macro/; make all
	cd pp_complementi/macro/; make all
	cd aa_tabelle/macro/; make all

copymacro:
	cd pp_statistica/macro/; make copy
	cd pp_distribuzioni/macro/; make copy
	cd pp_errori_II/macro/; make copy
	cd pp_fit/macro/; make copy
	cd pp_complementi/macro/; make copy
	cd aa_tabelle/macro/; make copy

cleanmacro:
	cd pp_statistica/macro/; make clean
	cd pp_distribuzioni/macro/; make clean
	cd pp_errori_II/macro/; make clean
	cd pp_fit/macro/; make clean
	cd pp_complementi/macro/; make clean
	cd aa_tabelle/macro/; make clean

oldint:
	make -i _oldint_

_oldint_:
	echo "Searching for old style integrals..."
	grep \\\\\int pp_*/*.tex
	echo "Done."

oldeq:
	make -i _oldeq_

_oldeq_:
	echo "Searching for old style equations..."
	grep \begin{equation} pp_*/*.tex
	grep \end{equation} pp_*/*.tex
	echo "Done."

oldexpect:
	make -i _oldexpect_

_oldexpect_:
	echo "Searching for old style expectation values..."
	grep 'E\[' pp_*/*.tex
	echo "Done."

oldfig:
	make -i _oldfig_

_oldfig_:
	echo "Searching for old style figures..."
	grep \begin{figure} pp_*/*.tex
	grep \end{figure} pp_*/*.tex
	grep \begin{figure} ps_*/*.tex
	grep \end{figure} ps_*/*.tex
	echo "Done."

obsolete:
	make oldint
	make oldfig
	make oldeq

accents:
	make -i _accents_

_accents_:
	echo "Searching for wrong accents..."
	grep perch\\\\\`e */*.tex -n
	grep poich\\\\\`e */*.tex -n
	grep affinch\\\\\`e */*.tex -n
	grep " s\\\\\`e " */*.tex -n
	echo "Done."
