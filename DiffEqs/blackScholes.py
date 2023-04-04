from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame
import pandas_datareader.data as web



#Found this article on Black-Scholes model on European options:
#https://medium.com/swlh/calculating-option-premiums-using-the-black-scholes-model-in-python-e9ed227afbee
if(True):

    def d1(S,K,T,r,sigma):
        """
        Get d1 of Black Scholes model.

        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        :return: d1
        """
        return(log(S/K)+(r+sigma**2/2.)*T)/(sigma*sqrt(T))
    def d2(S,K,T,r,sigma):
        """
        Get d2 of Black Scholes model.

        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        :return: d1
        """
        return d1(S,K,T,r,sigma)-sigma*sqrt(T)
    
    def bs_call(S,K,T,r,sigma):
        """
        Betting a stock will increase in value

        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset                
        """
        return S*norm.cdf(d1(S,K,T,r,sigma))-K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma))
  
    def bs_put(S,K,T,r,sigma):
        """
        Betting a stock will decrease in value

        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """
        return K*exp(-r*T)-S*bs_call(S,K,T,r,sigma)


    stock = 'SPY' #SPDR S&P 500 ETF Trust
    expiry = '04-01-2023'
    strike_price = 370

    today = datetime.now()
    one_year_ago = today.replace(year=today.year-1)

    #Yahoo has made changes to their API so this doesn't work
    df = web.DataReader(stock, 'yahoo', start=one_year_ago, end=today)
    df = df.sort_values(by="Date")
    df = df.dropna()
    df = df.assign(close_day_before=df.Close.shift(1))
    df['returns'] = ((df.Close - df.close_day_before)/df.close_day_before)
    sigma = np.sqrt(252) * df['returns'].std()
    uty = (web.DataReader("^TNX", 'yahoo', today.replace(day=today.day-1), today)['Close'].iloc[-1])/100
    lcp = df['Close'].iloc[-1]
    t = (datetime.strptime(expiry, "%m-%d-%Y") - datetime.utcnow()).days / 365
    print('The Option Price is: ', bs_call(lcp, strike_price, t, uty, sigma))

    #"Implied Volatility. It is defined as the expected future volatility of the stock over the life of the option."

    def call_implied_volatility(Price, S, K, T, r):
        sigma = 0.001
        while sigma < 1:
            Price_implied = S * \
                norm.cdf(d1(S, K, T, r, sigma))-K*exp(-r*T) * \
                norm.cdf(d2(S, K, T, r, sigma))
            if Price-(Price_implied) < 0.001:
                return sigma
            sigma += 0.001
        return "Not Found"

    def put_implied_volatility(Price, S, K, T, r):
        sigma = 0.001
        while sigma < 1:
            Price_implied = K*exp(-r*T)-S+bs_call(S, K, T, r, sigma)
            if Price-(Price_implied) < 0.001:
                return sigma
            sigma += 0.001
        return "Not Found"

    print("Implied Volatility: " +
          str(100 * call_implied_volatility(bs_call(lcp, strike_price, t, uty, sigma,), lcp, strike_price, t, uty,)) + " %")

    #Delta: the sensitivity of an option’s price changes relative to the changes in the underlying asset’s price.
    #Gamma: the delta’s change relative to the changes in the price of the underlying asset.
    #Vega: the sensitivity of an option price relative to the volatility of the underlying asset.
    #Theta: the sensitivity of the option price relative to the option’s time to maturity.
    #Rho: the sensitivity of the option price relative to interest rates.

    def call_delta(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """
        return norm.cdf(d1(S,K,T,r,sigma))
    
    def call_gamma(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*sqrt(T))
    
    def call_vega(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return 0.01*(S*norm.pdf(d1(S,K,T,r,sigma))*sqrt(T))
    
    def call_theta(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return 0.01*(-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*sqrt(T)) - r*K*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma)))
    
    def call_rho(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return 0.01*(K*T*exp(-r*T)*norm.cdf(d2(S,K,T,r,sigma)))

    def put_delta(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return -norm.cdf(-d1(S,K,T,r,sigma))

    def put_gamma(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """
    
        return norm.pdf(d1(S,K,T,r,sigma))/(S*sigma*sqrt(T))

    def put_vega(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return 0.01*(S*norm.pdf(d1(S,K,T,r,sigma))*sqrt(T))
    
    def put_theta(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return 0.01*(-(S*norm.pdf(d1(S,K,T,r,sigma))*sigma)/(2*sqrt(T)) + r*K*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma)))
    
    def put_rho(S,K,T,r,sigma):
        """        
        
        :param S: Spot price of asset
        :param K: Strike price
        :param T: Time to maturity
        :param r: Risk free interest rate
        :param sigma: Volatility of asset
        """

        return 0.01*(-K*T*exp(-r*T)*norm.cdf(-d2(S,K,T,r,sigma)))
