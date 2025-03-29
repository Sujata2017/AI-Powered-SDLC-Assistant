from utils.logger import log_output

def design_agent(llm, state):
    prompt = f"""
You are a senior software architect.

You are given:
- Original Requirement
- Product Owner's Review
- A list of User Stories

Your task:
Create a **Comprehensive Design Document**.

For each user story:
1. Add heading: ## 🧵 User Story N: [title]
2. Write:
   - 🔹 Functional Specifications
   - 🔧 Technical Specifications
   - 🏗 Architecture Diagrams (at least 2):
       - Sequence Diagram
       - Flowchart or Layered Architecture
       - Use Markdown syntax (Mermaid or code blocks)

=== Context ===
Original Requirement:
{state.get("input", "")}

Product Owner Review:
{state.get("po_review", "")}

User Stories:
{state.get("user_stories", "")}

Generate structured output in Markdown.
"""
    response = llm.invoke(prompt).content
    return log_output("DesignAgent", {"design_doc": response})


def design_review_agent(llm, state):
    prompt = f"""
You are a senior reviewer.

Review the following **Comprehensive Design Document**. For each user story:
- Check completeness of functional/technical specs
- Comment on clarity and architecture diagrams
- Suggest improvements if needed
- If everything looks good, write: ✅ APPROVED for this section

Design Document:
{state['design_doc']}

Review it section-by-section and return suggestions or ✅ approvals.
"""
    response = llm.invoke(prompt).content
    return log_output("DesignReviewAgent", {"design_review": response})
