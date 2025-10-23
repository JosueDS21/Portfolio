import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Josue Holguin - Data Portfolio",
    page_icon="📊",
    layout="centered"
)

# --- Sidebar Navigation ---
st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Explore",  # empty label
    ["About Me", "Experience", "Education", "Projects", "Hobbies"]
)

# --- ABOUT ME ---
if page == "About Me":
    st.title("👋 About Me")
    st.subheader("Josue Holguin")
    st.write("Data Engineer | From building computers to building data systems — always driven by curiosity | Ecuador ")
    
    st.markdown("""
    I’m Josue Holguin — a passionate, results-driven Data Engineer who turns raw data into powerful insights and intelligent systems. I don’t just work with data — I engineer it into clarity, efficiency, and impact.

    With a strong background in Python, SQL, Spark, and Databricks, I’ve mastered the full data lifecycle — from ingestion and transformation to modeling and visualization. My work doesn’t stop at building pipelines; I make sure they run flawlessly, scale intelligently, and deliver real business value.

    I’ve worked in the banking domain, where precision and reliability aren’t optional — they’re everything. That experience shaped me into a meticulous problem-solver who thrives on tackling complex data challenges under pressure.

    I believe excellence comes from curiosity and discipline — and I bring both to every project I take on. Whether it’s optimizing performance, cleaning messy datasets, or designing elegant ETL workflows, I do it with the mindset of someone who refuses to settle for average.

    I don’t just focus on getting things done — I focus on getting them done right. My mission is to build data solutions that empower organizations to make smarter, faster, and more confident decisions.
    
    🔍 *Currently seeking*: Data Analyst, Junior Data Scientist, or Data Engineering roles.
    """)
    
    st.write("📫 Let's connect!")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/josue-holguin-13694324b)")
    with col2:
        st.markdown("[GitHub](https://github.com/JosueDS21)")

# --- EXPERIENCE ---
elif page == "Experience":
    st.title("💼 Professional Experience")

    st.header("Data Engineer")
    st.subheader("Banco Bolivariano | Guayaquil, Ecuador")
    st.caption("November 2024 – May 2025")
    st.markdown("""
    **Advanced Analytics**  
    - Designed and implemented a data pipeline with validation scripts to compare on-premise and cloud data for accuracy and consistency.  
    - Built an ETL process that automatically emails Excel reports detailing failed tables and their impact on analytical models.  
    - Developed a **Streamlit app** and **Power BI dashboard** enabling BI users to upload datasets, view real-time dashboards, and download reports.  
    - Optimized a web scraping application for improved performance and reliability.  
    - Investigated methods to extract client email interactions from Hubspot email campaigns.
    - Built a **proof-of-concept (POC) in Databricks** and designed an **Entity Relationship Diagram (ERD)** for Data Engineering and Data Science leads.  

    **Data Quality**  
    - Migrated validation scripts from the **bronze to gold layer** in a Medallion architecture.  
    - Automated data quality validation jobs to ensure continuous monitoring.  
    - Conducted analysis, development, and implementation of end-to-end data quality solutions.  

    **Quality Assurance**  
    - Performed functional testing for the account opening process in the **24Móvil** mobile banking app.  
    - Reported and tracked bugs with development and support teams to resolution.
    """)

    st.markdown("---")

    st.header("Banking Core Developer")
    st.subheader("Genuide S.A. | Guayaquil, Ecuador (Remote)")
    st.caption("January 2023 – October 2024")    
    st.markdown("**ETL & Core Banking Development (May 2023 – Oct 2024)**")
    st.markdown("""
    - Extracted, transformed, and standardized data to meet **regulatory compliance requirements**.  
    - Collaborated with users, comptrollers, and auditors to validate data before final submission.  
    - Maintained and optimized PL/SQL stored procedures for client financial status queries.  
    - Developed database scripts (tables, indexes, views) and validation methods for a **monetary transfer project**.  
    - Created robust data querying and validation logic to ensure transaction integrity.
    """)

    st.markdown(" **QA Tester (Jan 2023 – Apr 2023)**")
    st.markdown("""
    - Verified **savings account** logic: interest calculations, transactions, and regulatory compliance.  
    - Validated **checking account** workflows: transaction processing, overdraft handling, and reconciliation.  
    - Ensured financial accuracy and alignment with banking standards.
    """)

    st.markdown("---")

    st.header("Computer Buyer Advisor (Freelance)")
    # st.subheader("Self-Employed | Ecuador")
    st.caption("August 2018 – July 2024")
    st.markdown("""
    - Advised clients on optimal computer specs for gaming, video editing, and software development.  
    - Recommended and validated custom hardware builds based on performance needs and budget.  
    - Stayed current with emerging tech trends to provide informed, future-proof recommendations.
    """)

# --- EDUCATION ---
elif page == "Education":
    st.title("🎓 Education & Credentials")

    st.header("🛠️ Technical & Domain Skills")
    st.markdown("""
    **🏦 Banking & Finance**: COBIS Core Banking, Domain Knowledge, Regulatory Compliance  
    **📌 Languages**: Python, PL/SQL, Java, Visual Basic  
    **📌 Data Engineering**: Spark, Databricks, Azure Data Factory, Medallion Architecture, ETL/ELT  
    **📌 Data Quality**: Validation Frameworks, ERD, Automation  
    **📌 Visualization**: Power BI, Streamlit  
    **📌 Cloud & DevOps**: Microsoft Azure, Git, Agile/Scrum  
    **📌 QA & Testing**: Functional Testing, Test Scripts, Bug Tracking
    """)

    st.markdown("---")

    st.header("🎓 Bachelor of Science in Computer Science")
    st.subheader("University of the People | Pasadena, California")
    st.caption("CGPA: 3.84 / 4.0")
    st.markdown("""
    - Coursework: Data Structures, Algorithms, Database Systems, Software Engineering, Distributed Systems
    """)

    st.markdown("---")

    st.header("📜 Certifications")
    
    # Python 101 for Data Science
    st.subheader("🐍 Python 101 for Data Science")
    st.caption("*Provided by IBM via Cognitive Class*")
    st.markdown(
        """
        <a href="https://courses.cognitiveclass.ai/certificates/4b2e8bc6fb51439a8adf115fcffa5bd0" 
           target="_blank" 
           style="text-decoration: none;">
            <button style="
                background-color: #005e99; 
                color: white; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 6px; 
                font-weight: bold;
                cursor: pointer;">
                🖨️ View Credential
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.caption("Issued: July 2024")

    st.markdown("<br>", unsafe_allow_html=True)

    # Introduction to Quantum Computing
    st.subheader("⚛️ Introduction to Quantum Computing")
    st.caption("*Provided by IBM via Cognitive Class*")
    st.markdown(
        """
        <a href="https://courses.cognitiveclass.ai/certificates/d0cd6828a139417dbd1c1928c33ce82a" 
           target="_blank" 
           style="text-decoration: none;">
            <button style="
                background-color: #005e99; 
                color: white; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 6px; 
                font-weight: bold;
                cursor: pointer;">
                🖨️ View Credential
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.caption("Issued: October 2025")

    st.markdown("<br>", unsafe_allow_html=True)

    # Encryption & Quantum-Safe Techniques
    st.subheader("🔐 Fundamentals of Encryption & Quantum-Safe Techniques")
    st.caption("*Provided by IBM via Cognitive Class*")
    st.markdown(
        """
        <a href="https://courses.cognitiveclass.ai/certificates/52ec6f420cd64689ac17a435256f0157" 
           target="_blank" 
           style="text-decoration: none;">
            <button style="
                background-color: #005e99; 
                color: white; 
                border: none; 
                padding: 10px 20px; 
                border-radius: 6px; 
                font-weight: bold;
                cursor: pointer;">
                🖨️ View Credential
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
    st.caption("Issued: October 2025")

# --- PROJECTS ---
elif page == "Projects":
    st.title("🚀 Projects")
    
    st.header("📈 S&P 500 App")
    st.write("""
    **Description**: This app retrieves the list of the S&P 500 and its corresponding stock closing price (year-to-date)!
    - **Tech Used**: base64, pandas, streamlit, matplotlib, yfinance
    - **Key Features**: 
        - Intuitive and user-friendly interface
        - Real-time data filtering and visualization
        - Easy download for data analysis
    """)
    
    st.markdown("💡 [Live Demo](https://sp500-appypy-dbqcczub6j9irmghjt3siw.streamlit.app)")
    st.markdown("💻 [View Code on GitHub](https://github.com/josueds21/sp500app/blob/main/sp500-appy.py)")
    
    st.markdown("---")
    st.info("🔜 More data projects coming soon!")

# --- HOBBIES ---
elif page == "Hobbies":
    st.title("🧪 Hobbies & Interests")
    st.write("""
    Outside of coding and data, I enjoy:
    - 🏋️ **Working out** – I love fitness in general, especially calisthenics training.  
    - 🎧 **Music** – I play the kalimba and bass; my favorite genre is indie rock.  
    - ⚽ **Football** – I play whenever I get the chance.  
    - 🏍️ **Motorcycling** – Riding dirt bikes is my #1 form of therapy.
    """)

# --- Footer ---
st.markdown("---")
st.caption("Built using Python & Streamlit | © 2025 Josue Holguin")