## Inspiration
The whole team has been extremely excited with the introduction of ChatGPT and GPT-3 and 4 which can intereact with people in human-like conversations. Also, ChatGPT excels in many areas, it lacks very domain specific knowledge and we think that is an area we could improve. One example, working at University of Oklahoma IT support most of the requests we get are repeated and all we do is copy paste answers from a shared document we have. This is an area that GPT models could excel at. However, when we asked ChatGPT how I connect my XBox to AccessOU, here it gave an **incorrect** answer: 
```
AccessOU is an online learning platform provided by the University of Oklahoma, and it is not designed for connecting gaming consoles like Xbox. However, if you're looking to connect your Xbox to the internet through the university's network, you can follow these steps:

Connect your Xbox to the university's network using an Ethernet cable or a wireless connection. To connect wirelessly, go to the Xbox Dashboard, select "Settings," then "Network Settings," and choose the university's network.

If prompted, enter your university login credentials to authenticate your device and connect to the network.

If you're having trouble connecting your Xbox to the network, contact the university's IT helpdesk for assistance.

Note that while you can connect your Xbox to the university's network, you may not be able to play online games or access certain online features due to restrictions set by the university's network. Make sure to review the university's acceptable use policy for more information.

```
## What it does

## How we built it

## Challenges we ran into
### Jamshed
#### Backend
1. Keeping a server running in production in an AWS EC2 instance: We choose FastAPI (a python web framework) because it makes it very fast to set up a server that serves APIs. Fast API uses uvicorn to set up another server which serves the requests made to the API. I set up an nginx web server, which router to localhost port 8000 where the uvicorn server could respond to API requests. But the issue was that whenever I closed the terminal through which I was connected to, the uvicorn server went down. And the API wasn't accessible. I found out that I need to create systemd service file to keep the server running. All the steps that I took are outlined here.
#### Frontend
1. Conditional rendering: How to display a loading message and replace that with the actual response that comes from the backend. It took a lot of trial an error to finally make it work. I set up the gpt_reply prop to an empty text and in the component put a conditional rendering. If text is === '', then show the loading message, otherwise show the message that comes from GPT. I tried with isLoading state which gets set to false after the response comes from the backend, but that did not work.
### Mohamed
Data Collection and Preparation
Web scraping for IT support articles: To collect data for our GPT-3 model, we built a web scraper to download articles from the IT support website. We used a list of URLs representing different categories on the website and built functions to download the HTML content, extract article links, and save the articles as text files. The BeautifulSoup library was used for parsing the HTML content, and we ensured the extracted content was cleaned by removing unnecessary elements such as images and replacing anchor tags with their text followed by the URL in parentheses. This process helped us gather a clean dataset for our model.
Building the GPT-3 Model
Creating a chatbot for IT support: We utilized OpenAI's GPT-3 model to create a chatbot that can answer IT support-related questions. The collected and cleaned dataset was used to fine-tune the GPT-3 model, improving its ability to provide accurate and contextually relevant responses for IT support queries. The chatbot was built using the llama_index library, which provides a convenient interface for indexing and querying the GPT-3 model.


## Accomplishments that we're proud of

## What we learned

## What's next for itsupport.ai
