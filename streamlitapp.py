
import pickle
import streamlit as st
import pandas as pd

# Load the trained model
with open('C:/Users/pc/Downloads/hamoye_group_project_real/model (1).pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Streamlit app
def main():
    st.title('Kidney Disease Prediction')

    # Create input form for patient information
    age = st.number_input('Age', min_value=1, max_value=120, value=30)
    bp = st.number_input('Blood Pressure (mmHg)', min_value=0, value=80)
    al = st.number_input('Albumin', min_value=0, value=0)
    su = st.number_input('Sugar', min_value=0, value=0)
    rbc = st.selectbox('Red Blood Cells', ['normal', 'abnormal'])
    pc = st.selectbox('Pus Cell', ['normal', 'abnormal'])
    pcc = st.selectbox('Pus Cell Clumps', ['notpresent', 'present'])
    ba = st.selectbox('Bacteria', ['notpresent', 'present'])
    bgr = st.number_input('Random Blood Glucose (mg/dL)', min_value=0, value=100)
    pcv = st.number_input('Packed Cell Volume', min_value=0, value=40)
    wbcc = st.number_input('White Blood Cell Count (cells/cubic mm)', min_value=0, value=8000)
    rbcc = st.number_input('Red Blood Cell Count (millions/cubic mm)', min_value=0, value=5)
    htn = st.selectbox('Hypertension', ['no', 'yes'])
    dm = st.selectbox('Diabetes Mellitus', ['no', 'yes'])
    cad = st.selectbox('Coronary Artery Disease', ['no', 'yes'])
    appet = st.selectbox('Appetite', ['poor', 'good'])
    pe = st.selectbox('Pedal Edema', ['no', 'yes'])
    ane = st.selectbox('Anemia', ['no', 'yes'])

    # Create input data DataFrame
    input_data = pd.DataFrame({
        'age': [age],
        'bp': [bp],
        'al': [al],
        'su': [su],
        'rbc': [rbc],
        'pc': [pc],
        'pcc': [pcc],
        'ba': [ba],
        'bgr': [bgr],
        'pcv': [pcv],
        'wbcc': [wbcc],
        'rbcc': [rbcc],
        'htn': [htn],
        'dm': [dm],
        'cad': [cad],
        'appet': [appet],
        'pe': [pe],
        'ane': [ane],
        'anemia': [0],  # Placeholder value for missing feature
        'bp_category': [0],  # Placeholder value for missing feature
        'bu': [0],  # Placeholder value for missing feature
        'glucose_bp_ratio': [0],  # Placeholder value for missing feature
        'hemo': [0],  # Placeholder value for missing feature
        'mcv': [0],  # Placeholder value for missing feature
        'pot': [0],  # Placeholder value for missing feature
        'sc': [0],  # Placeholder value for missing feature
        'sg': [0],  # Placeholder value for missing feature
        'sod': [0],  # Placeholder value for missing feature
        'total_blood_cell_count': [0]  # Placeholder value for missing feature
    })

    # Reorder the columns to match the trained model's feature order
    input_data = input_data[[
        'age', 'bp', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'pcv', 'wbcc', 'rbcc', 'htn',
        'dm', 'cad', 'appet', 'pe', 'ane', 'anemia', 'bp_category', 'bu', 'glucose_bp_ratio',
        'hemo', 'mcv', 'pot', 'sc', 'sg', 'sod', 'total_blood_cell_count'
    ]]

    # Create a button for prediction
    

    if st.button('Predict'):
        try:
            # Make prediction
            prediction = model.predict(input_data)[0]

            # Display the prediction result
            if prediction == 'ckd':
                st.success('The prediction result is: Chronic Kidney Disease (CKD)')
            else:
                st.success('The prediction result is: Not Chronic Kidney Disease (Not CKD)')
        except:
            st.error('Prediction failed. Please check your inputs.')

if __name__ == '__main__':
    main()

