all:
	make plots

copy:
	make copyplots

clean:
	make cleanplots

plots:
	gnuplot gp_plots.macro
	epstopdf function_large.eps
	epstopdf function_sampled.eps
	epstopdf function_small.eps

copyplots:
	cp function*.tex function*.pdf ../figure

cleanplots:
	rm -f *~ function*.tex function*.pdf function*.eps
