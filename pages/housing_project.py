import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

model = joblib.load('models/housing_price_predictor_model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')

numerical_features = ['size', 'Czynsz', 'price_per_sqm', 'has_balkon', 'has_taras', 'has_garaż_miejsce_parkingowe', 'has_piwnica', 'has_oddzielna_kuchnia', 'has_ogródek', 'has_pom._użytkowe']
categorical_features = ['Ogrzewanie', 'Stan wykończenia', 'Rynek', 'Forma własności', 'Typ ogłoszeniodawcy', 'neighborhood']

ogrzewanie_options = ['miejskie', 'gazowe', 'elektryczne', 'inne', 'brak', 'piece kaflowe', 'kotłownia']
stan_wykonczenia_options = ['do wykończenia', 'do remontu', 'wysoki standard', 'dobry', 'bardzo dobry', 'developerski']
rynek_options = ['wtórny', 'pierwotny']
forma_wlasnosci_options = ['pełna własność', 'spółdzielcze własnościowe', 'udział']
typ_ogloszeniodawcy_options = ['prywatne', 'agencja']
neighborhood_options = ['Śródmieście', 'Mokotów', 'Wola', 'Ursynów', 'Bielany', 'Praga-Południe', 'Targówek', 'Bemowo', 'Ochota', 'Praga-Północ', 'Białołęka', 'Wawer', 'Żoliborz', 'Wilanów', 'Rembertów', 'Wesoła', 'Ursus']

st.title("🏡 Warsaw Housing Price Predictor")
st.markdown("Welcome! Fill out the details below to estimate the price of a property in Warsaw.")

with st.expander("Property Details"):
    col1, col2 = st.columns(2)
    size = col1.number_input('Size (m²)', min_value=1.0, value=50.0)
    czynsz = col2.number_input('Monthly Rent (Czynsz)', min_value=0.0, value=300.0)

    ogrzewanie = st.selectbox('Heating (Ogrzewanie)', ogrzewanie_options)
    stan_wykonczenia = st.selectbox('Finishing Standard (Stan wykończenia)', stan_wykonczenia_options)
    rynek = st.selectbox('Market (Rynek)', rynek_options)
    forma_wlasnosci = st.selectbox('Ownership Form (Forma własności)', forma_wlasnosci_options)
    typ_ogloszeniodawcy = st.selectbox('Advertiser Type (Typ ogłoszeniodawcy)', typ_ogloszeniodawcy_options)
    neighborhood = st.selectbox('Neighborhood', neighborhood_options)

    st.subheader("Amenities")
    col3, col4, col5 = st.columns(3)
    has_balkon = col3.checkbox('Balcony')
    has_taras = col4.checkbox('Terrace')
    has_garaz_miejsce_parkingowe = col5.checkbox('Garage/Parking')
    has_piwnica = col3.checkbox('Basement')
    has_oddzielna_kuchnia = col4.checkbox('Separate Kitchen')
    has_ogrodek = col5.checkbox('Garden')
    has_pom_uzytkowe = col3.checkbox('Utility Room')

input_data = pd.DataFrame({
    'size': [size],
    'Czynsz': [czynsz],
    'Ogrzewanie': [ogrzewanie],
    'Stan wykończenia': [stan_wykonczenia],
    'Rynek': [rynek],
    'Forma własności': [forma_wlasnosci],
    'Typ ogłoszeniodawcy': [typ_ogloszeniodawcy],
    'neighborhood': [neighborhood],
    'has_balkon': [int(has_balkon)],
    'has_taras': [int(has_taras)],
    'has_garaż_miejsce_parkingowe': [int(has_garaz_miejsce_parkingowe)],
    'has_piwnica': [int(has_piwnica)],
    'has_oddzielna_kuchnia': [int(has_oddzielna_kuchnia)],
    'has_ogródek': [int(has_ogrodek)],
    'has_pom._użytkowe': [int(has_pom_uzytkowe)],
})

input_data['price_per_sqm'] = np.nan
if size != 0:
    input_data['price_per_sqm'] = input_data['Czynsz'] / size
else:
    input_data['price_per_sqm'] = 0

if st.button('Estimate Price'):
    input_data = input_data[numerical_features + categorical_features + ['price_per_sqm']]
    input_data = input_data.drop('price_per_sqm', axis=1)
    input_data['price_per_sqm'] = input_data['Czynsz'] / size if size != 0 else 0
    log_price_pred = model.predict(input_data)
    predicted_price = np.exp(log_price_pred)[0]
    st.markdown(f"<p class='big-font'>Estimated Price: {predicted_price:,.2f} zł</p>", unsafe_allow_html=True)

    col_vis1, col_vis2 = st.columns(2)

    with col_vis1:
        with st.expander("Feature Importance"):
            xgb_model = model.named_steps['regressor']
            feature_importance = xgb_model.feature_importances_
            feature_names = preprocessor.get_feature_names_out()
            feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
            feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

            fig, ax = plt.subplots(figsize=(10, 6))  
            sns.barplot(x='Importance', y='Feature', data=feature_importance_df, ax=ax, color="#4db6ac")
            ax.set_title('Feature Importance', color="#ffffff")
            ax.set_xlabel('Importance', color="#ffffff")
            ax.set_ylabel('Feature', color="#ffffff")
            ax.tick_params(axis='x', colors="#ffffff")
            ax.tick_params(axis='y', colors="#ffffff")
            ax.set_facecolor("#112d4e")
            fig.patch.set_facecolor("#112d4e")
            st.pyplot(fig, use_container_width=True)  

    with col_vis2:
        with st.expander("Neighborhood Map"):
            st.write(f"Selected Neighborhood in Warsaw: {neighborhood}")

            if neighborhood == 'Śródmieście':
                st.map(pd.DataFrame({'lat': [52.231958], 'lon': [21.006725]}))
            elif neighborhood == 'Mokotów':
                st.map(pd.DataFrame({'lat': [52.1901], 'lon': [21.0252]}))
            elif neighborhood == 'Wola':
                st.map(pd.DataFrame({'lat': [52.2384], 'lon': [20.9859]}))
            elif neighborhood == 'Ursynów':
                st.map(pd.DataFrame({'lat': [52.1647], 'lon': [21.0234]}))
            elif neighborhood == 'Bielany':
                st.map(pd.DataFrame({'lat': [52.2858], 'lon': [20.9381]}))
            elif neighborhood == 'Praga-Południe':
                st.map(pd.DataFrame({'lat': [52.2366], 'lon': [21.0543]}))
            elif neighborhood == 'Targówek':
                st.map(pd.DataFrame({'lat': [52.2796], 'lon': [21.0396]}))
            elif neighborhood == 'Bemowo':
                st.map(pd.DataFrame({'lat': [52.2598], 'lon': [20.9304]}))
            elif neighborhood == 'Ochota':
                st.map(pd.DataFrame({'lat': [52.2198], 'lon': [20.9793]}))
            elif neighborhood == 'Praga-Północ':
                st.map(pd.DataFrame({'lat': [52.2611], 'lon': [21.0366]}))
            elif neighborhood == 'Białołęka':
                st.map(pd.DataFrame({'lat': [52.3168], 'lon': [20.9926]}))
            elif neighborhood == 'Wawer':
                st.map(pd.DataFrame({'lat': [52.1895], 'lon': [21.1391]}))
            elif neighborhood == 'Żoliborz':
                st.map(pd.DataFrame({'lat': [52.2673], 'lon': [20.9739]}))
            elif neighborhood == 'Wilanów':
                st.map(pd.DataFrame({'lat': [52.1678], 'lon': [21.0965]}))
            elif neighborhood == 'Rembertów':
                st.map(pd.DataFrame({'lat': [52.2514], 'lon': [21.1663]}))
            elif neighborhood == 'Wesoła':
                st.map(pd.DataFrame({'lat': [52.2618], 'lon': [21.1969]}))
            elif neighborhood == 'Ursus':
                st.map(pd.DataFrame({'lat': [52.1965], 'lon': [20.8931]}))

    with st.expander("Price Distribution by Neighborhood"):
        st.write("Price Distribution by Neighborhood")
        data = pd.read_csv(r'models/Otodom_Webscraped.csv')
        data['price'] = data['price'].str.replace(' zł', '', regex=False).str.replace(' ', '', regex=False)
        data['price'] = pd.to_numeric(data['price'], errors='coerce')

        fig_price_dist, ax_price_dist = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='neighborhood', y='price', data=data, ax=ax_price_dist, color="#4db6ac")
        ax_price_dist.set_title('Price Distribution by Neighborhood', color="#ffffff")
        ax_price_dist.set_xlabel('Neighborhood', color="#ffffff")
        ax_price_dist.set_ylabel('Price', color="#ffffff")
        ax_price_dist.tick_params(axis='x', colors="#ffffff", rotation=45)
        ax_price_dist.tick_params(axis='y', colors="#ffffff")
        ax_price_dist.set_facecolor("#112d4e")
        fig_price_dist.patch.set_facecolor("#112d4e")
        ax_price_dist.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
        st.pyplot(fig_price_dist, use_container_width=True)