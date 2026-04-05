# Create the dataframe
initial_equilibrium = pd.DataFrame({
    'bid_price': [100, 99, 98, 97, 96, 95, 94],
    'bid_quantity': [1] * 7,
    'ask_price': [200, 201, 202, 203, 204, 205, 206],
    'ask_quantity': [1] * 7
})

demand_shift = pd.DataFrame({
    'bid_price': [100, 99, 98, 97, 96, 95, 94],
    'bid_quantity': [100, 1, 1, 1, 1, 1, 1],
    'ask_price': [200, 201, 202, 203, 204, 205, 206],
    'ask_quantity': [10, 1, 1, 1, 1, 1, 1]
})

supply_shift = pd.DataFrame({
    'bid_price': [100, 99, 98, 97, 96, 95, 94],
    'bid_quantity': [1] * 7,
    'ask_price': [200, 201, 202, 203, 204, 205, 206],
    'ask_quantity': [10, 1, 1, 1, 1, 1, 1]
})

# put all 3 into dictionary 
equilibrium_dict = {'Initial Equilibrium': initial_equilibrium, 
                   'Shift in Demand': demand_shift, 
                   'Shift in Supply': supply_shift}


times = list(equilibrium_dict.keys())

fig, ax = plt.subplots()

def animate_theoretical(i):
    ax.clear()  # Clear the axis to redraw
    
    # Extract the current time point data
    current_key = times[i]
    current_data = equilibrium_dict[current_key]
    
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
    ax.set_title(f'{current_key}')
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    ax.legend()

    ax.set_ylim(50, 250)
    ax.set_xlim(0, 15)



