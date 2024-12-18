import streamlit as st

def tile_bg(title, value, bg_color, link=None):
    content = f"""
    <div style="background-color:{bg_color}; padding:20px;border-radius:10px;text-align:center">
    <h3 style="color:white; font-size:24px">{title}</h3>
    <p style="color:white;font-size:24px">{value}</p>
    </div>
    """
    if link:
        content = f'<a href="{link}" target="_blank">{content}</a>'
    
    return st.markdown(content, unsafe_allow_html=True)

def tiles(result, place_name):
    col1, col2, col3 = st.columns(3)
    st.link_button("Go to reviews", f"https://www.google.com/maps/search/?api=1&query={place_name}")
    
    with col1:
        tile_bg("Month", result['month'], "#0077B6")
    
    with col2:
        tile_bg("Season", result['season'], "#FF8800")
    
    with col3:
        tile_bg("Review Count", result['reviewCount'], "#8A2BE2")
