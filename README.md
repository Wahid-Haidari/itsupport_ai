# Backend

# Frontend

# Challenges and learnin outcomes

### Jamshed

1. Backend
- *Keeping a server running in production in an AWS EC2 instance:* We choose FastAPI (a python web framework) because it makes it very fast to set up a server that serves APIs. Fast API uses uvicorn to set up another server which serves the requests made to the API. I set up an nginx web server, which router to localhost port 8000 where the uvicorn server could respond to API requests. But the issue was that whenever I closed the terminal through which I was connected to, the uvicorn server went down. And the API wasn't accessible. I found out that I need to create systemd service file to keep the server running. All the steps that I took are outlined here. 

2. Frontend
- *Conditional rendering*: How to display a loading message and replace that with the actual response that comes from the backend. It took a lot of trial an error to finally make it work. I set up the gpt_reply prop to an empty text and in the component put a conditional rendering. If text is === '', then show the loading message, otherwise show the message that comes from GPT. I tried with isLoading state which gets set to false after the response comes from the backend, but that did not work. 


### Mohamed

1. Data Collection and Preparation
- *Web scraping for IT support articles:* To collect data for our GPT-3 model, we built a web scraper to download articles from the IT support website. We used a list of URLs representing different categories on the website and built functions to download the HTML content, extract article links, and save the articles as text files. The BeautifulSoup library was used for parsing the HTML content, and we ensured the extracted content was cleaned by removing unnecessary elements such as images and replacing anchor tags with their text followed by the URL in parentheses. This process helped us gather a clean dataset for our model. Navigating through the IT support website's structure and extracting useful information proved challenging, especially when handling nested elements and different types of content such as lists and images. Properly cleaning and formatting the extracted data also posed a challenge.

2. Building the GPT-3 Model
- *Creating a chatbot for IT support:* We utilized OpenAI's GPT-3 model to create a chatbot that can answer IT support-related questions. The collected and cleaned dataset was used to fine-tune the GPT-3 model, improving its ability to provide accurate and contextually relevant responses for IT support queries. The chatbot was built using the llama_index library, which provides a convenient interface for indexing and querying the GPT-3 model. Adapting the GPT-3 model to provide accurate and relevant responses specifically for IT support-related questions required a significant amount of trial and error, along with iterative fine-tuning using the collected dataset.

# Accomplishments that we're proud of


- *Efficient backend infrastructure:* Successfully setting up a robust backend server using FastAPI and uvicorn on an AWS EC2 instance, and overcoming the challenge of maintaining server uptime by implementing a systemd service file.

- *Responsive frontend design:( Implementing a user-friendly frontend that employs conditional rendering to display a loading message until a response is received from the backend. This ensures a seamless user experience and clear communication of the chatbot's status.

- *High-quality data collection and preparation:* Developing a web scraper capable of collecting and cleaning IT support articles from various categories on the target website, resulting in a comprehensive dataset for fine-tuning the GPT-3 model.

- *Effective GPT-3 model fine-tuning:* Successfully adapting the GPT-3 model to provide accurate and contextually relevant responses for IT support-related questions, demonstrating the model's potential to serve as a valuable IT support tool.

# What's next for itsupport.ai

- *Expanding the dataset and scope:* Continuously improving the chatbot's performance by expanding the dataset, incorporating more IT support websites, and covering an even broader range of IT support topics to ensure comprehensive and accurate support.

- *User feedback integration:* Implementing a user feedback mechanism to gain valuable insights into the chatbot's performance, which can be used to fine-tune the GPT-3 model and improve the overall user experience.

- *Multi-language support:* Enhancing the chatbot's accessibility by adding multi-language support, enabling users from diverse backgrounds to access IT support in their preferred language.

- *Integration with other support channels:* Exploring options to integrate itsupport.ai with existing IT support channels, such as helpdesk ticketing systems and live chat platforms, to provide seamless support experiences for users and improve the efficiency of IT support teams.

- *Personalized user experiences:* Developing features that allow for personalized user experiences, such as remembering past interactions or providing tailored support based on user preferences and history.

- *Voice-enabled support:* Expanding the chatbot's capabilities to include voice-enabled support, making it more accessible and convenient for users who prefer to interact with the chatbot through spoken language.

- *Analytics and reporting:* Implementing analytics and reporting features to monitor the chatbot's performance, identify areas for improvement, and demonstrate the value it provides to IT support teams and end-users.
