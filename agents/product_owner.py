from utils.logger import log_output

def product_owner_agent(llm, state):
    prompt = f"Review the following user stories and respond with APPROVED or suggestions:\n{state['user_stories']}"
    #response = llm.predict(prompt)
    response = llm.invoke(prompt).content
    return log_output("ProductOwnerAgent", {"po_review": response})