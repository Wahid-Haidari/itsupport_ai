# Backend

# Frontend

# Challenges and learnin outcomes

### Jamshed

1. Backend
- *Keeping a server running in production in an AWS EC2 instance:* We choose FastAPI (a python web framework) because it makes it very fast to set up a server that serves APIs. Fast API uses uvicorn to set up another server which serves the requests made to the API. I set up an nginx web server, which router to localhost port 8000 where the uvicorn server could respond to API requests. But the issue was that whenever I closed the terminal through which I was connected to, the uvicorn server went down. And the API wasn't accessible. I found out that I need to create systemd service file to keep the server running. All the steps that I took are outlined here. 

2. Frontend
- *Conditional rendering*: How to display a loading message and replace that with the actual response that comes from the backend. It took a lot of trial an error to finally make it work. I set up the gpt_reply prop to an empty text and in the component put a conditional rendering. If text is === '', then show the loading message, otherwise show the message that comes from GPT. I tried with isLoading state which gets set to false after the response comes from the backend, but that did not work. 

