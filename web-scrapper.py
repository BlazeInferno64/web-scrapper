import requests as req # importing the requests library as req

#Staring our main function from here
def web_scrapper(url):
    try:
        response = req.get(url) # Sending a get request to the url entered by the user
        response.raise_for_status() 
        with open("response.txt", "w", encoding="utf-8") as file:
            file.write(format_response(url,response.text))  #Saving the response to response.txt file
        print(f"Sucessfully scrapped {url} and saved to response.txt") # Printing a sucess message
    except req.exceptions.RequestException as err:
        print(f"Error scrapping {url}: {err}") # If an exception occurs, we will print it


def take_input():
    url = input("Enter the URL: ")
    if url == "":
        print("Cannot scrap empty URL!")
    else:
        web_scrapper(url)

def format_response(url,text):
    """Formats the response!"""
    formatted_response = f"Scrapped from {url}:\n\n{text}"
    return formatted_response

if __name__ == "__main__":
    take_input() #Basically here we are running out take_input() function, which will take the input for url
                 #from the user
