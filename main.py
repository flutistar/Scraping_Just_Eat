#Start from here
# $python main.py

from getPostcode import getPostcode
from scrapRestaurants import scrapRestaurants
from scrapLists import getList
from test import insertintoSheet

postcodes = []
restaurantUrls = []
finalUrls = []
postcodes = getPostcode.importXlsx()
restaurantUrls = scrapRestaurants.loaddriver(postcodes)
finalUrls = getPostcode.checkDuplicate(restaurantUrls)
insertintoSheet(finalUrls)
getList(finalUrls)