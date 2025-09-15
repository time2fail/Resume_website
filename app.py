from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV |  Utku Cengiz Acar"
PAGE_ICON = ":wave:"
NAME = "Utku Cengiz Acar"
DESCRIPTION = """
"""
EMAIL = "utkucengizacar@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/utkucengizacar/",
    "GitHub": "https://github.com/time2fail",
    "Kaggle": "https://www.kaggle.com/utkucengizacar",
    "HackerRank": "https://www.hackerrank.com/profile/utkucengizacar"
}
ACCOMPLISHMENTS= {
    "🏆 Third in European Schools Chess Championship": "https://s1.chess-results.com/tnr179152.aspx?lan=1&art=1&SNode=S0",
    "🏆 3x Turkish Youth Chess Championship Champion": "",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)

    # Resume button
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    # Email
    st.write("📫", EMAIL)
    # Languages (right side, below email)
    st.write("🇬🇧 English: Advanced (C1)" " | 🇹🇷 Turkish: Native")



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ Strong hands-on experience and knowledge in Python and Excel  
- ✔️ Good understanding of statistical principles and their applications  
- ✔️ Excellent team-player with strong initiative on tasks  
"""
)


# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")

st.write("🎓 **Middle East Technical University (METU)**")
st.write("Bachelor of Science in Industrial Engineering | *Expected 2026* | GPA: 3.25")
st.write("Minor in Economics")
st.write('\n')

st.write("🎓 **Technical University of Sofia**")
st.write("Exchange Student Program | 2025")


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 **Programming:** Python (Scikit-learn, Pandas, Numpy), SEO, VBA, Matlab  
- 📊 **Modeling & Analytics:** Logistic Regression, Linear Regression, Decision Trees  
- 📈 **Tools:** Excel (Advanced), SQL, Streamlit  
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

st.write("🚧 **Risk Management Intern | [Garanti BBVA Pension](https://www.garantibbvaemeklilik.com.tr/)**")
st.write("07/2024 - 02/2025")
st.write(
    """
- ► Examined and analyzed financial and operational risks using Microsoft tools  
- ► Data entry and data cleaning for risk assessment reports  
"""
)

st.write('\n')
st.write("🚧 **Engineering Intern | [Turkish Aerospace Industries (TUSAŞ)](https://www.tusas.com/)**")
st.write("06/2024 - 07/2024")
st.write(
    """
- ► Focused on process optimization in industrial engineering workflows  
- ► Hands-on work with SQL and Excel for reporting and data management  
"""
)

st.write('\n')
st.write("🚧 **Arbitrage & Digital Product Marketing | ETSY**")
st.write("10/2021 - 02/2023")
st.write(
    """
- ► Conducted market analysis to identify profitable products for the US market  
- ► Wrote product descriptions with proper SEO to increase visibility  
- ► Leveraged AI tools to design and market digital products  
"""
)


# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in ACCOMPLISHMENTS.items():
    st.write(f"- 🏆 [{project}]({link})")


# --- ORGANIZATIONS ---
st.write('\n')
st.subheader("Organizations")
st.write("---")

st.write("🏛️ **METU Chess Club** | Director & Coordinator")
st.write("09/2021 – 06/2024 | Ankara, Turkey")
st.write(
    """
- ► Directed university-level chess tournaments  
- ► Organized club events and training sessions  
- ► Managed club’s social media presence and communications  
"""
)