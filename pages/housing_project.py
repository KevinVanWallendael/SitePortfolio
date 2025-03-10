import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the pre-trained model and preprocessor
model = joblib.load("models/housing_price_predictor_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# Define the features for the model
categorical_features = ['Ogrzewanie', 'Piętro', 'Stan wykończenia', 'Rynek', 'Forma własności', 'Typ ogłoszeniodawcy', 'neighborhood']
numerical_features = ['size', 'Czynsz', 'has_czynsz', 'price_per_sqm']

# List of amenities
amenities = ['balkon', 'taras', 'garaż/miejsce parkingowe', 'piwnica', 'oddzielna kuchnia', 'ogródek', 'pom. użytkowe']

# 🌟 Streamlit UI
st.title("🏡 Warsaw Housing Price Predictor")
st.markdown("Welcome! Fill out the details below to estimate the price of a property in Warsaw.")

# 🔹 **1. Property Details**
st.header("1. Property Details")
col1, col2 = st.columns(2)
with col1:
    size = st.number_input("Size (m²)", min_value=10, max_value=500, value=50, step=1)
    czynsz = st.number_input("Monthly Cost (PLN)", min_value=0, max_value=5000, value=500, step=10)
with col2:
    ogrzewanie = st.selectbox("Heating", ["miejskie", "gazowe", "elektryczne", "brak informacji"])
    pietro = st.selectbox("Floor", ["parter/3", "1/3", "2/3", "3/3", "4+", "brak informacji"])

# 🔹 **2. Property Condition and Type**
st.header("2. Property Condition and Type")
col3, col4 = st.columns(2)
with col3:
    stan_wykonczenia = st.selectbox("Condition", ["do zamieszkania", "do remontu", "deweloperski"])
    rynek = st.selectbox("Market", ["wtórny", "pierwotny"])
with col4:
    forma_wlasnosci = st.selectbox("Ownership", ["pełna własność", "spółdzielcze własnościowe", "brak informacji"])
    typ_ogloszeniodawcy = st.selectbox("Seller Type", ["prywatny", "biuro nieruchomości"])

# 🔹 **3. Location**
st.header("3. Location Details")
neighborhood = st.selectbox("Neighborhood", ["Praga-Północ", "Praga-Południe", "Śródmieście", "Mokotów", "Wola", "Żoliborz", "Ochota"])

# 🔹 **4. Amenities**
st.header("4. Amenities (Select Available Features)")
amenity_inputs = {amenity: st.checkbox(f"Has {amenity.capitalize()}") for amenity in amenities}

# Compute additional features
has_czynsz = 1 if czynsz > 0 else 0
price_per_sqm = size / czynsz if czynsz > 0 else 0

# Prepare user input data
user_data = pd.DataFrame([[size, czynsz, has_czynsz, price_per_sqm, ogrzewanie, pietro, stan_wykonczenia, rynek, forma_wlasnosci, typ_ogloszeniodawcy, neighborhood] + 
                          [1 if amenity_inputs[amenity] else 0 for amenity in amenities]],
                         columns=numerical_features + categorical_features + 
                                 [f'has_{amenity.replace("/", "_").replace(" ", "_").lower()}' for amenity in amenities])

# Ensure user_data has the correct columns
# expected_columns = numerical_features + categorical_features + [f'has_{amenity.replace("/", "_").replace(" ", "_").lower()}' for amenity in amenities]
# user_data = user_data[expected_columns]
# Ensure categorical variables are strings
user_data[categorical_features] = user_data[categorical_features].astype(str)

# Transform user input with the preprocessor
user_data_transformed = preprocessor.transform(user_data)



# Transform user input with the preprocessor
user_data_transformed = preprocessor.transform(user_data)

# 🔹 **Price Prediction**
st.markdown("---")
if st.button("Predict Price", use_container_width=True):
    predicted_price = np.exp(model.predict(user_data_transformed)[0]) 
    
    # Estimated MAE for range
    mae = 120000  
    lower_bound = predicted_price - mae
    upper_bound = predicted_price + mae

    st.subheader("🏠 Estimated Price:")
    st.markdown(f"<h1 style='text-align: center; color: green;'>{predicted_price:,.0f} PLN</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>Possible Range: {lower_bound:,.0f} - {upper_bound:,.0f} PLN</p>", unsafe_allow_html=True)

# 🔹 **Feature Importance Visualization**
st.markdown("---")
st.header("📊 Feature Importance")

# Extract feature importances
try:
    feature_names = model.named_steps['preprocessor'].get_feature_names_out()
    feature_importance = model.named_steps['regressor'].feature_importances_

    # Create DataFrame
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
    importance_df = importance_df.sort_values(by='Importance', ascending=False).head(10)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=importance_df, x='Importance', y='Feature', palette="coolwarm", ax=ax)

    # Titles and aesthetics
    plt.title("Feature Importance", fontsize=16, color="#ffffff")
    plt.xlabel("Importance", fontsize=12, color="#ffffff")
    plt.ylabel("Feature", fontsize=12, color="#ffffff")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.grid(axis="x", linestyle="--", alpha=0.5)

    # Dark mode theme adjustments
    fig.patch.set_facecolor("#0a192f")  
    ax.set_facecolor("#112d4e")  
    ax.tick_params(colors="#ffffff")  

    # Show plot
    st.pyplot(fig)

except AttributeError:
    st.write("Feature importance could not be displayed due to missing model attributes.")