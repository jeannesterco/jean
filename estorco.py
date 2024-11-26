import streamlit as st

def display_bio_form():
    st.title("BIOGRAPHY APP")
    
    st.header("Profile Picture")
    picture = st.file_uploader("Upload Your Picture", type=["jpg", "jpeg", "png"])

    if picture is not None:
        st.image(picture, caption="Uploaded Profile Picture", width=200)

    st.header("Basic Information")
    name = st.text_input("Name", value="Jeann D. Estorco")
    age = st.number_input("Age", min_value=0, max_value=120, value=19)
    birthdate = st.date_input("Birthdate", value=None)
    major = st.text_input("Major")
    school = st.text_input("School")
    
    st.header("About You")
    about_self = st.text_area("About yourself", value="I'm a first-year college student currently pursuing BS Computer Engineering at Surigao del Norte State University. I'm passionate about programming.")

    st.header("Favorites")
    favorite_color = st.text_input("Favorite Color", value="Sky Blue")
    favorite_food = st.text_input("Favorite Food", value="Salad")
    favorite_movie = st.text_input("Favorite Movie", value="The Notebook")

    st.header("Hobbies")
    hobbies = st.text_area("Hobbies", value="Riding Motorbike")

    st.header("Goals")
    goals = st.text_area("Goals", value="My goal is to be successful in life")

    st.header("Contact Information")
    email = st.text_input("Email", value="estrocojeann@gmail.com")
    phone = st.text_input("Phone", value="09381563950")

    if st.button("Submit"):
        st.subheader("Your Biography")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Birthdate:** {birthdate}")
        st.write(f"**Major:** {major}")
        st.write(f"**School:** {school}")
        st.write(f"**About You:** {about_self}")
        st.write(f"**Favorite Color:** {favorite_color}")
        st.write(f"**Favorite Food:** {favorite_food}")
        st.write(f"**Favorite Movie:** {favorite_movie}")
        st.write(f"**Hobbies:** {hobbies}")
        st.write(f"**Goals:** {goals}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")

if __name__ == "__main__":
    display_bio_form()
