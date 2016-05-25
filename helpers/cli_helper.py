__author__ = "Andrew Szymanski (andrew.szymanski@newsint.co.uk)"
__version__ = "0.1.0"

"""Cloudera Manager API & AWS boto combined
"""
import logging
import os
import inspect
import UserDict


# constants
LOG_INDENT = "  "        # to prettify logs
# keys in cfg file
CM_HOSTNAME = "cm_hostname"
CM_USERNAME = "cm_username"
CM_PASSWORD = "cm_password"
AWS_REGION = "aws_region"
AWS_BOTO_CFG = "aws_boto_cfg"


class CompositeHelper(object):
    """Our boto EC2 wrapper
    """    
    def __init__(self, *args, **kwargs):
        """Create an object and attach or initialize logger
        """
        self.__is_connected__ = False
        self.logger = kwargs.get('logger',None)
        if ( self.logger is None ):
            # Get an instance of a logger
            console = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s: %(levelname)-8s %(message)s',"%Y-%m-%d %H:%M:%S")
            console.setFormatter(formatter)
            logging.getLogger('').addHandler(console)
            self.logger = logging.getLogger('')
            self.logger.setLevel(logging.INFO)
        # initial log entry
        self.logger.debug("%s: %s version [%s]" % (self.__class__.__name__, inspect.getfile(inspect.currentframe()),__version__))
        # initialize variables - so all are listed here for convenience
        self.dict_config = {}   # dictionary, see cdh_manager.cfg example
        self.__cm_cdh__ = None
        self.__boto_ec2__ = None
        self.data = DataObjectSample(logger=self.logger)
        

    def configure(self, cfg=None):
        """Read in configuration file 
        """
        self.logger.debug("%s::%s starting..." %  (self.__class__.__name__ , inspect.stack()[0][3])) 
        if not cfg:
            raise Exception("cfg parameter (config file location) not specified.")
                
        cfg = os.path.expandvars(cfg)
        self.logger.debug("%s reading config file: [%s]..." % (LOG_INDENT, cfg))
        
        new_dict = {}
        # read Cloudera Manager config
        try:
            with open(cfg) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#"):           # comment line
                        continue
                    (key, val) = line.split('=')
                    key = key.strip()
                    val = val.strip()
                    val = os.path.expandvars(val)
                    new_dict[key] = val
        except Exception, e:
            raise Exception("Could not read config file: [%s], error: [%s]" % (cfg, e))
        
        # validate all params
        keys = [CM_HOSTNAME, CM_USERNAME, CM_PASSWORD, AWS_REGION, AWS_BOTO_CFG]
        for key in keys:
            value = new_dict.get(key, None)
            if not value:
                raise Exception("'%s' not defined in config file: [%s]" % (key, cfg))
        
        self.dict_config = new_dict
        self.logger.info("%s aws region: [%s]" % (LOG_INDENT, self.dict_config[AWS_REGION]))
        self.logger.info("%s boto cfg: [%s]" % (LOG_INDENT, self.dict_config[AWS_BOTO_CFG]))

    def run(self, cfg=None):
        """do something
        """        
        self.logger.debug("%s::%s starting..." %  (self.__class__.__name__ , inspect.stack()[0][3])) 
        self.logger.debug("%s::%s DONE" %  (self.__class__.__name__ , inspect.stack()[0][3])) 
        
        
        
        
        
#    def __len__(self): 
#        """ returns number of instances
#        """
#        return len(self.data) 

#    def __iter__(self): 
#        """ returns number of instances
#        """
#        return iter(self.data) 
#    
#
#    def iteritems(self): 
#        """ returns number of instances
#        """
#        return self.data.iteritems() 
    
    
    

class DataObjectSample:
    ''' data object 
    '''
    def __init__(self, *args, **kwargs):
        """Create an empty object
        """
        self.private_dns_name  = None    # AWS private hostname
        self.cdh_host = None             # Cloudera Manager API ApiHost object
        self.aws_instance = None         # boto AWS EC2 object
        self.aws_instance_name = None





