import numpy as np
import matplotlib.pyplot as plt




# Input
    
# --------------------------------------------------------------------->
name = "Vasilis Kokkinogenis" # to dokimasa me sketo "V" gia na do an simplironei 0 sto M=8 kai pianei
# <---------------------------------------------------------------------



# Step 1:  
def name_to_binary(name):
    binary_name = ""
    for char in name:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_name += binary_char
    return binary_name


# Example usage:
binary_name = name_to_binary(name)
print(binary_name) # for debug purposes




# Step 2a:
def gray_code(m):    # autos einai o kodikas sas apo to commlib
    if m == 1:
        g = ['0', '1']
    elif m > 1:
        gs = gray_code(m-1)
        gsr = gs[::-1]
        gs0 = ['0' + x for x in gs]
        gs1 = ['1' + x for x in gsr]
        g = gs0 + gs1
    return g

def binary_to_gray_code(binary_sequence, M):
    log2_M = int(np.log2(M))
    remaining_bits = len(binary_sequence) % log2_M
    if remaining_bits != 0:
        binary_sequence += '0' * (log2_M - remaining_bits)
        
        
    gray_code_bits = gray_code(log2_M)

    gray_code_bit_groups = []
    for i in range(0, len(binary_sequence), log2_M):
        bits = binary_sequence[i:i + log2_M]
        gray_code_bit_group = gray_code_bits[int(bits, 2)]
        gray_code_bit_groups.append(gray_code_bit_group)
    return gray_code_bit_groups




# Example usage:
# Initialize an empty list to store gray_code_bit_groups for each M
all_gray_code_bit_groups = []
for M in [2, 4, 8, 16]:
    gray_code_bit_groups = binary_to_gray_code(binary_name, M)
    # Convert to a list if needed
    gray_code_bit_groups = list(gray_code_bit_groups)
    
    # Append the result to the list
    all_gray_code_bit_groups.append(gray_code_bit_groups)
    print(f"M={M} - Gray Code Bits: {gray_code_bit_groups}")
    
    
    

# Step 2b:
def gray_code_to_ppm_symbols(gray_code_bit_groups):
    ppm_symbols = [int(gray_code, 2) for gray_code in gray_code_bit_groups]
    return ppm_symbols


# Example usage:
all_ppm_symbols = []
for M in [2, 4, 8, 16]:
    ppm_symbols = gray_code_to_ppm_symbols(all_gray_code_bit_groups[int(np.log2(M))-1])
    all_ppm_symbols.append(ppm_symbols)
    print(f"M={M} - PPM Symbols: {ppm_symbols}")
    
   
    
# Step 3:   
Rb = 10**9
Rbinv = 1 / Rb
Ts = np.log2(M) / Rb
for M in [2,4,8,16]:
    Ts_numerator = np.log2(M)
    symbols = all_ppm_symbols[int(np.log2(M))-1]
    number_of_symbols = len(symbols)
    print(f"{number_of_symbols} symbols")

    
    # Create a dummy signal (linear ramp from 0 to 1) for the plot
    
    # Create the plot
    #plt.plot(time)
    
    # Set x-axis ticks to 0, 0.5, and 1
    tick_positions = np.arange(0, number_of_symbols * Ts_numerator + Ts_numerator/M, Ts_numerator/M)
    

    # tick_labels = [f'{pos}' for pos in range(len(tick_positions))]   
    # tick_labels = [f'{pos - (i // M) * M}' for i, pos in enumerate(range(len(tick_positions)))]
    tick_labels = ['' for _ in range(len(tick_positions) - 1)] + [f'{number_of_symbols * M}/{M} * {Ts_numerator}*{Rbinv}']



    plt.figure(figsize=(11, 4))
        

    plt.xticks(tick_positions, tick_labels) 
    for i in range(int(number_of_symbols)):
        plt.axvline(x=i * Ts_numerator, color='red', linestyle='--', linewidth=0.8)

    
     
    for i, symbol in enumerate(symbols):
        rect_start = i * Ts_numerator + symbol * Ts_numerator/M
        rect = plt.Rectangle((rect_start, 0), Ts_numerator/M, 1, color='blue', alpha=0.5)  # Create a rectangle
        plt.gca().add_patch(rect)  # Add the rectangle to the plot

    plt.yticks(np.arange(0, 1 + 1, 1))

    plt.tight_layout()
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title(f'{M}-PPM')
    plt.show()
    
# ta print den ta ekana comment out giati mporei na mhn sas arkei to plot, gia na epivevaiosete kai eseis oti einai sosta
    
    
