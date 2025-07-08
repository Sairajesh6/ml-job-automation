def compute_match_score(job_title, skills):
    match = sum(skill.lower() in job_title.lower() for skill in skills)
    return match / len(skills)
