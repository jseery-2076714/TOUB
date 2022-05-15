# data_gen.py - Tu Nguyen 2022
#
# ----------------------------------
#
# Generates the toub data csv
#
# Resulting columns:
#   non-si - str
#   len(cm) - float
#   area(cm^2) - float
#   vol(cm^3) - float

# Imports
import pandas as pd
import numpy as np

# The write csv file
write = 'data_toub_conv.csv'
# Suppress numpy float sci form
np.set_printoptions(suppress=True)

def main():
    # resulting data frame
    dest_map = {}

    # col_names = ['non-si', 'len(cm)', 'area(cm^2)', 'vol(cm^3)']

    base_data = { 1: {'non-si': 'inch', 'len(cm)': 2.54, 'area(cm^2)': 6.4516, 'vol(cm^3)': 16.387064},
                  2: {'non-si': 'feet', 'len(cm)': 30.48, 'area(cm^2)': 929.0304, 'vol(cm^3)': 28316.84659},
                  3: {'non-si': 'yards', 'len(cm)': 91.44, 'area(cm^2)': 8361.2736, 'vol(cm^3)': 764554.858},
                  4: {'non-si': 'mile', 'len(cm)': 160934.4, 'area(cm^2)': 25899881103.0, 'vol(cm^3)': 4.16818E+15},
                  5: {'non-si': 'furlong', 'len(cm)': 20116.8, 'area(cm^2)': 404685642.2, 'vol(cm^3)': 8140980127814},
                  6: {'non-si': 'pints', 'len(cm)': 0.0, 'area(cm^2)': 0.0, 'vol(cm^3)': 0.0},
                  7: {'non-si': 'quarts', 'len(cm)': 0.0, 'area(cm^2)': 0.0, 'vol(cm^3)': 0.0},
                  8: {'non-si': 'cups', 'len(cm)': 0.0, 'area(cm^2)': 0.0, 'vol(cm^3)': 0.0}}
    
    dest_map.update(base_data)
    dest_df = pd.DataFrame.from_dict(dest_map).T
    
    # output results to write csv
    dest_df.to_csv(write, float_format='%.3f',index=False)
    
    print(dest_df)


    

if __name__ == "__main__":
    main()

#######################################################################################################################
#                                                     Data Gen                                                        #
#######################################################################################################################
#
# Non-SI	Length (cm)	Area (cm^2)	Volume (cm^3)
# Inch	2.54		16.3871
# Feet	30.48		28316.8
# Yards	91.44		764555
# Mile	160934.4		4.168e^15
# Furlong	20116.8		
# Pints	0		473.17
# Quarts	0		946.35
# Cups	0		236.58