# web-scrapper
Scrap the web using Python web scrapper!
|-----|
 
# Setup and installation
Before running the web scrapper <br>
Install the required libraries from the requirements.txt file or just copy and paste the follwing command in your terminal

```
pip install -r requirements.txt
```

# Breakdown
Let't break down the code 

First we will import the requests library in python

```python
import requests as req
```

After this we will define a function named web-scrapper() which will scrapp the web and <br> 
then save the response to a file named response.txt as follows -

```python
def web_scrapper(url):
    try:
        response = req.get(url) # Sending a get request to the url entered by the user
        response.raise_for_status() 
        with open("response.txt", "w", encoding="utf-8") as file:
            file.write(format_response(url,response.text))  #Saving the response to response.txt file
        print(f"Sucessfully scrapped {url} and saved to response.txt") # Printing a sucess message
    except req.exceptions.RequestException as err:
        print(f"Error scrapping {url}: {err}") #If an exception occurs, we will print it
```

Now it's time to define another function which will take the url input from the user and <br> 
then scrapp it!

```python
def take_input():
    url = input("Enter the URL: ")
    if url == "":
        print("Cannot scrap empty URL!")
    else:
        web_scrapper(url)
```

Who doesn't like nice formated code!
So, to format it, let's make another function named formatted_response()

```python
def format_response(url,text):
    """Formats the response!"""
    formatted_response = f"Scrapped from {url}:\n\n{text}"
    return formatted_response
```

Lastly, we will run this script using -

```python
if __name__ == "__main__":
    take_input() #Basically here we are running out take_input() function, which will take the input for url
                 #from the user
```

Now after putting all the pieces togther <br>
We will get the following script -

```python
import requests as req #importing the requests library as req

#Staring our main function from here
def web_scrapper(url):
    try:
        response = req.get(url) # Sending a get request to the url entered by the user
        response.raise_for_status() 
        with open("response.txt", "w", encoding="utf-8") as file:
            file.write(format_response(url,response.text))  #Saving the response to response.txt file
        print(f"Sucessfully scrapped {url} and saved to response.txt") # Printing a sucess message
    except req.exceptions.RequestException as err:
        print(f"Error scrapping {url}: {err}") #If an exception occurs, we will print it


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
```

<br>
<br>
 That's all for this simple web scrapper!


`
Thanks for reading :)
`
<br>
`
Have an absolutely fantastic day ahead :D
`

