#AI based Mental Health Support system 

Mental Health assistant that provides personalized mental health resources , including coping strategies and self care recommendations . The platform uses AI to analyze user inputs and perform sentiment analysis on user journals , offering personalized advice and resources. 

#Features
- sentiment analysis
- personalized recommendations

#Technologies used 

- Streamlit : for creating front end UI
- Pathway : for data processing and indexing 
- Gemini API : for AI generated personalized recommendations 
- Docker 


#how to run the project
- First , clone the repository and then run **docker build --network=host -t mental_health_assistant .**
- Then run **docker run -p 8501:8501 mental_health_support**