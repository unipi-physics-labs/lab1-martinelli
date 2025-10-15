
all:
	make centrallimit

copy:
	make copycentrallimit

clean:
	rm -f *~
	make cleancentrallimit

centrallimit:
	gnuplot gp_central_limit.macro
	epstopdf binomial_10.eps
	epstopdf binomial_20.eps
	epstopdf binomial_3.eps
	epstopdf binomial_1.eps
	epstopdf binomial_2.eps
	epstopdf binomial_4.eps

copycentrallimit:
	cp binomial*.pdf ../figure

cleancentrallimit:
	rm -f binomial*.tex binomial*.eps binomial*.pdf
