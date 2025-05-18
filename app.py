import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime

# Page Config with dark mode
st.set_page_config(
    page_title="MS Rakha - CV", 
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="📊",
    menu_items={
        'Get Help': 'https://rakhashaik.netlify.app',
        'Report a bug': 'https://rakhashaik.netlify.app',
        'About': 'AWS Developer | Cloud Enthusiast | AWS Data Engineer'
    }
)

# Force dark theme
st.markdown("""
<script>
    document.querySelector('body').classList.add('dark');
    localStorage.setItem('theme', 'dark');
</script>
""", unsafe_allow_html=True)

# Custom CSS for styling with dark mode colors
st.markdown("""
<style>
    /* Dark mode styling */
    body {
        color: #f0f2f6;
        background-color: #0e1117;
    }
    
    .main-header {
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        color: #4da6ff;
        margin-bottom: 0.5rem;
    }
    
    .title {
        font-size: 1.5rem;
        text-align: center;
        color: #f0f2f6;
        margin-bottom: 1.5rem;
    }
    
    .sub-header {
        font-size: 1.6rem;
        border-bottom: 2px solid #4da6ff;
        padding-bottom: 5px;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        color: #4da6ff;
    }
    
    .section {
        margin-bottom: 1.5rem;
        padding: 0.5rem;
    }
    
    .contact-info {
        display: flex;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 1.5rem;
    }
    
    .contact-item {
        text-align: center;
        flex: 1;
    }
    
    .portfolio-button {
        display: inline-block;
        padding: 7px;
        text-align: center;
        text-decoration: none;
        color: #ffffff;
        width: 200px;
        height: 32px;
        border-radius: 16px;
        background-color: #4da6ff;
        margin: 5px auto;
        display: block;
    }
    
    .skill-tag {
        background-color: #1e2a3a;
        color: #4da6ff;
        padding: 3px 7px;
        border-radius: 12px;
        font-size: 0.8rem;
        margin: 3px;
        display: inline-block;
    }
    
    .aws-skill {
        background-color: #232f3e;
        color: #ff9900;
    }
    
    .ai-skill {
        background-color: #1a3151;
        color: #61dafb;
    }
    
    .devops-skill {
        background-color: #2a1e30;
        color: #8c52ff;
    }
    
    .data-skill {
        background-color: #1e302a;
        color: #00c853;
    }
    
    .summary-text {
        text-align: justify;
        margin-bottom: 1rem;
        line-height: 1.5;
    }
    
    .bullet-points {
        margin-left: 1rem;
        margin-bottom: 1rem;
    }
    
    .project-title {
        color: #4da6ff;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        margin-top: 1rem;
    }
    
    .project-details {
        margin-left: 0.5rem;
    }
    
    .cert-item {
        margin-bottom: 0.3rem;
    }
    
    .skill-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        gap: 5px;
    }
    
    .skill-category {
        margin-bottom: 15px;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Adjust container padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Equal height columns */
    .equal-height {
        display: flex;
        flex-direction: column;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .contact-info {
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .contact-item {
            text-align: left;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="main-header">Rakha Shaik</h1>', unsafe_allow_html=True)
st.markdown('<div class="title">| AWS Data Engineer | AWS DevOps </div>', unsafe_allow_html=True)

# Contact Information - Evenly spaced row
st.markdown("""
<div class="contact-info">
    <div class="contact-item">📧 1.rakha.ms@gmail.com</div>
    <div class="contact-item">📞 +91 6305675227</div>
    <div class="contact-item">📍 Andhra Pradesh, India</div>
    <div class="contact-item">🌐 <a href="https://rakhashaik.netlify.app" target="_blank" style="color: #4da6ff;">Portfolio</a></div>
</div>
""", unsafe_allow_html=True)

# Professional Summary
st.markdown('<h2 class="sub-header">Professional Summary</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="summary-text">
Results-driven AWS Developer and Data Engineer with a strong focus on building scalable data solutions and optimizing cloud infrastructure in the healthcare domain. 
Committed to leveraging AWS technologies, Generative AI, and data engineering practices to enhance data processing and analytics capabilities. 
Proven ability to design and implement efficient data pipelines and solutions that drive business insights and improve healthcare outcomes.
</div>
""", unsafe_allow_html=True)

# Key skills in 2 columns
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    • Architect scalable data solutions using AWS best practices
    • Implement robust data pipelines for healthcare data
    • Enhance data reliability through automated monitoring
    """)
with col2:
    st.markdown("""
    • Leverage AWS Generative AI services for insights
    • Design DevOps workflows ensuring HIPAA compliance
    • Optimize cloud infrastructure for performance
    """)

# Main Columns for the rest of the content - equal width
left_col, right_col = st.columns([1, 1])

with left_col:
    # Work Experience
    st.markdown('<h2 class="sub-header">Work Experience</h2>', unsafe_allow_html=True)
    
    # Calculate experience duration
    start_date = datetime(2022, 8, 1)
    current_date = datetime.now()
    experience_years = current_date.year - start_date.year
    experience_months = current_date.month - start_date.month
    if experience_months < 0:
        experience_years -= 1
        experience_months += 12
    
    experience_text = f"{experience_years} years, {experience_months} months"
    
    # Work experience without expander for cleaner look
    st.markdown(f"### Product Engineer | TCS (Aug 2022 – Present) - {experience_text}")
    st.markdown("""
    • **Cloud Infrastructure:** Deployed and managed containerized applications using AWS EKS and ECR
    • **Data Engineering:** Developed ETL pipelines using AWS Glue, Redshift, and AWS Batch jobs
    • **AI/ML Development:** Engineered custom LLMs and implemented RAG frameworks using Amazon Bedrock
    • **DevOps Automation:** Implemented CI/CD pipelines with AWS CodePipeline and GitHub Actions
    • **Healthcare Analytics:** Built real-time dashboards using QuickSight and Grafana
    """)

    # Projects
    st.markdown('<h2 class="sub-header">Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown('<div class="project-title">Roche Genentech Healthcare Data Platform (Jan 2025 - Present)</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-details">', unsafe_allow_html=True)
    st.markdown("**Client:** Roche Genentech - Leading Biotechnology Company")
    st.markdown("**Role:** AWS Data Engineer")
    st.markdown("**Tools:** AWS (S3, Glue, Redshift), Python, Terraform, Amazon Bedrock, AWS HealthLake")
    st.markdown("""**Key Achievements:**
    • Designed data lake architecture for clinical trial data
    • Developed ETL pipelines for healthcare data
    • Implemented HIPAA-compliant security controls
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 2
    st.markdown('<div class="project-title">AWS Supply Chain Analytics Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-details">', unsafe_allow_html=True)
    st.markdown("**Client:** Global Retail Corporation")
    st.markdown("**Tools:** AWS (ECS, ECR, Lambda), Python, React.js, Docker, CloudWatch")
    st.markdown("""**Key Achievements:**
    • Led development of supply chain analytics solution with AWS services
    • Engineered ETL pipelines for real-time inventory tracking
    • Created React.js dashboards for supply chain visibility
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 3
    st.markdown('<div class="project-title">AI-Powered Customer Service Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-details">', unsafe_allow_html=True)
    st.markdown("**Client:** Technology Services Provider")
    st.markdown("**Tools:** AWS Comprehend, Claude, RAG Framework, Python, Streamlit")
    st.markdown("""**Key Achievements:**
    • Developed a custom LLM for automated customer support
    • Created an interactive Streamlit interface for service agents
    • Integrated sentiment analysis for customer feedback processing
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Education
    st.markdown('<h2 class="sub-header">Education</h2>', unsafe_allow_html=True)
    st.markdown("**B.Tech, Ashoka Women's Engineering College**")
    st.markdown("ECE | 2018-2022 | CGPA: 9.1")
    st.markdown("""
    • President of Ashoka Student Club
    • Winner of multiple quiz competitions
    """)
    
    st.markdown("**Intermediate & School, Nalanda University**")
    st.markdown("2016-2018 | CGPA: 9.8")
    # Certifications and Languages
    st.markdown('<h2 class="sub-header">Certifications & Languages</h2>', unsafe_allow_html=True)
    cert_col1, cert_col2 = st.columns(2)
    
    with cert_col1:
        st.markdown("**AWS Certifications:**")
        st.markdown("• AWS Solutions Architect – Associate")
        st.markdown("• AWS Cloud Practitioner & AI")
        st.markdown("• AWS Developer")
    
    with cert_col2:
        st.markdown("**Languages:**")
        st.markdown("• English (Professional)")
        st.markdown("• Hindi (Professional)")
        st.markdown("• Telugu (Native)")

with right_col:
    # Skills section with better organization
    st.markdown('<h2 class="sub-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    # AWS & Cloud - in columns
    st.markdown("#### AWS & Cloud")
    aws_col1, aws_col2, aws_col3 = st.columns(3)
    
    aws_skills = [
        ["AWS S3", "EC2", "Lambda"],
        ["AWS Glue", "Redshift", "HealthLake"],
        ["CloudFormation", "Terraform", "CloudWatch"]
    ]
    
    for i, col in enumerate([aws_col1, aws_col2, aws_col3]):
        with col:
            for skill in aws_skills[i]:
                st.markdown(f"""<span class="skill-tag aws-skill">{skill}</span>""", unsafe_allow_html=True)
    
    # AWS Generative AI - in columns
    st.markdown("#### AWS Generative AI")
    ai_col1, ai_col2 = st.columns(2)
    
    ai_skills = [
        ["Amazon Bedrock", "SageMaker", "AWS Comprehend Medical"],
        ["RAG Frameworks", "Vector Databases", "LLM Fine-tuning"]
    ]
    
    for i, col in enumerate([ai_col1, ai_col2]):
        with col:
            for skill in ai_skills[i]:
                st.markdown(f"""<span class="skill-tag ai-skill">{skill}</span>""", unsafe_allow_html=True)
    
    # AWS DevOps - in columns
    st.markdown("#### AWS DevOps")
    devops_col1, devops_col2 = st.columns(2)
    
    devops_skills = [
        ["AWS CodePipeline", "GitHub Actions", "CI/CD"],
        ["Docker", "Kubernetes", "AWS EKS/ECS"]
    ]
    
    for i, col in enumerate([devops_col1, devops_col2]):
        with col:
            for skill in devops_skills[i]:
                st.markdown(f"""<span class="skill-tag devops-skill">{skill}</span>""", unsafe_allow_html=True)
    
    # AWS Data Engineering - in columns
    st.markdown("#### AWS Data Engineering")
    data_col1, data_col2 = st.columns(2)
    
    data_skills = [
        ["AWS Glue ETL", "Redshift/RDS", "QuickSight"],
        ["Kinesis/Kafka", "Data Modeling", "Healthcare Data"]
    ]
    
    for i, col in enumerate([data_col1, data_col2]):
        with col:
            for skill in data_skills[i]:
                st.markdown(f"""<span class="skill-tag data-skill">{skill}</span>""", unsafe_allow_html=True)
    
    # Programming - in columns
    st.markdown("#### Programming")
    prog_col1, prog_col2, prog_col3 = st.columns(3)
    
    with prog_col1:
        st.markdown(f"""<span class="skill-tag">Python</span>""", unsafe_allow_html=True)
        st.markdown(f"""<span class="skill-tag">SQL</span>""", unsafe_allow_html=True)
    
    with prog_col2:
        st.markdown(f"""<span class="skill-tag">PySpark</span>""", unsafe_allow_html=True)
        st.markdown(f"""<span class="skill-tag">React.js</span>""", unsafe_allow_html=True)
    
    with prog_col3:
        st.markdown(f"""<span class="skill-tag">Bash</span>""", unsafe_allow_html=True)
        st.markdown(f"""<span class="skill-tag">HTML/CSS</span>""", unsafe_allow_html=True)
    
    # Additional Projects
    st.markdown('<h2 class="sub-header">Additional Projects</h2>', unsafe_allow_html=True)
    
    # Project 4
    st.markdown('<div class="project-title">DFI Batch Job Scheduler</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-details">', unsafe_allow_html=True)
    st.markdown("**Client:** DFI Corporation")
    st.markdown("**Tools:** AWS Step Functions, Lambda, EventBridge, Python, CloudWatch, Amazon Bedrock")
    st.markdown("""**Key Achievements:**
    • Implemented batch jobs for data extraction and transformation
    • Achieved 99.9% reliability with monitoring and error handling
    • Integrated Vector Database for efficient data retrieval
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 5
    st.markdown('<div class="project-title">Technical Documentation Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-details">', unsafe_allow_html=True)
    st.markdown("**Client:** Internal Tool Development")
    st.markdown("**Tools:** Claude API, Python, Streamlit, RAG Framework, Vector Database")
    st.markdown("""**Key Achievements:**
    • Developed an AI-powered documentation generator
    • Implemented version control for documentation
    • Created templates for high-quality technical content
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Project 6
    st.markdown('<div class="project-title">DevOps Pipeline for Flask Application</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-details">', unsafe_allow_html=True)
    st.markdown("**Client:** Enterprise Solutions Provider")
    st.markdown("**Tools:** Jenkins, Docker, Kubernetes, AWS EKS, Flask, Prometheus, Grafana")
    st.markdown("""**Key Achievements:**
    • Designed a CI/CD pipeline for Flask deployment
    • Established monitoring solutions with Prometheus and Grafana
    • Reduced deployment time by 70% while ensuring performance
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center;">Crafted with Streamlit | ©️ 2025 Rakha Shaik</div>', unsafe_allow_html=True)
