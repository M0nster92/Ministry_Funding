from textwrap import wrap
from bs4 import BeautifulSoup
import re
import csv

Funding_list = []
Funding_dict = {}
final_description = []
final_eligibility = []

csv_file = open('data-2.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Status', 'Ministry',
                    'Deadline', 'Description', 'Eligibility', 'url'])


def clear_text(text):
    temp_text = re.sub(r'[\ \n]{2,}', '', text)
    return temp_text


with open("test.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find("div", {"id": "pagebody"})

    for i in tags.find_all("h3"):
        if 'id' in i.attrs:
            h3Tags = i
            statusTag = h3Tags.findNext('strong')
            ministryTag = statusTag.findNext('p')
            deadLineTag = ministryTag.findNext('h4')
            descriptionTag = deadLineTag.findNext('h4')
            eligibilityTag = descriptionTag.findNext('h4')
            guidelineTag = eligibilityTag.findNext('h4')
            url = guidelineTag.findNext('a')
            if deadLineTag.text == "Deadline":
                deadLineInfoTag = deadLineTag.findNext('p')

            for descriptionInfo in descriptionTag.next_siblings:
                final_description.append(descriptionInfo)
                if descriptionInfo.text == "Eligibility":
                    break

            for eligibilityInfo in eligibilityTag.next_siblings:
                final_eligibility.append(eligibilityInfo)
                if eligibilityInfo.text == "Program Guidelines" or eligibilityInfo.text == "Program guidelines":
                    break

            h3tagTitles = clear_text(h3Tags.text)
            status = clear_text(statusTag.text)
            ministry = clear_text(ministryTag.text)
            deadline = clear_text(deadLineInfoTag.text)
            #description = clear_text(final_description.text)

            final_description.pop()
            description_str = ""
            for i in final_description:
                description_str += i.text
            final_format_description = '\n'.join(
                [m.lstrip() for m in description_str.split('\n')])

            final_eligibility.pop()
            eligibility_str = ""
            # print(final_eligibility)
            for i in final_eligibility:
                eligibility_str += i.text

            print('\n')
            print('\n')
            print("**********************")
            print('Title -->', h3tagTitles)
            print('Status -->', status)
            print('Ministry -->', ministry)
            print('Deadline -->', deadline)
            print('Description -->', final_format_description)
            print('Eligibility -->', eligibility_str)
            print('Url -->', url['href'])

            csv_writer.writerow([h3tagTitles, status, ministry,
                                deadline, final_format_description, eligibility_str, url['href']])

            final_description = []
            final_eligibility = []

'''
            csv_writer.writerow([h3tagTitles, status, ministry,
                                deadline, final_format_description, eligibility_str, url['href']])
                                

            Funding_list.append(Funding_dict)
            final_description = []
            final_eligibility = []
            '''
