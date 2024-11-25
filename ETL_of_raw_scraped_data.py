# Import necessary libraries
import pandas as pd
import re

# Load the raw data from the CSV file
df = pd.read_csv('c:/Users/Macbook/Desktop/ml stock project/raw_stock_messages.csv')

# Initialize lists to store processed data
stock_indices = []
options = []
trigger_prices = []
target_prices = []
stop_losses = []
timestamps = df["Timestamp"]
messages = df["Message"]

# Process each message to extract relevant information
for message in df['Message']:
    
    # Extract Stock/Index name
    stock_match = re.search(r"(BANKNIFTY|NIFTY|FINNIFTY|MARUTI|MIDCAPNIFTY|SENSEX)", message, re.IGNORECASE)
    stock_indices.append(stock_match.group(0) if stock_match else "Unmatched")
    
    # Extract option type and strike price
    option_match = re.search(r"(\d+)\s*(CE|PE)", message, re.IGNORECASE)
    options.append(option_match.group(0) if option_match else "Unmatched")
    
    # Extract tigger price
    trigger_match = re.search(r"\b(?:ABOVE|NEAR)\s+(\d+)", message, re.IGNORECASE)
    trigger_prices.append(trigger_match.group(1) if trigger_match else "Unmatched")
    
    # Extract Target price
    target_match = re.findall(r"TRG[-\s/]*(\d+)", message, re.IGNORECASE)
    if target_match:
        target_prices.append(target_match[0])
    else: 
        target_prices.append("Unmatched")
    
    # Extract Stop Loss details
    stop_loss_match = re.search(r"SL[-\s]*(\d+)", message, re.IGNORECASE)
    if stop_loss_match:
        stop_losses.append("SL Unpaid")
    elif re.search(r"SL\s+PAID", message, re.IGNORECASE):
        stop_losses.append("SL Paid")
    else:
        stop_losses.append("Unmatched")

# Create a DataFrame with the processed data
processed_df = pd.DataFrame({
    "Stock/Index" : stock_indices,
    "Option" : options,
    "Trigger Price" : trigger_prices,
    "Target price": target_prices,
    "Stop Loss" : stop_losses,
    "Message" : messages,
    "Timestamp" : timestamps
})

# Remove duplicate messages
processed_df = processed_df.drop_duplicates(subset=['Message'], keep = 'first')

# Save the processed data to a CSV file
processed_df.to_csv('c:/Users/Macbook/Desktop/ml stock project/processed_stock_signals.csv',index = False)

print("Data processed complete. Saved to 'processed_stock_signals.csv'.")