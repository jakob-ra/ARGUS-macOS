# -*- coding: utf-8 -*-
"""
Code to steer ARGUS

Created on Mon Jun  8 16:41:04 2020

@author: JDO
"""

# Modules
import os, sys, subprocess
import sys
import time


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

# get path to directory
script_dir = os.path.dirname(__file__)


class argus_settings:   
	os.chdir(script_dir)	# change working directory to project folder
	filepath = "/Users/parnianshahkar/Documents/KOF/Task2/ARGUS-main/test_urls.txt" 	# file path for list containing URLs
		
	# settings for ARGUS spider
	delimiter = "\t"    
	encoding = "utf-8"
	index_col = "id"		# column with IDs
	url_col = "url"		# column with URLs
	lang = "German"		# language
	n_cores = 1		# number of cores
	limit = 10		# scraping limit
	log_level = "INFO"
	prefer_short_urls = "on"
	pdfscrape = "off"

# Execute scraping
if __name__ == "__main__":
	# open_file(script_dir + r"/bin/start_server.bat")		# start scrapyd server
	time.sleep(2)
	# Start crawling
	from bin import start_crawl_steering
	start_crawl_steering.start_crawl()

