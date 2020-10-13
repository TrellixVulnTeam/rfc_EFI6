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
from configsetup1_1 import ConfigSetup1_1
# - Seleciona a interface
# - recebe thread de captura das mensagens já iniciada na main
# - inicia a captura
# - recebe o pacote e armazena numa lista
# - analisa o pacote recebido e armazenado na lista
# - 

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG,
                    datefmt="%H:%M:%S")

class Test162c:

    def __init__(self,config):
        self.__queue_wan = Queue()
        self.__queue_lan = Queue()
        # logging.info('self.__queue_size_inicio162')
        # logging.info(self.__queue_wan.qsize())
        self.__config = config
        self.__interface = None
        self.__pkt = None
        # self.__valid = False
        # self.__result = None
        # self.__device_lan_tn1 = None
        # self.__lan_mac_tn1 = None
        # self.__ceRouter_mac_addr = None
        # self.__flag_M = None
        # self.__flag_O = None
        # self.__flag_chlim = None
        # self.__flag_L = None
        # self.__flag_A = None
        # self.__flag_R = None
        # self.__validlifetime = None
        # self.__preferredlifetime = None
        # self.__interval = None
        # self.__routerlifetime = None
        # self.__ipv6_dst =None
        # self.__ipv6_src = None
        # self.__ether_src = None
        # self.__ether_dst = None
        # self.__xid = None
        # self.__server_duid = None
        # self.__client_duid = None
        # self.__ND_local_OK = False
        # self.__setup1_1_OK = False
        # self.__local_ping_OK = False
        # self.__global_ns_ok = False
        # self.__dhcp_ok = False
        # self.__iaid = None
        self.__local_addr_ceRouter =None
        self.__sendmsgs = SendMsgs(self.__config)
        self.__config_setup1_1 = ConfigSetup1_1(self.__config)
        self.__wan_device_tr1 = self.__config.get('wan','device_wan_tr1')
        self.__wan_mac_tr1 = self.__config.get('wan','wan_mac_tr1')
        self.__link_local_addr = self.__config.get('wan','link_local_addr')
        self.__all_nodes_addr = self.__config.get('multicast','all_nodes_addr')
        self.__test_desc = self.__config.get('tests','1.6.2c')
        

    def run(self):
        self.__packet_sniffer_wan = PacketSniffer('test162c',self.__queue_wan,self,self.__config,self.__wan_device_tr1)
        self.__config_setup1_1.flags_partB()
        self.__packet_sniffer_wan.start()
        # logging.info('Task Desc')
        logging.info(self.__test_desc)
        # logging.info('Qsize')
        # logging.info(self.__queue_wan.qsize())
        while not self.__queue_wan.full():

            pkt = self.__queue_wan.get()
            if not self.__config_setup1_1.get_setup1_1_OK():
                # logging.info('self.__queue_size')
                # logging.info(self.__queue_wan.qsize())
                self.__config_setup1_1.run_setup1_1(pkt)

            elif not self.__approved:
                self.set_ipv6_src(self.__config.get('wan','global_wan_addr'))
                self.set_ipv6_dst(self.__config.get('setup1-1_advertise','ia_na_address'))
                self.set_ether_src(self.__config.get('wan','link_local_mac'))
                self.set_ether_dst(self.get_ether_dst())
                self.__sendmsgs.send_echo_request(self)
                if pkt.haslayer(ICMPv6EchoReply):
                    mac_dst = pkt[Ether].dst
                    if mac_dst == self.__config.get('wan','ra_mac'):
                        return True
                    else:
                        return False
        while not self.__queue_wan.empty():
            # print('RS1')
            pkt = self.__queue_wan.get()       
        # logging.info('Passo4-t162run_sttop-theard success')
        # logging.info('self.__queue_size_fim')
        # logging.info(self.__queue_wan.qsize())  
            #time.sleep(2)
        self.__packet_sniffer_wan.stop()
            #time.sleep(2)
        return True
     
        