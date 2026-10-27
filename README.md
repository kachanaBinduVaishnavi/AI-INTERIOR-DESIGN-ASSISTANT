AI Interior Design Assistant

An AI-powered web application that provides personalized interior design recommendations based on room images, room type, preferred design style, and budget.

Overview

The AI Interior Design Assistant helps users explore interior design ideas for different spaces, such as bedrooms, living rooms, kitchens, and dining rooms. It combines a Flask web application with AI model integration to analyze room images and assist in generating design suggestions.

Features

- Room Image Upload:** Upload images of existing rooms for analysis.
- AI-Powered Room Analysis:** Use an AI vision model to analyze room images.
- Personalized Design Recommendations:** Get suggestions based on room type, design style, and budget.
- Multiple Interior Styles:** Explore styles such as Modern, Traditional, Minimalist, Luxury, and Bohemian.
- Budget-Based Suggestions:** Provide a budget to guide the design recommendations.
- Design History:** Store and view previous design requests using SQLite.
- Interactive Web Interface:** Access the application's functionality through a Flask-based web interface.

Technologies Used

| Technology | Purpose |

| Python | Application logic |
| Flask | Backend web framework |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| Ollama with LLaVA | Local AI model integration |
| SQLite | Design history storage |
| Git and GitHub | Version control and source code hosting |


Project Structure

AI-INTERIOR-DESIGN-ASSISTANT/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── uploads/
├── templates/
│   ├── history.html
│   ├── index.html
│   └── result.html
├── utils/
│   ├── database.py
│   ├── image_analyzer.py
│   └── image_generator.py
├── .gitignore
└── README.md
