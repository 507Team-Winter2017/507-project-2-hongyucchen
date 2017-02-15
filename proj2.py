#proj2.py
import requests
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url_1 = 'http://www.nytimes.com'
r = requests.get(base_url_1)
soup = BeautifulSoup(r.text, "html.parser")
story_headings = soup.find_all(class_="story-heading")

num = 0
for story_heading in story_headings:
	# print(story_heading)
	if story_heading.a:
		print(story_heading.a.text.replace("\n"," ").strip())
	else:
		print(story_heading.contents[0].strip())

	num += 1
	if num == 10:
		break


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url_2 = "http://www.michigandaily.com"
r = requests.get(base_url_2)
soup = BeautifulSoup(r.text, "html.parser")
mostread_panel = soup.find_all(class_="pane-mostread")
links = mostread_panel[0].find_all("a")
for mostread in links:
	print(mostread.text.replace("\n", " ").strip())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url_3 = "http://www.newmantaylor.com/gallery.html"
r = requests.get(base_url_3)
soup = BeautifulSoup(r.text, "html.parser")
imgs = soup.find_all("img")
for img in imgs:
	try:
		print(img['alt'])
	except:
		print("No alternative text provided!")


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
def print_contact_email_get_num(contacts, num):
	for contact in contacts:
		# print(contact.a["href"])
		try:
			r1 = requests.get(base+contact.a["href"])
			soup1 = BeautifulSoup(r1.text, "html.parser")
			email_div = soup1.find_all(class_="field-name-field-person-email")
			email = email_div[0].find_all("a")
			num += 1
			print(num, email[0].text)
		except:
			pass
	return num

base = "https://www.si.umich.edu"
base_url_4 = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
r = requests.get(base_url_4)
soup = BeautifulSoup(r.text, "html.parser")
contacts = soup.find_all(class_="field-name-contact-details")
pager_next = soup.find_all(class_="pager-next")
# while pager_next[0].a:
# 	r_next = requests.get(base+pager_next[0].a["href"])
# 	soup_next_page = BeautifulSoup(r_next.text, "html.parser")
# 	contacts += soup_next_page.find_all(class_="field-name-contact-details")
# print(len(contacts))
num = 0
num = print_contact_email_get_num(contacts, num)

while pager_next[0].a:
	r_next = requests.get(base+pager_next[0].a["href"])
	soup_next_page = BeautifulSoup(r_next.text, "html.parser")
	pager_next = soup_next_page.find_all(class_="pager-next")
	contacts = soup_next_page.find_all(class_="field-name-contact-details")
	num = print_contact_email_get_num(contacts, num)
