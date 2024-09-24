from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        listOfData = ['Patient Id', 'Age', 'Gender', 'Air Pollution', 'Alcohol use', 
                      'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk', 
                      'chronic Lung Disease', 'Balanced Diet', 'Obesity', 'Smoking', 
                      'Passive Smoker', 'Chest Pain', 'Coughing of Blood', 'Fatigue', 
                      'Weight Loss', 'Shortness of Breath', 'Wheezing', 
                      'Swallowing Difficulty', 'Clubbing of Finger Nails', 'Frequent Cold', 
                      'Dry Cough', 'Snoring']

        # Load the dataset
        file_path = 'dataset/cancer_patient_data_sets.csv'
        data = pd.read_csv(file_path)

        # Convert categorical columns to numeric if needed
        data['Patient Id'] = data['Patient Id'].astype('category').cat.codes  # Convert 'Patient Id' to categorical codes

        # Prepare the data for the model
        X = data[listOfData]
        y = data['Level']

        # Split the dataset into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Train a Naive Bayes model
        model = GaussianNB()
        model.fit(X_train, y_train)  # This should work if all data are numeric

        # Get JSON data from the request
        data = request.get_json()

        # Extract input values from JSON and convert 'patient_id' similarly
        patient_id = str(data['patient_id'])  # Keep it as string for display purposes
        patient_id_numeric = pd.Series(patient_id).astype('category').cat.codes[0]  # Convert to numeric
        age = int(data['age'])
        gender = int(data['gender'])
        air_pollution = int(data['air_pollution'])
        alcohol_use = int(data['alcohol_use'])
        dust_allergy = int(data['dust_allergy'])
        occupational_hazards = int(data['occupational_hazards'])
        genetic_risk = int(data['genetic_risk'])
        chronic_lung_disease = int(data['chronic_lung_disease'])
        balanced_diet = int(data['balanced_diet'])
        obesity = int(data['obesity'])
        smoking = int(data['smoking'])
        passive_smoker = int(data['passive_smoker'])
        chest_pain = int(data['chest_pain'])
        coughing_of_blood = int(data['coughing_of_blood'])
        fatigue = int(data['fatigue'])
        weight_loss = int(data['weight_loss'])
        shortness_of_breath = int(data['shortness_of_breath'])
        wheezing = int(data['wheezing'])
        swallowing_difficulty = int(data['swallowing_difficulty'])
        clubbing_of_finger_nails = int(data['clubbing_of_finger_nails'])
        frequent_cold = int(data['frequent_cold'])
        dry_cough = int(data['dry_cough'])
        snoring = int(data['snoring'])

        # Prepare input data for prediction
        input_data = pd.DataFrame([[patient_id_numeric, age, gender, air_pollution, alcohol_use, 
                                    dust_allergy, occupational_hazards, genetic_risk, 
                                    chronic_lung_disease, balanced_diet, obesity, smoking, 
                                    passive_smoker, chest_pain, coughing_of_blood, fatigue, 
                                    weight_loss, shortness_of_breath, wheezing, 
                                    swallowing_difficulty, clubbing_of_finger_nails, 
                                    frequent_cold, dry_cough, snoring]], columns=listOfData)

        # Make prediction
        prediction = model.predict(input_data)

        # Return prediction result
        return jsonify({'result': 'success', 'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e), 'line': str(e.__traceback__.tb_lineno)}), 500  # Return error message and line number

if __name__ == "__main__":
    app.run(debug=True)
