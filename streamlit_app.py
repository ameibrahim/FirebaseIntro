import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Authenticate to Firestore with the JSON account key.
if not firebase_admin._apps:
    cred = credentials.Certificate("key.json")
    firebase_admin.initialize_app(cred)


db = firestore.client()


def login():

    user = auth.create_user(email='ame.ibrahim@yahoo.com',password='lola1313',display_name='Ibrahim Ame')
    print('Sucessfully created new user: {0}'.format(user.uid))


# Create a reference to the Google post.
doc_ref = db.collection("pets").document("IEv3ovpXUgDTC0nIr307")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)

results = doc.to_dict()

st.title("Login")
st.text_input("Email", value="", placeholder="Enter Email")
st.text_input("Password", value="", type="password", placeholder="Enter Password")
loginButton = st.button("Login")

if loginButton:
    login()

st.write("name: ", results["name"])
st.write("age: ", results["age"])