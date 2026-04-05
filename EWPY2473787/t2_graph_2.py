def animate(i):
    # We first need to clear axes
    ax.clear()  
    # Extract the current time point data, using each dictionary key
    current_key = times[i]
    current_data = combined_dataframes[current_key]
    # Use our custom function to adjust row lengths & N/A values from chart 1.
    current_data = chart_data(current_data)
    # Calculate mid and micro prices
    mid_price = calculate_mid_price(current_data['bid_price'], 
                                    current_data['ask_price'])
    micro_price = calculate_micro_price(current_data['bid_price'], 
                                        current_data['bid_quantity'],
                                        current_data['ask_price'], 
                                        current_data['ask_quantity'])
    
    # So that both bid/ask start at 0 quantities, we add a new 0 quantity row at the highest price.
    current_data = pd.concat([
        pd.DataFrame({'bid_price': current_data.iloc[0]['bid_price'], 'bid_quantity': 0, 
                    'ask_price': current_data.iloc[0]['ask_price'], 'ask_quantity': 0}, index=[0]),
        current_data
    ], ignore_index=True)
    
    # Create step plots for bid and ask data

    ax.step(current_data['bid_quantity'].cumsum(), current_data['bid_price'], where='post', label='Demand', color='blue')
    ax.step(current_data['ask_quantity'].cumsum(), current_data['ask_price'], where='post', label='Supply', color='orange')
    
    # Plot mid and micro prices
    if not np.isnan(mid_price):
        ax.axhline(y=mid_price, color='green', linestyle='-', linewidth=2, label='Mid Price')
    if not np.isnan(micro_price):
        ax.axhline(y=micro_price, color='purple', linestyle='--', linewidth=2, label='Micro Price')

    # Add titles and labels
    ax.set_title(f'LOB {current_key} seconds after 9AM')
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    ax.legend()
