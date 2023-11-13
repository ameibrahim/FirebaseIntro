import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("key.json")

# Create a reference to the Google post.
doc_ref = db.collection("pets").document("IEv3ovpXUgDTC0nIr307")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)

results = doc.to_dict()
st.write("name: ", results.name)
st.write("age: ", results.age)