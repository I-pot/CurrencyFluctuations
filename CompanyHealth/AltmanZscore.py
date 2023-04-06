#===========================================
#Looking into different ways of predicting company health
#One place to start might be Altman Z score
#https://en.wikipedia.org/wiki/Altman_Z-score
#===========================================

def origZ(x1, x2, x3, x4, x5):
    """Definition of the original Altman Z score. bankrupt group avg at -0.25; Non-bankrupt group avg at +4.48.
    The formula based on linear discriminant analysis. Interpretation of the results:
    Z > 2.99 : "safe" zone
    1.81 < Z < 2.99 : "grey" zone
    Z < 1.81 : "distress" zone
    
    :param x1: Ratio of working capital to total assets
    :param x2: Ratio of retained earnings to total assets
    :param x3: Ratio of earnings before interest and taxes to total assets
    :param x4: Ratio of market value of equity to book value of total liabilities
    :param x5: Ratio of sales to total assets:
    :return: Z
    """
    c1 = 1.2 #Definition of the coefficients
    c2 = 1.4
    c3 = 3.3
    c4 = 0.6
    c5 = 1.0

    return c1*x1 + c2*x2 + c3*x3 + c4*x4 + c5*x5

def nonManufacturerZ(x1, x2, x3, x4):
    """Definition of the non-manufacturer Altman Z score. Interpretation of the results:
    Z > 2.6 : "safe" zone
    1.1 < Z < 2.6 : "grey" zone
    Z < 1.1 : "distress" zone
    
    :param x1: (current assets - current liabilities) / total assets
    :param x2: Retained earnings / total assets
    :param x3: Earnings before interest and taxes / total assets
    :param x4: Book value of equity / total liabilities
    :return: Z
    """
    c1 = 6.56 #Definition of the coefficients
    c2 = 3.26
    c3 = 6.72
    c4 = 1.05

    return c1*x1 + c2*x2 + c3*x3 + c4*x4

def emergingMarketZ(x1, x2, x3, x4):
    """Definition of the emerging market Altman Z score. Interpretation of the results:
    Z > 2.6 : "safe" zone
    1.1 < Z < 2.6 : "grey" zone
    Z < 1.1 : "distress" zone
    
    :param x1: (current assets - current liabilities) / total assets
    :param x2: Retained earnings / total assets
    :param x3: Earnings before interest and taxes / total assets
    :param x4: Book value of equity / total liabilities
    :return: Z
    """
    c0 = 3.25 #Definition of the coefficients
    c1 = 6.56 
    c2 = 3.26
    c3 = 6.72
    c4 = 1.05

    return c0 + c1*x1 + c2*x2 + c3*x3 + c4*x4

#Look into Ohlson O-score?
#https://en.wikipedia.org/wiki/Ohlson_O-score

#Cluster companies in terms of Z-score and what? Stock price? Need to do this as a function of time?
#Company size? Average price of the product they are selling

#==============================================================================
#Use data from the website:
#https://www.kaggle.com/datasets/pierrelouisdanieau/financial-data-sp500-companies
#==============================================================================

from sklearn.cluster import KMeans

Kmean = KMeans(n_clusters=2)

#Kmean.fit()
