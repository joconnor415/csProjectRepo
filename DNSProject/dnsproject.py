'''
Created on Aug 19, 2013

@author: joconner-m
'''

import os
import ngram
import csv
import enchant
import socket
import socks
import httplib
import os
import dns.resolver
import operator

#DNS Detetion Algorithm for Botnets and also Advanced Persistent Threat Attackers
#Preconditions: Assume Tor is running in order to preserve anonymity for lookups
#Unfinished, still have to finish clustering and polish
#Created own heuristics for APT, based on ngram distance to words in custom dictionary
#along with being recently updated, having low ranking ASN, and no text records
#Botent Detection based on character frequency analysis and Fast Flux Detection Algorithm 

#(TOR is installed/running on client), establishing TOR connection to do DNS lookups
def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    socket.socket= socks.socksocket
    print ("Connected to TOR")
    #additional TOR testing
    # conn= httplib.HTTPConnection("check.torproject.org")
    # conn.request("GET", "/")
    # response= conn.getresponse()
    # print (response.read())

#control TOR and establish new identity, assigns user new IP
def newIdentity():
    socks.setdefaultproxy()
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9051))
    s.send("AUTHENTICATE\r\n")
    response= s.recv(128)
    if response.startswith("250"):
        s.send("SIGNAL NEWNYM\r\n")
    s.close()
    connectTor()


flagged_queries= set()
flag_wan_dom= set()
pwl = enchant.request_pwl_dict("enchantAddList.txt")


from bulkwhois.shadowserver import BulkWhoisShadowserver

#retreived ASN rankings by number of ASes in system from http://as-rank.caida.org/
def getASNRankings():
    totalNumASes= 44086
    asn_rank_dic= {}
    for line in open("ASNRankingsByAS.txt", "rU"):
        line.strip()
        line= line.split(",")
        rank= line[0]
        rank= int(rank)
        asn= line[1]
        num_ASes= line[2]
        num_ASes= int(num_ASes)
        score= float(num_ASes)/totalNumASes
        asn_rank_dic[asn]= (rank, score)
    return asn_rank_dic    
ASNRankings= getASNRankings()

#identify if domain has any TXT records
def noTXTRecord(domain):
    count=0
    no_count=0
    total=0
    try:
        answer=dns.resolver.query(domain, "TXT")
        return False
#         for data in answer:
#            print data   
    except:
        return True

#if registrant has updated their domain recently, majority of APT have updates within 1 year
def isRecentlyUpdate(domain):
    import whois
    import math
    import datetime
    try: 
        w = whois.query(domain)
        diff= w.last_updated - datetime.datetime.now()
        val= math.fabs(diff.days)
        if (val) >= 365: #less than a year since last updated
            return False
        else:
            score= float(val)/365.0
            return score
    except:
        #print "Can't Find Info for: ", domain
        #cannot find any info for domain which is potential evil domain indicator
        return 0.0

#return WHOIS information on for lookup on IP
#python bulkwhois library
def WHOIS(ip):
    bulk_whois = BulkWhoisShadowserver()
    records = bulk_whois.lookup_ips([ip])
    org_name= ""
    cc=""
    ip=""
    register=""
    as_name=""
    bgp_prefix=""
    asn=""
    for record in records:
        org_name= records[record]["org_name"]
        cc= records[record]["cc"]
        ip= records[record]["ip"]
        register= records[record]["register"]
        as_name= records[record]["as_name"]
        bgp_prefix= records[record]["bgp_prefix"]
        asn= records[record]["asn"]
    return org_name, cc, ip, register, as_name, bgp_prefix, asn

#go thru dns raw logs
def walk_thru_files(dir):
    f_list= []
    for (folder, dirnames, files) in os.walk(dir):
        for dns_doc in files:
            f_list.append(folder + "/" + dns_doc)
    return f_list

#convert from unsigned int to dotted IP
def numToDottedQuad(n):
    #convert long int to dotted quad string"
    n= int(n)
    d = 256 * 256 * 256
    q = []
    while d > 0:
        m,n = divmod(n,d)
        q.append(str(m))
        d = d/256
    return '.'.join(q)

