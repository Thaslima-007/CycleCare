import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="CycleCare", page_icon="🌸")

st.title("🌸 CycleCare")
st.subheader("Menstrual Health Awareness")

st.write(
    "Learn about menstrual health, hygiene, "
    "and understand your menstrual cycle."
)

st.header("📚 Menstrual Health Education")

st.write("""
- Periods are a normal biological process.
- Change menstrual products regularly.
- Wash your hands before and after changing products.
- Eat nutritious food and stay hydrated.
- Severe period pain should not be ignored.
""")

st.header("📅 Period Estimator")

last_period = st.date_input(
    "First day of your last period",
    value=date.today()
)

cycle_length = st.number_input(
    "Usual cycle length (days)",
    min_value=21,
    max_value=45,
    value=28
)

if st.button("Estimate Next Period"):
    next_period = last_period + timedelta(days=int(cycle_length))
    st.success(
        f"Estimated next period: {next_period.strftime('%d %B %Y')}"
    )
    st.caption(
        "This is only an estimate, not medical advice "
        "or a method of contraception."
    )

st.divider()
st.caption("CycleCare | Awareness, Education and Empowerment")
