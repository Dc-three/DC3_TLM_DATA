import pandas as pd
import csv
import chardet
import json


# Define the file paths
input_file_path = './response-AttributeData.json'
output_file_path = './response-AttributeData.csv'


        

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


file_path = './response-AttributeData.csv'
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
    'latest.ATTRIBUTE.WellOperator.ts':'WellOperatorTimestamp',
    'latest.ATTRIBUTE.WellOperator.value':'WellOperatorValue',
    'latest.ATTRIBUTE.ChemicalType.ts' : 'ChemicalTypeTimestamp',
    'latest.ATTRIBUTE.ChemicalType.value': 'ChemicalTypeValue',
    'latest.ATTRIBUTE.ProductName.ts': 'ProductNameTimestamp',
    'latest.ATTRIBUTE.ProductName.value':'ProductNameValue',
    'latest.ATTRIBUTE.ProdType.ts':'ProdTypeTimestamp',
    'latest.ATTRIBUTE.ProdType.value':'ProdTypeValue',
    'latest.ATTRIBUTE.InjectionPoint.ts': 'InjectionPointTimestamp',
    'latest.ATTRIBUTE.InjectionPoint.value':'InjectionPointValue',
    'latest.ATTRIBUTE.active.ts': 'ActiveTimestamp',
    'latest.ATTRIBUTE.active.value':'ActiveStatusValue',
    'latest.ATTRIBUTE.Customer.ts': 'CustomerTimestamp',
    'latest.ATTRIBUTE.Customer.value':'CustomerValue',
    'latest.ATTRIBUTE.variance.ts':'VarianceTimestamp',
    'latest.ATTRIBUTE.variance.value':'VarianceValue',

    
    'activitytimetimestamp' : 'ActivityTimeTimestamp',

    'latest.ATTRIBUTE.SP_LowVoltage.ts':'SPlowVoltageTimestamp',
    'latest.ATTRIBUTE.SP_LowVoltage.value':'SPlowVoltageValue',
    'latest.ATTRIBUTE.SP_LowLevel.ts':'SPLowLevelTimestamp',
    'latest.ATTRIBUTE.SP_LowLevel.value':'SPLowLevelValue',
    'latest.ATTRIBUTE.SP_LowPress.ts':'SPLowpressTimestamp',
    'latest.ATTRIBUTE.SP_LowPress.value':'SPLowpressValue',
    'latest.ATTRIBUTE.SP_LowInjectRate.ts':'SPLowInjectRateTimestamp',
    'latest.ATTRIBUTE.SP_LowInjectRate.value':'SPLowInjectRateValue',
    'latest.ATTRIBUTE.SP_LowPumpConstant.ts':'SPLowPumpConstantTimestamp',
    'latest.ATTRIBUTE.SP_LowPumpConstant.value':'SPLowPumpConstantValue',
    'latest.ATTRIBUTE.SP_LoLoLevel.ts':'SPLoLoLevelTimestamp',
    'latest.ATTRIBUTE.SP_LoLoLevel.value':'SPLoLoLevelValue',
    'latest.ATTRIBUTE.SP_High_Injection_Rate.ts':'SPHighInjectionRateTimestamp',
    'latest.ATTRIBUTE.SP_High_Injection_Rate.value':'SPHighInjectionRateValue',
    'latest.ATTRIBUTE.SP_HighPress.ts':'SPHighpressTimestamp',
    'latest.ATTRIBUTE.SP_HighPress.value':'SPHighpressValue',
    'latest.ATTRIBUTE.SP_HighLevel.ts':'SPHighLevelTimestamp',
    'latest.ATTRIBUTE.SP_HighLevel.value':'SPHighLevelValue',
    'latest.ATTRIBUTE.SP_MaxCurrent.ts':'SPMaxCurrentTimestamp',
    'latest.ATTRIBUTE.SP_MaxCurrent.value':'SPMaxCurrentValue',
    'latest.ATTRIBUTE.sg.ts': 'sgTimestamp',
    'latest.ATTRIBUTE.sg.value': 'sgValue',

    'latest.ATTRIBUTE.Latitude.ts': 'LattitudeTimestamp',
    'latest.ATTRIBUTE.Latitude.value': 'LattitudeValue',
    'latest.ATTRIBUTE.Longitude.ts': 'LongitudeTimestamp',
    'latest.ATTRIBUTE.Longitude.value': 'LongitudeValue',
    'latest.ATTRIBUTE.Offset.ts':'OffsetTimestamp',
    'latest.ATTRIBUTE.Offset.value':'OffsetValue',
    'latest.ATTRIBUTE.tanktype.ts':'TankTypeTimestamp',
    'latest.ATTRIBUTE.tanktype.value':'TankTypeValue',
    'latest.ATTRIBUTE.TankHeight.ts':'TankHeightTimestamp',
    'latest.ATTRIBUTE.TankHeight.value':'TankHeightValue',
    'latest.ATTRIBUTE.lastActivityTime.ts':'LastActivityTimestamp',
    'latest.ATTRIBUTE.lastActivityTime.value':'LastActivityValue',
    'latest.ATTRIBUTE.actdate.ts':'ActDateTimestamp',
    'latest.ATTRIBUTE.actdate.value':'ActDateValue',
    'latest.ATTRIBUTE.inactivityAlarmTime.ts':'InactivityAlarmTimestamp',
    'latest.ATTRIBUTE.inactivityAlarmTime.value':'InactivityAlarmValue',
    'latest.ATTRIBUTE.Disable_RealTime_Emails.ts':'RealTimeEmailTimestamp',
    'latest.ATTRIBUTE.Disable_RealTime_Emails.value':'RealTimeEmailValue',
    'latest.ATTRIBUTE.FacilityID.ts':'FacilityIDTimestamp',
    'latest.ATTRIBUTE.FacilityID.value':'FacilityIDValue',
    'latest.ATTRIBUTE.inactivityTimeout.ts':'InactivityTimeoutTimestamp',
    'latest.ATTRIBUTE.inactivityTimeout.value':'InactivityTimeoutValue',
    'latest.ATTRIBUTE.CostCenter.ts':'CostCenterTimestamp',
    'latest.ATTRIBUTE.CostCenter.value':'CostCenterValue',
    'latest.ATTRIBUTE.UntiNo.ts':'UntilNoTimestamp',
    'latest.ATTRIBUTE.UntiNo.value':'UntilNoValue',
    'latest.ATTRIBUTE.LeaseNo.ts':'LeaseNoTimestamp',
    'latest.ATTRIBUTE.LeaseNo.value':'LeaseNoValue',
    'latest.ATTRIBUTE.sensortype.ts':'SensorTypeTimestamp',
    'latest.ATTRIBUTE.sensortype.value':'SensorTypeValue',
    'latest.ATTRIBUTE.MiradorSerialNo.ts':'MiradorSerialNoTimestamp',
    'latest.ATTRIBUTE.MiradorSerialNo.value':'MiradorSerialNoValue',


    



    
    












    'latest.ENTITY_FIELD.name.ts':'ENTITYFIELDTimestamp',
    'latest.ENTITY_FIELD.name.value':'ENTITYFIELDValue',
    'latest.ENTITY_FIELD.type.value':'ENTITYFIELDTypeValue',
    'latest.ENTITY_FIELD.type.ts' : 'ENTITYFIELDTs',
















    # Add more column mappings as needed
}

