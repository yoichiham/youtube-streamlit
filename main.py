import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("Streamlit 超入門")


st.write("プレグレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"


# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70], columns=["lat", "lon"]
# )
# st.map(df)

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=100) #引数が豊富に用意してある
# st.table(df.style.highlight_max(axis=0)) #性的な表を作成

st.write("Interactive Widgets")
text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味:", text, "です。"


left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
# buttonが押されたら
if button:
    right_column.write("ここは右カラムです")

expander = st.expander("問い合わせ1")
expander.write("問い合わせ1にたいしての回答")
expander = st.expander("問い合わせ2")
expander.write("問い合わせ2にたいしての回答")
expander = st.expander("問い合わせ3")
expander.write("問い合わせ3にたいしての回答")


# option = st.selectbox("あなたが好きな数字を教えてください、", list(range(1, 11)))
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)

# "あなたの好きな数字は、", option, "です。"
# "コンディション:", condition


# # インタラクティブなウィジェット
# if st.checkbox("Show Image"):
#     # 画像を表示
#     img = Image.open("test.jpg")
#     st.image(img, caption="test", use_column_width=True)

# """
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
