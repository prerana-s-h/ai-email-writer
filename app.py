import streamlit as st
from modules.generator import generate_email
st.set_page_config(
    page_title="AI Email Writer",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu, footer, header{
    visibility:hidden;
}

/* Hide Fullscreen Button */
button[title="View fullscreen"]{
    display:none !important;
}

[data-testid="stImage"] button{
    display:none !important;
}
/* Hide image fullscreen button */
button[title="Fullscreen"]{
    display:none !important;
}

[data-testid="StyledFullScreenButton"]{
    display:none !important;
}

[data-testid="stImage"] button{
    display:none !important;
}
.mail-container{
    display:flex;
    justify-content:center;
    margin-top:10px;
    margin-bottom:25px;
}

.envelope{
    position:relative;
    width:120px;
    height:90px;
}

.envelope-body{
    position:absolute;
    bottom:0;
    width:120px;
    height:75px;
    background:#38bdf8;
    border-radius:0 0 10px 10px;
}

.envelope-flap{
    position:absolute;
    top:0;
    width:0;
    height:0;
    border-left:60px solid transparent;
    border-right:60px solid transparent;
    border-bottom:40px solid #60a5fa;
}

.letter{
    position:absolute;
    left:15px;
    width:90px;
    height:55px;
    background:white;
    border-radius:5px;

    animation:letterMove 2s ease-in-out infinite;
}

@keyframes letterMove{
    0%{
        top:25px;
    }
    50%{
        top:-10px;
    }
    100%{
        top:25px;
    }
}
/* Background */
.stApp{
    background:
    linear-gradient(
        135deg,
        #5B21B6 0%,
        #4C1D95 20%,
        #312E81 45%,
        #0F172A 75%,
        #020617 100%
    );
}

/* Title */
.title{
    text-align:center;
    font-size:70px;
    font-weight:900;
    margin-bottom:10px;

    color:#c084fc;

    text-shadow:
        0 0 8px rgba(192,132,252,.4),
        0 0 15px rgba(139,92,246,.25);
}
/* Section Headings */
h3{
    color:white !important;
    text-align:center !important;

    text-shadow:
        0 0 10px #7c3aed,
        0 0 20px #7c3aed,
        0 0 35px #38bdf8;
}
/* Labels */
label{
    color:white !important;
    font-weight:600;
}

/* Text Inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTextArea textarea {

    background: rgba(15,23,42,.95) !important;
    color: white !important;

    border: none !important;
    outline: none !important;
    box-shadow: none !important;

    border-radius: 12px !important;
}

/* Outer container */
.stTextInput > div,
.stNumberInput > div,
.stTextArea > div {

    border: 2px solid #8b5cf6 !important;
    border-radius: 12px !important;
    background: rgba(15,23,42,.95) !important;

    box-shadow: none !important;
}

/* Remove focus ring */
.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {

    outline: none !important;
    box-shadow: none !important;
    border: 2px solid rgba(139,92,246,.6) !important;
}

/* Select Boxes */
.stSelectbox div[data-baseweb="select"]{
    background:rgba(15,23,42,.9);
    border-radius:12px;
}

/* Button Center */
div.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;

    background:linear-gradient(
        90deg,
        #ff00cc,
        #7c3aed,
        #38bdf8
    );

    color:white;
    font-size:20px;
    font-weight:700;

    box-shadow:
        0 0 15px #ff00cc,
        0 0 30px #7c3aed,
        0 0 45px #38bdf8;
}

/* Generate Button */
.stButton button{
    width:320px;
    height:60px;
    border:none;
    border-radius:15px;

    background:linear-gradient(
        90deg,
        #ff00cc,
        #7c3aed,
        #38bdf8
    );

    color:white;
    font-size:20px;
    font-weight:700;

    box-shadow:
    0 0 15px #ff00cc,
    0 0 30px #7c3aed,
    0 0 45px #38bdf8;
}

/* Generated Email Box */
.output{
    background:#0f172a;
    border-radius:20px;
    padding:25px;
    border:1px solid #38bdf8;
    color:white;
    margin-top:20px;
}

