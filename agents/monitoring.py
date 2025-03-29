from utils.logger import log_output

def monitoring_agent(llm, state):
    prompt = "Post-deployment monitoring: simulate or analyze errors/issues if any."
    #response = llm.predict(prompt)
    response = llm.invoke(prompt).content
    return log_output("MonitoringAgent", {"monitoring_feedback": response})