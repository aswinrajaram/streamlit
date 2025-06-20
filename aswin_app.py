import streamlit as st


def main():
    st.set_page_config(
        page_title="Aswin Rajaram - Analytics Engineer",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )

    # --- Header ---
    st.title("Aswin Rajaram")
    st.subheader("Analytics Engineer at Deliveroo")

    # --- About Me ---
    st.markdown("## About Me")
    st.write(
        "Data Engineer with progressive experience in Finance, Automotive, "
        "Marketplace, and Advertising domains, who is passionate about "
        "delivering business value and actionable insights through "
        "well-architected data products."
    )

    # --- Skills ---
    st.markdown("## Skills")
    skills = {
        "Cloud": ["AWS (S3, Athena, Glue, SNS, Lambda, EMR)", "Snowflake"],
        "Data Processing": ["PySpark", "dbt", "SSIS"],
        "Databases": ["Snowflake", "Hive", "SAP HANA"],
        "BI & Visualization": [
            "Amazon QuickSight",
            "Tableau",
            "Google Data Studio",
        ],
        "Orchestration": ["Oozie", "IBM TWS", "Fivetran"],
        "Languages": ["Python", "SQL"],
    }

    skill_columns = st.columns(len(skills))
    for i, (category, skill_list) in enumerate(skills.items()):
        with skill_columns[i]:
            st.markdown(f"**{category}**")
            for skill in skill_list:
                st.markdown(f"- {skill}")

    # --- Work Experience ---
    st.markdown("---")
    st.markdown("## Work Experience")

    st.markdown("### Analytics Engineer II, Deliveroo")
    st.markdown("*05/2023 - Present, Remote*")
    st.markdown(
        """
        - Designed and implemented data pipelines in Snowflake for self-serve
          analytics for stakeholders.
        - Collaborated with Data Scientists, ML Engineers, and Product teams to
          deliver robust analytics solutions.
        - Refactored and optimised legacy code for better run-time performance.
        - Influenced roadmap and product decisions to enable high quality data
          tracking and better-informed decision making.
        - Ran coding interview for applicants to Analytics Engineering role.
        """
    )

    st.markdown("### Data Engineer, PadSquad")
    st.markdown("*01/2021 - 04/2023, Remote*")
    st.markdown(
        """
        - Developed end-to-end Data Pipeline on AWS using Data Wrangler,
          S3, Athena, Glue, SNS, and, Lambda which processes data from
          mobile ad interactions.
        - Historical data processing using PySpark on AWS Glue and Amazon EMR.
        - Created interactive dashboards on Amazon QuickSight and Tableau for
          Business users.
        """
    )

    st.markdown("### Data Engineer, Nissan Digital")
    st.markdown("*11/2018 - 01/2021, Trivandrum, Kerala*")
    st.markdown(
        """
        - Data wrangling and ingestion into Hive and SAP HANA tables, and
          automation of workflows using Oozie.
        - Schedule, execute, and monitor Windows Batch jobs in IBM TWS.
        - Improved performance and restructured SAP HANA SQL Procedures to bring
          down the data load time from 1 hr to < 5 mins.
        """
    )

    st.markdown("### Product Development Engineer, Envestnet Inc.")
    st.markdown("*06/2017 - 11/2018, Trivandrum, Kerala*")
    st.markdown(
        """
        - Develop Data Warehouse for the financial platform used and
          reconcile errors after a monthly refresh.
        - Schedule and execute ETL jobs that generate report for the
          Securities and Exchanges Commission (SEC), USA.
        - Write stored procedures and design SSIS packages to transfer data
          from the platform to the staging and then to the database layers.
        """
    )

    # --- Personal Projects ---
    st.markdown("---")
    st.markdown("## Personal Projects")

    st.markdown("### PDF to Speech Converter")
    st.markdown(
        "Created a PDF to speech converter in Python using PyPDF2 and pyttsx3 "
        "libraries."
    )

    st.markdown("### Data Pipeline using Modern Data Stack (PoC)")
    st.markdown(
        "Created an end to end Data Pipeline using Google Sheets, Fivetran, "
        "Snowflake, dbt, and Google Studio."
    )

    # --- Education ---
    st.markdown("---")
    st.markdown("## Education")
    st.markdown("### B.Tech in Computer Science and Engineering")
    st.markdown("*Rajiv Gandhi Institute of Technology, Kottayam (2013 - 2017)*")

    # --- Languages ---
    st.markdown("---")
    st.markdown("## Languages")
    st.markdown("- **English**: Full Professional Proficiency")
    st.markdown("- **Hindi**: Professional Working Proficiency")
    st.markdown("- **Malayalam**: Native or Bilingual Proficiency")
    st.markdown("- **Tamil**: Limited Working Proficiency")


if __name__ == "__main__":
    main() 