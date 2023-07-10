import pandas as pd
import streamlit as st 
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
    )
st.table(df)