import requests
import json
import random

def random_int():
    return random.randint(1, 9)

url = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json'}
data = {
    'patient_id': "P234234",
    'age': 44,  # Usia
    'gender': 1,  # 1 untuk pria, 2 untuk wanita
    'air_pollution': 6,
    'alcohol_use': 7,
    'dust_allergy': 7,
    'occupational_hazards': 7,
    'genetic_risk': 7,
    'chronic_lung_disease': 6,
    'balanced_diet': 7,
    'obesity': 7,
    'smoking': 7,
    'passive_smoker': 8,
    'chest_pain': 7,
    'coughing_of_blood': 7,
    'fatigue': 5,
    'weight_loss': 3,
    'shortness_of_breath': 2,
    'wheezing': 7,
    'swallowing_difficulty': 8,
    'clubbing_of_finger_nails': 2,
    'frequent_cold': 4,
    'dry_cough': 5,
    'snoring': 3,
}

# Format string output
output = f"{data['patient_id']},{data['age']},{data['gender']}," + \
         f"{data['air_pollution']},{data['alcohol_use']},{data['dust_allergy']}," + \
         f"{data['occupational_hazards']},{data['genetic_risk']},{data['chronic_lung_disease']}," + \
         f"{data['balanced_diet']},{data['obesity']},{data['smoking']}," + \
         f"{data['passive_smoker']},{data['chest_pain']},{data['coughing_of_blood']}," + \
         f"{data['fatigue']},{data['weight_loss']},{data['shortness_of_breath']}," + \
         f"{data['wheezing']},{data['swallowing_difficulty']},{data['clubbing_of_finger_nails']}," + \
         f"{data['frequent_cold']},{data['dry_cough']},{data['snoring']}"

print(output)

response = requests.post(url, headers=headers, data=json.dumps(data))

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Debug status code and content
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content.decode('utf-8')}")

    # Only try to parse JSON if the status code is 200 (OK)
    if response.status_code == 200:
        try:
            result = response.json()
            print(f"Hasil: {result['result']}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response content was: {response.content.decode('utf-8')}")
    else:
        print(f"Terjadi error saat memanggil API: {response.content.decode('utf-8')}")

except Exception as e:
    print(f"An error occurred: {e}")