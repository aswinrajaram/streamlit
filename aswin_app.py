import streamlit as st

def colored_header(label, color):
    st.markdown(
        f"""
        <h2 style='background-color:{color};
                   padding:0.2em 1em;
                   border-radius:8px;
                   color:white;
                   margin-bottom:0.3em;
                   font-size:1.6em;'>  <!-- Change this value for desired size -->
            {label}
        </h2>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(
        page_title="Aswin Rajaram - Data Engineer",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )


    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # --- Header (Centered) ---
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style='margin-bottom:0;'>Aswin Rajaram</h1>
            <h2 style='color:#4F8BF9;margin-top:0;'>Data Engineer</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Contact ---
    st.markdown(
        """
        <div style="display:flex;justify-content:center;gap:2.5em;align-items:center;margin: 18px 0 28px 0;">
            <div style="display:flex;align-items:center;gap:0.4em;">
                <span style="font-size:1.3em;">📧</span>
                <a href="mailto:aswin.rajaram@email.com" style="color:#FFF;font-size:1.1em;text-decoration:none;">aswin.rajaram@email.com</a>
            </div>
            <div style="display:flex;align-items:center;gap:0.4em;">
                <span style="font-size:1.3em;">📱</span>
                <a href="tel:+919400725091" style="color:#FFF;font-size:1.1em;text-decoration:none;">+91 94007 25091</a>
            </div>
            <div style="display:flex;align-items:center;gap:0.4em;">
                <span style="font-size:1.3em;">💼</span>
                <a href="https://www.linkedin.com/in/aswin-rajaram/" target="_blank" style="color:#FFF;font-size:1.1em;text-decoration:none;">linkedin.com/in/aswinrajaram</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- About Me ---
    colored_header("About Me", "#4F8BF9")
    st.write(
        "👋 Data Engineer with progressive experience in **Finance**, **Automotive**, "
        "**Marketplace**, and **Advertising** domains, passionate about delivering "
        "business value and actionable insights through well-architected data products."
    )

    

    # --- Skills ---
    colored_header("Skills", "#4F8BF9")
    skills = {
        "Cloud ☁️": ["AWS (S3, Athena, Glue, SNS, Lambda, EMR)", "Snowflake"],
        "Data Processing 🔄": ["PySpark", "dbt", "SSIS"],
        "Databases 🗄️": ["Snowflake", "Hive", "SAP HANA", "Postgres"],
        "BI & Visualisation 📊": [
            "Amazon QuickSight",
            "Tableau",
            "Looker",
        ],
        "Orchestration ⏰": ["Oozie", "IBM TWS", "Fivetran"],
        "Languages 💻": ["Python", "SQL"],
        "GenAI 🤖": ["Cursor", "GitHub Copilot", "ChatGPT", "Gemini"],
    }
    skill_columns = st.columns(len(skills))
    for i, (category, skill_list) in enumerate(skills.items()):
        with skill_columns[i]:
            st.markdown(f"<b style='color:#F97B22'>{category}</b>", unsafe_allow_html=True)
            for skill in skill_list:
                st.markdown(f"<span style='color:#FFF;'>{skill}</span>", unsafe_allow_html=True)

    # --- Work Experience ---
    colored_header("Work Experience", "#4F8BF9")

    with st.container():
        st.markdown("#### <span style='color:#4F8BF9'>Analytics Engineer II, Deliveroo</span>", unsafe_allow_html=True)
        st.markdown("*05/2023 - Present, Hyderabad, Telangana*")
        st.markdown(
            """
            - 🚀 Designed and implemented data pipelines in Snowflake for self-serve analytics.
            - 🤝 Collaborated with Data Scientists, ML Engineers, and Product teams.
            - ⚡ Refactored and optimised legacy code for better performance.
            - 🗺️ Influenced roadmap and product decisions for high quality data tracking.
            - 🧑‍💻 Ran coding interviews for Analytics Engineering applicants.
            """
        )

        st.markdown("#### <span style='color:#4F8BF9'>Data Engineer, PadSquad</span>", unsafe_allow_html=True)
        st.markdown("*01/2021 - 04/2023, Remote*")
        st.markdown(
            """
            - 🏗️ Built end-to-end Data Pipeline on AWS (Data Wrangler, S3, Athena, Glue, SNS, Lambda).
            - 🔄 Processed historical data using PySpark on AWS Glue and EMR.
            - 📊 Created interactive dashboards on Amazon QuickSight and Tableau.
            """
        )

        st.markdown("#### <span style='color:#4F8BF9'>Data Engineer, Nissan Digital</span>", unsafe_allow_html=True)
        st.markdown("*11/2018 - 01/2021, Trivandrum, Kerala*")
        st.markdown(
            """
            - 🧹 Data wrangling and ingestion into Hive and SAP HANA tables.
            - 🤖 Automated workflows using Oozie and IBM TWS.
            - ⚡ Improved SAP HANA SQL Procedures, reducing load time from 1 hr to < 5 mins.
            """
        )

        st.markdown("#### <span style='color:#4F8BF9'>Product Development Engineer, Envestnet Inc.</span>", unsafe_allow_html=True)
        st.markdown("*06/2017 - 11/2018, Trivandrum, Kerala*")
        st.markdown(
            """
            - 🏦 Developed Data Warehouse for financial platform.
            - ⏰ Scheduled and executed ETL jobs for SEC reporting.
            - 📝 Wrote stored procedures and designed SSIS packages.
            """
        )

    # --- Personal Projects ---
    colored_header("Personal Projects", "#4F8BF9")
    st.markdown("🔊 **PDF to Speech Converter**: Created a PDF to speech converter in Python using PyPDF2 and pyttsx3 libraries.")
    st.markdown("🛠️ **Data Pipeline using Modern Data Stack (PoC)**: Built an end-to-end pipeline using Google Sheets, Fivetran, Snowflake, dbt, and Google Studio.")

    # --- Education ---
    colored_header("Education", "#4F8BF9")
    st.markdown("**B.Tech in Computer Science and Engineering**")
    st.markdown("*Rajiv Gandhi Institute of Technology, Kottayam (2013 - 2017)*")

    # --- Languages ---
    colored_header("Languages", "#4F8BF9")
    st.markdown("- <b>English</b>: Full Professional Proficiency", unsafe_allow_html=True)
    st.markdown("- <b>Hindi</b>: Professional Working Proficiency", unsafe_allow_html=True)
    st.markdown("- <b>Malayalam</b>: Native or Bilingual Proficiency", unsafe_allow_html=True)
    st.markdown("- <b>Tamil</b>: Limited Working Proficiency", unsafe_allow_html=True)

if __name__ == "__main__":
    main()