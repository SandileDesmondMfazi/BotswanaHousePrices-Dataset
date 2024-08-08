# Botswana Property Prices

This repository contains scripts to scrape real estate data from various property listing websites in Botswana, consolidating the data into a single dataset. The goal is to analyze and monitor property price trends in the country.

## Project Structure

- `data/`: Contains the datasets generated from the scraping scripts.
  - `Botswana_Property_Prices.csv`: The consolidated dataset combining data from all three websites.
  - `New_Property24.csv`, `New_ReMax.csv`, `Seeff.csv`: Original datasets from individual websites.

- `notebooks/`: Jupyter notebooks containing the scraping scripts.
  - `scrape_property24.ipynb`: Script to scrape property listings from Property24.
  - `scrape_remax.ipynb`: Script to scrape property listings from ReMax.
  - `scrape_seeff.ipynb`: Script to scrape property listings from Seeff.

## Dataset

The consolidated dataset contains property listing data from three major real estate websites in Botswana:
- **Property24**
- **ReMax**
- **Seeff**

### Features:

- **Title**: The title of the property listing.
- **Location**: The location of the property.
- **Description**: Description of the property.
- **Link**: URL to the property listing.
- **Bedrooms**: Number of bedrooms.
- **Bathrooms**: Number of bathrooms.
- **Parking Spaces**: Number of parking spaces.
- **Erf Size**: Size of the property (if available).
- **Agency**: The real estate agency listing the property.
- **Price**: The price of the property.

## How to Use

1. Clone the repository:
git clone https://github.com/your-username/botswana-property-prices.git

2. Navigate to the repository folder:
cd botswana-property-prices

3. Run the Jupyter notebooks in the `notebooks/` directory to scrape new data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvements.

## Contact

For any inquiries or suggestions, please contact [sandilemfazi12@gmail.com] or open an issue in this repository.