## Flask Weather App with 3D Scenes ☁️✨

This Flask application displays the current weather conditions and a corresponding 3D weather scene for a user-specified location.

**Features:**

* Retrieves weather data using OpenWeatherMap API
* Displays weather information (temperature, description, icon)
* Integrates 3D weather scenes based on weather conditions (under development)

**Technologies:**

* Flask
* OpenWeatherMap API (API Key Required)
* Spline 3D viewer (optional)

**Setup:**

1. Create a virtual environment and install Flask:

   ```bash
   python -m venv venv
   source venv/bin/activate (or venv\Scripts\activate on Windows)
   pip install Flask
   ```

2. (Optional) Install Spline 3D viewer:

   ```bash
   npm install @splinetool/viewer
   ```

3. Replace `'your_api_key'` in `weather.py` with your OpenWeatherMap API key.

4. Run the application:

   ```bash
   python app.py
   ```

**How it Works:**

The application uses Flask to handle user requests and render HTML templates. The weather data is retrieved from the OpenWeatherMap API using the `weather.py` module. The retrieved data is then used to display the weather information and conditionally load the corresponding 3D scene using Spline.

**Note:**

* The 3D scene selection logic is currently under development and might require further refinement.
* Consider storing the API key securely using environment variables.

**Further Improvements:**

* Implement error handling for API calls.
* Enhance the 3D scene selection based on weather conditions.

This project provides a foundation for building interactive weather applications with Flask and 3D visualizations. Feel free to explore and customize it further!
