import streamlit as st

# Function to display a project
def display_project(title, description, image_path, github_link, live_link):
    st.subheader(title)
    st.image(image_path, use_column_width=True)
    st.write(description)
    github_markdown = f"[GitHub]({github_link})"
    live_link_markdown = f"[Live Link]({live_link})" if live_link else ""
    st.markdown(f"{github_markdown} {'| ' + live_link_markdown if live_link else ''}")
    st.write("---")

def display_certification(name, issuer, issue_date, cert_link):
    st.subheader(name)
    st.write(f"Issuer: {issuer}")
    st.write(f"Issue Date: {issue_date}")
    st.markdown(f"[View Certificate]({cert_link})")
    st.write("---")

# Set up the page
st.set_page_config(page_title="Portfolio", layout="centered")
st.title("My Portfolio")

nav_selection = st.sidebar.radio("Navigation", ["About Me", "Projects", "Skills","Certifications"])

if nav_selection == "About Me":

    st.image("profile.jpg",width=350)
    st.subheader("About Me")
    st.write("""
        👋 Hello! I am **Patel Dhruv Nishesh**, a passionate and driven individual specializing in Data Science, Data Analysis, Machine Learning, and Deep Learning. I am committed to leveraging my analytical skills to uncover actionable insights and contribute to the success of a forward-thinking organization as a data science intern.

        🎓 I hold a **Bachelor of Engineering in Information Technology** from Gujarat Technological University, Gujarat, India, graduating in May 2024 with a **CGPA of 8.81**. My academic journey has equipped me with the technical knowledge and problem-solving abilities essential for tackling complex data challenges.

        🔍 I have hands-on experience in building predictive models, performing comprehensive data analyses, and utilizing various data manipulation techniques. My proficiency in Python, SQL, and various data visualization tools allows me to extract meaningful insights from large datasets.

        🚀 My curiosity and eagerness to learn drive me to stay updated with the latest advancements in technology. I actively engage in continuous learning through online courses, workshops, and by participating in tech communities. I enjoy sharing my knowledge by writing articles and contributing to community discussions, which helps me refine my understanding and connect with like-minded professionals.

        🌟 Outside of my professional pursuits, I am an avid tech enthusiast who loves exploring new tools and technologies. I am particularly interested in the applications of AI and machine learning in solving real-world problems. I also enjoy reading, traveling, and engaging in outdoor activities that allow me to unwind and gain new perspectives.

        🤝 I believe in the power of teamwork and effective communication to drive innovation and achieve collective goals. I am excited about the opportunity to apply my skills and grow as part of a dynamic team. My soft skills include being a hardworking, ambitious, intellectually curious, quick learner, creative thinker, and having an inquisitive mind.

        📬 Feel free to reach out to me for collaboration, networking, or just a chat about the latest in tech!
    """)
    st.subheader("EDUCATION")
    st.write("""
            - Bachelor of Engineering (INFORMATION TECHNOLOGY) \n
            - Gujarat Technological University, Gujarat, India\n
            - May 2024\n
            - CGPA: 8.81 """)
    st.subheader("INTERESTS & HOBBIES")
    st.write("""
        - 📚 **Reading:** I enjoy reading books on technology, psychology, and personal development.
        - 🌍 **Traveling:** I love exploring new places and experiencing different cultures.
        - 🏞️ **Hiking:** I find peace and inspiration in nature, often going on hikes during weekends.
        - 🎮 **Gaming:** I am an avid gamer, enjoying both strategy games and immersive storytelling experiences.
    """)
    st.write("### Connect with me")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DhruvPatel1409) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dhruv-patel-9a4755252) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox)")

elif nav_selection == "Skills":
    st.subheader("Skills")

    st.subheader("Major Skills :rocket:")
    st.write("Python, Tableau, SQL, PostGRE SQL")

    st.subheader(" Python Libraries Known :computer:")
    st.write("Numpy, Pandas, Seaborn, Plotly, Matplotlib, Sci-kit Learn")

    st.subheader(" Front End Skills Known :art:")
    st.write("HTML, CSS, Bootstrap")

    st.subheader(" Soft Skills :bulb:")
    st.write("Hardworking, Ambitious, Intellectually Curious, Quick Learner, Creative Thinker, Inquisitive Mind")

