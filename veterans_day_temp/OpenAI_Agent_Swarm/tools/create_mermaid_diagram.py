import openai

openai.api_key = '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'

def extract_code_structure(python_file_path):
    with open(python_file_path, 'r') as file:
        code_content = file.read()
    return code_content

def create_mermaid_diagram(python_file_path, diagram_type):
    code_structure = extract_code_structure(python_file_path)
    prompt = f"Generate the source text for a {diagram_type} Mermaid diagram based on this Python code:\n\n```python\n{code_structure}\n```\n"

    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        prompt=prompt,
        max_tokens=150
    )

    mermaid_diagram_source = response.choices[0].text.strip()
    return mermaid_diagram_source