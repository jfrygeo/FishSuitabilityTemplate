#-------------------------------------------------------------------------------
# Name:        DOYToTime.py
# Purpose:     Function to convert Day of Year to time
#
# Author:      JFry
#
# Created:     12/08/2016
# Edited:      12/08/2016
# Copyright:   (c) john6807 2016
# Licence:  Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/
#-------------------------------------------------------------------------------

import datetime, time

#this would be your input
#ExampleString = "A.2016340.L3m_DAY_SST4_sst4_4km"

def getdate ():
    timesplit = str(ExampleString.split(".")[1])
    print (timesplit)
    year = int(timesplit[0:4])
    doy = int(timesplit[4:7])
    t1 = (year,0,0,0,0,0,0,doy,0)
    t2 = time.struct_time(t1)
    t3 = time.strftime('%Y%j',(t2))
    t4 = datetime.datetime.strptime(t3,'%Y%j')
    t5 = t4.strftime('%m/%d/%Y')
    print (t5)
    return (t5)

getdate()