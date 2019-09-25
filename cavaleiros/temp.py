import webbrowser
import numpy as np

try:
    a = np.array([[4,5,6],[3,4]])
    b = np.array([1,2,3])
    print(np.dot(a,b))
except Exception as e:
    erro = str(e).replace(" ", "+")
    url = f"https://stackoverflow.com/search?q={e}"
    webbrowser.open_new_tab(url)