import streamlit as st
import requests

st.title('Customer Churn Prediction')

st.write('Enter Customer Data:  ')


gender=st.selectbox(
    'Gender',["Male", "Female"]
)

phone_service=st.selectbox(
    "Phone Service", ['Yes','No']
)
internet=st.selectbox(
    'Internet Service',['Fiber Optic','DSL' ,'No']
)
contract=st.selectbox(
    'Contract', ["Month-to-month", "One year","Two year"]
    
)

paperless=st.selectbox(
    "Paperless Billing", ['Yes', 'No']
)

payment_method=st.selectbox(
    "Payment Method",
    [ "Electronic Check", "Mailed Check", "Credit Card","Bank Transfer"]
)


if st.button("Predict Churn"):

    payload = {
        "gender": gender,
        "PhoneService": phone_service,
        "InternetService": internet,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment_method
    }

    response = requests.post(
        "http://fastapi:8000/predict",
        json=payload
    )

    prediction = response.json()

    
    if prediction['prediction'] == 'Yes':
        st.write(f'Probality of the Customer will be churn: {prediction["probability"]}')
        st.write(f'Baseline model Prediction: {prediction['baseline']}')
        st.error(f"Customer likely to churn.")
    else:
        st.write(f'Probality of Customer will not be Churn: {prediction["probability"]}')
        st.write(f'Baseline model Prediction: {prediction['baseline']}')
        st.success("Customer likely to stay.")
    