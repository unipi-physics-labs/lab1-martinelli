
all:
	make correlation

clean:
	rm -f *~
	make cleancorrelation

copy:
	make copycorrelation

correlation:
	gnuplot gp_chiodini.macro
	epstopdf chiodini.eps

cleancorrelation:
	rm -f chiodini.tex chiodini.eps chiodini.pdf

copycorrelation:
	cp chiodini.tex chiodini.pdf ../figure