# Rename columns
df.rename(columns=rename_dict, inplace=True)

# Display the first few rows of the DataFrame to verify changes
print(df.head())





# List of columns to delete
columns_to_delete = [
    'EntityType', 
    'readAttrs',
    'readTs',
    'ENTITYFIELDTs',
    'ENTITYFIELDTimestamp',
    'SPlowVoltageTimestamp',
    'SPHighInjectionRateTimestamp',
    'CorpIDTimestamp',
    'ChemicalTypeTimestamp',
    'CustomerTimestamp',
    'SPLowLevelTimestamp',
    'SPLowpressTimestamp',
    'LattitudeTimestamp',
    'WellOperatorTimestamp',
    'InactivityAlarmTimestamp',
    'SPLowInjectRateTimestamp',
    'RealTimeEmailTimestamp',
    'FacilityIDTimestamp',
    'InactivityTimeoutTimestamp',
    'CostCenterTimestamp',
    'sgTimestamp',
    'SPLoLoLevelTimestamp',
    'SPHighpressTimestamp',
    'UntilNoTimestamp',
    'APINoTimestamp',
    'WellNameTimestamp',
    'LeaseNoTimestamp',
    'SPLowPumpConstantTimestamp',
    'SPMaxCurrentTimestamp',
    'SPHighLevelTimestamp',
    'InjectionPointTimestamp',
    'ProdTypeTimestamp',
    'SensorTypeTimestamp',
    'MiradorSerialNoTimestamp',
    'LongitudeTimestamp',
    'OffsetTimestamp',
    'TankTypeTimestamp',
    'TankHeightTimestamp',
    'AreaTimestamp',
    'VarianceTimestamp',



    
    
    
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
output_file_path ='./final_ATTRIBUTE_DATA.csv'
df.to_csv(output_file_path, index=False)

print(f'Modified file saved to {output_file_path}')