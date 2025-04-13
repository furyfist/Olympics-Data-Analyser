# Olympics Data Analyser

Hi, I'm Furyfist, and I made this project, it is a **Streamlit-based web application** for analyzing Olympics data. It provides insights into medal tallies, athlete performance, and trends over the years using interactive visualizations.

---

## Features

1. **Medal Tally**:
   - View medal tallies by year and country.
   - Filter by specific years or countries.

2. **Overall Analysis**:
   - Key statistics like total editions, cities, sports, events, athletes, and nations.
   - Trends in participating nations, events, and athletes over the years.
   - Heatmap of events across sports and years.
   - List of the most successful athletes.

3. **Country-Wise Analysis**:
   - Medal tally trends for a selected country.
   - Sports in which the country excels (heatmap).
   - Top 10 athletes from the selected country.

4. **Athlete-Wise Analysis**:
   - Age distribution of athletes (overall and medalists).
   - Age distribution across famous sports.
   - Height vs. Weight scatter plot for athletes.
   - Male vs. Female participation trends over the years.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/olympics-data-analyser.git
   cd olympics-data-analyser
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## File Structure

- **`app.py`**: Main Streamlit application.
- **`helper.py`**: Contains helper functions for data processing and analysis.
- **`Preprocessor.py`**: Preprocesses the datasets.
- **`athlete_events.csv`**: Dataset containing athlete data.
- **`noc_regions.csv`**: Dataset mapping NOCs to regions.

---

## Datasets

- **`athlete_events.csv`**: Contains data on athletes, events, and medals.
- **`noc_regions.csv`**: Maps National Olympic Committees (NOCs) to regions.

---

## Visualizations

- Line plots (e.g., trends over years).
- Heatmaps (e.g., events by sport and year).
- Distribution plots (e.g., age distribution).
- Scatter plots (e.g., height vs. weight).

---

## Requirements

- Python 3.7+
- Libraries: `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `scipy`

---

## Contributing

Feel free to fork the repository and submit pull requests for improvements or new features.

---

## License

This project is licensed under the MIT License.
