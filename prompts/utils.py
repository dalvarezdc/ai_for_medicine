def generate_prompts(research_info: dict, subject: str):
    prompts = []
    apa_reference = "References: AuthorLastName, AuthorFirstInitial. (Year). Title of the Source. Publisher. URL: [URL]"
    subject_reference = f"For the following subject {subject}, Explain in detail:"

    for category, details in research_info.items():
        for subcategory, content in details.items():
            if isinstance(content, dict):
                for key, value in content.items():
                    # prompt = f"Explain in detail: {category} - {subcategory} - {key}: {value}"
                    prompt = f"{subject_reference} {subcategory} - {key}: {value}. ADD: {apa_reference}"
                    prompts.append(prompt)
            else:
                # prompt = f"Explain in detail: {category} - {subcategory}: {content}"
                prompt = f"{subject_reference}  {subcategory}: {content}. ADD: {apa_reference}"
                prompts.append(prompt)

    print(*prompts, sep='\n\n')
    return prompts


