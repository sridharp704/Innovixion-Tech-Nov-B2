from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information based on HTML tags and structure
        # Replace these with the actual tags and structure of the website you're scraping
        title = soup.title.text.strip()
        headings = [h1.text.strip() for h1 in soup.find_all('h2')]
        paragraphs = [p.text.strip() for p in soup.find_all('p')]
        links = [a.text.strip() for a in soup.find_all('a')]

        # Print the title of the website
        print(f'Title: {title}')
        
        # Printing ist 10 headingsof the website
        print('\nHeadings are: (1st 10)\n')
        for idx, heading in enumerate(headings[:10], start=1):
            print(f'{idx}. {heading}')
           
         # Printing ist 10 paragraphs of the website
        print('\nParagraphs are: (1st 10)\n' )
        for idx, paragraph in enumerate(paragraphs[:10], start=1):
            print(f'{idx}. {paragraph}')
           
         # Printing all the tags used inthe website
        
        print("\nAll tags used are\n") 
        tag_list=[]
        for tag in soup.find_all(True):
            tag_list.append(tag.name)
        print(list(set(tag_list)))
        
         # Printing ist 10 paragraphs of the website
        print('\nLinks are: (1st 10)\n' )
        for idx, link in enumerate(links[:10], start=1):
            print(f'{idx}. {link}')
    else:
        print(f'Error: Unable to fetch the webpage. Status Code: {response.status_code}')

# enter your url here
scrape_website("https://www.geeksforgeeks.org/python-web-scraping-tutorial/")

#
#In this code, we function called `scrape_website` that takes a URL as an argument. The function sends a GET request to the URL and checks if the request was successful. If the request was successful, it parses the HTML content of the page using BeautifulSoup.
#
#The function then extracts information from the parsed HTML based on specific HTML tags and structures. In this case, we extract the title of the webpage, the text of the first 10 headings, the text of the first 10 paragraphs, and the text of the first 10 links.
#
#Finally, the function prints the extracted information..</s>
