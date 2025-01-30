from datetime import datetime
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
import datetime

# Uncomment the following line to use an example of a custom tool
# from prastav_ai.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@CrewBase
class PrastavAiCrew():
	"""PrastavAi crew"""

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			llm=LLM(model="ollama/deepseek-r1:8b", base_url="http://localhost:11434"),
			config=self.agents_config['project_Manager'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)
		print("Project Manager Agent created successfully.")

	@agent
	def solution_designer(self) -> Agent:
		return Agent(
			llm=LLM(model="ollama/deepseek-r1:8b", base_url="http://localhost:11434"),
			config=self.agents_config['solution_designer'],
			# tools=[SerperDevTool()],
			verbose=True
		)
		print("Solution designer Agent created successfully.")
	
	@agent
	def praposal_writer(self) -> Agent:
		return Agent(
			llm=LLM(model="ollama/deepseek-r1:8b", base_url="http://localhost:11434"),
			config=self.agents_config['praposal_writer'],
			verbose=True
		)
		print("Praposal writer Agent created successfully.")
	
	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			llm=LLM(model="ollama/deepseek-r1:8b", base_url="http://localhost:11434"),
			config=self.agents_config['financial_analyst'],
			# tools=[SerperDevTool()],
			verbose=True
		)
		print("Financial analyst Agent created successfully.")
	

	@task
	def project_planning_task(self) -> Task:
 	   return Task(
        config=self.tasks_config['project_planning_task'],
		output_file=f'output/project_planning_task_{now}.md',
    	)

	@task
	def project_analysis_task(self) -> Task:
		return Task(
		config=self.tasks_config['project_analysis_task'],
		output_file=f'output/project_analysis_task_{now}.md',
		)
	
	@task
	def praposal_writing_task(self) -> Task:
		return Task(
		config=self.tasks_config['praposal_writing_task'],
		output_file=f'output/praposal_writing_task_{now}.md',
		)
	

	@task
	def finance_Review_task(self) -> Task:
		return Task(
		config=self.tasks_config['finance_Review_task'],
		output_file=f'output/finance_Review_task_{now}.md',
		)

	
	@crew
	def crew(self) -> Crew:
		"""Creates the PrastavAi crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)  