import math
from config import *

class Fdict():
    def __init__(self):
        self.mid = self.readDict('./rules/mid.txt')
        self.common_pwd = self.readDict('./rules/commonPwd.txt')
        self.weak_suf = self.readDict('./rules/suf.txt')
        self.year = self.readDict('./rules/year.txt')
        self.pwd = []
        self.username = []
        self.initModifyString()

    def readDict(self,filename):
        """
        return ['a','b','c']
        """
        with open(filename,'r',encoding='utf-8')as f:
            results = [data.strip() for data in f.readlines()]
        return results
    
    def modifyString(self,str):
        """
        input  ['ab']
        return ['ab','Ab','AB]
        """
        strs = []
        strs.append(str)
        strs.append(str.upper())
        strs.append(str.capitalize())
        return strs

    def concactString(self,pre,mid,suf):
        """
        return [pre[0]+mid[0]+suf[0],...]
        """
        _pwd = []
        for p in pre:
            for m in mid:
                _pwd += [p + m + s for s in suf]
        return _pwd

    def buildUsername(self):
        """
        return ['a','b','c']
        """
        self.user = []
        jobNo_len = len(jobNo)
        if build_jobNo_username:
            jobNos = ['0'*int(jobNo_len-len(str(j))) + str(j) for j in range(int(math.pow(10,jobNo_len)))]
            self.user += self.concactString(self.company_short_names,[''],jobNos)
        if build_other_username:
            pass

    def initModifyString(self):
        self.usernames = self.modifyString(username)
        self.company_short_names = self.modifyString(company_short_name)
        self.company_city_short_names = self.modifyString(company_city_short_name)

    def initConcact(self,head):
        """
        input ['head']
        return ['head'+mid+othersuf]
        """
        _pwd = []
        _pwd += self.concactString(head,self.mid,self.weak_suf)
        _pwd += self.concactString(head,self.mid,self.year)
        return _pwd
    
    def savePwd(self,filename,data):
        with open(filename,'a',encoding='utf-8')as f:
            for d in data:
                f.write(d + '\n')

    def removeRepeat(self):
        self.pwd = set(self.pwd)
        self.pwd = list(self.pwd)
    
    def filterPwd(self):
        tmp_pwd = self.pwd[:]
        for p in tmp_pwd:
            if len(p) < min_pwd:
                self.pwd.remove(p)
            if len(p) > max_pwd:
                self.pwd.remove(p)
    
    def addSufPre(self):
        tmp_pwd = self.pwd[:]
        if is_add_suf:
            for a in add_suf:
                self.pwd += [p + a for p in tmp_pwd]
        if is_add_pre:
            for a in add_pre:
                self.pwd += [a + p for p in tmp_pwd]

    def main(self):
        if jobNo:
            pwdJobNos = [jobNo]
            if len(jobNo) < 6:
                pwdJobNos.append('00'+jobNo)
            self.pwd += self.initConcact(pwdJobNos)
        if jobNo and company_domain:
            self.pwd += self.concactString(pwdJobNos,self.mid,company_domain)
        if jobNo and company_short_name:
            self.pwd += self.concactString(self.company_short_names,self.mid,pwdJobNos)
        if jobNo and company_city_short_name:
            self.pwd += self.concactString(self.company_city_short_names,self.mid,pwdJobNos)
        if jobNo and company_short_name and company_city_short_name:
            cmid = [company_short_name + m for m in self.mid]
            self.pwd += self.concactString(self.company_city_short_names,cmid,pwdJobNos)

        if username:
            self.pwd += self.initConcact(self.usernames)
        if username and company_code:
            self.pwd += self.concactString(self.usernames,self.mid,company_code)
        if username and company_domain:
            self.pwd += self.concactString([company_domain.split('.')[0]],self.mid,self.usernames)
            self.pwd += self.concactString(self.usernames,self.mid,company_domain)
        if username and company_short_name:
            self.pwd += self.concactString(self.usernames,self.mid,self.company_short_names)
            self.pwd += self.concactString(self.company_short_names,self.mid,self.usernames)
            self.pwd += self.concactString(self.company_short_names,self.mid,[username[0]])
        if username and company_city_short_name:
            self.pwd += self.concactString(self.company_city_short_names,self.mid,self.usernames)
            self.pwd += self.concactString(self.usernames,self.mid,self.company_city_short_names)

        if company_code:
            self.initConcact(company_code)
        if company_code and company_domain:
            self.pwd += self.concactString(company_code,self.mid,[company_domain])
            self.pwd += self.concactString([company_domain.split('.')[0]],self.mid,company_code)
        if company_code and company_short_name:
            self.pwd += self.concactString(self.company_short_names,self.mid,company_code)
        if company_code and company_city_short_name:
            self.pwd += self.concactString(self.company_city_short_names,self.mid,company_code)
        if company_code and company_domain and company_short_name and company_city_short_name:
            for code in company_code:
                cmid = [code + m for m in self.mid]
            self.pwd += self.concactString(self.company_city_short_names,cmid,company_domain)
            self.pwd += self.concactString(self.company_short_names,cmid,company_domain)
        if company_domain:
            self.initConcact(company_domain)
        if company_domain and company_short_name:
            self.pwd += self.concactString(self.company_short_names,self.mid,[company_domain])
            self.pwd += self.concactString([company_domain.split('.')[0]],self.mid,self.company_short_names)
        if company_domain and company_city_short_name:
            self.pwd += self.concactString(self.company_city_short_names,self.mid,[company_domain])
            self.pwd += self.concactString([company_domain.split('.')[0]],self.mid,self.company_city_short_names)
        if company_domain and company_short_name and company_city_short_name:
            cmid = [company_short_name + m for m in self.mid]
            self.pwd += self.concactString(self.company_city_short_names,self.mid,[company_domain])
            self.pwd += self.concactString(self.company_city_short_names,cmid,[company_domain])
        
        if company_short_name:
            self.pwd += self.initConcact(self.company_short_names)  
        if company_short_name and company_city_short_name:
            self.pwd += self.concactString(self.company_city_short_names,self.mid,company_short_name)
            self.pwd += self.concactString(company_short_name,self.mid,company_city_short_name)
        
        if company_city_short_name:
            self.pwd += self.initConcact(self.company_city_short_names)
        self.addSufPre()
        self.removeRepeat()
        self.filterPwd()
        self.buildUsername()
        if company_domain:
            self.savePwd('./results/{}.txt'.format(company_domain),self.pwd)
            self.savePwd('./results/username-{}.txt'.format(company_domain),self.user)
        else:
            self.savePwd('./results/passwords.txt',self.pwd)
            self.savePwd('./results/usernames.txt',self.user)

if __name__ == '__main__':
    fdict = Fdict()
    fdict.main()