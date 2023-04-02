## Inspiration
The whole team has been extremely excited with the introduction of ChatGPT and GPT-3 and 4 which can intereact with people in human-like conversations. Also, ChatGPT excels in many areas, it lacks very domain specific knowledge and we think that is an area we could improve. One example, working at University of Oklahoma IT support most of the requests we get are repeated and all we do is copy paste answers from a shared document we have. This is an area that GPT models could excel at. However, when we asked ChatGPT how I connect my XBox to AccessOU, here it gave an **incorrect** answer: 
```
AccessOU is an online learning platform provided by the University of Oklahoma, and it is not designed for connecting gaming consoles like Xbox. However, if you're looking to connect your Xbox to the internet through the university's network, you can follow these steps:

Connect your Xbox to the university's network using an Ethernet cable or a wireless connection. To connect wirelessly, go to the Xbox Dashboard, select "Settings," then "Network Settings," and choose the university's network.

If prompted, enter your university login credentials to authenticate your device and connect to the network.

If you're having trouble connecting your Xbox to the network, contact the university's IT helpdesk for assistance.

Note that while you can connect your Xbox to the university's network, you may not be able to play online games or access certain online features due to restrictions set by the university's network. Make sure to review the university's acceptable use policy for more information.
```

And we wanted to create a chatbot that can act as customer support specialist for OU IT and answer the questions correctly. 
## What it does
There is a chat interface that a customer can ask a question. The makes a request to the backend and displays the response to the user. 
## How we built it
The collected and cleaned over 380 support articles from OU. We used llama-index to create index of the cleaned data. The prompt goes into the index and finds the exact context that can help asnwer the question. It sends the context to GPT-3 API with the user prompt and the GPT replies back to the user question based on the input. We stored the model in AWS server which can be accessed through an API. We build the API using FastAPI python framework. On the front-end, we build the UI using react.js and tailwind.css. 

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


### Wahid
To design the front-end, we encountered a challenge in creating a page layout that would keep certain components in place while allowing users to scroll through past messages. Our main objective was to ensure that components such as the chat input field and submit button remained fixed in position while users scrolled through previous messages.

In addition, we faced difficulties in making sure that the page automatically scrolled to the bottom to display the most recently generated response after a user had submitted a message. This required careful consideration of the page's layout and the use of appropriate code to achieve the desired functionality.

Overall, we were able to overcome these challenges through a combination of careful design and rigorous testing, and we are proud of the final result.

## Accomplishments that we're proud of

Efficient backend infrastructure: Successfully setting up a robust backend server using FastAPI and uvicorn on an AWS EC2 instance, and overcoming the challenge of maintaining server uptime by implementing a systemd service file.

*Responsive frontend design:( Implementing a user-friendly frontend that employs conditional rendering to display a loading message until a response is received from the backend. This ensures a seamless user experience and clear communication of the chatbot's status.

High-quality data collection and preparation: Developing a web scraper capable of collecting and cleaning IT support articles from various categories on the target website, resulting in a comprehensive dataset for fine-tuning the GPT-3 model.

Effective GPT-3 model fine-tuning: Successfully adapting the GPT-3 model to provide accurate and contextually relevant responses for IT support-related questions, demonstrating the model's potential to serve as a valuable IT support tool.

## What we learned
- Deploying an API server that is running on an AWS EC2 instance 24/7
- Customizing GPT-3 on our own data by using llama-index
- A deeper understand of how Large Language Models work. We believe customizing GPT models is the future
- Accessing OpenAI's APIs
- Responsive frontend design
- State management in React with API requests 

## What's next for itsupport.ai
Expanding the dataset and scope: Continuously improving the chatbot's performance by expanding the dataset, such as potentiallt incorporating OU IT's internal articles and support ticket history, and covering an even broader range of IT support topics to ensure comprehensive and accurate support.

User feedback integration: Implementing a user feedback mechanism to gain valuable insights into the chatbot's performance, which can be used to fine-tune the GPT-3 model and improve the overall user experience.

Multi-language support: Enhancing the chatbot's accessibility by adding multi-language support, enabling users from diverse backgrounds to access IT support in their preferred language.

Integration with other support channels: Exploring options to integrate itsupport.ai with existing IT support channels, such as helpdesk ticketing systems and live chat platforms, to provide seamless support experiences for users and improve the efficiency of IT support teams.

Personalized user experiences: Developing features that allow for personalized user experiences, such as remembering past interactions or providing tailored support based on user preferences and history.

Voice-enabled support: Expanding the chatbot's capabilities to include voice-enabled support, making it more accessible and convenient for users who prefer to interact with the chatbot through spoken language.

Analytics and reporting: Implementing analytics and reporting features to monitor the chatbot's performance, identify areas for improvement, and demonstrate the value it provides to IT support teams and end-users.
