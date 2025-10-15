
all:
	make tables

copy:
	make copytables

clean:
	rm -f *~ *.pyc
	make cleantables
	make cleangraphs

erf:
	python table_erf.py
	python table_erf_inverse.py

copyerf:
	cp table_erf.tex ..
	cp table_erf_inverse.tex ..

chisquare:
	python table_chisquare.py

copychisquare:
	cp table_chisquare_*.tex ..

student:
	python table_student.py
	python table_student_inverse.py

copystudent:
	cp table_student.tex ..
	cp table_student_inverse.tex ..

tables:
	make erf
	make chisquare
	make student

copytables:
	make copyerf
	make copychisquare
	make copystudent

cleantables:
	rm -f *.tex *.pyc

graphs:
	gnuplot gp_tables.macro
	epstopdf chisquare_pvalues.eps
	epstopdf gauss_integral.eps
	epstopdf t_integral.eps
	epstopdf erf.eps
	epstopdf gauss_integral_inverse.eps
	epstopdf t_integral_inverse.eps

copygraphs:
	cp -f *.tex *.pdf ../figure/

cleangraphs:
	rm -f *.eps *.pdf *.tex

