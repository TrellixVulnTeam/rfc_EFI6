import logging
import logging.config
import logging.handlers
from configparser import ConfigParser
from threading import Thread
from subprocess import call
import sys
import argparse
from scapy.all import *
from config import Config
import time
from packetsniffer import PacketSniffer
from commontestsetup1_1 import CommonTestSetup1_1
from sendmsgs import SendMsgs

class ConfigSetup1_1_Lan:

    def __init__(self,config):
        #self.__queue_wan = Queue()
        #self.__queue_lan = Queue()
        #logging.info('self.__queue_size_inicio162')
        #logging.info(self.__queue_wan.qsize())
        self.__config = config
        self.__interface = None
        self.__pkt = None
        self.__valid = False
        self.__result = None
        self.__device_lan_tn1 = None
        self.__lan_mac_tn1 = None
        self.__ceRouter_mac_addr = None
        self.__flag_M = None
        self.__flag_O = None
        self.__flag_chlim = None
        self.__flag_L = None
        self.__flag_A = None
        self.__flag_R = None
        self.__validlifetime = None
        self.__preferredlifetime = None
        self.__interval = None
        self.__routerlifetime = None
        self.__ipv6_dst =None
        self.__ipv6_src = None
        self.__ether_src = None
        self.__ether_dst = None
        self.__xid = None
        self.__server_duid = None
        self.__client_duid = None
        self.__ND_local_OK = False
        self.__setup1_1_OK = False
        self.__local_ping_OK = False
        self.__global_ns_ok = False
        self.__dhcp_ok = False
        self.__iaid = None
        self.__flag_prf = None
        self.__prefixaddr_CeRouter =None
        self.__l_CeRouter =None
        self.__A_CeRouter =None
        self.__R_CeRouter =None
        self.__validlifetime_CeRouter =None
        self.__preferredlifetime_CeRouter =None
        self.__prefixlen_CeRouter =None
        self.__r_prefixaddr_CeRouter =None
        self.__r_plen_CeRouter =None
        self.__r_prf_CeRouter =None
        self.__r_lifetime_CeRouter =None
        self.__rdnss_dns_CeRouter =None
        self.__rdnss_lifetime_CeRouter  =None
         self.__domainname =None
        self.__domainname_lifetime_CeRouter  =None
        self.__linklayer_CeRouter = None





        self.__disapproved = False
        self.__dhcp_reconf_type = None
        self.__local_addr_ceRouter =None
        self.__sendmsgssetup1_1 = SendMsgs(self.__config)
        self.__wan_device_tr1 = self.__config.get('wan','device_wan_tr1')
        self.__lan_device  = self.__config.get('lan','lan_device')
        self.__wan_mac_tr1 = self.__config.get('wan','wan_mac_tr1')
        self.__link_local_addr = self.__config.get('wan','link_local_addr')
        self.__all_nodes_addr = self.__config.get('multicast','all_nodes_addr')
        self.__test_desc = self.__config.get('tests','1.6.2b')
        self.__elapsetime.
        self.__fdqn
        self.__vendor_class
        self.__enterprise
        self.opt_req
        #self.__packet_sniffer.daemon=True


    def send_icmpv6_ra(self,pkt):
        et = Ether(src=self.__wan_mac_tr1)#,\
                   #dst=pkt[Ether].src)
        ip = IPv6(src=self.__link_local_addr,\
                  dst=self.__all_nodes_addr)
        icmp_ra = ICMPv6ND_RA()
        sendp(et/ip/icmp_ra,iface=self.__wan_device_tr1)

    def send_echo_request_lan(self):
        et = Ether(src=self.__wan_mac_tr1,\
                   dst=self.__ceRouter_mac_addr)
        ip = IPv6(src=self.__link_local_addr,\
                  dst=self.__all_nodes_addr)
        icmp_ra = ICMPv6EchoRequest()
        sendp(et/ip/icmp_ra,iface=self.__wan_device_tr1)

    def flags_partA(self):
        self.__flag_M = self.__config.get('t1.6.2_flags_part_a','flag_m')
        self.__flag_O = self.__config.get('t1.6.2_flags_part_a','flag_o')
        self.__flag_chlim = self.__config.get('t1.6.2_flags_part_a','flag_chlim')
        self.__flag_L = self.__config.get('t1.6.2_flags_part_a','flag_l')
        self.__flag_A = self.__config.get('t1.6.2_flags_part_a','flag_a')
        self.__flag_R = self.__config.get('t1.6.2_flags_part_a','flag_r')
        self.__validlifetime = self.__config.get('t1.6.2_flags_part_a','validlifetime')
        self.__preferredlifetime = self.__config.get('t1.6.2_flags_part_a','preferredlifetime')
        self.__routerlifetime = self.__config.get('t1.6.2_flags_part_a','routerlifetime')
        self.__intervalo = self.__config.get('t1.6.2_flags_part_a','intervalo')

    def flags_partB(self):
        self.__flag_M = self.__config.get('t1.6.2_flags_part_b','flag_m')
        self.__flag_O = self.__config.get('t1.6.2_flags_part_b','flag_o')
        self.__flag_chlim = self.__config.get('t1.6.2_flags_part_b','flag_chlim')
        self.__flag_L = self.__config.get('t1.6.2_flags_part_b','flag_l')
        self.__flag_A = self.__config.get('t1.6.2_flags_part_b','flag_a')
        self.__flag_R = self.__config.get('t1.6.2_flags_part_b','flag_r')
        self.__validlifetime = self.__config.get('t1.6.2_flags_part_b','validlifetime')
        self.__preferredlifetime = self.__config.get('t1.6.2_flags_part_b','preferredlifetime')
        self.__routerlifetime = self.__config.get('t1.6.2_flags_part_b','routerlifetime')
        self.__intervalo = self.__config.get('t1.6.2_flags_part_b','intervalo')

