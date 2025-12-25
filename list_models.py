from google import genai

client = genai.Client(api_key="AIzaSyCm4y-Il_pErcBjlAe71F-N_NxoyTIkMJM")

models = client.models.list()

for m in models:
    print(m.name)
