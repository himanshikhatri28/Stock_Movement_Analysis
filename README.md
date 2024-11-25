# Stock_Movement_Analysis
This project is designed to predict stock price movements based on messages scraped from the INTRADAY_JACKPOT_ADDA_TRADING Telegram channel. The channel contains messages that share stock option trading strategies. The project follows these steps:  1. Data Collection 2. ETL Process  3. Machine Learning Model
# STOCK MOVEMENT ANALYSIS BASED ON SOCIAL MEDIA SENTIMENT (USING TELEGRAM DATA)

## Project Description

This project is designed to predict stock price movements based on messages scraped from the **INTRADAY_JACKPOT_ADDA_TRADING** Telegram channel. The channel contains messages that share stock option trading strategies.
The project follows these steps:

1. **Data Collection**: We scarpe relevant messages from the Telegram channel using a Python script
and the **Telethon** library.
2. **ETL Process**: The scraped data is cleaned and transformed to extract useful information, such as Stock indices,options,trigger prices, target prices, and stop losses.
3. **Machine Learning**: A machine learning model is trained to predict stock movements based on the processed data.

-----

## Data Collection

### Raw Data Scraping

The data collection is done using the script **raw_data_scraping.py**, which connects to the **INTRADAY_JACKPOT_ADDA_TRADING** Telegram channel using the **Telethon** library. This script requires you to input your own **API ID**, **API HASH**, and **Phone number** for authentication.

1. **API Credentials**: You need to provide your own **Telegram API ID** and **API HASH**, which you can obtain by registering on the Telegram website.
2. **Phone Number**: You must also input your phone number that is associated with your Telegram account.

### Authentication

After providing your credentials, the script will request a **One-time-code** that is sent to your Telegram Account.
Enter this code into the script to authenticate the ssesion and allow the script to scrape messages from the Telegram channel.

The script then scrapes all relevent messages from the **INTRADAY_JACKPOT_ADDA_TRADIND** channel, filtering messages that contain the keyword **"INDEX OPTION LOVERS"** or **"STOCK OPTION LOVERS"**. The scraped data is saved as a **CSV file** named **'raw_stock_messages.csv'**, which inculdes:
- **Message**: The full message text from the channel.
- **Timestamp**: The timestamp of when the message was sent.

## ETL Process

The **ETL process** is implemented in the script **'ETL_of_raw_scraped_data.py'**, which processes the raw data and extracts useful information.

### Key Features Extracted:

1. **Stock/Index**: Extracts stock or index names such as **BANKNIFTY**, **NIFTY**, **MARUTI**, **MIDCAPNIFTY**, **SENSEX**, and **FINNIFTY**.
2. **Options**: Extracts the stock options in the form of **40000CE**, **40000PE**, etc. If the option has a space between the number and the option type (e.g., `40000 CE`), it is cleaned and formatted correctly.
3. **Trigger Price**: Extracts trigger prices, which are typically prefixed with the keywords **ABOVE** or **NEAR**.
4. **Target Price**: Extracts target prices from messages containing **TRG** followed by the target price value.
5. **Stop Loss**: Extracts stop loss information, which is categorized as **SL Unpaid** or **SL Paid**, depending on the presence of specific keywords in the message.

The **ETL script** transforms the data into a clean, structured format and saves it into the **processed_stock_signals.csv** file. The final dataset includes the following columns: 
- **Stock/Index**
- **Option** 
- **Trigger Price** 
- **Target Price** 
- **Stop Loss** 
- **Message** 
- **Timestamp**

--- 

## Machine Learning Model 

### Model Script: **`hybrid_model_Stock_Movement.py`**

The final step involves using the processed data to train a **Machine Learning model** that predicts stock price movements based on historical data. 

1. **Feature Selection**: The model uses **Trigger Price**,**Target Price**,**option type**,**Option numeric** and 
**Option type Encoded** as input features to predict the **Stop Loss** (whether it is "SL Paid" or "SL Unpaid"). 
2. **Data Splitting**: The dataset is split into a **training set** and a **test set** (70-30 split). 
3. **PCA (Principal Component Analysis)**: PCA is applied to reduce the dimensionality of the data and improve model performance. 
4. **Model**: A **Naive Bayes classifier** is used to train the model on the processed data. 
5. **Model Evaluation**: The model's performance is evaluated using metrics such as **accuracy**, **precision**, **recall**, and **confusion matrix**. 

### Visualization: 

The performance of the model is visualized using a **heatmap confusion matrix** ,**PCA scatter plot** and **Stock movement Prediction line chart** 
--- 

## How to Run the Code 

### Step 1: Set Up Telegram API Credentials 

In the **raw_data_scraping.py** file, input your own **API ID**, **API hash**, and **Phone number**. 

### python
 api_id = "YOUR_API_ID" **Replace with your API ID**
 api_hash = "YOUR_API_HASH"  **Replace with your API hash** 
 phone_number = "YOUR_PHONE_NUMBER" **Replace with your phone number**
 

### Step 2: Install Required Libraries

Install all the required libraries by running the following command in your project directory:

**pip install library_name**


### Step 3: Run the Data Scraping Script

Execute the **raw_data_scraping.py** script to scrape messages from the Telegram channel.


### Step 4: Run the ETL Process

After the data is scraped, execute the **ETL_of_raw_scraped.py** script to process the raw messages and extract relevant features.


### Step 5: Train and Evaluate the Model

Finally, run the **hybrid_model_Stock_Movement.py** to train the machine learning model and evaluate its performance.


### Challenges and Limitations

1. **Data Quality**: The quality of the data depends on how well the Telegram messages follow a consistent format. Any deviation from the expected format can result in missing or incorrect data.

2. **API Limits**: Telegram API limits could restrict the number of messages that can be fetched in a single run.

3. **Keyword Filtering**: The success of the filtering and extraction process relies on the presence of predefined keywords. If the structure of the messages changes, the script might fail to extract the relevant information.

4. **Model Performance**: The performance of the machine learning model is directly impacted by the quality of the data and the number of relevant messages available for training.

---

