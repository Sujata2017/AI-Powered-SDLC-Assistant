from utils.logger import log_output

def security_review_agent(llm, state):
    prompt = f"Check this code for potential security issues and respond with APPROVED or suggestions:\n{state['code']}"
    #response = llm.predict(prompt)
    response = llm.invoke(prompt).content
    return log_output("SecurityReviewAgent", {"security_review": response})