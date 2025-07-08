import requests
import pandas as pd

def fetch_remotive_jobs():
    url = "https://remotive.io/api/remote-jobs?search=machine+learning"
    response = requests.get(url)
    jobs = response.json().get("jobs", [])
    return [{
        "company": job["company_name"],
        "title": job["title"],
        "location": job["candidate_required_location"],
        "url": job["url"],
        "tags": job["tags"]
    } for job in jobs if "India" in job["candidate_required_location"] or "Remote" in job["candidate_required_location"]]

if __name__ == "__main__":
    jobs = fetch_remotive_jobs()
    pd.DataFrame(jobs).to_csv("jobs/remotive_jobs.csv", index=False)
