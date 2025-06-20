import streamlit as st

def colored_header(label, color):
    st.markdown(
        f"""
        <h2 style='background-color:{color};padding:0.5em 1em;border-radius:8px;color:white;margin-bottom:0.5em'>
            {label}
        </h2>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.set_page_config(
        page_title="Aswin Rajaram - Analytics Engineer",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )

    # --- Header ---
    st.markdown(
        """
        <div style='display:flex;align-items:center;gap:1em;'>
            <img src="https://avatars.githubusercontent.com/u/9919?s=200&v=4" width="80" style="border-radius:50%;border:2px solid #4F8BF9"/>
            <div>
                <h1 style='margin-bottom:0;'>Aswin Rajaram</h1>
                <h4 style='color:#4F8BF9;margin-top:0;'>Analytics Engineer at Deliveroo</h4>
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
    colored_header("Skills", "#F97B22")
    skills = {
        "Cloud ☁️": ["AWS (S3, Athena, Glue, SNS, Lambda, EMR)", "Snowflake"],
        "Data Processing 🔄": ["PySpark", "dbt", "SSIS"],
        "Databases 🗄️": ["Snowflake", "Hive", "SAP HANA"],
        "BI & Visualization 📊": [
            "Amazon QuickSight",
            "Tableau",
            "Google Data Studio",
        ],
        "Orchestration ⏰": ["Oozie", "IBM TWS", "Fivetran"],
        "Languages 💻": ["Python", "SQL"],
    }
    skill_columns = st.columns(len(skills))
    for i, (category, skill_list) in enumerate(skills.items()):
        with skill_columns[i]:
            st.markdown(f"<b style='color:#F97B22'>{category}</b>", unsafe_allow_html=True)
            for skill in skill_list:
                st.markdown(f"<span style='color:#444;'>• {skill}</span>", unsafe_allow_html=True)

    # --- Work Experience ---
    st.markdown("<hr style='border:2px solid #4F8BF9;border-radius:2px;'>", unsafe_allow_html=True)
    colored_header("Work Experience", "#43BCCD")

    with st.container():
        st.markdown("#### <span style='color:#43BCCD'>Analytics Engineer II, Deliveroo</span>", unsafe_allow_html=True)
        st.markdown("*05/2023 - Present, Remote*")
        st.markdown(
            """
            - 🚀 Designed and implemented data pipelines in Snowflake for self-serve analytics.
            - 🤝 Collaborated with Data Scientists, ML Engineers, and Product teams.
            - ⚡ Refactored and optimised legacy code for better performance.
            - 🗺️ Influenced roadmap and product decisions for high quality data tracking.
            - 🧑‍💻 Ran coding interviews for Analytics Engineering applicants.
            """
        )

        st.markdown("#### <span style='color:#43BCCD'>Data Engineer, PadSquad</span>", unsafe_allow_html=True)
        st.markdown("*01/2021 - 04/2023, Remote*")
        st.markdown(
            """
            - Built end-to-end Data Pipeline on AWS (Data Wrangler, S3, Athena, Glue, SNS, Lambda).
            - Processed historical data using PySpark on AWS Glue and EMR.
            - Created interactive dashboards on Amazon QuickSight and Tableau.
            """
        )

        st.markdown("#### <span style='color:#43BCCD'>Data Engineer, Nissan Digital</span>", unsafe_allow_html=True)
        st.markdown("*11/2018 - 01/2021, Trivandrum, Kerala*")
        st.markdown(
            """
            - Data wrangling and ingestion into Hive and SAP HANA tables.
            - Automated workflows using Oozie and IBM TWS.
            - Improved SAP HANA SQL Procedures, reducing load time from 1 hr to < 5 mins.
            """
        )

        st.markdown("#### <span style='color:#43BCCD'>Product Development Engineer, Envestnet Inc.</span>", unsafe_allow_html=True)
        st.markdown("*06/2017 - 11/2018, Trivandrum, Kerala*")
        st.markdown(
            """
            - Developed Data Warehouse for financial platform.
            - Scheduled and executed ETL jobs for SEC reporting.
            - Wrote stored procedures and designed SSIS packages.
            """
        )

    # --- Personal Projects ---
    st.markdown("<hr style='border:2px solid #F97B22;border-radius:2px;'>", unsafe_allow_html=True)
    colored_header("Personal Projects", "#F97B22")
    st.markdown("**PDF to Speech Converter**: Created a PDF to speech converter in Python using PyPDF2 and pyttsx3 libraries. 🔊")
    st.markdown("**Data Pipeline using Modern Data Stack (PoC)**: Built an end-to-end pipeline using Google Sheets, Fivetran, Snowflake, dbt, and Google Studio. 🛠️")

    # --- Education ---
    st.markdown("<hr style='border:2px solid #43BCCD;border-radius:2px;'>", unsafe_allow_html=True)
    colored_header("Education", "#43BCCD")
    st.markdown("**B.Tech in Computer Science and Engineering**")
    st.markdown("*Rajiv Gandhi Institute of Technology, Kottayam (2013 - 2017)*")

    # --- Languages ---
    st.markdown("<hr style='border:2px solid #4F8BF9;border-radius:2px;'>", unsafe_allow_html=True)
    colored_header("Languages", "#4F8BF9")
    st.markdown("- <b>English</b>: Full Professional Proficiency 🇬🇧", unsafe_allow_html=True)
    st.markdown("- <b>Hindi</b>: Professional Working Proficiency 🇮🇳", unsafe_allow_html=True)
    st.markdown("- <b>Malayalam</b>: Native or Bilingual Proficiency 🇮🇳", unsafe_allow_html=True)
    st.markdown("- <b>Tamil</b>: Limited Working Proficiency 🇮🇳", unsafe_allow_html=True)

if __name__ == "__main__":
    main()