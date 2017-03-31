#!/usr/bin/python

from selenium import webdriver

def scrape_youtube_videos():
	driver = webdriver.Chrome('/Users/harshal/Downloads/chromedriver')
	url = "https://www.youtube.com/results?q=formula+1"

	driver.get(url)

	results = driver.find_elements_by_class_name("yt-lockup-content")

	for result in results:
		video = result.find_element_by_xpath('.//h3/a')
		title = video.get_attribute('title')
		url = video.get_attribute('href')
		print title + " " + url


if __name__ == "__main__":
	scrape_youtube_videos()
