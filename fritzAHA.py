import hashlib, sys
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

class FritzDect:
    """
    Class which represents the AVM HomeAutomation Interface
    """
    __Url = u'http://fritz.box'
    __HaUrl = u'/webservices/homeautoswitch.lua'
    __LoginUrl = u'/login_sid.lua'


    def __init__(self):
        self.data = []
     
    def GetSid(self, username, password, url = None):
        """Returns a valid SID"""

        if url is None:
            base_url = u'{0}{1}?username={2}'.format(self.__Url, self.__LoginUrl, username)
        else:
            base_url = u'{0}{1}?username={2}'.format(url, self.__LoginUrl, username)
  
        get_challenge = None
        try:
            get_challenge = urllib2.urlopen(base_url).read().decode('ascii')
        except urllib2.HTTPError as exception:
            print('HTTPError = ' + str(exception.code))
        except urllib2.URLError as  exception:
            print('URLError = ' + str(exception.reason))
        except Exception as exception:
            print('generic exception: ' + str(exception))
            raise

        challenge = get_challenge.split(
            '<Challenge>')[1].split('</Challenge>')[0]
        challenge_b = (
            challenge + '-' + password).encode().decode('iso-8859-1').encode('utf-16le')

        md5hash = hashlib.md5()
        md5hash.update(challenge_b)

        response_b = challenge + '-' + md5hash.hexdigest().lower()
        get_sid = urllib2.urlopen('{0}&response={1}'.format(base_url, response_b)).read().decode('utf-8')
        sid = get_sid.split('<SID>')[1].split('</SID>')[0]

        return sid
			
    def RunCmd(self, username, password, command, ain = None, url = None):
        """Calls a command"""

        sid = self.GetSid(username, password, url)

        if url is None:
            queryUrl = u'{0}'.format(self.__Url)
        else:
            queryUrl = u'{0}'.format(url)	

        queryUrl = u'{0}{1}?sid={2}'.format(queryUrl,self.__HaUrl, sid)

        if ain is not None:
            queryUrl = u'{0}&ain={1}'.format(queryUrl, ain)        

        queryUrl = u'{0}&switchcmd={1}'.format(queryUrl, command)

        return self.Query(queryUrl)
		
    
    def Query(self, url):
        """Reads a URL"""
        try:
            return urllib2.urlopen(url).read().decode('utf-8').replace('\n', '')         
        except urllib2.HTTPError:
            _, exception, _ = sys.exc_info()            
            return 'HTTPError = ' + str(exception.code)
        except urllib2.URLError:
            _, exception, _ = sys.exc_info()           
            return 'URLError = ' + str(exception.reason)
        except Exception:
            _, exception, _ = sys.exc_info()           
            return 'generic exception: ' + str(exception)
            raise
            pass
        return "Error"

    def GetSwitchList(self, username, password, url=None):     
        return self.RunCmd(username, password, "getswitchlist", None, url).split(',')

    def SetSwitchOn(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "setswitchon", ain, url).split(',')

    def SetSwitchOff(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "setswitchoff", ain, url).split(',')

    def SetSwitchToggle(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "setswitchtoggle", ain, url).split(',')

    def GetSwitchState(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "getswitchstate", ain, url).split(',')

    def GetSwitchPresent(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "getswitchpresent", ain, url)

    def GetSwitchPower(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "getswitchpower", ain, url)

    def GetSwitchEnergy(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "getswitchenergy", ain, url)

    def GetSwitchName(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "getswitchname", ain, url)
    
    def GetDeviceListInfos(self, username, password, url = None): 
        return self.RunCmd(username, password, "getdevicelistinfos", None, url)

    def GetTemperature(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "gettemperature", ain, url)

    def GetHkrtSoll(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "gethkrtsoll", ain, url)

    def GetHkrKomfort(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "gethkrkomfort", ain, url)
    
    def SetHkrtSoll(self, username, password, ain, url = None): 
        return self.RunCmd(username, password, "sethkrtsoll", ain, url)