#===========LAN======================

    def get_prefixaddr_CeRouter(self):
        return self.__prefixaddr_CeRouter
    def get_l_CeRouter(self):
        return self.__l_CeRouter 
    def get_A_CeRouter(self):
        return self.__A_CeRouter 
    def get_R_CeRouter(self):
        return self.__R_CeRouter 
    def get_validlifetime_CeRouter(self):
        return self.__validlifetime_CeRouter 
    def get_preferredlifetime_CeRouter(self):
        return self.__preferredlifetime_CeRouter
    def get_prefixlen_CeRouter(self):
        return self.__prefixlen_CeRouter
    def get_r_prefixaddr_CeRouter(self):
        return self.__r_prefixaddr_CeRouter 
    def get_r_plen_CeRouter(self):
        return self.__r_plen_CeRouter
    def get_r_prf_CeRouter(self):
        return self.__r_prf_CeRouter 
    def get_r_lifetime_CeRouter(self):
        return self.__r_lifetime_CeRouter 
    def get_rdnss_dns_CeRouter(self):
        return self.__rdnss_dns_CeRouter
    def get_rdnss_lifetime_CeRouter(self):
        return self.__rdnss_lifetime_CeRouter 
    def get_domainname(self):
        return self.__domainname
    def get_domainname_lifetime_CeRouter(self):
        return self.__domainname_lifetime_CeRouter  
    def get_linklayer_CeRouter(self):
        return self.__linklayer_CeRouter 
   
    def get_lan_device(self):
        return self.__lan_device
    #recebe o pacote
    #packetSniffer return pkt
    def get_setup_OK(self):
        return self.__setup1_1_OK

    def get_elapsetime(self):
        return self.__elapsetime

    def set_elapsetime(self,valor):
        self.__elapsetime = valor

    def get_fdqn(self):
        return self.__fdqn
    
    def set_fdqn(self,valor):
        self.__fdqn = valor

    def get_vendor_class(self):
        return self.__vendor_class

    def set_vendor_class(self,valor):
        self.__vendor_class = valor

    def get_enterprise(self):
        return self.__enterprise

    def set_enterprise(self,valor):
        self.__enterprise = valor 

    def get_opt_req(self):
        return self.opt_req

    def set_opt_req(self,valor):
        self.opt_req = valor

