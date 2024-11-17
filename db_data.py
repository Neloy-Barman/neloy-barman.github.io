
# Personal Details
personal_details = {
    'name': 'Neloy Barman',
    'profile_pic_url': '',
    'email': 'neloycareer018@gmail.com',
    'phone_number': '+8801708708167',
    'city': 'Narayanganj',
    'province': 'Dhaka',
    'country': 'Bangladesh',
    'intro': 'Hello, I’m Neloy. I obtained my bachelor of science degree in computer science and engineering with a CGPA of 3.542 from Ahsanullah University of Science and Technology. During my academic pursuits, I have worked on various types of projects both individually and collaboratively. Now, I am looking forward to pursuing a career in machine learning. I have hands-on experience in data science tools such as, pandas, sklearn and deep learning libraries such as pytorch, tensorflow, fastai and others. I already completed some promising ML projects. I think my strong work ethic, collaborative nature, and eagerness to gain further practical experience will contribute to my professional growth and ensure fruitful contributions to future endeavors. For now, I’m exploring more of this huge field.',
    'github_url': 'https://github.com/Neloy-Barman',
    'linked_in': 'https://www.linkedin.com/in/neloy-barman/',
    'kaggle': 'https://www.kaggle.com/neloybarman018',
    'leet_code': 'https://leetcode.com/u/neloycareer018/',
}


# Interest Details
interest_details = [
    (
        'Data Analysis',
        'ri-bar-chart-box-line',
        '#FF0000'
    ),
    (
        'Machine Learning',
        'ri-database-2-line',
        '#0000FF'
    ),
    (
        'Computer Vision',
        'ri-camera-3-line',
        '#FF0000'
    ),
    (
        'Natural Language Processing',
        'ri-english-input',
        '#0000FF'
    ),
    (
        'Mobile Application',
        'ri-smartphone-line',
        '#FF0000'
    ),
    (
        'Software Development',
        'ri-global-line',
        '#0000FF'
    ),
]


# Professional Experience
professional_details = [
      (
        'Gravitas AI',
        'Chatbot Developer',
        'https://www.gravitas.ai/',
        'July',
        2024,
        '',
        Null,
        ''
    ),
    (
        'Mastercourse Bangladesh',
        'Trainee Machine Learning Engineer',
        'https://mastercourse.site/',
        'October',
        2023,
        'March',
        2024,
        'Dataset creation using web scraping.~Performing data cleaning, visualization and data analysis using required tools such as pandas, numpy, tableau and others.~Choosing machine learning models for dataset, training on them and performance evaluation.~Deployment of ml models to open-source platforms and intigration to website.'
    ),
    (
        'Karnaphuli Jewellery Trading LLC',
        'Associate Flutter Developer',
        'https://karnaphulijewellery.com/',
        'July',
        2023,
        'October',
        2023,
        'Implementation of pixel-perfect user interface design~Collaboration with the existing codebase and debugging errors.~Integration of RESTful API endpoints and employment of state management using Provider.'
    )
]




# Educational Data
educational_details = [
    (
        'Bachelor of Science in Computer Science and Engineering',
        'Ahsanullah University of Science & Technology',
        2018,
        2023,
        4.00,
        3.542
    ),
    (
        'Higher Secondary Certificate',
        'Engineering University School & College',
        2016,
        2018,
        5.00,
        5.00
    ),
    (
        'Secondary Secondary Certificate',
        'Narayanganj Ideal School',
        NULL,
        2016,
        5.00,
        5.00
    ),
]