#character frequency analysis to detect if domain has botnet characteristics
#for example: ltmxaxfxm29hqawaqazavf22e31jrpse61i15.info
cons_set= set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w','x', 'y', 'z'])
vowel_set= set(['a', 'e', 'i', 'o', 'u'])
def queryCharStats(query):
    c_count=0
    vowel_count= 0
    dash_count=0
    dot_count=0
    colon_count=0
    max_num_consec_cons=0
    new_max_num_consec_cons=0
    for c in query:
        if c in cons_set:
            c_count+=1
            new_max_num_consec_cons+=1
        elif c in vowel_set:
            vowel_count+=1
            max_num_consec_cons<=new_max_num_consec_cons
            new_max_num_consec_cons=0  
        elif c=="-":
            dash_count+=1
            max_num_consec_cons<=new_max_num_consec_cons
            new_max_num_consec_cons=0  
        elif c==".":
            dot_count+=1
            max_num_consec_cons<=new_max_num_consec_cons
            new_max_num_consec_cons=0  
        elif c==":":
            colon_count+=1
            max_num_consec_cons<=new_max_num_consec_cons
            new_max_num_consec_cons=0  
        else:
            max_num_consec_cons<=new_max_num_consec_cons
            new_max_num_consec_cons=0  
            continue
    total=float(vowel_count)/ float(c_count)
    return total, dash_count, dot_count, colon_count, max_num_consec_cons

#get number of numerical digits in domain, botnet characteristc to be added in
def getNumNumericalCharsRatio(SLD):
    count=0
    for c in SLD:
        if c.isdigit():
            count +=1
        else:
            continue
    return count

#Check for .co.uk an .co.jp TLDs.  Other checks may be necessary.
def checkDoubleTLD(query):
    
    DoubleTLDs = {
                    'uk': ['co','org', 'net'],
                    'jp': ['co','ne'],
                    'cr': ['co'],
                    'pe': ['org'],
                    'er': ['com'],
                    'kr': ['go', 'co'],
                    'cn': ['com','edu','net', 'sh', 'fj'],
                    'au': ['com', 'net'],
                    'sg': ['com'],
                    'hk': ['com'],
                    'br': ['com'],
                    'ar': ['com'],
                    'id':['net'],
                    'za':['co'],
                    'tw':['edu'],
                    'pl':['net','wp', 'com']
                }

    if query.split('.')[-1] in DoubleTLDs.keys() and query.split('.')[-2] in DoubleTLDs[query.split('.')[-1]]:
        return True
    else: return False

#check if the query contains a known double TLD and split it into host/domain components as appropriate
def splitHostDomain(query):
   
    if checkDoubleTLD(query):
        domain = ".".join(query.split('.')[-3:])
        host = ".".join(query.split('.')[0:-3])
    else:
        domain = ".".join(query.split('.')[-2:])
        host = ".".join(query.split('.')[0:-2])
    if host == '': host = '*'
    return (domain,host)


#read whitelist.txt and return result as a set of domains
def getWhitelistedDomains():
    
    whitelist = set()
    for line in open('whitelist.txt','r'):
        whitelist.add(line.rstrip())
    return whitelist
import csv
whiteset= getWhitelistedDomains()


def build_files(filename, d):
    f = open(filename, 'r')
    reader = csv.reader(f)
    domain_mult_IP_dict={}
    totalAPTDomains=[]
    foundAPT=[]
    kmeans_arr= []
    for row in reader:
        timestamp= row[0].strip('\'')
        query = row[4].strip('\'')
        try: 
            ip = int(row[5].strip('\''))
            ip= numToDottedQuad(ip)
            ttl= int(row[6].strip('\''))
            domain, host= splitHostDomain(query)
            #find Botnets
            if ttl <=60:
                if domain_ips_dict.has_key(query)==False:
                    domain_ips_dict[query]= [ip]
                else:
                    domain_ips_dict[query].append(ip)
            #find APT
            try:
                domain_list = domain.split(".")
                SLD=domain_list[-2]
                if pwl.check(SLD)==False:
                    sugg =pwl.suggest(SLD)
                    G = ngram.NGram(sugg)
                    distance_score= G.search(SLD)[0][1]
                    #ngram analysis distance score from words in enchantAddList
                    if distance_score <= .99 and distance_score >=.05:
                        org_name, cc, ip, register, as_name, bgp_prefix, asn= WHOIS(ip[1:])
                        asn_rank, asn_score= (ASNRankings[asn])
                        #check for low ranking ASN and recently updated domain- heuristics indicative of majority of APT domains
                        rec_update_score= isRecentlyUpdate(domain)
                        if (ASNRankings[asn]) >= 1000 and rec_update_score!=False and noTXTRecord(domain):
                            scoring_vector= (distance_score, asn_score, rec_update_score, 1.0)
                            
                            #iptional debugs
                            #print "BAD ASN and recently updated: ", domain, cc, asn_rank, asn_score, org_name, ip
                            foundAPT.append(scoring_vector)
                            print foundAPT# + ", SLD: " + SLD+", hit on: "  + G.search(SLD)[0][0]+ " IP: " + str(ip) + "ASN: "+ asn + "CC: "+ cc)
            except:
                continue
        except:
            continue
    return domain_ips_dict
  
