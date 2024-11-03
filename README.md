# Tiger-Hacks-2024
Submission for Tiger Hacks 2024: Theme Food and Agriculture


# Nutrient Scan
Nutrient Scan is a web app that displays nutritional information from scanning UPCs in a visually appealing way, featuring graphs and allergen warnings.

## Inspiration
We wanted to make it easy to check for specific allergens or quickly see macronutrients in food products.

## How We Built It
We built Nutrient Scan using the following technologies:
- **Django**: Our primary web framework.
- **Pillow** and **pyzbar**: Python libraries used to scan barcodes from uploaded images.
- **Grafana**: For displaying infographics related to nutrients and allergen warnings.
- **HTML/CSS**: Raw HTML and CSS for the frontend design.
- **Nginx**: Used as the web server.
- **Docker**: The entire application is containerized for ease of deployment.

## Challenges We Ran Into
This was the first experience with Django for all team members, and for many, it was also their first time using Docker and Grafana. Navigating these new technologies presented a learning curve.

## Accomplishments That We're Proud Of
- Successfully implementing Python libraries to scan and process images uploaded to the website.
- Integrating an API for searching UPCs to retrieve product information.
- Created a user-friendly interface using CSS and HTML.

## What We Learned
Our team gained valuable knowledge in:
- Web development and frontend design.
- Working with SQLite3, Grafana, Nginx, Docker, Pillow, and pyzbar.
- Utilizing Django for building robust web applications.

## What's Next for Nutrient Scan
We would plan to introduce several exciting features, including:
- A recommendation system for alternative foods that are similar to the searched product but free from specified allergens or ingredients.
- User account functionality, allowing users to store previous searches and save nutritional information for future reference.

## Installation and Setup
To run Nutrient Scan locally, follow these steps:

### Prerequisites
- **Docker** and **Docker Compose** must be installed on your machine. You can download them from the official [Docker website](https://www.docker.com/get-started).


1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/nutrient-scan.git
   cd nutrient-scan
2. **Configure Environment Variables:**
   Place your api key into
   ```
   ocr_nutrition_app/NutritionApp/api/api_key.txt
3. **Run Docker Compose**
   ```bash
   docker compose up --build 
5. **Access the Application**
- By default this would be http://localhost:9420
