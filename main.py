import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pickle
from PIL import Image
import sklearn
from functions import (df_area_wrangle, df_wrangle, plot_town_avg_rent,
                       plot_all_town, plot_apart_type_price, pred_actual)
pd.options.display.float_format = '{:,.2f}'.format


with open("random_forest_Reg.pkl", "rb") as f:
    model = pickle.load(f)

df = df_wrangle()
df = df.drop(index=df.loc[df.bedroom > 6].index)
df = df.reset_index().drop(columns="index")

df_area = df_area_wrangle(df)
image = Image.open("lagos.jpg")
st.image(image, use_column_width=True)
st.markdown("<h1 style='text-align: center;'>House Rent Price in Lagos State</h1>", unsafe_allow_html=True)

st.markdown("""<p style='text-align:justify;'>
         This web application is designed to calculate the average price for renting an apartment in 
         Lagos State. The data was sourced from <a href="https://nigeriapropertycentre.com/">Nigeria Property Center<a>.
         </p>""", unsafe_allow_html=True)

st.dataframe(df.head(10), use_container_width=True)
st.write(f"Shape: {df.shape}")
less_50_rows = df.town.value_counts()[df.town.value_counts() < 50].index.to_list()
df["town_new"] = df.town.apply(lambda x: x if x not in less_50_rows else "Others")

st.sidebar.header("Explore and Predict House Rent in Lagos")
section = st.sidebar.selectbox("What Would You Like to Explore?", ["Summary Statistics", "Exploratory Statistics", "Estimate Yearly Rent"])

if section == "Summary Statistics":
    st.header("Summary Statistics")
    st.sidebar.markdown("<h4>Summary Statistics</h4>", unsafe_allow_html=True)
    var = st.sidebar.selectbox("Variable Type", ["Numerical", "Categorical"])
    st.write("***")
    if var == "Numerical":
        st.markdown("""<h5>Summary Statistics for Numerical Features</h5>
                    <p style='text-align: justify;'>The summary statistics show the count, mean, standard deviation, 
                    mininum value, first quantile, median, third quantile, and maximum 
                    value for each numerical feature: bedroom, bathroom, toilet, price, 
                    and price per bedroom.</p>""", unsafe_allow_html=True)
        st.dataframe(df.describe())
    else:
        to_dict = df.town_new.value_counts().sort_index().to_dict()
        data = pd.DataFrame(to_dict, index=["count"])
        st.markdown(f"""<h5>Summary Statistics for Categorical Feature: Location</h5>
                    <p style='text-align: justify;'>
                    The summary statistics show the count for each town in the dataset. It shows
                    that Ibeju-Lekki-Ajah region has the most observations ({data.loc["count","Ibeju-Lekki-Ajah"]:,}).
                    </p>""", unsafe_allow_html=True)
        st.dataframe(data)
        st.write(df.town_new.describe())
elif section == "Exploratory Statistics":
    st.header("Exploratory Analysis")
    st.write("***")
    st.sidebar.markdown("<h4>Exploratory Statistics</h4>", unsafe_allow_html=True)
    explore_type = st.sidebar.selectbox("Apartment and Price", sorted(["Location and Average Price","Distribution of Apartment Price", "Apartment Feature Correlation Matrix","Apartment Type and Average Price"]))
    if explore_type == "Location and Average Price":
        st.markdown("""<h5>Location and Average Rent Price</h5>
            <p style='text-align: justify;'>The horizontal bar charts displayed for the towns in Lagos State,
            show that the average yearly price of renting an apartment vary
            significantly by location. The price of renting an apartment in
            Towns such as Victoria Island, Ikoyi, Ikeja, and Lekki are significantly
            higher when compared to Ikorodu, Ojo, Alimosho, Agege, and Epe
            </p>""", unsafe_allow_html=True)
        explore_ana = st.sidebar.selectbox("Towns and Areas", sorted(list(df_area.town.unique()) + ["All Towns"]))
        if explore_ana == "All Towns":
            st.pyplot(plot_all_town(df))
        else:
            st.pyplot(plot_town_avg_rent(df_area, explore_ana))
    
    elif explore_type == "Distribution of Apartment Price":
        st.markdown("""<h5>Distribution of House Rent</h5>
                    <p style='text-align: justify;'>The histogram shows the distribution of the yearly price to rent an apartment in Lagos State. The chart shows that the price distribution is highly skewed to the right, with the majority of the prices falling between 0.5 million and 3.0 million Naira. The skewness is a result of apartments in locations with a very high standard of living and also apartments with a high number of bedrooms, bathrooms, and toilets.</p>""", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(15, 8))
        (df.price/1e6).plot.hist(bins=10, ax=ax, color=sns.color_palette()[3])
        plt.xlabel("Price (1 million naira)")
        plt.ylabel("Frequency [count]")
        plt.title("Distribution of House Rent Price");
        st.pyplot(fig)
    elif explore_type == "Apartment Type and Average Price":
        st.markdown("""<h5>Apartment and Average Rent Price</h5>
                    <p style='text-align: justify;'>
                    The horizontal bar chart shows that the price of renting an apartment varies significantly with apartment features.
                    </p>""", unsafe_allow_html=True)
               
        st.pyplot(plot_apart_type_price(df))
    else:
        st.markdown("""<h5>Correlation Matrix</h5>
                    <p style='text-align: justify;'>The heatmap shows the correlation coefficient between, bedroom, bathroom, 
                    toilet, and price. It shows that bedroom, bathroom, and toilet are highly 
                    correlated. It also shows that the yearly rent price is also correlated 
                    with these features.</p>""", unsafe_allow_html=True)
        fig, ax = plt.subplots()
        corr = df.loc[:,["bedroom", "bathroom", "toilet", "price"]].corr()
        mask = np.zeros_like(corr)
        i = np.triu_indices_from(mask)
        mask[i] = True
        sns.heatmap(corr, annot=True, fmt=".2f", mask = mask, cmap="gray_r", ax=ax, vmin=0, vmax=1, xticklabels=["Bedroom", "Bathroom", "Toilet"], yticklabels=["","Bathroom","Toilet","Price"])
        st.pyplot(fig)
else:
    st.sidebar.markdown("<h4>Estimate Price</h4>", unsafe_allow_html=True)
    method_est = st.sidebar.selectbox("Method of Estimate", ["Estimate with Filtering", "Estimate with Regression Model"])
    st.header("Predict Yearly Rent in Lagos State")
    st.write("***")
    
    if method_est == "Estimate with Filtering":
        town = st.sidebar.selectbox("Town", sorted(df_area.town.unique()),index=6)
        mask1 = df_area.town == town
        area = st.sidebar.selectbox(f"Area in {town}", sorted(df_area.loc[mask1].area.unique()))
        mask2 = (df_area.town == town) & (df_area.area == area)
        apartment = st.sidebar.selectbox("Apartment Type", sorted(df_area.loc[mask2].apartment_type.unique()))
        mask3 = mask2 & (df_area.apartment_type == apartment)
        bathroom = st.sidebar.selectbox("Bathroom", sorted(df_area.loc[mask3].bathroom.unique().astype(int)))
        mask4 = mask3 & (df_area.bathroom == bathroom)
        toilet = st.sidebar.selectbox("Toilet", sorted(df_area.loc[mask4].toilet.unique().astype(int)))
        mask5 = mask4 & (df_area.toilet == toilet)
        mean = df_area[mask5].price.mean()
        possible_combination = len(df_area.loc[mask5])
        st.markdown(f"""
                <p style='text-align: justify;'>The expected price (per year) to rent a {apartment} apartment with {toilet} toilet(s) and {bathroom} bathroom(s) in {area}, {town}, Lagos is:
                </p>""", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'>\u20A6{mean:,.0f}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <p style='margin-top:50px; text-align: center; color:rgb(140,140,140)'>
                        Pls note that there are only {possible_combination} record(s) for this combination in the dataset.</p>
                    """, unsafe_allow_html=True)
    else:
        apartment = st.sidebar.selectbox("Apartment Type", sorted(df.apartment_type.unique()), index=3)
        bathroom = st.sidebar.slider("Bathroom", min_value=1, max_value=5, value=3)
        toilet = st.sidebar.slider("Toilet", min_value=1, max_value=5, value=3)
        town = st.sidebar.selectbox("Town", sorted(df.town_new.unique()), index=5)

        possible_combination = len(df.loc[(df.bathroom == int(bathroom)) & (df.toilet == int(toilet)) & (df.apartment_type == apartment) & (df.town == town)])
        
        
        X = pd.DataFrame({"apartment_type":apartment, "bathroom":int(bathroom), "toilet":int(toilet), "town_new": town}, index=[0])
        prediction = model.predict(X)[0]

        st.markdown(f"""
                <p style='text-align: justify;'>The expected price (per year) to rent a {apartment} apartment with {toilet} toilet(s) and {bathroom} bathroom(s) in {town}, Lagos is:
                </p>""", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'>\u20A6{prediction:,.0f}</h2>", unsafe_allow_html=True)
        st.markdown(f"""
                    <p style='margin-top:50px; color:rgb(140,140,140)'>
                        The total records for a {apartment} with {toilet} toilet(s) and {bathroom} bathroom(s) in {town} in the dataset is {possible_combination}. The higher the number of records, the better the estimated rent price.</p>
                    """, unsafe_allow_html=True)
        st.write("***")
        st.markdown("<h5 style='margin-top: 50px; color:rgb(140,140,140)'>About Regression Model</h5>", unsafe_allow_html=True)
        st.markdown(f"""
                    <p style='margin-top: 30px; color:rgb(140,140,140)'>Things to note when using this model for prediction:
                    </p>
                    <ul style='text-align: justify; color:rgb(140,140,140)'>
                    <li>The regression model will hallucinate the expected yearly rent price for feature combinations it has not seen for certain locations, most especially locations with less than 200 observations (e.g., Shomolu). Check the categorical summary statistics for a list of these locations.</li>
                    <li>The regression model will hallucinate the expected rent price for outrageous feature combinations (e.g., a single room with five bathrooms and toilets).</li>
                    <li>The regression model mean absolute error and R-Squared are \u20A61,709,951 and 68.37%, respectively.</li>
                    </ul>
                    """, unsafe_allow_html=True)
        
        model_eval = st.sidebar.selectbox("Model Evaluation", sorted(["Predicted vs Actual Plot", "Feature Importance", "Distribution of Error"]))
        if model_eval == "Predicted vs Actual Plot":
            st.pyplot(pred_actual(df, model, type=1))
        elif model_eval == "Feature Importance":
            st.pyplot(pred_actual(df, model, 2))
        else:
            st.pyplot(pred_actual(df, model, type=0))
