from tkinter.messagebox import IGNORE
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# --- IGNORE ---

df2 = pd.DataFrame({'A': df['A'] * 2, 'B': df['B'] * 2})
