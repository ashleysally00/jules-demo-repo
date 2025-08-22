import requests

OWNER = "ashleysally00" 
REPO = "jules-demo-repo"  

url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

response = requests.get(url)

if response.status_code == 200:
    issues = response.json()
    if issues:
        for issue in issues:
            print(f"Issue: {issue['title']} (#{issue['number']})")
    else:
        print("✅ No issues found.")
else:
    print(f"❌ Error: {response.status_code} - {response.json().get('message')}")