elif nav_selection == "Projects":
    st.subheader("Projects")
    col1, col2 = st.columns(2)

    projects = [
        {
            "title": "CUSTOMER CHURN PREDICTION",
            "description": "My customer churn prediction project leverages machine learning algorithms to analyze historical customer data and predict the likelihood of customer attrition. By utilizing features such as customer demographics, transaction history, and engagement metrics, our model identifies patterns and behaviors indicative of potential churn. Through predictive analytics, we aim to proactively identify at-risk customers and implement targeted retention strategies, thereby minimizing customer loss and maximizing revenue. By continuously refining our predictive models and adapting to evolving customer behaviors, we strive to enhance customer satisfaction and foster long-term relationships, ultimately driving sustainable business growth.",
            "image_path": "cc.png",
            "github_link": "https://github.com/DhruvPatel1409/Customer-Churn-Prediction",
            "live_link": " https://customer-churn-prediction-hbdj2zr4wzfemujd7rbbny.streamlit.app/"
        },
        {
            "title": "RAILWAY RESERVATION SYSTEM",
            "description": "My railway reservation system project, built using Streamlit and SQL, offers a seamless platform for users to manage their train bookings efficiently. With features such as adding trains, viewing train schedules, searching for available trains, booking tickets, and canceling reservations, our system simplifies the entire ticketing process. Users can easily search for trains based on their preferences, view detailed information about train routes and timings, and book tickets hassle-free. The system also allows for easy cancellation of tickets, providing flexibility to users in case of changes in travel plans. By leveraging Streamlit's intuitive interface and SQL database management, we ensure a smooth and user-friendly experience for both passengers and administrators, thereby enhancing the efficiency and reliability of railway ticketing services.",
            "image_path": "Railway-Reservation-System.jpg",
            "github_link": "https://github.com/DhruvPatel1409/Railway-Reservation-System",
            "live_link": "https://railway-reservation-system-w4wph3xmvnywbfimkjdwvw.streamlit.app/"
        },
        {
            "title": "FAKE NEWS DETECTOR",
            "description": "My fake news detector project harnesses the power of machine learning and natural language processing to combat the spread of misinformation. By leveraging advanced ML algorithms and NLP techniques, our system analyzes the linguistic patterns and semantic cues present in news articles to distinguish between genuine and fake news. Through feature extraction and sentiment analysis, the model identifies key indicators of deceptive content, such as sensationalism, biased language, and factual inaccuracies. By providing users with a reliable tool to verify the authenticity of news sources, we empower individuals to make informed decisions and combat the proliferation of misinformation in the digital age.",
            "image_path": "Fake-News.png",
            "github_link": "https://github.com/DhruvPatel1409/Fake-News-Detector",
            "live_link": "https://fake-news-detector-lvjxmvsakkrnrkkeqfxlpd.streamlit.app/"
        },
        {
            "title": "LAPTOP PRICE PREDICTOR",
            "description": "My  laptop price predictor project harnesses the power of machine learning algorithms to accurately estimate the price of laptops based on various features and specifications. By analyzing a diverse dataset of laptops encompassing attributes such as processor speed, RAM capacity, storage size, display resolution, and graphics card type, our model learns to identify patterns and correlations that influence laptop prices. Through advanced regression techniques and feature engineering, we have developed a robust predictive model capable of providing users with reliable price estimates for laptops of different configurations.",
            "image_path": "Railway-Reservation-System.jpg",
            "github_link": "https://github.com/DhruvPatel1409/Laptop-Price-Predictor",
            "live_link": "https://fake-news-detector-lvjxmvsakkrnrkkeqfxlpd.streamlit.app/"
        },
        {
            "title": "CHATBOT",
            "description": "My  chatbot, powered by machine learning algorithms, offers users a personalized and interactive conversational experience. Leveraging natural language processing (NLP) techniques, my chatbot is trained on large datasets of conversations to understand and respond to user queries effectively. With each interaction, the chatbot learns and improves its responses, adapting to the user's preferences and language nuances over time. Whether it's providing customer support, answering frequently asked questions, or engaging users in casual conversation, my chatbot enhances user engagement and satisfaction.",
            "image_path": "chatbot.webp",
            "github_link": "https://github.com/DhruvPatel1409/Chatbot",
            "live_link": "https://chatbot-uwuxfazxuzbzcc8bzrz4et.streamlit.app/"
        },
        {
            "title": "HOUSE PRICE PREDICTION SYSTEM",
            "description": "My  house price prediction project utilizes cutting-edge machine learning techniques to forecast property prices accurately. By leveraging a rich dataset containing key features such as location, square footage, number of bedrooms and bathrooms, amenities, and historical sales data, our model learns intricate patterns and relationships within the housing market. Through advanced regression algorithms and feature engineering, we have developed a robust predictive model capable of providing precise estimates of house prices in various neighborhoods and markets.",
            "image_path": "home.jpeg",
            "github_link": "https://github.com/DhruvPatel1409/House-Price-Prediction",
            "live_link": " https://house-price-prediction-rdk9lx53wjssvsnyctszat.streamlit.app/"
        },
        {
            "title": "CAR PRICE PREDICTION SYSTEM",
            "description": "My car price prediction project leverages machine learning algorithms to forecast the prices of vehicles based on a variety of factors and features. By analyzing a comprehensive dataset containing information such as car make, model, year, mileage, fuel type, engine size, and transmission type, our model learns to recognize patterns and relationships that influence car prices. Through extensive data preprocessing, feature selection, and model training, we have developed a robust predictive model capable of providing accurate estimates of car prices.",
            "image_path": "car_image.jpg",
            "github_link": "https://github.com/DhruvPatel1409/car-price-prediction",
            "live_link": "https://car-price-prediction-gu7hupsucftzoytpsnmqkb.streamlit.app/"
        },
        {
            "title": "MULTIPLE DISEASE PREDICTION SYSTEM",
            "description": "My  chatbot, powered by machine learning algorithms, offers users a personalized and interactive conversational experience. Leveraging natural language processing (NLP) techniques, my chatbot is trained on large datasets of conversations to understand and respond to user queries effectively. With each interaction, the chatbot learns and improves its responses, adapting to the user's preferences and language nuances over time. Whether it's providing customer support, answering frequently asked questions, or engaging users in casual conversation, my chatbot enhances user engagement and satisfaction.",
            "image_path": "disease.jpeg",
            "github_link": "https://github.com/DhruvPatel1409/Multiple-Disease-Prediction-System",
            "live_link" : ""
        },
        {
            "title": "COVID 19 ANALYSIS",
            "description": "My Exploratory Data Analysis (EDA) on the COVID-19 dataset involved a thorough examination of various key aspects, including trends in daily new cases, recoveries, and fatalities across different regions and time periods. Visualizations like line charts, bar graphs, and heatmaps were employed to identify patterns and correlations, such as the impact of government interventions on case numbers and the relationship between population density and infection rates. Additionally, demographic factors like age and comorbidities were analyzed to understand their influence on mortality rates.",
            "image_path": "c19.jpeg",
            "github_link": "https://github.com/DhruvPatel1409/covid19-analysis",
            "live_link" : ""
        },
        {
            "title": "EDA ON WOMEN CLOTHING REVIEWS",
            "description": "My Exploratory Data Analysis (EDA) on the Women Clothing Reviews dataset involved examining various aspects of customer feedback to derive meaningful insights. Key areas of focus included analyzing the distribution of ratings, identifying the most commonly reviewed product categories, and assessing the sentiment of customer reviews. Visualizations such as bar charts and word clouds were used to highlight trends in customer preferences and common themes in positive and negative feedback. This analysis aimed to inform business strategies by identifying areas for improvement in product quality and customer satisfaction.",
            "image_path": "cloth.jpg",
            "github_link": "https://github.com/DhruvPatel1409/EDA-on-women-E-Commerce-Clothing-Reviews",
            "live_link" : ""
        }
        
    ]

    for i, project in enumerate(projects):
        if i % 2 == 0:
            with col1:
                display_project(
                    project["title"],
                    project["description"],
                    project["image_path"],
                    project["github_link"],
                    project["live_link"]
                )
        else:
            with col2:
                display_project(
                    project["title"],
                    project["description"],
                    project["image_path"],
                    project["github_link"],
                    project["live_link"]
                )

