
all:
	make fwhm
	make triangular
	make dices
	make histograms

copy:
	make copyfwhm
	make copytriangular
	make copydices
	make copyhistograms

clean:
	rm -f *~
	make cleanfwhm
	make cleantriangular
	make cleandices
	make cleanhistograms

fwhm:
	gnuplot gp_fwhm.macro
	epstopdf fwhm.eps

copyfwhm:
	cp -f fwhm*.tex fwhm*.pdf ../figure

cleanfwhm:
	rm -f fwhm*.tex fwhm*.eps fwhm*.pdf

triangular:
	gnuplot gp_triangular.macro
	epstopdf triangular.eps

copytriangular:
	cp -f triangular*.tex triangular*.pdf ../figure

cleantriangular:
	rm -f triangular*.tex triangular*.eps triangular*.pdf

dices:
	gnuplot gp_dices.macro
	epstopdf dices_frequency.eps
	epstopdf dices_relative_frequency.eps

copydices:
	cp -f dices*.tex dices*.pdf ../figure

cleandices:
	rm -f dices*.tex dices*.eps dices*.pdf

histograms:
	gnuplot gp_histograms.macro
	epstopdf histogram_107_bins.eps
	epstopdf histogram_12_bins_frequency.eps
	epstopdf histogram_12_bins.eps
	epstopdf histogram_3_bins.eps

copyhistograms:
	cp -f histogram*.tex histogram*.pdf ../figure

cleanhistograms:
	rm -f histogram*.tex histogram*.eps histogram*.pdf
