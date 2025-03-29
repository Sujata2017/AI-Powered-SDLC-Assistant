from utils.logger import log_output

def requirement_agent(llm, state):
    prompt = f"Analyze the following software requirement and break it into user stories:\n{state['input']}"
    #response = llm.predict(prompt)
    #response = llm.invoke(prompt)
    response = llm.invoke(prompt).content
    return log_output("RequirementAgent", {"user_stories": response})