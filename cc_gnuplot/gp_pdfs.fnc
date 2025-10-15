##
## Useful probability density distributions.
##

# Binomial distribution.
binomial_coeff(n, x) = n!/(n-int(x))!/int(x)!
binomial_pdf(x, n, p) = (x<0) ? 0 :\
	((x>n) ? 0 : binomial_coeff(n, x)*p**int(x)*(1.0-p)**(n-int(x)))
binomial_mean(n, p) = n*p
binomial_rms(n, p) = sqrt(n*p*(1.0-p))

# Poisson distribution.
poisson_pdf(x, mu) = (x<0) ? 0 : mu**x*exp(-mu)/int(x)!
poisson_mean(mu) = mu
poisson_rms(mu) = sqrt(mu)

# Uniform distribution.
uniform_pdf(x, a, b) = (x>a && x<b) ? 1.0/(b-a) : 0
uniform_mean(a, b) = (a+b)/2.0
uniform_rms(a, b) = (b-a)/sqrt(12.0)

# Triangular distribution.
peak_value(a, b, peak)  = 2.0/(b-a)
slope_left(a, b, peak)  = peak_value(a, b, peak)/(peak-a)
slope_right(a, b, peak) = peak_value(a, b, peak)/(peak-b)
triangular_pdf(x, a, b, peak) = (x>=a && x<=peak) ?\
	slope_left(a, b, peak)*(x-a):\
	((x>peak && x<=b) ? slope_right(a, b, peak)*(x-b) : 0)

# Exponential distribution.
exponential_pdf(x, lambda) = (x<0) ? 0 : lambda*exp(-lambda*x)
exponential_mean(lambda) = 1.0/lambda
exponential_rms(lambda) = 1.0/lambda

# Gaussian distribution.
gauss_pdf(x, mu, sigma) = 1.0/(sigma*sqrt(2.0*pi))*exp(-0.5*((x-mu)/sigma)**2)
gauss_mean(mu, sigma) = mu
gauss_rms(mu, sigma) = sigma

# Chi-square distribution.
chisquare_norm(n) = 1.0/(2**(0.5*n)*gamma(0.5*n))
chisquare_pdf(x, n) = chisquare_norm(n)*x**(0.5*n-1)*exp(-0.5*x)
chisquare_mean(n) = n
chisquare_rms(n) = sqrt(2.0*n)

# Cauchy distribution.
cauchy_pdf(x, a) = a/(pi*(a**2 + x**2))
cauchy_median(a) = 0
cauchy_hwhm(a)   = a
