from utils.logger import log_output

def test_case_agent(llm, state):
    prompt = f"Write detailed test cases for the following Python code:\n\n{state['code']}\n\nInclude positive, negative, and edge cases. Format each test with:\n- Test Case\n- Steps\n- Expected Result"
    response = llm.invoke(prompt).content
    return log_output("TestCaseAgent", {"test_cases": response})


def test_case_review_agent(llm, state):
    prompt = f"Review these test cases and suggest improvements or respond with 'APPROVED':\n\n{state['test_cases']}"
    response = llm.invoke(prompt).content
    return log_output("TestCaseReviewAgent", {"test_case_review": response})






def qa_testing_agent(llm, state):
    prompt = f"""
    You are a QA tester.
You are given:
1. Python code to test
2. A list of test cases written for it
Simulate executing the test cases against the code. For each test:
- Describe what was tested
- Mention the actual vs expected result
- Declare the test as Passed or Failed
Only use the logic provided in the code. Do not hallucinate UI or unrelated modules.

    Test Cases:
    {state['test_cases']}

    Code:
    {state['code']}

    Provide QA test result with pass/fail status and brief justification for each case.
    """
    response = llm.invoke(prompt).content
    return log_output("QATestingAgent", {"qa_result": response})
