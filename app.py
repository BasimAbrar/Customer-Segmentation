import streamlit as st
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

kmm = joblib.load("kmeans_Model.joblib")
scaler = joblib.load("scaler_Encoder.joblib")

cluster_labels = {
    0: "Cluster 0 – Average customers",
    1: "Cluster 1 – Premium customers",
    2: "Cluster 2 – Value for money customers",
    3: "Cluster 3 – Cautious spenders",
    4: "Cluster 4 – Budget customers"
}

st.title("Customer Segmentation (KMeans)")

st.write("### Enter customer details:")
income = st.slider("Annual Income (k$)", min_value=10, max_value=150, value=60)
score = st.slider("Spending Score (1-100)", min_value=1, max_value=100, value=50)

if st.button("Predict Cluster"):
    # Prepare input
    customer = pd.DataFrame([[income, score]], columns=["Annual Income (k$)", "Spending Score (1-100)"])
    customer_scaled = scaler.transform(customer)

    # Predict
    cluster = kmm.predict(customer_scaled)[0]
    st.success(f"👉 This customer belongs to {cluster_labels[cluster]}")
    print(cluster)
    # ----------------------
    # Optional: Show clusters with new customer highlighted
    # ----------------------
    data = pd.read_csv("Mall_Customers.csv")
    X = data[["Annual Income (k$)", "Spending Score (1-100)"]]
    X_scaled = scaler.transform(X)
    data["Cluster"] = kmm.predict(X_scaled)

    fig, ax = plt.subplots(figsize=(7,5))
    sns.scatterplot(
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Cluster",
        palette="tab10",
        data=data,
        ax=ax,
        s=60
    )

    # Highlight the new customer
    ax.scatter(income, score, color="red", s=200, edgecolor="black", marker="X", label="New Customer")
    ax.legend()
    st.pyplot(fig)
