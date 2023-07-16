import urllib.request as req 
import bs4 

# url = "https://www.linkedin.com/jobs/search?trk=content-hub-home-page_guest_nav_menu_jobs&position=1&pageNum=0"
url = "https://getbootstrap.com/"

request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})



with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    page = bs4.BeautifulSoup(data, "html.parser")
    search_title = page.find("title")
    print(search_title)
    
# print(data)