#=========== WAN/LAN===================

    def set_result(self, valor):
        self.__result = valor
        
    def get_result(self):
        return self.__result

    def get_flag_M(self):
        return int(self.__flag_M)

    def set_flag_M(self,valor):
        self.__flag_M = valor

    def get_flag_O(self):
        return int(self.__flag_O)

    def get_flag_prf(self):
        return int(self.__flag_prf)

    def set_flag_prf(self,valor):
        self.__flag_prf = valor

    def set_flag_0(self,valor):
        self.__flag_O = valor

    def set_routerlifetime(self,valor):
        self.__routerlifetime= valor

    def set_flag_L(self,valor):
        self.__flag_L = valor
        
    def set_flag_A(self,valor):
        self.__flag_A = valor

    def set_flag_R(self,valor):
        self.__flag_R = valor

    def set_validlifetime(self,valor):
        self.__validlifetime = valor

    def set_preferredlifetime(self,valor):
        self.__preferredlifetime = valor

    def set_intervalo(self,valor):
        self.__intervalo = valor
        
    def set_flag_chlim(self,valor):
        self.__flag_chlim = valor

    def get_flag_chlim(self):
        return int(self.__flag_chlim)

    def get_flag_L(self):
        return  int(self.__flag_L)

    def get_flag_A(self):
        return int(self.__flag_A)

    def get_flag_R(self):
        return int(self.__flag_R)

    def get_validlifetime(self):
        return int(self.__validlifetime)

    def get_preferredlifetime(self):
        return int(self.__preferredlifetime)

    def get_interval(self):
        return int(self.__intervalo)

    def get_routerlifetime(self):
        return int(self.__routerlifetime)
    
    def set_ipv6_dst(self, valor):
        self.__ipv6_dst = valor

    def get_ipv6_dst(self):
        return self.__ipv6_dst

    def set_ipv6_src(self, valor):
        self.__ipv6_src = valor

    def get_ipv6_src(self):
        return self.__ipv6_src

    def set_ether_dst(self, valor):
        self.__ether_dst = valor

    def get_ether_dst(self):
        return self.__ether_dst

    def set_ether_src(self, valor):
        self.__ether_src = valor

    def get_ether_src(self):
        return self.__ether_src
    
    def set_local_addr_ceRouter(self,valor):
        self.__local_addr_ceRouter = valor

    def get_local_addr_ceRouter(self):
        return self.__local_addr_ceRouter

    def set_tgt(self,valor):
        self.__tgt = valor

    def get_tgt(self):
        return self.__tgt

    def set_xid(self,valor):
        self.__xid = valor

    def get_xid(self):
        return self.__xid

    def set_client_duid(self,valor):
        self.__client_duid = valor

    def get_client_duid(self):
        return self.__client_duid

    def set_server_duid(self,valor):
        self.__server_duid = valor

    def get_server_duid(self):
        return self.__server_duid

    def set_iaid(self,valor):
        self.__iaid = valor

    def get_iaid(self):
        return self.__iaid
    
    def get_local_ping(self):
        return self.__local_ping_OK

    def get_ND_local_OK(self):
        return  self.__ND_local_OK

    def get_dhcp_reconf_type(self):
        return self.__dhcp_reconf_type
    
    def set_dhcp_reconf_type(self,valor):
        self.__dhcp_reconf_type = valor

    def set_mac_ceRouter(self,valor):
        self.__mac_cerouter = valor

    def get_mac_ceRouter(self):
        return self.__mac_cerouter

    def get_disapproved(self):
        return self.__disapproved

    def run_setup1_1(self,pkt):
        
        if self.__disapproved:
            return False

        if not send_solicit:
            self.set_ipv6_src(self.__config.get('solicitlan','ip'))
            self.set_ether_src(self.__config.get('solicitlan','mac'))
            self.set_ether_dst(self.__config.get('multicast','all_mac_routers'))
            self.set_ipv6_dst(self.__config.get('multicast','all_routers_addr'))
            self.set_elapsetime(self.__config.get('solicitlan','elapsetime')))
            self.set_client_duid(self.__config.get('solicitlan','duid')))
            self.set_fdqn(self.__config.get('solicitlan','clientfqdn'))
            self.__sendmsgssetup1_1.send_dhcp_solicit_ia_na(self)
            send_solicit = True
            return
        if send_solicit:
            self.set_ipv6_src(self.__config.get('informationlan','ip'))
            self.set_ether_src(self.__config.get('informationlan','mac'))
            self.set_ether_dst(self.__config.get('multicast','all_mac_routers'))
            self.set_ipv6_dst(self.__config.get('multicast','all_routers_addr'))
            self.set_elapsetime(self.__config.get('solicitlan','elapsetime')))
            self.set_client_duid(self.__config.get('solicitlan','duid')))
            self.set_fdqn(self.__config.get('solicitlan','clientfqdn'))
            self.__sendmsgssetup1_1.send_dhcp_solicit_ia_na(self)
            send_solicit = True
            return

        if pkt.haslayer(ICMPv6ND_RA):
            if pkt.haslayer(ICMPv6NDOptPrefixInfo):
                self.__prefixaddr_CeRouter = pkt[ICMPv6NDOptPrefixInfo].prefix
                self.__l_CeRouter = pkt[ICMPv6NDOptPrefixInfo].L
                self.__A_CeRouter = pkt[ICMPv6NDOptPrefixInfo].A
                self.__R_CeRouter = pkt[ICMPv6NDOptPrefixInfo].R
                self.__validlifetime_CeRouter = pkt[ICMPv6NDOptPrefixInfo].validlifetime
                self.__preferredlifetime_CeRouter = pkt[ICMPv6NDOptPrefixInfo].preferredlifetime
                self.__prefixlen_CeRouter = pkt[ICMPv6NDOptPrefixInfo].prefixlen

            if pkt.haslayer(ICMPv6NDOptRouteInfo):
                self.__r_prefixaddr_CeRouter = pkt[ICMPv6NDOptRouteInfo].prefix
                self.__r_plen_CeRouter = pkt[ICMPv6NDOptRouteInfo].plen
                self.__r_prf_CeRouter = pkt[ICMPv6NDOptRouteInfo].prf
                self.__r_lifetime_CeRouter = pkt[ICMPv6NDOptRouteInfo].rlifetime

            if pkt.haslayer(ICMPv6NDOptRDNSS):
                self.__rdnss_dns_CeRouter = pkt[ICMPv6NDOptRDNSS].dns
                self.__rdnss_lifetime_CeRouter = pkt[ICMPv6NDOptRDNSS].lifetime
            
            if pkt.haslayer(ICMPv6NDOptDNSSL):
                self.__domainname = pkt[ICMPv6NDOptDNSSL].searchlist
                self.__domainname_lifetime_CeRouter = pkt[ICMPv6NDOptDNSSL].lifetime

            if pkt.haslayer(ICMPv6NDOptSrcLLAddr):
                self.__linklayer_CeRouter = pkt[ICMPv6NDOptDNSSL].lladdr                

