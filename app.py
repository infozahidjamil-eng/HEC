import streamlit as st
import random

st.title("⚡ VoltGuard AI")

# SAFE RANGES DISPLAY
st.subheader("📊 Safe Operating Ranges")
st.markdown("""
🔌 Voltage: 198V – 242V (Safe Range)  
⚡ Current: 0A – 20A (Safe Range)  
🌡️ Temperature: 0°C – 70°C (Safe Range)
""")

# SIMULATED SENSOR VALUES
voltage = random.randint(210, 260)
current = random.randint(5, 25)
temp = random.randint(30, 90)

st.subheader("📡 Live Electrical Data")

st.write(f"Voltage: {voltage} V")
st.write(f"Current: {current} A")
st.write(f"Temperature: {temp} °C")

# ANALYSIS BUTTON
if st.button("Analyze System"):

    st.subheader("⚡ System Analysis Report")

    # ---------------- VOLTAGE ----------------
    if voltage < 198 or voltage > 242:
        st.error("⚠️ Voltage Out of Safe Range!")
        st.write("📌 Problem: Voltage instability detected.")
        st.write("🧠 Reason: Supply voltage is not within standard industrial limits (198V–242V).")
        st.write("🛠️ Action: Check stabilizer, transformer, or power supply line.")
    else:
        st.success("✔️ Voltage is Normal")
        st.write("📌 Problem: Voltage within safe range.")
        st.write("🧠 Reason: Supply is stable and within limits.")
        st.write("🛠️ Action: No action required.")

    st.markdown("---")

    # ---------------- CURRENT ----------------
    if current > 20:
        st.error("⚠️ Overcurrent Detected!")
        st.write("📌 Problem: Electrical load is too high.")
        st.write("🧠 Reason: Connected devices are drawing excessive current beyond 20A limit.")
        st.write("🛠️ Action: Reduce load or disconnect extra devices.")
    else:
        st.success("✔️ Current is Normal")
        st.write("📌 Problem: Current is within safe range.")
        st.write("🧠 Reason: Load demand is balanced.")
        st.write("🛠️ Action: No action required.")

    st.markdown("---")

    # ---------------- TEMPERATURE ----------------
    if temp <= 70:
        st.success("🌡️ Temperature Normal")
        st.write("📌 Problem: No overheating detected.")
        st.write("🧠 Reason: Thermal condition is stable below 70°C.")
        st.write("🛠️ Action: Continue normal operation.")

    elif temp <= 85:
        st.warning("🌡️ Temperature High (Warning Zone)")
        st.write("📌 Problem: Device is heating up.")
        st.write("🧠 Reason: Heat accumulation due to load or poor ventilation.")
        st.write("🛠️ Action: Improve cooling or reduce load.")

    else:
        st.error("🌡️ Critical Overheating!")
        st.write("📌 Problem: Dangerous temperature level.")
        st.write("🧠 Reason: Thermal limit exceeded (>85°C). Risk of damage or failure.")
        st.write("🛠️ Action: Immediate shutdown required.")