#Calculate the overlap between pair of IPs  
def calcOverlap(ip1_start_time, ip1_end_time, ip2_start_time, ip2_end_time):
    print "OVERLAP: ", ip1_start_time, ip1_end_time, ip2_start_time, ip2_end_time
    OVERLAP=0
    if ip1_end_time < ip2_end_time:
        OVERLAP= float(ip1_end_time-ip2_start_time)/ float(ip2_end_time- ip1_start_time)
    else:
        OVERLAP= float(ip2_end_time- ip2_start_time)/ float(ip1_end_time-ip1_start_time)
    return OVERLAP

#Distance function to calculate distance between pair of IP addresses
def simple_distance (ip1, ip2):
    ip1_l= ip1.split(".")
    ip2_l= ip2.split(".")
    Aij=0
    Bij=0
    Cij=0
    if (ip1_l[0]!= ip2_l[0]):
        Aij=1
    if (ip1_l[1]!= ip2_l[1]):
        Bij=1
    if (ip1_l[2]!= ip2_l[2]):
        Cij=1
    distance= float((3 *Aij) + 2* Bij + Cij) /(6.0)
    return distance

#Check For for transient/fast flux domains, call after created dictionary key:domain, values: ips
def checkForFastFlux(domain_ip_dict):
    transientDomainList=set()
    import operator
    for x in domain_ip_dict.items():
        ip_ts_dict= x[1]
        
        if len(ip_ts_dict) >=6: #set at 3 for transient, higher threshold for Fast Flux Domains
            #sort the ip/ts dictionary based on first seen
            ip_ts_dict = sorted(ip_ts_dict.iteritems(), key=operator.itemgetter(1), reverse= True)
            print ip_ts_dict
            overlap_sum=0
            distance_sum=0
            ip_pair_count= 0
            for i in range ((len(ip_ts_dict))-1):
                #print ip_ts_dict[i], ip_ts_dict[i+1]
                ip1_s= ip_ts_dict[i][1][0]
                ip1_e= ip_ts_dict[i][1][1]
                ip2_s= ip_ts_dict[i+1][1][0]
                ip2_e= ip_ts_dict[i+1][1][1]
                ip1= ip_ts_dict[i][0]
                ip2= ip_ts_dict[i+1][0]
                try:
                    overlap= calcOverlap(ip1_s, ip1_e,ip2_s,ip2_e)
                    overlap_sum+=overlap
                    distance= simple_distance(ip1, ip2)
                    ip_pair_count+=1
                except:
                    continue
            avg_overlap=  float(overlap_sum)/ip_pair_count
            avg_distance= float(distance_sum)/ip_pair_count
            #requires more thereshold research
            if avg_overlap <.5 and avg_distance >.7:
                transientDomainList.add(x[0])
        else:
            continue
    
#Check if query contains bot characteristics 
def checkShortLife(domain):
    import whois
    import math
    import datetime
 
    try: 
     
        w = whois.query(domain)
        diff=w.creation_date-datetime.datetime.now()
        diff= math.fabs(diff.days)
        if diff<= 30:
            print "Short: ", domain, "Days: ", diff
            return True
        else:
            return False
 
 
    except:
        print "Can't Find Info for: ", domain
        return True

#check for potential bots
def checkBot(domain_ips_dict):
    b=set()
    for query, ips in domain_ips_dict.items():
        if len(ips) >=3:
            count=0
            for i in range(len(ips)-1):
                ip1= ips[i]
                ip2= ips[i+1]
                dist= simple_distance(ip1,ip2)
                if dist >=0.7:
                    count+=1
                    if count >=3:
                        if checkShortLife(query):
                            if len(query1)>=15:
                                vow_2_cons_rat, d_count, dots, num_colons, max_num_consec_cons= queryCharStats(query1)
                                if max_num_consec_cons>=5:
                                    b.add(query)
                                if vow_2_cons_rat<=.2:
                                    b.add(query)
                                if getNumNumericalCharsRatio(query1)>=5:
                                    b.add(query)
                                if d_count >=5:
                                    b.add(query)
                                if dots>=4:
                                    b.add(query)
                                if num_colons>=5: #filer out ipv6 addresses
                                    continue
                        else:
                            continue
                    else:continue
                else:continue
        else:
            continue
    for x in b:
        print x
    print len(b)  

        
def main():
    f_list= walk_thru_files('clientfiles')
    d={}
    for f in f_list:
        d.update(build_files(f, d))
        
    checkBot(d)
if __name__ == '__main__': main()



