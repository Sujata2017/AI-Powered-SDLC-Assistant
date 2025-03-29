import requests, base64
from datetime import datetime

def push_files_to_github(token, repo, files):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # ✅ Check if repo exists
    repo_check = requests.get(f"https://api.github.com/repos/{repo}", headers=headers)
    if repo_check.status_code == 404:
        user = repo.split("/")[0]
        repo_name = repo.split("/")[1]
        create_resp = requests.post(
            "https://api.github.com/user/repos",
            headers=headers,
            json={"name": repo_name, "private": False, "auto_init": True}
        )
        if create_resp.status_code not in [200, 201]:
            raise Exception(f"❌ Repo creation failed: {create_resp.text}")
    elif repo_check.status_code != 200:
        raise Exception(f"❌ Failed to access repo: {repo_check.text}")

    # ✅ Push/Update Files
    for filename, content in files.items():
        url = f"https://api.github.com/repos/{repo}/contents/{filename}"
        encoded_content = base64.b64encode(content.encode()).decode()
        commit_msg = f"Update {filename} via SDLC App on {datetime.now().isoformat()}"

        # 👇 Check if file already exists to get SHA
        get_resp = requests.get(url, headers=headers)
        sha = get_resp.json().get("sha") if get_resp.status_code == 200 else None

        payload = {
            "message": commit_msg,
            "content": encoded_content,
            "branch": "main"
        }
        if sha:
            payload["sha"] = sha  # 🧠 required for updates

        put_resp = requests.put(url, headers=headers, json=payload)
        if put_resp.status_code not in [200, 201]:
            raise Exception(f"❌ Failed to upload {filename}: {put_resp.text}")
