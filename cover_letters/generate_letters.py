from jinja2 import Template
import os

def generate_cover_letter(company, role):
    with open("templates/cover_letter_template.txt") as f:
        template = Template(f.read())
    letter = template.render(company=company, role=role)
    output_path = f"cover_letters/{company}_{role}_cover_letter.txt"
    with open(output_path, "w") as f:
        f.write(letter)
    return output_path
