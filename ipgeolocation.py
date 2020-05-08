__author__  = 'maldevel'


import sys, os
from core.IpGeoLocationLib import IpGeoLocationLib
from core.Logger import Logger
from core.Menu import parser,args,banner
    
def main():

    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    logsDir = os.path.join(os.getcwd(), 'logs')
    #resultsDir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)
    #if not os.path.exists(resultsDir):
    #    os.mkdir(resultsDir)
        
    logger = Logger(args.nolog, args.verbose)
    
    #single target or multiple targets 
    if(args.target and args.tlist):
        logger.PrintError("Вы можете запросить геолокационную информацию либо для одной цели (- t), либо для списка целей(-T). Только не оба!", args.nolog)
        sys.exit(2)
        
    #my ip address or single target
    if(args.target and args.myip):
        logger.PrintError("Вы можете запросить геолокационную информацию либо для одной цели (- t), либо для вашего собственного IP-адреса. Только не оба!", args.nolog)
        sys.exit(3)
        
    #multiple targets or my ip address
    if(args.tlist and args.myip):
        logger.PrintError("Вы можете запросить геолокационную информацию либо для списка целей (- T), либо для вашего собственного IP-адреса. Только не оба!!", args.nolog)
        sys.exit(4)
    
    #single target and google maps only allowed
    if(args.tlist and args.g):
        logger.PrintError("Google maps location работает только с одиночными целями.", args.nolog)
        sys.exit(5)
    
    #specify user-agent or random
    if(args.uagent and args.ulist):
        logger.PrintError("Вы можете либо указать строку агента пользователя, либо позволить IPGeolocation выбрать случайные строки агента пользователя для вас из файла.", args.nolog)
        sys.exit(6)
        
    #specify proxy or random
    if(args.proxy and args.xlist):
        logger.PrintError("Вы можете либо указать прокси-сервер, либо позволить IPGeolocation выбрать случайные прокси-соединения для вас из файла.", args.nolog)
        sys.exit(7)
        
        
    #init lib
    ipGeoLocRequest = IpGeoLocationLib(args.target, logger, args.noprint)
    
    print(banner)
    
    #retrieve information
    if not ipGeoLocRequest.GetInfo(args.uagent, args.tlist, 
                                     args.ulist, args.proxy, args.xlist,
                                     args.csv, args.xml, args.txt, args.g):
        logger.PrintError("Не удалось получить информацию о геолокации IP-адресов.")
        sys.exit(8)


if __name__ == '__main__':
    main()
    