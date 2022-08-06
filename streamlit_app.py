
import streamlit
streamlit.title("My Mom's New Healthy Dinner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 and Blueberry Omelet')
streamlit.text('🥗 Kale, Spinach, and Rocket Smoothie')
streamlit.text('🐔 Hard-boild Free-ranged Egg')
streamlit.text('🥑🍞 Avocado Toast')
                

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')        


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

