from utils.logger import log_output


#def code_generation_agent(llm, state):
    #prompt = f"Write clean, well-documented Python code based on this design:\n{state['design_doc']}"
    #response = llm.predict(prompt)
    #response = llm.invoke(prompt).content
    #return log_output("CodeGenAgent", {"code": response})




def code_generation_agent(llm, state):
    prompt = (
        f"Generate production-ready deployable code based on this design doc:\n\n"
        f"{state['design_doc']}\n\n"
        "Return ONLY the actual code files as separate sections, like this format:\n\n"
        "=== app.py ===\n<python code>\n\n"
        "=== templates/index.html ===\n<html code>\n\n"
        "=== static/styles.css ===\n<css>\n\n"
        "DO NOT include explanation, only raw code."
    )
    response = llm.invoke(prompt).content
    return log_output("CodeGenerationAgent", {"code": response})



def code_review_agent(llm, state):
    prompt = f"Review this code and provide feedback or respond with APPROVED:\n{state['code']}"
    #response = llm.predict(prompt)
    response = llm.invoke(prompt).content
    return log_output("CodeReviewAgent", {"code_review": response})