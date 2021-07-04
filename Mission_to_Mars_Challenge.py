#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
# define the parent element
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


# Use the parent element to find the first content title
slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text (the article summary)
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
#There are only three instances of <button> in the code.  
#The "Full Image" button is the second one ([1])

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[19]:


# 5. Quit the browser
browser.quit()


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[14]:


#create a DataFrame from the HTML table --pull only the first table ([0])
df = pd.read_html('https://galaxyfacts-mars.com')[0]

#assign column names
df.columns=['description', 'Mars', 'Earth']

# set the index to description column
df.set_index('description', inplace=True)

df


# In[15]:


#convert the DataFrame back into HTML
df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[37]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
img_links= browser.find_by_css('a.product-item img')

for i in range(len(links)):
    hemispheres = {}
    browser.find_by_css('a.product-item img')[i].click()
    jpg_file = browser.links.find_by_text('Sample').first
    hemispheres['image_url']=jpg_file['href']

    #get the title
    hemispheres['title'] = browser.find_by_css('h2.title').text

#append the title and img_url to the list
    hemisphere_image_urls.append(hemispheres)

    browser.back()
    

# 5. Quit the browser
browser.quit()

