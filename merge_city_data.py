import pandas as pd
import os

# My working directory path
data_dir = 'C:/Users/Aryan/Desktop/Python'

# Mapping  city names to CSV file names
city_files = {
    'Mumbai': 'mumbai.csv',
    'Bangalore': 'bangalore.csv',
    'Chennai': 'chennai.csv',
    'Hyderabad': 'hyderabad.csv'
}

# Initialize an empty DataFrame
combined_df = pd.DataFrame()

# Loop through each file and append city column
for city, filename in city_files.items():
    file_path = os.path.join(data_dir, filename)
    try:
        df = pd.read_csv(file_path)

        # Add a 'City' column
        df['City'] = city

        # Append to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)
        print(f"Loaded and added: {filename}")
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
    except Exception as e:
        print(f"⚠️ Error reading {filename}: {e}")

# Save the final merged CSV
output_file = os.path.join(data_dir, 'combined_city_data.csv')
combined_df.to_csv(output_file, index=False)
print(f"\n✅ Combined dataset saved as: {output_file}")
print(f"🧾 Final dataset shape: {combined_df.shape}")
print("📌 Columns:", combined_df.columns.tolist())
