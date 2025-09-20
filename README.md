# Customer-Segmentation
Customer segmentation using Mall Customer dataset. Applied K-Means and DBSCAN to group customers based on income and spending score. Best results with K-Means (k=5), producing clear, interpretable clusters for business insights.
## Dataset  
- **Source:** Mall Customer Dataset (Kaggle)  
- **Description:** Contains customer demographic and behavioral features including annual income and spending score.  

## Methodology  
1. **Data Preprocessing** – cleaned the dataset and applied feature scaling.  
2. **Exploratory Visualization** – scatter plots to observe potential groupings.  
3. **K-Means Clustering**  
   - Applied the Elbow Method to determine optimal cluster count.  
   - Tested k=3 and k=5 to compare grouping quality.  
4. **DBSCAN Clustering** – tested density-based clustering and analyzed outliers.  
5. **Cluster Analysis** – evaluated income/spending patterns and average spending per cluster.  

## Results  
- **K-Means** produced clear customer segments:  
  - With **k=3**: broad groups (high spenders, low spenders, cautious spenders).  
  - With **k=5**: more detailed groups with distinct income and spending patterns.  
- **DBSCAN** identified 3 clusters plus outliers:  
  - One high spender cluster, one low/medium spender cluster, and several outliers.  
- **Overall:** K-Means was more effective, giving interpretable and actionable business insights, while DBSCAN was better for outlier detection.  

## Tools & Libraries  
- Python  
- Pandas – data handling  
- Matplotlib – visualization  
- Scikit-learn – clustering (K-Means, DBSCAN)  
