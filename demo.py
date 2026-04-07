import requests

BASE_URL = "https://rishav-515-it-support-env.hf.space"

def run_demo():
    print("🔄 Resetting environment...")
    res = requests.post(f"{BASE_URL}/reset")
    print("Reset Response:", res.json())

    print("\n➡ Step 1: Asking question")
    res = requests.post(f"{BASE_URL}/step", json={
        "action_type": "ask_question",
        "content": "What is your internet speed?"
    })
    print(res.json())

    print("\n➡ Step 2: Suggest fix")
    res = requests.post(f"{BASE_URL}/step", json={
        "action_type": "suggest_fix",
        "content": "restart router"
    })
    print(res.json())

if __name__ == "__main__":
    run_demo()