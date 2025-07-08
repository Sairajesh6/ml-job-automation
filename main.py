from jobs.scrape_jobs import fetch_remotive_jobs
from cover_letters.generate_letters import generate_cover_letter
from mailer.send_email import send_email
from utils.config import USER_SKILLS
from utils.match_score import compute_match_score
from resume.update_resume import update_resume

if __name__ == "__main__":
    jobs = fetch_remotive_jobs()
    selected_jobs = [job for job in jobs if compute_match_score(job['title'], USER_SKILLS) >= 0.5]

    body = "Here are today's top matched AI/ML jobs:\n\n"
    attachments = []

    for job in selected_jobs[:5]:
        body += f"{job['title']} at {job['company']} - {job['url']}\n"
        update_resume(job['company'], job['title'])
        letter_path = generate_cover_letter(job['company'], job['title'])
        attachments.append(letter_path)

    send_email(
        subject="🚀 Daily AI/ML Job Picks",
        body=body,
        to="sairajeshvelagana6@gmail.com",
        attachments=attachments
    )
