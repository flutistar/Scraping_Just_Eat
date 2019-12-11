#Start from here
# $python main.py

from getPostcode import getPostcode
from scrapRestaurants import scrapRestaurants
from scrapLists import scrapLists
from test import insertintoSheet

postcodes = []
postcodes = getPostcode.importXlsx()
restaurantUrls = scrapRestaurants.loaddriver(postcodes)
restaurantUrls = list(set(restaurantUrls)) 
insertintoSheet(restaurantUrls)
scrapLists.getList(restaurantUrls)