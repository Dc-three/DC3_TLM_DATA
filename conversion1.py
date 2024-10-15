import pandas as pd
import csv
import chardet
import json


# Define the file paths
input_file_path = './response-TimeseriesData.json'
output_file_path = './response-TimeseriesData.csv'


        

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


file_path = './response-TimeseriesData.csv'
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
    'latest.ATTRIBUTE.ChemicalType.value': 'ChemicalTypeValue',
    'latest.ATTRIBUTE.ProductName.ts': 'ProductNameTimestamp',
    'latest.ATTRIBUTE.ProductName.value':'ProductNameValue',
    'latest.ATTRIBUTE.InjectionPoint.ts': 'InjectionPointTimestamp',
    'latest.ATTRIBUTE.InjectionPoint.value':'InjectionPointValue',
    'latest.ATTRIBUTE.active.ts': 'ActiveTimestamp',
    'latest.ATTRIBUTE.active.value':'ActiveStatusValue',
    'activitytimetimestamp' : 'ActivityTimeTimestamp',

    'latest.TIME_SERIES.101.ts':'PumpEnergizeTimestamp',
    'latest.TIME_SERIES.101.value':'PumpEnergizeValue',
    'latest.TIME_SERIES.102.ts':'ValveEnergizeTimestamp',
    'latest.TIME_SERIES.102.value':'ValveEnergizeValue',
    'latest.TIME_SERIES.1100.ts':'OperatingModeTimestamp',
    'latest.TIME_SERIES.1100.value':'OperatingModeValue',
    'latest.TIME_SERIES.1101.ts':'PumpOntimeTimestamp',
    'latest.TIME_SERIES.1101.value':'PumpOntimeValue',
    'latest.TIME_SERIES.1102.ts':'PumpCycletimeTimestamp',
    'latest.TIME_SERIES.1102.value':'PumpCycletimeValue',
    'latest.TIME_SERIES.1103.ts':'MasterVolumeFlowTimestamp',
    'latest.TIME_SERIES.1103.value':'MasterVolumeFlowValue',
    'latest.TIME_SERIES.1104.ts':'MasterVolumeTimebaseTimestamp',
    'latest.TIME_SERIES.1104.value':'MasterVolumeTimebaseFlowValue',
    'latest.TIME_SERIES.1105.ts':'ErrorStatusBitTimestamp',
    'latest.TIME_SERIES.1105.value':'ErrorStatusBitValue',
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
     'latest.TIME_SERIES.1115.ts':'115Timestamp',
    'latest.TIME_SERIES.1115.value':'1115Value',
    'latest.TIME_SERIES.1116.ts':'SensorAnalogInputTimestamp',
    'latest.TIME_SERIES.1116.value':'SensorAnalogInputValue',
    'latest.TIME_SERIES.1118.ts':'TankLevelTimestamp',
    'latest.TIME_SERIES.1118.value':'TankLevelValue',
    'latest.TIME_SERIES.1120.ts':'Amountpumpedthis24HrcontractperiodTimestamp',
    'latest.TIME_SERIES.1120.value':'Amountpumpedthis24HrcontractperiodValue',
    'latest.TIME_SERIES.1122.ts':'Amountpumpedprevious24HrcontractperiodTimestamp',
    'latest.TIME_SERIES.1122.value':'Amountpumpedprevious24HrcontractperiodValue',
    'latest.TIME_SERIES.1124.ts':'ActualInjectionRateTimestamp',
    'latest.TIME_SERIES.1124.value':'ActualInjectionRateValue',
    'latest.TIME_SERIES.1126.ts':'TargetInjectionRateTimestamp',
    'latest.TIME_SERIES.1126.value':'TargetInjectionRateValue',
    'latest.TIME_SERIES.1128.ts':'TargetRatioforAutoTrackModeTimestamp',
    'latest.TIME_SERIES.1128.value':'TargetRatioforAutoTrackModeValue',
    'latest.TIME_SERIES.1130.ts':'HighTemperatureShutoffPointTimestamp',
    'latest.TIME_SERIES.1130.value':'HighTemperatureShutoffPointValue',
    'latest.TIME_SERIES.1150.ts':'PumpRelayStateTimestamp',
    'latest.TIME_SERIES.1150.value':'PumpRelayStateValue',
    'latest.TIME_SERIES.1151.ts':'PumpConstantVoltageTimestamp',
    'latest.TIME_SERIES.1151.value':'PumpConstantVoltageValue',
    'latest.TIME_SERIES.1152.ts':'PumpCalibrationStatusTimestamp',
    'latest.TIME_SERIES.1152.value':'PumpCalibrationStatusValue',
    'latest.TIME_SERIES.1153.ts':'PumpTypeTimestamp',
    'latest.TIME_SERIES.1153.value':'PumpTypeValue',
    'latest.TIME_SERIES.1178.ts': 'PumpConstantTimestamp',
    'latest.TIME_SERIES.1178.value': 'PumpConstantValue',
    'latest.TIME_SERIES.1192.ts':'TemperatureTimestamp',
    'latest.TIME_SERIES.1192.value':'TemperatureValue',
    'latest.TIME_SERIES.1194.ts':'VariableSpeedPumpTimestamp',
    'latest.TIME_SERIES.1194.value':'VariableSpeedPumpValue',
    'latest.TIME_SERIES.1196.ts':'LastPumpConstantTimestamp',
    'latest.TIME_SERIES.1196.value':'LastPumpConstantValue',
    
    
    'latest.TIME_SERIES.9995.ts':'SupplyvoltageoftheCIControllerTimestamp',
    'latest.TIME_SERIES.9995.value':'SupplyvoltageoftheCIControllerValue',
    






    'latest.TIME_SERIES.varianceRate.ts':'VarianceRateTimestamp',
    'latest.TIME_SERIES.varianceRate.value':'VarianceRateValue',
    'latest.TIME_SERIES.Variance7Day.ts':'Variance7DayTimestamp',
    'latest.TIME_SERIES.Variance7Day.value' : 'Variance7DayValue',
    'latest.TIME_SERIES.Variance1Day.ts':'Variance1DayTimestamp',
    'latest.TIME_SERIES.Variance1Day.value':'Variance1DayValue',
    'latest.TIME_SERIES.ControllerStatus.ts':'ControllerStatusTimestamp',
    'latest.TIME_SERIES.ControllerStatus.value':'ControllerStatusValue',
    'latest.TIME_SERIES.maxgallons.ts':'MaxGallonsTimestamp',
    'latest.TIME_SERIES.maxgallons.value':'MaxGallonsValue',
    'latest.TIME_SERIES.gallons.ts':'GallonsTimestamp',
    'latest.TIME_SERIES.gallons.value':'GallonsValue',
    'latest.TIME_SERIES.Gal1day.ts':'Gal1dayTimestamp',
    'latest.TIME_SERIES.Gal1day.value':'Gal1Value',
    'latest.TIME_SERIES.Gal2day.ts':'Gal2dayTimestamp',
    'latest.TIME_SERIES.Gal2day.value':'Gal2Value',
    'latest.TIME_SERIES.Gal3day.ts':'Gal3dayTimestamp',
    'latest.TIME_SERIES.Gal3day.value':'Gal3Value',
    'latest.TIME_SERIES.Gal7day.ts':'Gal7dayTimestamp',
    'latest.TIME_SERIES.Gal7day.value':'Gal7Value',
    'latest.TIME_SERIES.targetA.ts':'targetATimestamp',
    'latest.TIME_SERIES.targetA.value':'targetAValue',
    'latest.TIME_SERIES.RadarStatus.ts':'RadarStatusTimestamp',
    'latest.TIME_SERIES.RadarStatus.value':'RadarStatusValue',
    'latest.TIME_SERIES.RadarFirmware.ts':'RadarFirmwareTimestamp',
    'latest.TIME_SERIES.RadarFirmware.value':'RadarFirmwareValue',
    'latest.TIME_SERIES.sensor_temp.ts':'SensorTempTimestamp',
    'latest.TIME_SERIES.sensor_temp.value':'SensorTempValue',
    'latest.TIME_SERIES.sonic_rssi.ts':'SonicRssiTimestamp',
    'latest.TIME_SERIES.sonic_rssi.value':'SonicRssiValue',
    'latest.TIME_SERIES.sonic_result_code.ts':'SonicResultCodeTimestamp',
    'latest.TIME_SERIES.sonic_result_code.value':'SonicResultCodeValue',
    'latest.TIME_SERIES.NetRSSI.ts':'NetRssiTimestamp',
    'latest.TIME_SERIES.NetRSSI.value':'NetRssiValue',
    'latest.TIME_SERIES.IMSI.ts':'ImsiTimestamp',
    'latest.TIME_SERIES.IMSI.value':'ImsiValue',
    'latest.TIME_SERIES.IMEI.ts':'ImeiTimestamp',
    'latest.TIME_SERIES.IMEI.value':'ImeiValue',
    'latest.TIME_SERIES.SendAttempts.ts':'SendAttemptsTimestamp',
    'latest.TIME_SERIES.SendAttempts.value':'SendAttemptsValue',
    'latest.TIME_SERIES.CSQ.ts':'CSQTimestamp',
    'latest.TIME_SERIES.CSQ.value':'CSQValue',
    'latest.TIME_SERIES.gsm_rat.ts':'GsmRatTimestamp',
    'latest.TIME_SERIES.gsm_rat.value':'GsmRatValue',
    'latest.TIME_SERIES.gsm_network_roaming_status.ts':'GsmNetworkTimestamp',
    'latest.TIME_SERIES.gsm_network_roaming_status.value':'GsmNetworkValue',
    'latest.TIME_SERIES.BattEnergy.ts':'BattEnergyTimestamp',
    'latest.TIME_SERIES.BattEnergy.value':'BattEnergyValue',
    'latest.TIME_SERIES.BattLevel.ts':'BattLevelTimestamp',
    'latest.TIME_SERIES.BattLevel.value':'BattLevelValue',
    'latest.TIME_SERIES.BattVolt.ts': 'BattVoltTimestamp',
    'latest.TIME_SERIES.BattVolt.value':'BattVoltValue',
    'latest.TIME_SERIES.ContactReason.ts':'ContactReasonTimestamp',
    'latest.TIME_SERIES.ContactReason.value':'ContactReasonValue',
    'latest.TIME_SERIES.Status-1.ts': 'Status1Timestamp',
    'latest.TIME_SERIES.Status-1.value': 'Status1Value',
    'latest.TIME_SERIES.daysInv.ts':'DaysInvTimestamp',
    'latest.TIME_SERIES.daysInv.value':'DaysInvValue',
    'latest.TIME_SERIES.Data0.ts':'Data0Timestamp',
    'latest.TIME_SERIES.Data0.value':'Data0Value',
    'latest.TIME_SERIES.NewData.ts':'NewDataTimestamp',
    'latest.TIME_SERIES.NewData.value':'NewDataValue',
    'latest.TIME_SERIES.rawData.ts':'RawDataTimestamp',
    'latest.TIME_SERIES.rawData.value':'RawDataValue',
    'latest.TIME_SERIES.amount_to_full.ts':'AmountToFullTimestamp',
    'latest.TIME_SERIES.amount_to_full.value':'AmountToFullValue',
    'latest.TIME_SERIES.FillGal.ts':'FillGalTimestamp',
    'latest.TIME_SERIES.FillGal.value':'FillGalValue',
    'latest.TIME_SERIES.pumpUtil.ts': 'pumpUtilTimestamp',
    'latest.TIME_SERIES.pumpUtil.value': 'pumpUtilValue',
    'latest.TIME_SERIES.Orientation.ts':'OrientationTimestamp',
    'latest.TIME_SERIES.Orientation.value':'OrientationValue',
    'latest.TIME_SERIES.limit_3.ts':'Limit3Timestamp',
    'latest.TIME_SERIES.limit_3.value':'Limit3Value',
    'latest.TIME_SERIES.limit_2.ts':'Limit2Timestamp',
    'latest.TIME_SERIES.limit_2.value':'Limit2Value',
    'latest.TIME_SERIES.limit_1.ts':'Limit1Timestamp',
    'latest.TIME_SERIES.limit_1.value':'Limit1Value',
    'latest.TIME_SERIES.Ullage.ts':'UllageTimestamp',
    'latest.TIME_SERIES.Ullage.value':'UllageValue',
    'latest.TIME_SERIES.Ullage2.ts':'Ullage2Timestamp',
    'latest.TIME_SERIES.Ullage2.value':'Ullage2Value',
    'latest.TIME_SERIES.publish.ts':'PublishTimestamp',
    'latest.TIME_SERIES.publish.value':'PublishValue',



    'latest.ENTITY_FIELD.name.ts':'ENTITYFIELDTimestamp',
    'latest.ENTITY_FIELD.name.value':'ENTITYFIELDValue',
    'latest.ENTITY_FIELD.type.value':'ENTITYFIELDType',
    'latest.ENTITY_FIELD.type.ts' : 'ENTITYFIELDTs'
















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
    'ENTITYFIELDTimestamp',
    'PumpEnergizeTimestamp',
    'ValveEnergizeTimestamp',
    'OperatingModeTimestamp',
    'PumpOntimeTimestamp',
    'PumpCycletimeTimestamp',
    'MasterVolumeFlowTimestamp',
    'MasterVolumeTimebaseTimestamp',
    'ErrorStatusBitTimestamp',
    'PumpOperatingOnTimeTimestamp',
    'PumpOperatingCycleTimeTimestamp',
    'AmbientTemperatureTimestamp',
    'PeakPumpCurrentTimestamp',
    'AveragePumpCurrentCalculatedTimestamp',
    'CurrentPumpConstantTimestamp',
    'TargetInjectionRateSetPointforAutoVolumeModeTimestamp',
    '115Timestamp',
    '1115Value',
    'SensorAnalogInputTimestamp',
    'TankLevelTimestamp',
    'Amountpumpedthis24HrcontractperiodTimestamp',
    'Amountpumpedprevious24HrcontractperiodTimestamp',
    'ActualInjectionRateTimestamp',
    'TargetInjectionRateTimestamp',
    'TargetRatioforAutoTrackModeTimestamp',
    'HighTemperatureShutoffPointTimestamp',
    'PumpRelayStateTimestamp',
    'PumpConstantVoltageTimestamp',
    'PumpCalibrationStatusTimestamp',
    'PumpTypeTimestamp',
    'PumpConstantTimestamp',
    'TemperatureTimestamp',
    'VariableSpeedPumpTimestamp',
    'LastPumpConstantTimestamp',
    'pumpUtilTimestamp',
    'Variance7DayTimestamp',
    'BattVoltTimestamp',
    'GallonsTimestamp',
    'Gal1dayTimestamp',
    'targetATimestamp',
    'RadarStatusTimestamp',
    'SensorTempTimestamp',
    'OrientationTimestamp',
    'SonicRssiTimestamp',
    'BattEnergyTimestamp',
    'Gal2dayTimestamp',
    'BattLevelTimestamp',
    'VarianceRateTimestamp',
    'DaysInvTimestamp',
    'Data0Timestamp',
    'Data0Value',
    'RawDataTimestamp',
    'RawDataValue',
    'AmountToFullTimestamp',
    'Variance1DayTimestamp',
    'Gal3dayTimestamp',
    'ImsiTimestamp',
    'Gal7dayTimestamp',
    'NetRssiTimestamp',
    'SendAttemptsTimestamp',
    'SonicResultCodeTimestamp',
    'ImeiTimestamp',
    'RadarFirmwareTimestamp',
    'GsmRatTimestamp',
    'GsmNetworkTimestamp',
    'Ullage2Timestamp',
    'Ullage2Value',
    'MaxGallonsTimestamp',
    
    
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
output_file_path ='./final_TIMESERIES_DATA.csv'
df.to_csv(output_file_path, index=False)

print(f'Modified file saved to {output_file_path}')