# Project Detailed Data
project_details = [
    # An Interpretable Bengali Fish Recognizer
    (
        'An Interpretable Bengali Fish Recognizer', 
        'Machine Learning', 
        'Individual', 
        'Language: Python~Libraries: Matplotlib, FastAI, Grad-CAM, HuggingFace~IDE: VS Code~Notebook: Google Colab', 
        'https://github.com/Neloy-Barman/Interpretable-Bengali-Fish-Recognizer', 
        'https://neloy-barman.github.io/Interpretable-Bengali-Fish-Recognizer/', 
        'https://www.linkedin.com/feed/update/urn:li:activity:7154152192059293696/', 
        '', 
        '', 
        'I collected images for 20 different fishes that mostly get sold in bengali fish markets using fastai’s search and download methods. Then I cleaned the data using fastai vision’s cleaner widgets. I prepared the dataloader with a batch size of 32. DenseNet-121, VGG-19 and ResNet-50 were chosen as the learner models based on my previous research experience. Then I trained them using fastai’s fine_tune() and fit_one_cycle() both methods. ResNet-50 showed the best performance. To find out the important regions for the predictions, I applied Grad-CAM, an XAI approach on all the models. Lastly I deployed the best model to huggingface and created a website integration using github pages.'
    ),
    # Scientific Papers Keywords Categorization
    (
        'An Interpretable Bengali Fish Recognizer', 
        'Machine Learning', 
        'Individual', 
        'Language: Python~Libraries: Selenium, Pandas, FastAI, Blurr, HuggingFace, ONNX, Flask~IDE: VS Code~Notebook: Google Colab', 
        'https://github.com/Neloy-Barman/Scientific-Paper-Keywords-Categorization', 
        'https://scientific-paper-keywords-categorization.onrender.com/', 
        'https://www.linkedin.com/feed/update/urn:li:activity:7158861904692539393/', 
        '', 
        '', 
        'I decided to perform a multi-label classification task. The main goal is to categorize some optimized keywords based on papers abstract to show the paper to the relatable users. That''s why I scraped IEEE. I fetched papers abstract and the keywords. Then I performed data cleaning and data preprocessing parts to feed transformers. I choose BERT, DistilBERT and RoBERTa as the learners. After haivng trained, the BERT showed a better performance than others. As the model was larger in size, I compressed the model using ONNX and it costs slightly decreasing performancce. I deployed the model to huggingface. Lastly, I created a website from scratch using flask and integrated the model api.'
    ),
    # An XAI based OSCC Detection System
    (
        'An XAI based OSCC Detection System', 
        'Machine Learning', 
        'Collaborative', 
        'Language: Python~Libraries: Keras, TensorFlow, Scikit-Learn, Grad-CAM, LIME~Notebook: Google Colab', 
        'https://github.com/Neloy-Barman/XAI-OSCC-Detection', 
        '', 
        '', 
        '', 
        '',
        'During our thesis work, our focus was on binary classification for the detection of Oral Squamous Cell Carcinoma in histopathological images. Drawing upon relevant research papers, we implemented state-of-the-art techniques to achieve compelling results. We used some CNN based models such as VGG-16, DenseNet-121, InceptionV3 and others. Each model exhibited distinct performance characteristics, yielding varying outcomes across different scenarios. To enhance the interpretability of our models and gain insights into their decision-making processes, we incorporated several explainable Artificial Intelligence (XAI) methods. Notably, we deployed techniques such as LIME, Score-CAM, and others. With the successful outcomes of our research, we are enthusiastic about the prospect of publishing a relevant paper. By sharing our methodologies and significant findings, we aim to contribute to the scientific community''s knowledge base.'
    ),
    # Daraz 11.11 Top Selling Product Data Analysis
    (
        'Daraz 11.11 Top Selling Product Data Analysis', 
        'Data Analysis', 
        'Individual', 
        'Language: Python~Libraries: Selenium, Pandas, Matplotlib~IDE: VS Code~Analysis App: Tableau', 
        'https://github.com/Neloy-Barman/Daraz-11.11-Top-Selling-Product-Data-Analysis', 
        '', 
        'https://www.linkedin.com/feed/update/urn:li:activity:7149069888232243200/', 
        'https://public.tableau.com/app/profile/neloy.barman/viz/Daraz11_11TopSellingProductDataAnalysis/analysis_on_overall_data', 
        '', 
        'I scraped a tiny portion of the top selling product data from the sale for each category as well as its subcategories using a web scraper created using selenium. Then merging all the data container csv files, I performed data cleaning. I exported the final data and performed EDA using pandas & created data visualization using matplotlib. Finally, I proceed to the dashboard creation using Tableau to make the analysis visual.'
   ),
   # Goodreads Book Data Analysis
   (
        'Goodreads Book Data Analysis', 
        'Data Analysis', 
        'Individual', 
        'Language: Python~Libraries: Selenium, Pandas, Matplotlib~IDE: VS Code~Analysis App: Tableau', 
        'https://github.com/Neloy-Barman/Goodreads-Book-Data-Analysis', 
        '', 
        '', 
        'https://public.tableau.com/app/profile/neloy.barman/viz/GoodreadsBookDataAnalysis/author__book_data', 
        '',
        'In the website, there are many lists of books. So, I selected 6 lists and decided to scrape data. Then inspecting the web elements properly, I created web scrapers using selenium. After scraping the data, I did necessary merging and performed data cleaning and data manipulation part. These results in a final and cleaned dataset. Lastly, I created some interactive dashboard to perform data analysis part using tableau.'
   ),
   # OSCC Detector
   (
        'OSCC Detector', 
        'Mobile App', 
        'Individual', 
        'Language: Flutter & Dart~Packages: Tensorflow Lite, Provider, Image Picker, Camera', 
        'https://github.com/Neloy-Barman/OSCC-Detector-App', 
        '', 
        '', 
        '', 
        '',
        'I have developed a mobile application that serves as a condensed implementation of my undergraduate thesis work. This application enables users to capture real-time images or upload images from their gallery. By leveraging an integrated model, the app performs image classification to determine the presence of cancerous cells. Additionally, the app provides comprehensive information on cancerous and non-cancerous cell characteristics. This project showcases the ability to combine advanced machine learning techniques with mobile application development, contributing to the field of medical diagnostics.'
   ),
   # Bone Fracture Classifier
   (
        'Bone Fracture Classifier', 
        'Machine Learning', 
        'Collaborative', 
        'Language: Python~Libraries: Keras, TensorFlow, Scikit-Learn, Grad-CAM, LIME~Notebook: Google Colab', 
        'https://github.com/Neloy-Barman/Bone-Fracture-Classification-System', 
        '', 
        '', 
        '', 
        '',
        'Within the context of an academic project, we leveraged the MURA dataset, specifically curated for bone fractures. By thoroughly studying relevant papers, we acquired valuable insights and implemented techniques aligned with our objectives, focusing on Convolutional Neural Network (CNN) models. Our aim was to construct a robust classification system capable of detecting fractures while identifying the corresponding bone region within the body. Furthermore, we employed XAI (Explainable Artificial Intelligence) techniques, including Grad-CAM and Grad-CAM++, to enhance interpretability and provide insights into the decision-making process. Although our initial results did not meet our desired level of satisfaction, we remain committed to further exploration and experimentation, aiming to apply alternative approaches that hold promise for improving the overall performance and accuracy of our fracture detection system.'
   ),
   # Mobile Price Predictor
   (
        'Mobile Price Predictor', 
        'Machine Learning', 
        'Collaborative', 
        'Language: Python~Libraries: Pandas, Numpy, Scikit-Learn~Notebook: Google Colab', 
        'https://github.com/Neloy-Barman/Machine_learning/tree/main/Mobile_price_prediction', 
        '', 
        '', 
        '', 
        '',
        'This is a project from 4th year 1st semester Artificial Intelligence based on traditional machine learning models for regression problems.'
   ),
   # Football Club Management System
   (
        'Football Club Management System', 
        'Database', 
        'Collaborative', 
        'Language: Java, MSSQL~IDE: IntelliJ IDEA~RDBMS: MS SQL Server', 
        'https://github.com/Neloy-Barman/FCMS', 
        '', 
        'https://www.youtube.com/watch?v=zJW6YVEsldU', 
        '', 
        '',
        'During our 3rd year 2nd semester, me with my 2 teammates developed this relational database management system imagining it for a football club. I developed the whole database schema using mssql. It involves players info addition, deletion and manipulation. Managing the match shedules and organizing team based on that, positioning players according to the formations. If the club wants to sell or buy new players, then it''s also possible. Other than that, it includes the staffs and coaches management. My other teammates handeled the database integration to a computer application and make it visually more appealing to the users.'
   ),
   # Style Loop
   (
        'Style Loop', 
        'Mobile App', 
        'Individual', 
        'Language: Flutter & Dart~Packages: Dotted Line, Curved Navigation Bar, Badges', 
        'https://github.com/Neloy-Barman/Clothing-Design-App', 
        '', 
        '', 
        '', 
        '',
        'An e-commerce mobile app with an exquisite UI/UX design. Leveraging Flutter and Dart, I have meticulously transformed a collected UI resource into a functional code structure, encompassing valuable screens tailored for an exceptional shopping experience. Currently in the backend development phase, I am working towards enriching the app with real-time user interaction capabilities, facilitated by REST APIs such as Firebase. This integration will empower the app with its own database, ensuring seamless data management.'
   ),
   # A Banking App interface
   (
        'A Banking App interface', 
        'Mobile App', 
        'Individual', 
        'Language: Flutter & Dart~Packages: Font Awesome Icon, Dropdown', 
        'https://github.com/Neloy-Barman/Bank-App', 
        '', 
        '', 
        '', 
        '',
        'I have successfully implemented a visually stunning bank app user interface utilizing Flutter and Dart. The design, which I obtained from Freepik, showcases seamless Sign Up, Home, and Transaction History screens, among others. By employing dummy data, I have created a functional frontend with navigation capabilities. As part of my future plans, I intend to develop a robust backend system complete with a REST API to enhance the app''s functionality and provide real-time data.'
   ),
   # DeshiEats
   (
        'DeshiEats', 
        'Web App', 
        'Collaborative', 
        'Language: HTML, PHP~Styling: CSS, Bootstrap~IDE: VS Code', 
        'https://github.com/Neloy-Barman/DeshiEats', 
        '', 
        '', 
        '', 
        '',
        'I have actively participated in a group project during my academic journey, where we developed a comprehensive website catering to both users acting as chefs and customers. The website encompasses the perspectives of both roles, allowing users to register and create their individual profiles. Chef users are empowered to showcase their menus and establish appropriate pricing for their culinary offerings. On the other hand, customers can explore various chef profiles and conveniently place orders for their desired food services. My specific contribution to the project involved dedicating half of my efforts towards front-end design enhancements, aimed at providing users with an enhanced visual experience.'
  )
]

