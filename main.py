import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import tiles

@st.cache_data
def load_data(file_name):
    return pd.read_csv(file_name)

# Input fields for place and visit option
place = st.text_input("Enter the name of the place or State (e.g., Taj Mahal, Goa)")
visit_option = st.selectbox("Select visit option", ["Most Visited", "Least Visited"])

# Load crime data from CSV file
crime_data = load_data("Data/processedData/crimeData.csv")

# Create dropdown for crime ranking
crime_ranking = st.selectbox("Select crime ranking", ["Top 5 Safest", "Top 5 Most Dangerous"])

if place and visit_option:
    place_lower = place.lower()

    # Taj Mahal - Agra
    if "taj mahal" in place_lower or "agra" in place_lower or "uttar pradesh" in place_lower:
        taj_mahal_coords = pd.DataFrame({
            'lat': [27.1751],
            'lon': [78.0421]
        })
        st.header("Location of the Taj Mahal")
        st.map(taj_mahal_coords, zoom=13)

        # Find the rank of Agra for crime data
        agra_rank = crime_data[crime_data['State/UT'].str.contains('Uttar Pradesh', case=False)]['Rank'].values[0]
        place_rank = agra_rank
        place_name = "Agra (Uttar Pradesh)"
        highlight_state = "Uttar Pradesh"

        # Load tourist data for Taj Mahal
        df_taj_mahal = load_data("Data/processedData/tajMahal.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_sorted_taj_mahal = df_taj_mahal.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_taj_mahal = df_sorted_taj_mahal.iloc[1]  # Second highest review count
        else:
            result_taj_mahal = df_sorted_taj_mahal.iloc[-1]  # Least visited

        # Display tourist data for Taj Mahal in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")

        tiles(result_taj_mahal, "Taj Mahal")

    # GOA     
    elif "goa" in place_lower or "dudh sagar falls" in place_lower:
        goa_coords = pd.DataFrame({
            'lat': [15.329768],
            'lon': [74.093665]
        })
        st.header("Location of Goa")
        st.map(goa_coords, zoom=8)

        # Find the rank of Goa for crime data
        goa_rank = crime_data[crime_data['State/UT'].str.contains('Goa', case=False)]['Rank'].values[0]
        place_rank = goa_rank
        place_name = "Goa"
        highlight_state = "Goa"

        # Load tourist data for Goa
        df_goa = load_data("Data/processedData/goa.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_sorted_goa = df_goa.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_goa = df_sorted_goa.iloc[1]  # Second highest review count
        else:
            result_goa = df_sorted_goa.iloc[-1]  # Least visited

        # Display tourist data for Goa in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_goa, "Goa")

    # Gujarat

    elif "gujarat" in place_lower or "somnath temple" in place_lower:
        gujarat_coords = pd.DataFrame({
            'lat': [20.887939],
            'lon': [70.401418]
        })
        st.header("Location of Somnath Temple in Gujarat")
        st.map(gujarat_coords, zoom=8)

        # Find the rank of Gujarat for crime data
        gujarat_rank = crime_data[crime_data['State/UT'].str.contains('Gujarat', case=False)]['Rank'].values[0]
        place_rank = gujarat_rank
        place_name = "Gujarat"
        highlight_state = "Gujarat"

        # Load tourist data for Somnath Temple (Gujarat)
        df_somnath_temple = load_data("Data/processedData/somnathTemple.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_sorted_somnath_temple = df_somnath_temple.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_gujarat = df_sorted_somnath_temple.iloc[1]  # Second highest review count
        else:
            result_gujarat = df_sorted_somnath_temple.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_gujarat, "Gujarat")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

        
        
    # Orrisa  

    elif "odisha" in place_lower or "chilika lake" in place_lower or "orissa" in place_lower:
        odisha_coords = pd.DataFrame({
            'lat': [19.781402],
            'lon': [85.309564],
        })
        st.header("Location of Chilika Lake in Odisha")
        st.map(odisha_coords, zoom=8)

        # Find the rank of Gujarat for crime data
        odisha_rank = crime_data[crime_data['State/UT'].str.contains('Odisha', case=False)]['Rank'].values[0]
        place_rank = odisha_rank
        place_name = "Odisha"
        highlight_state = "Odisha"

        # Load tourist data for Somnath Temple (Gujarat)
        df_odisha = load_data("Data/processedData/chilikaLake.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_odisha = df_odisha.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_odisha = df_odisha.iloc[1]  # Second highest review count
        else:
            result_odisha = df_odisha.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_odisha, "Odisha")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Jammu and Kashmir 

    elif "jammu and kashmir" in place_lower or "dal lake" in place_lower or "srinagar" in place_lower:
        odisha_coords = pd.DataFrame({
            'lat': [34.116036],
            'lon': [74.855215],
        })
        st.header("Location of Dal Lake in Jammu and Kashmir")
        st.map(odisha_coords, zoom=8)

        # Find the rank of Gujarat for crime data
        odisha_rank = crime_data[crime_data['State/UT'].str.contains('Jammu and Kashmir', case=False)]['Rank'].values[0]
        place_rank = odisha_rank
        place_name = "Jammu and Kashmir"
        highlight_state = "Jammu and Kashmir"

        # Load tourist data for Somnath Temple (Gujarat)
        df_dalLake = load_data("Data/processedData/dalLake.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_dalLake = df_dalLake.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_dalLake = df_dalLake.iloc[1]  # Second highest review count
        else:
            result_dalLake = df_dalLake.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_dalLake, "Jammu and Kashmir")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Andaman and Nicobar Islands

    elif "andaman and nicobar" in place_lower or "cellular jail" in place_lower or "srinagar" in place_lower:
        andaman_coords = pd.DataFrame({
            'lat': [11.674410],
            'lon': [92.747836],
        })
        st.header("Location of the Cellular Jail in Andaman and Nicobar islands")
        st.map(andaman_coords, zoom=8)

        # Find the rank of Gujarat for crime data
        andaman_rank = crime_data[crime_data['State/UT'].str.contains('A&N', case=False)]['Rank'].values[0]
        place_rank = andaman_rank
        place_name = "A&N"
        highlight_state = "A&N"

        # Load tourist data for Somnath Temple (Gujarat)
        df_andaman = load_data("Data/processedData/cellularJail.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_andaman = df_andaman.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_andaman = df_andaman.iloc[1]  # Second highest review count
        else:
            result_andaman = df_andaman.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_andaman, "Cellular Jail")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Madhya Pradesh    

    elif "madhya pradesh" in place_lower or "upper lake" in place_lower or "bhopal" in place_lower:
        mp_coords = pd.DataFrame({
            'lat': [23.256776],
            'lon': [77.393125],
        })
        st.header("Location of the Upper Lake in Madhya Pradesh")
        st.map(mp_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        mp_rank = crime_data[crime_data['State/UT'].str.contains('Madhya Pradesh', case=False)]['Rank'].values[0]
        place_rank = mp_rank
        place_name = "Madhya Pradesh"
        highlight_state = "Madhya Pradesh"

        # Load tourist data for Somnath Temple (Gujarat)
        df_mp = load_data("Data/processedData/madhyaPradesh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_mp = df_mp.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_mp = df_mp.iloc[1]  # Second highest review count
        else:
            result_mp = df_mp.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_mp, "Upper Lake Madhya Pradesh")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    
    # Sikkim   

    elif "sikkim" in place_lower or "naga falls" in place_lower or "gangtok" in place_lower:
        sikkim_coords = pd.DataFrame({
            'lat': [23.256776],
            'lon': [77.393125],
        })
        st.header("Location of the Naga Falls in Sikkim")
        st.map(sikkim_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        mp_rank = crime_data[crime_data['State/UT'].str.contains('Sikkim', case=False)]['Rank'].values[0]
        place_rank = mp_rank
        place_name = "Sikkim"
        highlight_state = "Sikkim"

        # Load tourist data for Somnath Temple (Gujarat)
        df_sikkim = load_data("Data/processedData/sikkim.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_sikkim = df_sikkim.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_sikkim = df_sikkim.iloc[1]  # Second highest review count
        else:
            result_sikkim = df_sikkim.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_sikkim, "Sikkim")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")



    # Haryana   

    elif "haryana" in place_lower or "Jal mahal" in place_lower or "chandigarh" in place_lower:
        haryana_coords = pd.DataFrame({
            'lat': [26.953659444776775],
            'lon': [75.84649204617223],
        })
        st.header("Location of the Jal Mahal in Haryana")
        st.map(haryana_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        haryana_rank = crime_data[crime_data['State/UT'].str.contains('Haryana', case=False)]['Rank'].values[0]
        place_rank = haryana_rank
        place_name = "Haryana"
        highlight_state = "Haryana"

        # Load tourist data for Somnath Temple (Gujarat)
        df_haryana = load_data("Data/processedData/madhyaPradesh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_haryana = df_haryana.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_haryana = df_haryana.iloc[1]  # Second highest review count
        else:
            result_haryana = df_haryana.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_haryana, "Jal Mahal India")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # West Bengal

    elif "west bengal" in place_lower or "peace pagoda" in place_lower or "darjeeling" in place_lower:
        westBengal_coords = pd.DataFrame({
            'lat': [27.028078867007636],
            'lon': [88.25892282158227],
        })
        st.header("Location of the Peace Pagoda in West Bengal")
        st.map(westBengal_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        westBengal_rank = crime_data[crime_data['State/UT'].str.contains('West Bengal', case=False)]['Rank'].values[0]
        place_rank = westBengal_rank
        place_name = "West Bengal"
        highlight_state = "West Bengal"

        # Load tourist data for Somnath Temple (Gujarat)
        df_westBengal = load_data("Data/processedData/madhyaPradesh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_westBengal = df_westBengal.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_westBengal = df_westBengal.iloc[1]  # Second highest review count
        else:
            result_westBengal = df_westBengal.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_westBengal, "Peace Pagoda, Darjeeling")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Meghlaya
    elif "meghalaya" in place_lower or "elephant falls" in place_lower or "shillong" in place_lower:
        meghalaya_coords = pd.DataFrame({
            'lat': [25.537822979165746],
            'lon': [91.8225513],
        })
        st.header("Location of the Elephant Falls in Meghlaya")
        st.map(meghalaya_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        meghalaya_rank = crime_data[crime_data['State/UT'].str.contains('Meghalaya', case=False)]['Rank'].values[0]
        place_rank = meghalaya_rank
        place_name = "Meghalaya"
        highlight_state = "Meghalaya"

        # Load tourist data for Somnath Temple (Gujarat)
        df_meghalaya = load_data("Data/processedData/madhyaPradesh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_meghalaya = df_meghalaya.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_meghalaya = df_meghalaya.iloc[1]  # Second highest review count
        else:
            result_meghalaya = df_meghalaya.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_meghalaya, "Meghalaya")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Tamil Nadu

    elif "tamil nadu" in place_lower or "vivekananda rock memorial" in place_lower or "chennai" in place_lower:
        tamilNadu_coords = pd.DataFrame({
            'lat': [8.078304875912309],
            'lon': [77.55569813271933],
        })
        st.header("Location of the Vivekananda Rock Memorial in Tamil Nadu")
        st.map(tamilNadu_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        tamilNadu_rank = crime_data[crime_data['State/UT'].str.contains('Tamil Nadu', case=False)]['Rank'].values[0]
        place_rank = tamilNadu_rank
        place_name = "Tamil Nadu"
        highlight_state = "Tamil Nadu"

        # Load tourist data for Somnath Temple (Gujarat)
        df_tamilNadu = load_data("Data/processedData/tamilNadu.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_tamilNadu = df_tamilNadu.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_tamilNadu = df_tamilNadu.iloc[1]  # Second highest review count
        else:
            result_tamilNadu = df_tamilNadu.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_tamilNadu, "Vivekananda Rock Memorial")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Kerala   

    elif "kerala" in place_lower or "periyar national park" in place_lower or "thiruvananthapuram " in place_lower:
        kerala_coords = pd.DataFrame({
            'lat': [8.078304875912309],
            'lon': [77.55569813271933],
        })
        st.header("Location of the periyar national park")
        st.map(kerala_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        kerala_rank = crime_data[crime_data['State/UT'].str.contains('Kerala', case=False)]['Rank'].values[0]
        place_rank = kerala_rank
        place_name = "Kerala"
        highlight_state = "Kerala"

        # Load tourist data for Somnath Temple (Gujarat)
        df_kerala = load_data("Data/processedData/kerala.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_kerala = df_kerala.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_kerala = df_kerala.iloc[1]  # Second highest review count
        else:
            result_kerala = df_kerala.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_kerala, "periyar national park")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Assam

    elif "assam" in place_lower or "maha mrityunjay temple" in place_lower:
        assam_coords = pd.DataFrame({
            'lat': [26.358683089725965],
            'lon': [92.81521922101489],
        })
        st.header("Location of the periyar national park")
        st.map(assam_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        assam_rank = crime_data[crime_data['State/UT'].str.contains('Assam', case=False)]['Rank'].values[0]
        place_rank = assam_rank
        place_name = "Assam"
        highlight_state = "Assam"

        # Load tourist data for Somnath Temple (Gujarat)
        df_assam = load_data("Data/processedData/assam.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_assam = df_assam.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_assam = df_assam.iloc[1]  # Second highest review count
        else:
            result_assam = df_assam.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_assam, "Maha Mrityunjay Temple, Nagaon")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Karnatka

    elif "karnataka" in place_lower or "mysore palace" in place_lower:
        karnataka_coords = pd.DataFrame({
            'lat': [26.358683089725965],
            'lon': [92.81521922101489],
        })
        st.header("Location of the Mysore Palace")
        st.map(karnataka_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        karnataka_rank = crime_data[crime_data['State/UT'].str.contains('Karnataka', case=False)]['Rank'].values[0]
        place_rank = karnataka_rank
        place_name = "karnataka"
        highlight_state = "karnataka"

        # Load tourist data for Somnath Temple (Gujarat)
        df_karnataka = load_data("Data/processedData/karnataka.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_karnataka = df_karnataka.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_karnataka = df_karnataka.iloc[1]  # Second highest review count
        else:
            result_karnataka = df_karnataka.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_karnataka, "Mysore Palace")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Himachal pradesh

    elif "himachal pradesh" in place_lower or "chalal trec trail" in place_lower:
        himachalPradesh_coords = pd.DataFrame({
            'lat': [26.358683089725965],
            'lon': [92.81521922101489],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(himachalPradesh_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        himachalPradesh_rank = crime_data[crime_data['State/UT'].str.contains('Himachal Pradesh', case=False)]['Rank'].values[0]
        place_rank = himachalPradesh_rank
        place_name = "Himachal Pradesh"
        highlight_state = "Himachal Pradesh"

        # Load tourist data for Somnath Temple (Gujarat)
        df_himachalPradesh = load_data("Data/processedData/himachalPradesh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_himachalPradesh = df_himachalPradesh.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_himachalPradesh = df_himachalPradesh.iloc[1]  # Second highest review count
        else:
            result_himachalPradesh = df_himachalPradesh.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_himachalPradesh, "chalal trec trail, Himachal Pradesh")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Rajasthan

    elif "rajasthan" in place_lower or "hawa mahal" in place_lower:
        rajasthan_coords = pd.DataFrame({
            'lat': [26.358683089725965],
            'lon': [92.81521922101489],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(rajasthan_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        rajasthan_rank = crime_data[crime_data['State/UT'].str.contains('Rajasthan', case=False)]['Rank'].values[0]
        place_rank = rajasthan_rank
        place_name = "Rajasthan"
        highlight_state = "Rajasthan"

        # Load tourist data for Somnath Temple (Gujarat)
        df_rajasthan = load_data("Data/processedData/rajasthan.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_rajasthan = df_rajasthan.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_rajasthan = df_rajasthan.iloc[1]  # Second highest review count
        else:
            result_rajasthan = df_rajasthan.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_rajasthan, "Hawa Mahal")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")


    # Maharashtra

    elif "maharashtra" in place_lower or "elephanta caves" in place_lower:
        maharashtra_coords = pd.DataFrame({
            'lat': [18.96661272047191],
            'lon': [72.93161942596768],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(maharashtra_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        maharashtra_rank = crime_data[crime_data['State/UT'].str.contains('Maharashtra', case=False)]['Rank'].values[0]
        place_rank = maharashtra_rank
        place_name = "Maharashtra"
        highlight_state = "Maharashtra"

        # Load tourist data for Somnath Temple (Gujarat)
        df_maharashtra = load_data("Data/processedData/maharashtra.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_maharashtra = df_maharashtra.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_maharashtra = df_maharashtra.iloc[1]  # Second highest review count
        else:
            result_maharashtra = df_maharashtra.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_maharashtra, "Hawa Mahal")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Punjab

    elif "punjab" in place_lower or "golden temple" in place_lower:
        punjab_coords = pd.DataFrame({
            'lat': [31.620932374257283],
            'lon': [74.8771021064963],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(punjab_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        punjab_rank = crime_data[crime_data['State/UT'].str.contains('Punjab', case=False)]['Rank'].values[0]
        place_rank = punjab_rank
        place_name = "Punjab"
        highlight_state = "Punjab"

        # Load tourist data for Somnath Temple (Gujarat)
        df_punjab = load_data("Data/processedData/punjab.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_punjab = df_punjab.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_punjab = df_punjab.iloc[1]  # Second highest review count
        else:
            result_punjab = df_punjab.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_punjab, "golden temple, punjab")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Uttrakhand

    elif "uttarakhand" in place_lower or "jim corbett national park" in place_lower:
        uttarakhand_coords = pd.DataFrame({
            'lat': [29.795367658483087],
            'lon': [78.82661223333953],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(uttarakhand_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        uttarakhand_rank = crime_data[crime_data['State/UT'].str.contains('Uttarakhand', case=False)]['Rank'].values[0]
        place_rank = uttarakhand_rank
        place_name = "Uttarakhand"
        highlight_state = "Uttarakhand"

        # Load tourist data for Somnath Temple (Gujarat)
        df_uttarakhand = load_data("Data/processedData/uttarakhand.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_uttarakhand = df_uttarakhand.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_uttarakhand = df_uttarakhand.iloc[1]  # Second highest review count
        else:
            result_uttarakhand = df_uttarakhand.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_uttarakhand, "golden temple, punjab")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")
    
    # Chhattisgarh - chitr kuut water

    elif "chhattisgarh" in place_lower or "chitrakote waterfalls" in place_lower:
        chhattisgarh_coords = pd.DataFrame({
            'lat': [19.20778027318942],
            'lon': [81.70104694132837],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(chhattisgarh_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        chhattisgarh_rank = crime_data[crime_data['State/UT'].str.contains('chhattisgarh', case=False)]['Rank'].values[0]
        place_rank = chhattisgarh_rank
        place_name = "chhattisgarh"
        highlight_state = "chhattisgarh"

        # Load tourist data for Somnath Temple (Gujarat)
        df_chhattisgarh = load_data("Data/processedData/chhattisgarh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_chhattisgarh = df_chhattisgarh.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_chhattisgarh = df_chhattisgarh.iloc[1]  # Second highest review count
        else:
            result_chhattisgarh = df_chhattisgarh.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_chhattisgarh, "Chitrakote Waterfalls, chhattisgarh")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Bihar - Pragbodhi Cave

    elif "bihar" in place_lower or "pragbodhi cave" in place_lower:
        bihar_coords = pd.DataFrame({
            'lat': [24.736896165094556],
            'lon': [85.04795903443905],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(bihar_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        bihar_rank = crime_data[crime_data['State/UT'].str.contains('Bihar', case=False)]['Rank'].values[0]
        place_rank = bihar_rank
        place_name = "Bihar"
        highlight_state = "Bihar"

        # Load tourist data for Somnath Temple (Gujarat)
        df_bihar = load_data("Data/processedData/bihar.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_bihar = df_bihar.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_bihar = df_bihar.iloc[1]  # Second highest review count
        else:
            result_bihar = df_bihar.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_bihar, "Pragbodhi Cave, Bihar")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Jharkhand - dassam falls

    elif "jharkhad" in place_lower or "dassam falls" in place_lower:
        jharkhad_coords = pd.DataFrame({
            'lat': [23.146664950250265],
            'lon': [85.4673736734195],
        })
        st.header("Location of the chalal trec trail Himachal Pradesh")
        st.map(jharkhad_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        jharkhad_rank = crime_data[crime_data['State/UT'].str.contains('Jharkhad', case=False)]['Rank'].values[0]
        place_rank = jharkhad_rank
        place_name = "Jharkhad"
        highlight_state = "Jharkhad"

        # Load tourist data for Somnath Temple (Gujarat)
        df_jharkhad = load_data("Data/processedData/jharkhad.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_jharkhad = df_jharkhad.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_jharkhad = df_jharkhad.iloc[1]  # Second highest review count
        else:
            result_jharkhad = df_jharkhad.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_jharkhad, "dassam falls, jharkhad")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")

    # Andhra Pradesh - nallamala Hills

    elif "andhra pradesh" in place_lower or "nallamala hills" in place_lower:
        andhraPradesh_coords = pd.DataFrame({
            'lat': [16.256059046842417],
            'lon': [79.44507375783138],
        })
        st.header("Location of the nallamala hills Andhra Pradesh")
        st.map(andhraPradesh_coords, zoom=7)

        # Find the rank of Gujarat for crime data
        andhraPradesh_rank = crime_data[crime_data['State/UT'].str.contains('Andhra Pradesh', case=False)]['Rank'].values[0]
        place_rank = andhraPradesh_rank
        place_name = "Andhra Pradesh"
        highlight_state = "Andhra Pradesh"

        # Load tourist data for Somnath Temple (Gujarat)
        df_andhraPradesh = load_data("Data/processedData/andhraPradesh.csv")

        # Sort by reviewCount and get the result based on visit_option
        df_andhraPradesh = df_andhraPradesh.sort_values('reviewCount', ascending=False)
        if visit_option == "Most Visited":
            result_andhraPradesh = df_andhraPradesh.iloc[1]  # Second highest review count
        else:
            result_andhraPradesh = df_andhraPradesh.iloc[-1]  # Least visited

        # Display tourist data for Somnath Temple (Gujarat) in tiles (side by side)
        st.subheader(f"{place_name} - {visit_option} Time of the year")
        tiles(result_andhraPradesh, "Nallamala hills Andhra Pradesh")
        st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}", type="primary")



    else:
        st.error("Please enter a valid place, city or state from India")

    # Display crime rank for the selected place
    st.subheader("Crime Ranking")
    st.write(f"Crime Rank of {place_name}: {place_rank}")

    # Create bar plot with temperature colors for danger level
    fig, ax = plt.subplots(figsize=(12, 6))
    crime_data_sorted = crime_data.sort_values('Rank')
    danger_gradient = np.linspace(0, 1, len(crime_data_sorted))
    colors = plt.cm.plasma(danger_gradient)
    bars = ax.bar(crime_data_sorted['State/UT'], crime_data_sorted['Rank'], color=colors)
    highlight_index = crime_data_sorted[crime_data_sorted['State/UT'].str.contains(highlight_state, case=False)].index[0]
    bars[highlight_index].set_color('red')
    plt.xticks(rotation=90)
    plt.ylabel('Crime Rank')
    plt.title('Crime Ranking by State/UT')
    sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin=1, vmax=crime_data_sorted['Rank'].max()))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, label='Danger Level (1=Least Dangerous, Higher Rank=More Dangerous)')
    cbar.set_ticks([1, crime_data_sorted['Rank'].max()])
    cbar.set_ticklabels(['Least Dangerous', 'Most Dangerous'])
    ax.bar(0, 0, color='red', label=highlight_state)
    plt.legend()
    plt.tight_layout()
    st.pyplot(fig)

else:
    st.info("Please enter a place name and select a visit option.")

# Display overall crime ranking based on user selection
st.subheader("Overall Crime Ranking")
if crime_ranking == "Top 5 Safest":
    top_5_safest = crime_data.sort_values('Rank').head()
    st.write(top_5_safest[['State/UT', 'Rank']])
else:
    top_5_dangerous = crime_data.sort_values('Rank', ascending=False).head()
    st.write(top_5_dangerous[['State/UT', 'Rank']])