#             ICMPv6NDOptPrefixInfo prefix
#                 self.set_mac_ceRouter(pkt[Ether].src)
# >>> ls(ICMPv6NDOptRDNSS)                                                                                                                                                                                                                                                        
# type       : ByteField                           = (25)
# len        : FieldLenField                       = (None)
# res        : ShortField                          = (None)
# lifetime   : IntField                            = (4294967295)
# dns        : IP6ListField                        = ([])

# >>> ls(ICMPv6NDOptRouteInfo)                                                                                                                                                                                                                                                    
# type       : ByteField                           = (24)
# len        : FieldLenField                       = (None)
# plen       : ByteField                           = (None)
# res1       : BitField  (3 bits)                  = (0)
# prf        : BitEnumField  (2 bits)              = (0)
# res2       : BitField  (3 bits)                  = (0)
# rtlifetime : IntField                            = (4294967295)
# prefix     : _IP6PrefixField                     = (None)

# >>> ls(ICMPv6NDOptDNSSL)                                                                                                                                                                                                                                                        
# type       : ByteField                           = (31)
# len        : FieldLenField                       = (None)
# res        : ShortField                          = (None)
# lifetime   : IntField                            = (4294967295)
# searchlist : DomainNameListField                 = ([])

# ls(ICMPv6NDOptSrcLLAddr)                                                                                                                                                                                                                                                    
# type       : ByteField                           = (1)
# len        : ByteField                           = (1)
# lladdr     : MACField                            = ('00:00:00:00:00:00')




        #if send_info_req:

    # def get_elapsetime(self):
    #     return self.__elapsetime

    # def set_elapsetime(self,valor):
    #     self.__elapsetime = valor

    # def get_fdqn(self):
    #     return self.__fdqn
    
    # def set_fdqn(self,valor):
    #     self.__fdqn = valor

    # def get_vendor_class(self):
    #     return self.__vendor_class

    # def set_vendor_class(self,valor):
    #     self.__vendor_class = valor

    # def get_enterprise(self):
    #     return self.__enterprise

    # def set_enterprise(self,valor):
    #     self.__enterprise = valor 

    # def get_opt_req(self):
    #     return self.opt_req

    # def set_opt_req(self,valor):
    #     self.opt_req = valor

        if pkt.haslayer(ICMPv6ND_NS):
            if pkt[ICMPv6ND_NS].tgt == '::':
                return
            if pkt[IPv6].src == '::':
                return
            if pkt[IPv6].src == self.__config.get('wan','link_local_addr'):
                return
            if pkt[IPv6].src == self.__config.get('wan','global_wan_addr'):
                return
            if not self.__ND_local_OK:
                #self.set_ether_dst(pkt[Ether].src)
                self.set_mac_ceRouter(pkt[Ether].src)
                # print('local addr ND')
                self.set_local_addr_ceRouter(pkt[ICMPv6ND_NS].tgt)
                # print('local addr')
                # print(self.get_local_addr_ceRouter())
                # print('ether dst')
                # print(self.get_ether_dst())
                self.__ND_local_OK = True

        if self.__ND_local_OK and not self.__local_ping_OK:
            #print('send_echoreq:')
            #logging.info('send_echoreq:')
            self.set_ipv6_src(self.__config.get('wan','link_local_addr'))
            self.set_ipv6_dst(self.get_local_addr_ceRouter())
            self.set_ether_src(self.__config.get('wan','link_local_mac'))
            self.set_ether_dst(self.get_mac_ceRouter())
            self.__sendmsgssetup1_1.send_echo_request(self)
            self.__local_ping_OK = True

        if pkt.haslayer(ICMPv6ND_RS):
            if not self.__ND_local_OK:
                self.__disapproved = True
                logging.info('Reprovado Setup 1.1 - Não Recebeu ICMP_NS antes de ICMP_RS')
                return False
            else:
                self.set_ether_src(self.__config.get('wan','ra_mac'))
                self.set_ether_dst(self.__config.get('multicast','all_mac_nodes'))
                self.set_ipv6_src(self.__config.get('wan','ra_address'))
                self.set_ipv6_dst(self.__config.get('multicast','all_nodes_addr'))
                self.__sendmsgssetup1_1.send_tr1_RA(self)


        if pkt.haslayer(DHCP6_Solicit):
            #print('send_dhcpadv:')
            #logging.info('send_dhcp_adv:')
            self.set_xid(pkt[DHCP6_Solicit].trid)
            self.set_client_duid(pkt[DHCP6OptClientId].duid)
            self.set_server_duid((self.__config.get('setup1-1_advertise','server_duid')))
            self.set_iaid(pkt[DHCP6OptIA_NA].iaid)
            self.set_ether_src(self.__config.get('wan','link_local_mac'))
            self.set_ether_dst(self.get_mac_ceRouter())
            self.set_ipv6_dst(self.get_local_addr_ceRouter())
            # print('local addr')
            # print(self.get_local_addr_ceRouter())
            # print('ether dst')
            # print(self.get_ether_dst())
            self.set_ipv6_src(self.__config.get('wan','link_local_addr'))  

            self.__sendmsgssetup1_1.send_dhcp_advertise(self)

        if pkt.haslayer(DHCP6_Request):
            #print('send_dhcpreply:')
            #logging.info('send_dhcp_reply:')
            self.set_ether_src(self.__config.get('wan','link_local_mac'))
            self.set_ether_dst(self.get_mac_ceRouter())
            self.set_ipv6_dst(self.get_local_addr_ceRouter())
            self.set_ipv6_src(self.__config.get('wan','link_local_addr'))
            self.__sendmsgssetup1_1.send_dhcp_reply(self)
            self.__dhcp_ok = True
            self.__setup1_1_OK = True
            logging.info("Common Test Setup 1.1 OK")

        if self.__dhcp_ok:
            #print('send_icmp_ns:')
            #logging.info('send_icmp_ns:')
            self.set_ether_src(self.__config.get('multicast','all_mac_nodes'))
            self.set_ether_dst(self.__config.get('wan','link_local_mac'))
            self.set_ipv6_dst(self.__config.get('multicast','all_nodes_addr'))
            self.set_ipv6_src(self.__config.get('wan','global_wan_addr'))
            self.set_tgt(self.__config.get('wan','link_local_addr'))
            self.__sendmsgssetup1_1.send_icmp_ns(self)
            self.__global_ns_ok = True
            
        #1 sned ping test



        if pkt.haslayer(ICMPv6EchoReply):
            #print('DESTINO IPv6:' + pkt[IPv6].dst)
            if pkt[IPv6].dst == self.__config.get('wan','link_local_addr'):
                #print('DESTINO IPv6 OKKKK')
                self.__local_ping_OK = True