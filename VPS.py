import requests
import json
class VPS(object):
    def getLiveInfo(self):
        u = self.url+"getLiveServiceInfo"
        form_data = {
                'veid':self.veId,
                'api_key':self.apiKey
                }
        serverInfo = self.s.post(u,data=form_data)
        print(serverInfo.content)
        return serverInfo

    def __init__(self):
        self.url = "https://api.64clouds.com/v1/"
        self.veId = '1162879'
        self.apiKey = '********************************'
        self.s = requests.Session()
        self.serverInfo = self.getLiveInfo()
        j = self.serverInfo.json()
        self.infoDt = json.loads(json.dumps(j))

    def setKey(veid,apikey):
        self.veid = veid
        self.apiKey = apikey

    def getIp(self):
        ip = self.infoDt["ip_addresses"][0]
        return ip

    def getSSHPort(self):
        port = self.infoDt['ssh_port']
        return str(port)

    def getOs(self):
        os = self.infoDt['os']
        return os

    def getLocation(self):
        l = self.infoDt['node_datacenter']
        return l

    def getLA(self):
        r = self.infoDt["ve_status"]
        la = self.infoDt["load_average"]
        return r+": "+la

# use Byte default below
    def getPlanData(self):
        plan = self.infoDt["plan_monthly_data"]
        return plan

    def getUsagData(self):
        data = self.infoDt["data_counter"]
        return data

    def getRamFree(self):
        free = self.infoDt["mem_available_kb"]
        return free*1024

    def getRamTotal(self):
        total = self.infoDt["plan_ram"]
        return total

    def getUsagDisk(self):
        usage = self.infoDt["ve_used_disk_space_b"]
        return usage

    def getPlanDisk(self):
        plan = self.infoDt["plan_disk"]
        return plan

    def getPlanSwap(self):
        plan = self.infoDt["swap_total_kb"]
        return plan*1024

    def getFreeSwap(self):
        free = self.infoDt["swap_available_kb"]
        return free*1024