/* Email Glow */
@keyframes glow{
    0%{
        box-shadow:0 0 10px #7c3aed;
    }
    50%{
        box-shadow:0 0 35px #38bdf8;
    }
    100%{
        box-shadow:0 0 10px #7c3aed;
    }
}

.output{
    animation:glow 3s infinite;
}

/* Generated Email Title */
.generated-title{
    text-align:center;
    color:white;
    margin-top:30px;
    margin-bottom:15px;
}

/* Image Glow */
[data-testid="stImage"] img{
    filter:
        drop-shadow(0 0 20px #38bdf8)
        drop-shadow(0 0 40px #7c3aed);
}
.mail-container{
    display:flex;
    justify-content:center;
    margin-top:5px;
    margin-bottom:30px;
}

.envelope{
    position:relative;
    width:120px;
    height:100px;
}

/* Letter */
.letter{
    position:absolute;
    left:15px;
    width:90px;
    height:60px;

    background:white;
    border-radius:6px;

    z-index:1;

    animation:letterMove 2s ease-in-out infinite;
}

/* Triangle flap behind */
.envelope-flap{
    position:absolute;
    top:15px;
    left:0;

    width:0;
    height:0;

    border-left:60px solid transparent;
    border-right:60px solid transparent;
    border-bottom:40px solid #fde047;

    z-index:0;
}

/* Front envelope */
.envelope-body{
    position:absolute;
    bottom:0;

    width:120px;
    height:70px;

    background:#facc15;
    border-radius:0 0 10px 10px;

    z-index:2;

    box-shadow:
        0 0 15px rgba(250,204,21,.5);
}

/* Paper moves but remains partially hidden */
@keyframes letterMove{

    0%{
        top:35px;
    }

    50%{
        top:0px;
    }

    100%{
        top:35px;
    }
}
</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================

st.markdown(
    """
    <div class="title">
        ⚡ AI EMAIL WRITER
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<div class="mail-container">
    <div class="envelope">
        <div class="letter"></div>
        <div class="envelope-flap"></div>
        <div class="envelope-body"></div>
    </div>
</div>
""", unsafe_allow_html=True)
# ======================
# SENDER & RECIPIENT
# ======================

left, right = st.columns(2)

with left:

    st.subheader("📤 Sender Details")

    sender_name = st.text_input(
        "From Name",
        placeholder="Prerana S H"
    )

    sender_email = st.text_input(
        "From Email",
        placeholder="prerana@gmail.com"
    )

with right:

    st.subheader("📥 Recipient Details")

    receiver_name = st.text_input(
        "To Name",
        placeholder="Hiring Manager"
    )

    receiver_email = st.text_input(
        "To Email",
        placeholder="hr@company.com"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# EMAIL INFORMATION
# ======================

st.subheader("📝 Email Information")

purpose = st.text_area(
    "Purpose",
    placeholder="Example: Applying for Data Analyst Internship"
)

word_limit = st.number_input(
    "Keep the email under words",
    min_value=50,
    max_value=1000,
    value=150,
    step=10
)

col1, col2 = st.columns(2)

with col1:

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Polite",
            "Persuasive"
        ]
    )

with col2:

    length = st.selectbox(
        "Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

st.markdown("<br>", unsafe_allow_html=True)

# ======================
# CENTER BUTTON
# ======================

c1, c2, c3 = st.columns([1,2,1])

with c2:
    generate = st.button(
        "Generate Email",
        use_container_width=True
    )
# ======================
# OUTPUT
# ======================

if generate:

    if (
        not sender_name.strip()
        or not sender_email.strip()
        or not receiver_name.strip()
        or not receiver_email.strip()
        or not purpose.strip()
    ):

        st.warning("Please fill all fields.")

    else:

        try:

            with st.spinner("Generating Email..."):

                email = generate_email(
                    sender_name,
                    receiver_name,
                    purpose,
                    tone,
                    length,
                    word_limit
                )

            st.markdown(
                """
                <h2 class="generated-title">
                📩 Generated Email
                </h2>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="output">
                <pre style="
                    white-space:pre-wrap;
                    color:white;
                    font-size:16px;
                    font-family:Arial;
                    margin:0;
                ">{email}</pre>
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")
