#!/usr/bin/env python
# coding: utf-8

# In[145]:


import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import time
import urllib



# In[146]:


#get_ipython().system('which chromedriver')


# In[147]:

def init_browser():
    executable_path = {"executable_path":r"C:/Users/slimp/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)




# In[148]:

def scrape_info():
    browser = init_browser()
    url_news = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


    # In[149]:


    browser.visit(url_news)


    # In[150]:


    html = browser.html
    soup = bs(html,"html.parser")


    # In[151]:


    news_title= soup.find("div", class_="content_title").text
    news_title


    # In[152]:


    news_p = soup.find("div", class_ ="article_teaser_body")
    print (news_p.text)


    # In[153]:


    #JPL Mars Space Images - Featured Image
    url_image= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)


    # In[154]:


    html = browser.html
    soup = bs(html,"html.parser")


    # In[155]:


    main_url = "https://www.jpl.nasa.gov"
    jpl_image = soup.find('a', class_='fancybox')
    featured_image_url= main_url+jpl_image["data-fancybox-href"]
    print(featured_image_url)


    # In[156]:


    #Mars Weather
    twitter_url="https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)


    # In[157]:


    html = browser.html
    soup = bs(html, "html.parser")


    # In[158]:


    #mars_weather = soup.find('p', class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather = soup.find(class_ = "tweet-text").text
    mars_weather


    # In[159]:


    #Mars Facts
    url_facts = "https://space-facts.com/mars/"
    browser.visit(url_facts)


    # In[160]:


    html = browser.html
    soup = bs(html, "html.parser")


    # In[161]:


    tables = pd.read_html(url_facts)
    tables


    # In[162]:


    tables=pd.DataFrame(tables[1])
    table_html = tables.to_html(header = False, index = False)
    print(table_html)


    # In[163]:


    tables.columns = ['Properties', 'Value']
    tables.set_index('Properties')
    #table_df= table_info

    #table_df=pd.read_html(table_df)
    #table_df


    # In[164]:


    #table_df.dtypes
    #table_cols = ["0", "1", "3"]
    #table_transformed= table_df[table_cols].copy()
    #table_transformed = table_transformed.rename(columns={"0": "Attr",
                                                         # "1": "mars"})
    #table_cols.dtypes
    #table_transformed.head()

    print(tables)
    #table_info.head


    # In[192]:


    #Mars Hemispheres
    url_Hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    url_Home= "https://astrogeology.usgs.gov"
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url_Hemispheres)
    time.sleep(3)


    # In[193]:


    html = browser.html
    soup = bs(html, "html.parser")


    # In[194]:


    hemisphere_image_urls = []
    result = soup.find("div", class_ ="description")
    holder = {}
    parser = 1
    #result


    #In[195]:


    h_file = soup.find_all("div", class_="item")
    #h_file


    # In[196]:


    ##


    # In[199]:


    for h in h_file:
        title = h.find("h3").text
        title = title.replace("Enhanced", "")
        main_url = url_Home + h.find("a")["href"]    
        browser.visit(main_url)
        html = browser.html
        time.sleep(3)
        soup=bs(html, "html.parser")
        #image_link = soup.find("div", class_="downloads")
        main_img = soup.find('img',  class_="wide-image")
        hemisphere_img = url_Home+main_img["src"]
        hemisphere_image_urls.append({"title": title, "img_url": hemisphere_img})
        holder['title'+str(parser)] = title
        holder['img_url'+str(parser)] = hemisphere_img
        parser += 1
  


    # In[200]:


        #hemisphere_image_urls
        #holder

    mars_data = {
        "News_Title": news_title,
        "News_Paragraph": news_p,
        "Featured_Image": featured_image_url,
        "Mars_Weather": mars_weather,
        "Mars_Facts": table_html,
        "Mars_Hemisphere":hemisphere_image_urls
    }
    browser.quit()
    return mars_data
    # In[ ]:




