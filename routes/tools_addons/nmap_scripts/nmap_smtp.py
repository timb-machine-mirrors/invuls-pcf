class nmap_plugin():
    # user-defined
    script_id = 'SMTP'
    script_types = ['info']

    script_obj = None
    output = ''

    def __init__(self, script_object):
        self.script_obj = script_object
        self.output = script_object['output']

    def info(self):
        """
        return
            {
                "protocol": "http",
                "info": "Nginx 1.12.0"
            }
        """

        info_object = {
            'protocol': 'smtp',
        }
        if "with errors or timeout" not in self.output:
            info_object['info'] = "SNMP info:\n" + self.output
        return info_object
