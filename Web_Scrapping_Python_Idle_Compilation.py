import pandas as pd
from selenium import webdriver
import time
import os

'To click on Individual Links in the Chrome Browser and fetch data'
driver_1=[]
driver_2=[]


try:
    
    driver_1=webdriver.Chrome("CHROME_EXT_DIR")
    planid=100110
    for planid in range(100111):
        
        print("\tPlanid=\t",planid)
        os.chdir("DIR")
        driver_1.get("PLAN_ID_LINK"+str(planid))
        planid=planid+1
        driver_1.find_Elements_By_Class_Name("m_centered")
        driver_1.find_Elements_By_Class_Name("m_visible-sm-md-lg")
        print("To print the total document dimensions")
        driver_1.sleep(15)
        driver_2=driver_1
        print(len(driver_2))
        for x in range(len(driver_2)):
            df1=pd.DataFrame()
            df1=x.text
            os.chdir("DIR")
            df1.to_csv("OUTPUT_DIR"+{Sheet_X}.csv)
            df1.append(df1)

except OSError:
        print("Ignored Due to OS Error Handling which needs Indepth Understanding and TroubleShooting")
          

