
all:	
	make clean
	make motion
	make lotto

copy:
	make copymotion
	make copylotto

clean:
	rm -f *~
	make cleanmotion
	make cleanlotto

motion:
	python motion.py
	gnuplot gp_motion.macro
	epstopdf least_squares.eps
	epstopdf least_chisquare.eps
	epstopdf least_chisquare_noerror.eps
	epstopdf least_chisquare_pol10.eps
	epstopdf least_chisquare_pol10_test.eps

copymotion:
	cp -f least_squares.tex least_squares.pdf ../figure
	cp -f least_chisquare.tex least_chisquare.pdf ../figure
	cp -f least_chisquare_noerror.tex least_chisquare_noerror.pdf ../figure
	cp -f least_chisquare_pol10.tex least_chisquare_pol10.pdf ../figure
	cp -f least_chisquare_pol10_test.tex least_chisquare_pol10_test.pdf ../figure
	cp -f least_*_l*.tex ../
	cp -f *_table.tex ../
	cp -f fit.log ../fit.output

cleanmotion:
	rm -f fit.log
	rm -f least_*.dat least_*.tex least_*.eps least_*.pdf

lotto:
	python lotto.py
	gnuplot gp_lotto.macro
	epstopdf lotto_BA.eps

copylotto:
	cp lotto_BA.tex lotto_BA.pdf ../figure

cleanlotto:
	rm -f lotto_*.dat lotto_*.tex lotto_*.eps lotto_*.pdf
