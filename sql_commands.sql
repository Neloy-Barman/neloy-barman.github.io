
-- Educational Details 
drop table if exists educational_details;

create table educational_details(
	id serial primary key,
	degree character varying(100) not null,
	institution character varying(100) not null,
	start_year integer,
	end_year integer,
	base_result numeric(10, 2) not null,
	result numeric(10, 2) not null
);

insert into educational_details(degree, institution, start_year, end_year, base_result, result)
values('Bachelor of Science in Computer Science and Engineering', 'Ahsanullah University of Science & Technology', 2018, 2023, 4.00, 3.542);

insert into educational_details(degree, institution, start_year, end_year, base_result, result)
values('Secondary Secondary Certificate', 'Narayanganj Ideal School', null, 2016, 5.00, 5.00);

select * from educational_details;



-- Professional Details Table
drop table if exists professional_details;

create table professional_details(
	id serial primary key,
	company character varying(100) not null,
	position character varying(100) not null,
	web_url character varying(100) not null,
	start_month character varying(10) not null,
	start_year integer,
	end_month character varying(10) not null,
	end_year integer,
	responsibilities text not null
);

insert into professional_details(company, position, web_url, start_month, start_year, end_month, end_year, responsibilities)
values('Gravitas AI', 'Chatbot Developer', 'https://www.gravitas.ai/', 'July', 2024, '', null, '');

insert into professional_details(company, position, web_url, start_month, start_year, end_month, end_year, responsibilities)
values('Karnaphuli Jewellery Trading LLC', 'Associate Flutter Developer', 'https://karnaphulijewellery.com/', 'July', 2023, 'October', 2023, 'Implementation of pixel-perfect user interface design~Collaboration with the existing codebase and debugging errors.~Integration of RESTful API endpoints and employment of state management using Provider.');

select * from professional_details;



-- Interest Details
drop table if exists interest_details;

create table interest_details(
	id serial primary key,
	interest character varying(100) not null,
	icon character varying(50),
	color character(7) not null
);

insert into interest_details(interest, icon, color)
values('Data Analysis', 'ri-bar-chart-box-line', '#FF0000');

insert into interest_details(interest, icon, color)
values('Machine Learning', null, '#0000FF');

select * from interest_details;



-- Project Details 
drop table if exists projects;

create table projects(
	id serial primary key,
	title character varying(100) not null,
	project_class character varying(50) not null, 
	project_type character varying(50) not null, 
	tech_stack text not null,
	github_url character varying(100) not null,
	website_url character varying(100),
	video_demo character varying(100) ,
	tableau_dashboard character varying(100),
	image_url character varying(100) not null,
	description text not null
);

insert into projects(title, project_class, project_type, tech_stack, github_url, website_url, video_demo, tableau_dashboard, image_url, description)
values('An Interpretable Bengali Fish Recognizer', 'Machine Learning', 'Individual', 'Language: Python~Libraries: Matplotlib, FastAI, Grad-CAM, HuggingFace~IDE: VS Code~Notebook: Google Colab', 'https://github.com/Neloy-Barman/Interpretable-Bengali-Fish-Recognizer', 'https://neloy-barman.github.io/Interpretable-Bengali-Fish-Recognizer/', 'https://www.linkedin.com/feed/update/urn:li:activity:7154152192059293696/', null, '', 'I collected images for 20 different fishes that mostly get sold in bengali fish markets using fastai’s search and download methods. Then I cleaned the data using fastai vision’s cleaner widgets. I prepared the dataloader with a batch size of 32. DenseNet-121, VGG-19 and ResNet-50 were chosen as the learner models based on my previous research experience. Then I trained them using fastai’s fine_tune() and fit_one_cycle() both methods. ResNet-50 showed the best performance. To find out the important regions for the predictions, I applied Grad-CAM, an XAI approach on all the models. Lastly I deployed the best model to huggingface and created a website integration using github pages.');

insert into projects(title, project_class, project_type, tech_stack, github_url, website_url, video_demo, tableau_dashboard, image_url, description)
values('DeshiEats', 'Web App', 'Collaborative', 'Language: HTML, PHP~Styling: CSS, Bootstrap~IDE: VS Code', 'https://github.com/Neloy-Barman/DeshiEats', null, null, null, '', 'I have actively participated in a group project during my academic journey, where we developed a comprehensive website catering to both users acting as chefs and customers. The website encompasses the perspectives of both roles, allowing users to register and create their individual profiles. Chef users are empowered to showcase their menus and establish appropriate pricing for their culinary offerings. On the other hand, customers can explore various chef profiles and conveniently place orders for their desired food services. My specific contribution to the project involved dedicating half of my efforts towards front-end design enhancements, aimed at providing users with an enhanced visual experience.');

select * from projects;
