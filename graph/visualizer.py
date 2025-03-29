from graphviz import Digraph

def render_langgraph_diagram():
    dot = Digraph(format='png')
    dot.attr(rankdir='TB', fontname='Helvetica', fontsize='10')

    stages = {
        "Input": "UI: User Inputs Requirements",
        "GenerateStories": "Auto-generate User Stories",
        "POReview": "Product Owner Review",
        "ReviseStories": "Revise User Stories",
        "DesignDoc": "Create Design Documents - Functional and Technical",
        "DesignReview": "Design Review",
        "GenerateCode": "Generate Code",
        "CodeReview": "Code Review",
        "FixCodeReview": "Fix Code after Code Review",
        "SecurityReview": "Security Review",
        "FixSecurity": "Fix Code after Security",
        "WriteTests": "Write Test Cases",
        "TestReview": "Test Cases Review",
        "FixTests": "Fix Test Cases after Review",
        "QA": "QA Testing",
        "FixQA": "Fix Code after QA Feedback",
        "Deploy": "Deployment",
        "Monitor": "Monitoring and Feedback",
        "Maintain": "Maintenance and Updates"
    }

    for node, label in stages.items():
        dot.node(node, label, shape='box', style='filled,rounded', fillcolor='#e6f2ff')

    # Edges representing LangGraph workflow
    edges = [
        ("Input", "GenerateStories"),
        ("GenerateStories", "POReview"),
        ("POReview", "ReviseStories"),
        ("ReviseStories", "GenerateStories"),
        ("POReview", "DesignDoc"),
        ("DesignDoc", "DesignReview"),
        ("DesignReview", "DesignDoc"),
        ("DesignReview", "GenerateCode"),
        ("GenerateCode", "CodeReview"),
        ("CodeReview", "FixCodeReview"),
        ("FixCodeReview", "GenerateCode"),
        ("CodeReview", "SecurityReview"),
        ("SecurityReview", "FixSecurity"),
        ("FixSecurity", "GenerateCode"),
        ("SecurityReview", "WriteTests"),
        ("WriteTests", "TestReview"),
        ("TestReview", "FixTests"),
        ("FixTests", "WriteTests"),
        ("TestReview", "QA"),
        ("QA", "FixQA"),
        ("FixQA", "GenerateCode"),
        ("QA", "Deploy"),
        ("Deploy", "Monitor"),
        ("Monitor", "Maintain"),
        ("Maintain", "Input")
    ]
    for src, dst in edges:
        dot.edge(src, dst)

    return dot.source  # Streamlit supports rendering DOT source
