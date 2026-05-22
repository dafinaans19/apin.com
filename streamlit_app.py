import streamlit as st

st.title("🎈apin's castle")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
st.text(body, *, help=None, width="content", text_alignment="left")
import streamlit as st

color = st.color_picker("Pick A Color", "#f900ee")
st.write("The current color is", color)
