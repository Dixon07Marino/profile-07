from fastapi import FastAPI
import requests, json

app = FastAPI()

url = 'https://api.github.com/users/Dixon07Marino'
url_ = 'https://api.github.com/users/Dixon07Marino/repos'

@app.get("/api/profile/Dixon07Marino")
async def get_profile():
    response = requests.get(url).json()
    with open('profile.json', 'w') as f:
        f.write(json.dumps(response, indent=4))
        return {"message": "Profile data saved to profile.json"}
    
@app.get("/api/repos/Dixon07Marino")
async def get_repos():
    response = requests.get(url_).json()
    with open('repos.json', 'w') as f:
        f.write(json.dumps(response, indent=4))
        return {"message": "Repos data saved to repos.json"}