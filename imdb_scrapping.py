from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.imdb.com/chart/top?ref_=nv_mv_250"
response=requests.get(url)
data=response.text
name_of_the_movie_list=list()
year_released_list=list()
idbm_rating_list=list()
number_of_reviewers_list=list()
name_of_the_movie_list_temp=list()
censor_rating_list=list()
length_list=list()
genre_1_list=list()
genre_2_list=list()
genre_3_list=list()
genre_4_list=list()
release_date_list=list()
story_summary_list=list()
director_list=list()
writer_1_list=list()
writer_2_list=list()
star_1_list=list()
star_2_list=list()
star_3_list=list()
list1=list()
soup=BeautifulSoup(data,'html.parser')
table_tag=soup.find("table",{"class":"chart"})

years_released=soup.find_all("span",{"class":"secondaryInfo"})
for year_released in years_released:
	year_released_list.append(year_released.text)
rating_tags=table_tag.find_all("strong")
for rating_tag in rating_tags:
	idbm_rating_list.append(rating_tag.text)
title_columns=soup.find_all("td",{"class":"titleColumn"})
for title_column in title_columns:
	title=title_column.find("a")
	name_of_the_movie_list.append(title.text)
table_tag=soup.find("table",{"class":"chart"})
url_tags=table_tag.find_all("a")
for url_tag in url_tags:
	url_crawl="https://www.imdb.com"+url_tag.get('href')
	list1.append(url_crawl)
def Remove(duplicate): 
	final_list = [] 
	for num in duplicate: 
		if num not in final_list: 
			final_list.append(num) 
	return final_list
url_list=Remove(list1)
for URL in url_list:
	response_crawl=requests.get(URL)
	response_crawl
	data_crawl=response_crawl.text
	soup_crawl=BeautifulSoup(data_crawl,'html.parser')
	reviews=soup_crawl.find("span",{"class":"small"})
	number_of_reviewers_list.append(reviews.text)
	subtext=soup_crawl.find("div",{"class":"subtext"}).text
	subtext.strip()
	words=subtext.split('|')
	if len(words)==3:
		censor_rating_list.append('NA')
	else:
		censor_rating_list.append(words[0].strip())
	duration_tag=soup_crawl.find("time")
	duration=duration_tag.text.strip()
	length_list.append(duration)
	division=soup_crawl.find("div",{"class":"subtext"})
	ancors=division.find_all("a")
	ancors_list=list()
	for ancor in ancors:
		ancors_list.append(ancor.text)
	release_date=ancors_list[-1]
	release_date_list.append(release_date)
	del ancors_list[-1]
	no_of_genre=len(ancors_list)
	for i in ancors_list:
		try:
			genre_1=ancors_list[0]
		except:
			genre_1='NA'
		try:
			genre_2=ancors_list[1]
		except:
			genre_2='NA'
		try:
			genre_3=ancors_list[2]
		except:
			genre_3='NA'
		try:
			genre_4=ancors_list[3]
		except:
			genre_4='NA'
	genre_1_list.append(genre_1)
	genre_2_list.append(genre_2)
	genre_3_list.append(genre_3)
	genre_4_list.append(genre_4)
	short_summary=soup_crawl.find("div",{"class":"summary_text"}).text
	short_summary=short_summary.strip()
	story_summary_list.append(short_summary)
	details_tag=soup_crawl.find("div",{"class","plot_summary"})
	details_list=list()
	details=details_tag.find_all("a")
	for detail in details:
		details_list.append(detail.text)
	details_list
	details_list.remove(details_list[-1])
	if len(details_list)>6:
		details_list.remove(details_list[3])
	director=details_list[0]
	director_list.append(director)
	writer_1=details_list[1]
	writer_1_list.append(writer_1)
	writer_2=details_list[2]
	writer_2_list.append(writer_2)
	try:
		star_1=details_list[3]
		star_1_list.append(star_1)
	except:
		star_1_list.append('NA')
	try:
		star_2=details_list[4]
		star_2_list.append(star_2)
	except:
		star_2_list.append(NA)
	try:
		star_3=details_list[5]
		star_3_list.append(star_3)
	except:
		star_3_list.append('NA')
d={'Name of the movie ':name_of_the_movie_list,'Year released':year_released_list,'IMDB rating':idbm_rating_list,'Number of reviewers':number_of_reviewers_list,'Censor board rating ':censor_rating_list,'Length of the movie ':length_list,'Genre 1':genre_1_list,'Genre 2':genre_2_list,'Genre 3':genre_3_list,'Genre 4':genre_4_list,'Release date':release_date_list,'story summary':story_summary_list,'Director Name':director_list,'Writer 1':writer_1_list,'Writer 2':writer_2_list,'Star 1':star_1_list,'Star 2':star_2_list,'Star 3':star_3_list}
df=pd.DataFrame(d)
df.to_csv('results_assignment.csv')

