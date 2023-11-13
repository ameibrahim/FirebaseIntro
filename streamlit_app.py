import streamlit as st
from google.cloud import firestore

def login():
    st.write("hello")



# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("key.json")

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
st.button("Login", on_click=login())

st.write("name: ", results["name"])
st.write("age: ", results["age"])