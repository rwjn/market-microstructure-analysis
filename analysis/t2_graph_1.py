# Set up the chart
fig, ax = plt.subplots()

# Calculate mid and micro prices using my custom functions
mid_price = calculate_mid_price(g1_data['bid_price'], g1_data['ask_price'])
micro_price = calculate_micro_price(g1_data['bid_price'], g1_data['bid_quantity'], g1_data['ask_price'], g1_data['ask_quantity'])

# So that both bid/ask start at 0 quantities, we add a new 0 quantity row at the highest price.
# Important to do this after we calulcate mid/micro prices.
g1_data = pd.concat([
    pd.DataFrame({'bid_price': g1_data.iloc[0]['bid_price'], 'bid_quantity': 0, 
                    'ask_price': g1_data.iloc[0]['ask_price'], 'ask_quantity': 0}, index=[0]),
    g1_data
], ignore_index=True)
# Create step plots for bid and ask data
ax.step(g1_data['bid_quantity'].cumsum(), g1_data['bid_price'], where='post', label='Bid', color='blue')
ax.step(g1_data['ask_quantity'].cumsum(), g1_data['ask_price'], where='post', label='Ask', color='orange')
# Plot mid and micro prices
if not np.isnan(mid_price):
    ax.axhline(y=mid_price, color='green', linestyle='-', linewidth=2, label='Mid Price')
if not np.isnan(micro_price):
    ax.axhline(y=micro_price, color='purple', linestyle='--', linewidth=2, label='Micro Price')
# Add title
ax.set_title(f'Market Depth at {g1_time_seconds} after 9AM on {g1_date_input}')
ax.set_xlabel('Quantity')
ax.set_ylabel('Price')
ax.legend()

plt.show()
