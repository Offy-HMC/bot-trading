from iqoptionapi.stable_api import IQ_Option
import time

# config
email = "ssrivattanasup@gmail.com"
password = "c#nQ9S*2Ces?ru%"
acc_type = "PRACTICE"

asset = "EURUSD-OTC"
amount = 100  # Trade amount
direction = "put"  # "call" for UP, "put" for DOWN
duration = 1  # Duration in minutes

# init information
print("IQ-Option Bot V.1.0 by OffyOk")
print("Hi there, Here R Offy Bot Trade for IQ option")
print("Contact Line ID: offyok")
print("--------------------------------------------")

# Initialize API
api = IQ_Option(email, password)
api.connect()


# Check if the connection is successful
if api.check_connect():
    print("Successfully connected!")
    print(f"API Version: ")
    print("--------------------------------------------")
else:
    print("Failed to connect. Check your credentials.")
    exit()

# Set account type to PRACTICE
api.change_balance(acc_type)

# show config information
print("-- Information --")
print(f"Email: {email}")
print(f"Time frame: ")
print(f"Target (USD): ")
print(f"Stoploss (USD): ")
print("--------------------------------------------")

# List asset is open ?
def check_asset():
    assets = api.get_all_open_time()
    print("Available assets:", assets)

# Function to check balance
def get_balance():
    balance = api.get_balance()
    print(f"Current Balance: {balance}")
    return balance




# Function to place a trade
def place_trade(asset_pt, direction_pt, amount_pt, duration_pt, round_pt):
    status, trade_id = api.buy(amount_pt, asset_pt, direction_pt, duration_pt)
    if status:
        print(f"Round: {round_pt}")
        print(f"Trade placed: {trade_id}")
        print(f"Asset: {asset_pt}")
        print(f"Signal: {direction_pt}")
        print(f"Trading amount: {amount_pt}")
        print("--------------------------------------------")
        print("wait trading result for 1 minute")
    else:
        print("Failed to place trade")

    time.sleep(duration * 60)
    check_result(trade_id)

# Check trade result
def check_result(id):
    result = api.check_win_v3(id)
    if result > 0:
        print("--------------------------------------------")
        print(f"Mode: {acc_type}")
        print(f"Win Rate: ")
        print(f"Continue win: ")
        print(f"Continue loss: ")
        print(f"Profit: {result}")
        get_balance()
        print(f"Result: -- Win --")
        print("--------------------------------------------")
    elif result < 0:
        print("--------------------------------------------")
        print(f"Mode: {acc_type}")
        print(f"Win Rate: ")
        print(f"Continue win: ")
        print(f"Continue loss: ")
        print(f"Profit: {-result}")
        get_balance()
        print(f"Result: -- Loss --")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(f"Mode: {acc_type}")
        print(f"Win Rate: ")
        print(f"Continue win: 0")
        print(f"Continue loss: 0")
        print(f"Profit: 0")
        get_balance()
        print(f"Result: -- Tie --")
        print("--------------------------------------------")

# Main trading logic
def trade_bot():
    round = 1
    while True:
        # Example: Place a call trade
        print("Placing trade...")
        place_trade(asset, direction, amount, duration,round)
        round +=1

if __name__ == "__main__":
    get_balance()
    trade_bot()



