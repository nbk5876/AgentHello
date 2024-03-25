#---------------------------------------------------------
# crewHelloFormup.py
# Assemble the Crew
#---------------------------------------------------------
from crewai import Crew, Process
from crewHello import researcher, writer
from crewHelloTasks import research_task, write_task


# Forming the tech-focused crew with enhanced configurations
crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential  # Optional: Sequential task execution is default
)

if __name__ == "__main__":
    #main()
    print("Running crewHelloFormup.py")

    # Starting the task execution process with enhanced feedback
    #result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
    #result = crew.kickoff(inputs={'topic': 'whimsical cat and mouse stories'})
    result = crew.kickoff(inputs={'topic': 'tank warefare'})

    print(result)


