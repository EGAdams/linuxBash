from mermaid_generator import generate_all_diagrams

def generate_mermaid_diagrams(source_code, output_path):
    # Analyze the source code and create diagrams
    diagrams = generate_all_diagrams(source_code)
    
    # Save each diagram to a separate Markdown file
    for diagram_type, diagram_code in diagrams.items():
        file_name = f"{output_path}/{diagram_type}.md"
        with open(file_name, "w") as f:
            f.write(f"# {diagram_type.replace('_', ' ').title()} Diagram\n\n")
            f.write("```mermaid\n")
            f.write(diagram_code)
            f.write("\n```")
    
    return {"message": "Mermaid diagrams created and saved to specified path."}
