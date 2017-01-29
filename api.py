"""First hug API (local and HTTP access)"""
import hug
from fritzAHA import FritzDect


@hug.get('/GetSwitchList')
@hug.local()
def GetSwitchList(username, password, url=None): 
    fritz = FritzDect()   
    return fritz.GetSwitchList(username, password, url)

@hug.get('/SetSwitchOn')
@hug.local()
def SetSwitchOn(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.SetSwitchOn(username, password,ain, url)

@hug.get('/SetSwitchOff')
@hug.local()
def SetSwitchOff(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.SetSwitchOff(username, password,ain, url)

@hug.get('/SetSwitchToggle')
@hug.local()
def SetSwitchToggle(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.SetSwitchToggle(username, password,ain, url)

@hug.get('/GetSwitchState')
@hug.local()
def GetSwitchState(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetSwitchState(username, password,ain, url)

@hug.get('/GetSwitchPresent')
@hug.local()
def GetSwitchPresent(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetSwitchPresent(username, password,ain, url)

@hug.get('/GetSwitchPower')
@hug.local()
def GetSwitchPower(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetSwitchPower(username, password,ain, url)

@hug.get('/GetSwitchEnergy')
@hug.local()
def GetSwitchEnergy(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetSwitchEnergy(username, password,ain, url)

@hug.get('/GetSwitchName')
@hug.local()
def GetSwitchName(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetSwitchName(username, password,ain, url)

@hug.get('/GetDeviceListInfos')
@hug.local()
def GetDeviceListInfos(username, password, url=None): 
    fritz = FritzDect()
    return fritz.GetDeviceListInfos(username, password, url)

@hug.get('/GetTemperature')
@hug.local()
def GetTemperature(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetTemperature(username, password,ain, url)

@hug.get('/GetHkrtSoll')
@hug.local()
def GetHkrtSoll(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetHkrtSoll(username, password,ain, url)

@hug.get('/GetHkrKomfort')
@hug.local()
def GetHkrKomfort(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.GetHkrKomfort(username, password,ain, url)

@hug.get('/SetHkrtSoll')
@hug.local()
def SetHkrtSoll(username, password, ain, url=None): 
    fritz = FritzDect()
    return fritz.SetHkrtSoll(username, password,ain, url)
