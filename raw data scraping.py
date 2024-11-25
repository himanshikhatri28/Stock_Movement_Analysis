# Import necessary libraries
from telethon import TelegramClient # library for interacting with the Telegram API
import pandas as pd 

# Promt the user to input their Telegram API credentials at runtime
api_id =  input("Enter your API ID: ") 
api_hash = input("Enter your API Hash: ") 
phone_number = input("Enter your phone number (with country code (eg: +91)): ") 

# Define a session name for the Telegram client
session_name = 'Stock_Scraping'

# Initialize the Telegram client with the session name, API ID and API Hash
client = TelegramClient(session_name,api_id,api_hash)

# define the main asynchronous function for scraping data
async def main():
    # Start the Telegram client and authenticate with your phone number
    await client.start(phone_number)
    
    # Specify the Telegram channel link you want to scrape messages from
    # This code is specifically designed to scrape messages from the 'INTERDAY JACKPOT ADDA TRADING' channel.
    # The filters below are set to capture messages with specific keywords that are common in this channel.
    channel_invite_link = 'https://t.me/INTRADAY_JACKPOT_ADDA_TRADING'
    channel = await client.get_entity(channel_invite_link)

    print(f"Connected to channel: {channel.title}") 

    # Fetch up to 5000 most recent messages from the channel
    messages = await client.get_messages(channel, limit=5000)
    
    # Initialize an entity list to store relevant messages
    data = []

    # Loop through the fetched messages
    for message in messages:
        # Fetching messages based on the filters (only relavent for this channel)
        if message.text and (
            "INDEX OPTION LOVERS" in message.text or # Keyword filter 1
            "STOCK OPTION LOVERS" in message.text # Keyword filter 2
        ):

           # If the message matches, add it to the list along with its timestamp
           data.append({
            'Message': message.text.strip(), # Store the cleaned message text
            'Timestamp' : message.date       # Store the message timestamp
           })
    
    # Convert the collected data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Check if the Dataframe is not empty
    if not df.empty:
        # Save the DataFrame to a CSV file
        df.to_csv('c:/Users/Macbook/Desktop/ml stock project/raw_stock_messages.csv',index = False)
        print("All relevant messages saved to 'raw_stock_messages.csv'")
    else:
        print("No relevant messages found.") 
 
    # Disconnect the Telegram client after scraping
    await client.disconnect()

# Run the main asynchronous function to execute the scraping process
client.loop.run_until_complete(main())