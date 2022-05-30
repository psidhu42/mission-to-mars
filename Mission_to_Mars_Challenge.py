#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Import Splinter and BeautifulSoup

from splinter import Browser

from bs4 import BeautifulSoup as soup

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[24]:


executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless=False)


# In[25]:


# Visit the mars nasa news site

url = 'https://redplanetscience.com'

browser.visit(url)

# Optional delay for loading the page

browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[26]:


# Set up the HTML parser

html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[27]:


# Use the parent element to find the first `a` tag and save it as `news_title`

news_title = slide_elem.find('div', class_='content_title').get_text()

news_title


# In[28]:


# Use the parent element to find the paragraph text

news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

news_p


# ### Featured Images

# In[29]:


# Visit URL

url = 'https://spaceimages-mars.com'

browser.visit(url)


# In[30]:


# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]

full_image_elem.click()


# In[31]:


# Parse the resulting html with soup

html = browser.html

img_soup = soup(html, 'html.parser')


# In[32]:


# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

img_url_rel


# In[33]:


# Use the base URL to create an absolute URL

img_url = f'https://spaceimages-mars.com/{img_url_rel}'

img_url


# ### Mars Facts Table

# In[34]:


# Scrape Table

df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['description', 'Mars', 'Earth']

df.set_index('description', inplace=True)

df


# In[35]:


# Convert the DataFrame back into HTML-ready code

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[36]:


# 1. Use browser to visit the URL

url = 'https://marshemispheres.com/'

browser.visit(url)


# In[37]:


# 2. Create a list to hold the images and titles.

hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for i in range(4):
    
    # Create dictionary
    mars_hemispheres = {}
    
    # Get image 
    browser.find_by_css('a.product-item h3')[i].click()
    
    element = browser.find_link_by_text('Sample').first
    
    img_url = element['href']
    
    # Get title
    title = browser.find_by_css("h2.title").text
    
    # Get each hemisphere image an link in list
    mars_hemispheres["img_url"] = img_url
    
    mars_hemispheres["title"] = title
    
    hemisphere_image_urls.append(mars_hemispheres)
    
    # Go back to main page
    browser.back()


# In[38]:


# 4. Print the list that holds the dictionary of each image url and title.

hemisphere_image_urls


# In[39]:


# 5. Quit the browser

browser.quit()


# In[ ]:




