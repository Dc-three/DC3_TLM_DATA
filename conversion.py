import pandas as pd
import csv
import chardet
import json


# Define the file paths
input_file_path = './response-Controller-and-TLM-data.json'
output_file_path = './redefined-data.csv'


        

# Step 1: Read the JSON data from the file
with open(input_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Step 2: Normalize the JSON data to handle nested structures
# Assuming the JSON file contains a list of records
if isinstance(json_data, list):
    normalized_data = pd.json_normalize(json_data)
else:
    # If the JSON structure is a dictionary with nested records under a specific key
    # Replace 'data' with the actual key in your JSON structure if different
    nested_data = json_data.get('data', json_data)
    normalized_data = pd.json_normalize(nested_data)

# Step 3: Convert the normalized JSON data to a pandas DataFrame
df = pd.DataFrame(normalized_data)

# Step 4: Write the DataFrame to an Excel file
df.to_csv(output_file_path, index=False)

print(f"Data has been successfully processed and saved to {output_file_path}")


file_path = './redefined-data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Original DataFrame:")
print(df.head())


# Example dictionary to rename columns
rename_dict = {
    'entityId.entityType': 'EntityType',
    'entityId.id': 'EntityId',
    'latest.ATTRIBUTE.Area.ts': 'AreaTimestamp',
    'latest.ATTRIBUTE.Area.value': 'AreaValue',
    'latest.ATTRIBUTE.APINo.ts': 'APINoTimestamp',
    'latest.ATTRIBUTE.APINo.value': 'APINoValue',
    'latest.ATTRIBUTE.CorpID.ts' : 'CorpIDTimestamp',
    'latest.ATTRIBUTE.CorpID.value': 'CorpIDValue',
    'latest.ATTRIBUTE.WellName.ts': 'WellNameTimestamp',
    'latest.ATTRIBUTE.WellName.value' :'WellNameValue',
    'latest.ATTRIBUTE.ChemicalType.ts' : 'ChemicalTypeTimestamp',
    'latest.ATTRIBUTE/ChemicalType.value': 'ChemicalTypeValue',
    'latest.ATTRIBUTE.ProductName.ts': 'ProductNameTimestamp',
    'latest.ATTRIBUTE.ProductName.value':'ProductNameValue',
    'latest.ATTRIBUTE.InjectionPoint.ts': 'InjectionPointTimestamp',
    'latest.ATTRIBUTE.InjectionPoint.value':'InjectionPointValue',
    'latest.ATTRIBUTE.active.ts': 'ActiveTimestamp',
    'latest.ATTRIBUTE.active.ts':'ActiveStatus',
    'latest.TIME_SERIES.1100.ts':'OperatingModeTimestamp',
    'latest.TIME_SERIES.1100.value':'OperatingModeValue',
    'latest.TIME_SERIES.1103.ts':'MasterVolumeFlowTimestamp',
    'latest.TIME_SERIES.1103.value':'MasterVolumeFlowValue',
    'latest.TIME_SERIES.1106.ts':'PumpOperatingOnTimeTimestamp',
    'latest.TIME_SERIES.1106.value':'PumpOperatingOnTimeValue',
    'latest.TIME_SERIES.1107.ts':'PumpOperatingCycleTimeTimestamp',
    'latest.TIME_SERIES.1107.value':'PumpOperatingCycleTimeValue',
    'latest.TIME_SERIES.1108.ts':'AmbientTemperatureTimestamp',
    'latest.TIME_SERIES.1108.value':'AmbientTemperatureValue',
    'latest.TIME_SERIES.1110.ts':'PeakPumpCurrentTimestamp',
    'latest.TIME_SERIES.1110.value':'PeakPumpCurrentValue',
    'latest.TIME_SERIES.1111.ts':'AveragePumpCurrentCalculatedTimestamp',
    'latest.TIME_SERIES.1111.value':'AveragePumpCurrentCalculatedValue',
    'latest.TIME_SERIES.1112.ts':'CurrentPumpConstantTimestamp',
    'latest.TIME_SERIES.1112.value':'CurrentPumpConstantValue',
    'latest.TIME_SERIES.1114.ts':'TargetInjectionRateSetPointforAutoVolumeModeTimestamp',
    'latest.TIME_SERIES.1114.value':'TargetInjectionRateSetPointforAutoVolumeModeValue',
    'latest.TIME_SERIES.1118.ts':'TankLevel(inches)Timestamp',
    'latest.TIME_SERIES.1118.value':'TankLevel(inches)Value',
    'latest.TIME_SERIES.1120.ts':'Amountpumpedthis24HrcontractperiodTimestamp',
    'latest.TIME_SERIES.1120.value':'Amountpumpedthis24HrcontractperiodValue',
    'latest.TIME_SERIES.1122.ts':'Amountpumpedprevious24HrcontractperiodTimestamp',
    'latest.TIME_SERIES.1122.value':'Amountpumpedprevious24HrcontractperiodValue',
    'latest.TIME_SERIES.1124.ts':'ActualInjectionRateTimestamp',
    'latest.TIME_SERIES.1124.value':'ActualInjectionRateValue',
    'latest.TIME_SERIES.1126.ts':'TargetInjectionRateTimestamp',
    'latest.TIME_SERIES.1126.value':'TargetInjectionRateValue',
    'latest.TIME_SERIES.1128.ts':'TargetRatioforAutoTrackMode(Quarts/Unit Master Volume)Timestamp',
    'latest.TIME_SERIES.1128.value':'TargetRatioforAutoTrackMode(Quarts/Unit Master Volume)Value',
    'latest.TIME_SERIES.1130.ts':'HighTemperatureShutoffPointTimestamp',
    'latest.TIME_SERIES.1130.value':'HighTemperatureShutoffPointValue',
    'latest.TIME_SERIES.9995.ts':'SupplyvoltageoftheCIControllerTimestamp',
    'latest.TIME_SERIES.9995.value':'SupplyvoltageoftheCIControllerValue',
    'latest.TIME_SERIES.varianceRate.ts':'VarianceRateTimestamp',
    'latest.TIME_SERIES.varianceRate.value':'VarianceRateValue',
    'latest.TIME_SERIES.ControllerStatus.ts':'ControllerStatusTimestamp',
    'latest.TIME_SERIES.ControllerStatus.value':'ControllerStatusValue',
    'latest.TIME_SERIES.gallons.ts':'GallonsTimestamp',
    'latest.TIME_SERIES.gallons.value':'GallonsValue',
    'latest.ENTITY_FIELD.name.ts':'ENTITY_FIELDTimestamp',
    'latest.ENTITY_FIELD.name.value':'ENTITY_FIELDValue',















    # Add more column mappings as needed
}

# Rename columns
df.rename(columns=rename_dict, inplace=True)

# Display the first few rows of the DataFrame to verify changes
print(df.head())





# List of columns to delete
columns_to_delete = [
    'EntityType', 
    'readTs',
    'ENTITY_FIELDTimestamp',
    
    # Add more columns to delete as needed
]

# Drop columns
df.drop(columns=columns_to_delete, inplace=True)
print(df.head())



# Convert Unix timestamps to datetime
timestamp_columns = [col for col in df.columns if col.endswith('Timestamp')]

for col in timestamp_columns:
    df[col] = pd.to_datetime(df[col], unit='ms')

# Display the DataFrame after converting timestamps
print("DataFrame after converting Unix timestamps to datetime:")
print(df.head())









# Save the modified DataFrame to a new CSV file
output_file_path = './final_output.csv'
df.to_csv(output_file_path, index=False)

print(f'Modified file saved to {output_file_path}')




