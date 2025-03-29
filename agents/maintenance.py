from utils.logger import log_output

def maintenance_agent(llm, state):
    prompt = f"Based on the following feedback, suggest bug fixes or improvements:\n{state['monitoring_feedback']}"
    #response = llm.predict(prompt)
    response = llm.invoke(prompt).content
    return log_output("MaintenanceAgent", {"maintenance_done": response})