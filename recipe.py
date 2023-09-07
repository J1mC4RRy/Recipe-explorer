import streamlit as st
import pandas as pd
import random

# Load your DataFrame (assuming you have a CSV for simplicity)
df = pd.read_csv('recipes.csv')

# Streamlit App
st.title("Shiva's Recipe Explorer")


def display_recipe(recipe_row):
    st.subheader(recipe_row['RecipeName'])
    st.write("**Translated Name:**", recipe_row['TranslatedRecipeName'])
    st.write("**Ingredients:**", recipe_row['Ingredients'])
    st.write("**Translated Ingredients:**", recipe_row['TranslatedIngredients'])
    st.write("**Preparation Time (in mins):**", recipe_row['PrepTimeInMins'])
    st.write("**Cook Time (in mins):**", recipe_row['CookTimeInMins'])
    st.write("**Total Time (in mins):**", recipe_row['TotalTimeInMins'])
    st.write("**Servings:**", recipe_row['Servings'])
    st.write("**Cuisine:**", recipe_row['Cuisine'])
    st.write("**Course:**", recipe_row['Course'])
    st.write("**Diet:**", recipe_row['Diet'])
    st.write("**Instructions:**", recipe_row['Instructions'])
    st.write("**Translated Instructions:**", recipe_row['TranslatedInstructions'])
    st.write("**[Recipe URL](" + recipe_row['URL'] + ")**")


# Recipe Search
st.header("Search for a Recipe")
recipe_query = st.text_input("Enter the name of the recipe")

if recipe_query:
    results = df[df['RecipeName'].str.contains(recipe_query, case=False)]
    
    if not results.empty:
        # Show the matching recipes in a selectbox
        selected_recipe = st.selectbox('Select a recipe:', results['RecipeName'].tolist())

        # Display the details for the selected recipe
        recipe_row = results[results['RecipeName'] == selected_recipe].iloc[0]
        display_recipe(recipe_row)
    else:
        st.write("No recipes found for your query!")

# Recipe of the Day
st.header("Recipe of the Day")
recipe_of_day_index = random.choice(df['Srno'].tolist())
recipe_of_day = df[df['Srno'] == recipe_of_day_index].iloc[0]
display_recipe(recipe_of_day)



if __name__ == "__main__":
    st.write("Welcome to the Recipe Explorer! Above you'll find the recipe of the day and a search bar to find any recipe you desire.")
