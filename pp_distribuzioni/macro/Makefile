
all:
	make binomial
	make poisson
	make uniform
	make exponential
	make gaussian
	make chisquare
	make cauchy
	make rainfall

copy:
	make copybinomial
	make copypoisson
	make copyuniform
	make copyexponential
	make copygaussian
	make copychisquare
	make copycauchy
	make copyrainfall

clean:
	rm -f *~
	make cleanbinomial
	make cleanpoisson
	make cleanuniform
	make cleanexponential
	make cleangaussian
	make cleanchisquare
	make cleancauchy
	make cleanrainfall

binomial:
	gnuplot gp_binomial.macro
	epstopdf binomial_10_1-2.eps
	epstopdf binomial_10_1-6.eps
	epstopdf binomial_4_1-2.eps
	epstopdf binomial_4_1-6.eps
	epstopdf binomial_detailed.eps

copybinomial:
	cp -f binomial*.tex binomial*.pdf ../figure/

cleanbinomial:
	rm -f binomial*.tex binomial*.eps binomial*.pdf

poisson:
	gnuplot gp_poisson.macro
	epstopdf poisson_10.eps
	epstopdf poisson_2.eps
	epstopdf poisson_detailed.eps
	epstopdf poisson_1.eps
	epstopdf poisson_5.eps


copypoisson:
	cp -f poisson*.tex poisson*.pdf ../figure/

cleanpoisson:
	rm -f poisson*.tex poisson*.eps poisson*.pdf

uniform:
	gnuplot gp_uniform.macro
	epstopdf uniform_0_1.eps
	epstopdf uniform_-1_1.eps
	epstopdf uniform_detailed.eps
	epstopdf uniform_0_2.eps
	epstopdf uniform_-2_2.eps

copyuniform:
	cp -f uniform*.tex uniform*.pdf ../figure/

cleanuniform:
	rm -f uniform*.tex uniform*.eps uniform*.pdf

exponential:
	gnuplot gp_exponential.macro
	epstopdf exponential_0_5.eps
	epstopdf exponential_1_5.eps
	epstopdf exponential_detailed.eps
	epstopdf exponential_1_0.eps
	epstopdf exponential_2_0.eps

copyexponential:
	cp -f exponential*.tex exponential*.pdf ../figure/

cleanexponential:
	rm -f exponential*.tex exponential*.eps exponential*.pdf

gaussian:
	gnuplot gp_gaussian.macro
	epstopdf gaussian_0_1.eps
	epstopdf gaussian_-1_0_5.eps
	epstopdf gaussian_detailed.eps
	epstopdf gaussian_0_2.eps
	epstopdf gaussian_1_1.eps
	epstopdf gaussian_vs_poisson.eps

copygaussian:
	cp -f gaussian*.tex gaussian*.pdf ../figure/

cleangaussian:
	rm -f gaussian*.tex gaussian*.eps gaussian*.pdf

chisquare:
	gnuplot gp_chisquare.macro
	epstopdf chisquare_1.eps
	epstopdf chisquare_3.eps
	epstopdf chisquare_detailed.eps
	epstopdf chisquare_2.eps
	epstopdf chisquare_15.eps

copychisquare:
	cp -f chisquare*.tex chisquare*.pdf ../figure/

cleanchisquare:
	rm -f chisquare*.tex chisquare*.eps chisquare*.pdf

cauchy:
	gnuplot gp_cauchy.macro
	epstopdf cauchy_02.eps
	epstopdf cauchy_05.eps
	epstopdf cauchy_1.eps
	epstopdf cauchy_2.eps
	epstopdf cauchy_detailed.eps

copycauchy:
	cp -f cauchy*.tex cauchy*.pdf ../figure/

cleancauchy:
	rm -f cauchy*.tex cauchy*.eps cauchy*.pdf

rainfall:
	python rainfall.py
	gnuplot gp_rainfall.macro
	epstopdf rainfall_0.eps
	epstopdf rainfall_1.eps
	epstopdf rainfall_2.eps
	epstopdf rainfall_3.eps
	epstopdf rainfall_4.eps
	epstopdf rainfall_5.eps
	epstopdf rainfall_6.eps
	epstopdf rainfall_7.eps
	epstopdf rainfall_8.eps
	epstopdf rainfall_9.eps
	epstopdf rainfall_10.eps
	epstopdf rainfall_11.eps
	epstopdf rainfall_12.eps

copyrainfall:
	cp rainfall_0.tex rainfall_1.tex rainfall_0.pdf rainfall_1.pdf ../figure

cleanrainfall:
	rm -f rainfall_*.*
