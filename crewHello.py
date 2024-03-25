#------------------------------------------------------------
# crewHello.py
#------------------------------------------------------------
# Inital Setup
#   cd \Users\gb105\OneDrive\go\home\Github\AgentHello
#   python -m venv venv
#   .\venv\Scripts\activate
#   pip install crewai
#   pip install crewai[tools]
# 
#---------------------------------------------------------
import os
#os.environ["SERPER_API_KEY"] = "15ef214.......6b36362bbe7579" # serper.dev API key
serper_api_key = os.getenv("SERPER_API_KEY")

#os.environ["OPENAI_API_KEY"] = "sk-p9BjfozWJiX....NWc6kALEdwC2vwQZd"
openai_api_key = os.getenv("OPENAI_API_KEY")

from crewai import Agent
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
  role='Senior Researcher',
  goal='Uncover groundbreaking technologies in {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could change"
    "the world."
  ),
  tools=[search_tool],
  allow_delegation=True,
  max_iter=2 
)

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[search_tool],
  allow_delegation=False
)