else:
    st.subheader("Certifications")
    
    certifications = [
        {
            "name": "Learn python by doing real world projects from scratch ",
            "issuer": "Udemy",
            "issue_date": "May 2024",
            "cert_link": "https://www.udemy.com/certificate/UC-279f4d03-f9df-47b0-908a-bccb551a2b9a/"
        },
        {
            "name": "Python for data science and ML : zero to hero",
            "issuer": "Udemy",
            "issue_date": "March 2023",
            "cert_link": "https://www.udemy.com/certificate/UC-bede24b0-6d8b-4a6f-b528-ff406464cd06/"
        },
        {
            "name": "Machine learning using python",
            "issuer": "Udemy",
            "issue_date": "January 2024",
            "cert_link": "https://www.udemy.com/certificate/UC-40dfb7f7-e395-4479-85e4-f189db1b7c28/"
        },
        {
            "name": "Machine Learning basics in hindi - Regression analysis",
            "issuer": "Udemy",
            "issue_date": "August 2023",
            "cert_link": "https://www.udemy.com/certificate/UC-25504ac6-22de-4aca-9732-8dbf4308c7e2/"
        },
        {
            "name": "Seaborn - Mastering data visualisation with seaborn",
            "issuer": "Udemy",
            "issue_date": "November 2023",
            "cert_link": "https://www.udemy.com/certificate/UC-13a09141-84a6-4112-8aec-599d3b012597/"
        },
        {
            "name": "Statistics and Hypothesis Testing for Data Science",
            "issuer": "Udemy",
            "issue_date": "May 2024",
            "cert_link": "https://www.udemy.com/certificate/UC-fe8ed573-a649-429c-b260-593ee4bd4a31/"
        },
        {
            "name": "Complete Railway Reservation System Using Sqlite and Streamlit",
            "issuer": "Udemy",
            "issue_date": "March 2024",
            "cert_link": "https://www.udemy.com/certificate/UC-d6d99728-5579-4fd4-9c32-79c450b6560f/"
        },
        {
            "name": "CHATBOT USING MACHINE LEARNING ",
            "issuer": "Udemy",
            "issue_date": "April 2024",
            "cert_link": "https://www.udemy.com/certificate/UC-72cd0aa2-331e-420a-94db-93c83bc98e19/"
        }
    ]
    
    for cert in certifications:
        display_certification(
            cert["name"],
            cert["issuer"],
            cert["issue_date"],
            cert["cert_link"]
        )
